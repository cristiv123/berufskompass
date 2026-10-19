# -*- coding: utf-8 -*-
"""Stamp a version on every CSS/JS reference so browsers fetch fresh files after a release.

Usage: python tools/set_version.py 3
"""
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
version = sys.argv[1]
pattern = re.compile(r"""((?:href|src)="(?:css|js)/[\w./-]+\.(?:css|js)|from '\./[\w.-]+\.js)(?:\?v=[\w.-]+)?""")

files = [os.path.join(ROOT, "index.html")] + [os.path.join(ROOT, "js", f) for f in os.listdir(os.path.join(ROOT, "js"))
                                               if f.endswith(".js")]
for path in files:
    src = open(path, encoding="utf-8").read()
    new, n = pattern.subn(lambda m: f"{m.group(1)}?v={version}", src)
    if new != src:
        open(path, "w", encoding="utf-8", newline="").write(new)
    print(f"{os.path.relpath(path, ROOT)}: {n}")
