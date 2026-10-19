# -*- coding: utf-8 -*-
"""Pull the item lists out of the two PDF generator scripts and write js/data.js."""
import json
import re
import sys

KEYS = ["TYPE_NAME", "TYPE_DESC", "INT", "CONF", "ANCHORS", "B5", "B5_NAME", "SDT", "CTX", "ADAPT", "OPEN", "OCC",
        "SC_LIKE", "SC_CONF", "SC_TRUE", "SC_DESC", "SC_STR"]


def load(path):
    src = open(path, encoding="utf-8").read()
    start = src.index("TYPES = [")
    end = src.index("n_int =")
    ns = {}
    exec(src[start:end], ns)
    return {k: ns[k] for k in KEYS}


ro = load(sys.argv[1])
de = load(sys.argv[2])


def pack(d, lang):
    return {
        "typeName": d["TYPE_NAME"], "typeDesc": d["TYPE_DESC"],
        "int": d["INT"], "conf": d["CONF"],
        "anchors": [{"code": c, "name": n, "items": it, "desc": ds} for c, n, it, ds in d["ANCHORS"]],
        "b5": [{"trait": t, "rev": k != "+", "txt": x} for t, k, x in d["B5"]],
        "b5Name": d["B5_NAME"],
        "sdt": [{"name": n, "items": it} for n, it in d["SDT"].items()],
        "ctx": [list(p) for p in d["CTX"]],
        "adapt": [{"name": n, "items": it} for n, it in d["ADAPT"].items()],
        "open": [{"name": n, "q": q, "what": w} for n, q, w in d["OPEN"]],
        "scales": {"like": d["SC_LIKE"], "conf": d["SC_CONF"], "true": d["SC_TRUE"], "desc": d["SC_DESC"],
                   "strength": d["SC_STR"]},
    }


out = {"ro": pack(ro, "ro"), "de": pack(de, "de")}
assert len(ro["OCC"]) == len(de["OCC"])
out["occ"] = [{"ro": r[0], "de": r[1], "code": r[2]} for r in ro["OCC"]]
for r, d in zip(ro["OCC"], de["OCC"]):
    assert r[2] == d[1], (r, d)

js = ("// Generated from the Busola Vocațională / Berufskompass document sources. Edit there, then regenerate.\n"
      "export const DATA = " + json.dumps(out, ensure_ascii=False, indent=1) + ";\n")
open(sys.argv[3], "w", encoding="utf-8").write(js)
print("ok", len(js))
