# -*- coding: utf-8 -*-
import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Italic", r"C:\Windows\Fonts\ariali.ttf"))
pdfmetrics.registerFont(TTFont("Arial-BoldItalic", r"C:\Windows\Fonts\arialbi.ttf"))
pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold", italic="Arial-Italic",
                              boldItalic="Arial-BoldItalic")

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "busola_vocationala_test_de.pdf")

INK = colors.HexColor("#18262A")
ACCENT = colors.HexColor("#0E6B66")
MUTED = colors.HexColor("#5A6A6E")
LINE = colors.HexColor("#C9D3D0")
HEAD_BG = colors.HexColor("#E3ECE9")
TYPE_COL = {"R": "#B0542C", "I": "#2F6DAE", "A": "#8A4FA6", "S": "#2D8A58", "E": "#B97F12", "C": "#56636B"}

ss = getSampleStyleSheet()
body = ParagraphStyle("body", parent=ss["Normal"], fontName="Arial", fontSize=9.6, leading=13.4, textColor=INK,
                      spaceAfter=5)
small = ParagraphStyle("small", parent=body, fontSize=8.4, leading=11.2, textColor=MUTED, spaceAfter=3)
cell = ParagraphStyle("cell", parent=body, fontSize=8.8, leading=11.6, spaceAfter=0)
cellb = ParagraphStyle("cellb", parent=cell, fontName="Arial-Bold")
title = ParagraphStyle("title", parent=body, fontName="Arial-Bold", fontSize=24, leading=28, textColor=INK, spaceAfter=4)
subtitle = ParagraphStyle("subtitle", parent=body, fontSize=11.5, leading=15, textColor=MUTED, spaceAfter=14)
h1 = ParagraphStyle("h1", parent=body, fontName="Arial-Bold", fontSize=15, leading=19, textColor=ACCENT,
                    spaceBefore=12, spaceAfter=7)
h2 = ParagraphStyle("h2", parent=body, fontName="Arial-Bold", fontSize=11.6, leading=15, textColor=INK,
                    spaceBefore=10, spaceAfter=4)
h3 = ParagraphStyle("h3", parent=body, fontName="Arial-Bold", fontSize=10, leading=13, textColor=INK,
                    spaceBefore=7, spaceAfter=3)
bullet = ParagraphStyle("bullet", parent=body, leftIndent=12, bulletIndent=2, spaceAfter=3)

story = []
P = lambda t, s=body: story.append(Paragraph(t, s))
SP = lambda h=4: story.append(Spacer(1, h))


def bullets(items):
    for it in items:
        story.append(Paragraph(it, bullet, bulletText="•"))


def table(rows, widths, header=True, style_extra=None):
    data = [[Paragraph(c, cellb if (header and r == 0) else cell) for c in row] for r, row in enumerate(rows)]
    t = Table(data, colWidths=[w * mm for w in widths], repeatRows=1 if header else 0)
    st = [("GRID", (0, 0), (-1, -1), 0.35, LINE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
          ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5)]
    if header:
        st.append(("BACKGROUND", (0, 0), (-1, 0), HEAD_BG))
    if style_extra:
        st += style_extra
    t.setStyle(TableStyle(st))
    story.append(t)


def scale_table(options):
    table([["Punkte"] + [str(i + 1) for i in range(len(options))], ["Option"] + options],
          [20] + [32] * len(options))


# ------------------------------------------------------------------ Inhalt

TYPES = ["R", "I", "A", "S", "E", "C"]
TYPE_NAME = {"R": "Realistisch", "I": "Investigativ", "A": "Artistisch", "S": "Sozial", "E": "Unternehmerisch",
             "C": "Konventionell"}
TYPE_DESC = {
    "R": "mit den Händen, Werkzeugen, Maschinen, in der Natur arbeiten; konkrete Ergebnisse",
    "I": "analysieren, forschen, verstehen, wie Dinge funktionieren",
    "A": "gestalten, sich ausdrücken, Design, Arbeit ohne feste Regeln",
    "S": "lehren, unterstützen, betreuen und beraten",
    "E": "überzeugen, führen, verkaufen, Risiken eingehen",
    "C": "Struktur, Daten, Abläufe, Genauigkeit und Kontrolle",
}

INT = {
    "R": ["Geräte, Maschinen oder Apparate reparieren oder warten.",
          "Eine technische Anlage montieren, anschliessen und in Betrieb nehmen.",
          "In einer Werkstatt mit Werkzeugen arbeiten (Holz, Metall, Elektronik).",
          "Im Freien arbeiten: auf einer Baustelle, im Wald oder auf einem Bauernhof.",
          "Fahrzeuge, Drohnen oder Maschinen fahren oder bedienen.",
          "Nach einem Plan etwas Physisches von Grund auf bauen.",
          "Herausfinden, warum ein Gerät nicht funktioniert, und es eigenhändig reparieren.",
          "Pflanzen, Tiere oder ein Gelände pflegen."],
    "I": ["Daten analysieren, um einen Trend oder eine verborgene Ursache zu finden.",
          "Genau verstehen, wie ein komplexes System funktioniert.",
          "Experimente durchführen und Hypothesen prüfen.",
          "Wissenschaftliche oder technische Studien aus Ihrem Fachgebiet lesen.",
          "Ein schwieriges logisches Problem lösen, für das es noch keine Lösung gibt.",
          "Ein mathematisches oder statistisches Modell erstellen.",
          "Die Hauptursache einer Störung oder eines Vorfalls untersuchen.",
          "Sich selbstständig eine neue Technologie oder Theorie aneignen, bis Sie sie beherrschen."],
    "A": ["Das visuelle Erscheinungsbild eines Produkts, einer App oder eines Raums gestalten.",
          "Texte, Geschichten oder Artikel schreiben.",
          "Musik komponieren, singen oder produzieren.",
          "Fotografieren, filmen oder Videos schneiden.",
          "Ein völlig neues Konzept oder eine völlig neue Idee erfinden.",
          "Vor Publikum eine Rolle spielen, präsentieren oder improvisieren.",
          "Ohne feste Regeln arbeiten, dort, wo der persönliche Stil zählt.",
          "Zeichnen, malen oder dekorative Gegenstände gestalten."],
    "S": ["Jemandem, der gerade erst anfängt, etwas Kompliziertes erklären.",
          "Einer Person durch eine schwierige Zeit helfen.",
          "Einen Kurs oder einen Workshop leiten.",
          "Kranke, ältere Menschen oder Menschen mit Behinderung betreuen.",
          "In einem Konflikt zwischen zwei Personen vermitteln.",
          "Eine jüngere Kollegin oder einen jüngeren Kollegen als Mentor/in begleiten.",
          "An einem Projekt arbeiten, das das Leben einer Gemeinschaft verbessert.",
          "Menschen zuhören und beraten, die Sie um Rat fragen."],
    "E": ["Eine Kundin oder einen Kunden überzeugen, sich für Ihre Lösung zu entscheiden.",
          "Ein Team zu einem ehrgeizigen Ziel führen.",
          "Ein eigenes Unternehmen oder ein eigenes Projekt starten.",
          "Einen Vertrag, einen Preis oder einen Lohn verhandeln.",
          "Eine Idee vor der Geschäftsleitung präsentieren, um Budget zu erhalten.",
          "Mit unvollständigen Informationen schnell entscheiden.",
          "Ein berufliches Netzwerk aufbauen.",
          "Um messbare Ergebnisse konkurrieren (Umsatz, Marktanteil)."],
    "C": ["Zahlen, Dokumente oder Lagerbestände genau erfassen.",
          "Prüfen, ob ein Prozess Regeln und Standards einhält.",
          "Informationen in Tabellen, Datenbanken oder Archiven ordnen.",
          "Budgets, Rechnungen oder Finanzberichte erstellen.",
          "Einem klaren Ablauf Schritt für Schritt fehlerfrei folgen.",
          "Termine, Fristen und Ressourcen planen.",
          "Die Qualität eines Produkts oder einer Dokumentation kontrollieren.",
          "Ordnung in ein chaotisches System aus Dateien, Daten oder Abläufen bringen."],
}

CONF = {
    "R": ["Ein elektrisches oder elektronisches Gerät reparieren.",
          "Elektrowerkzeuge sicher verwenden.",
          "Einen technischen Plan lesen und danach arbeiten.",
          "Möbel oder eine einfache Installation ohne detaillierte Anleitung montieren."],
    "I": ["Einen Datensatz analysieren und korrekte Schlüsse ziehen.",
          "Einen wissenschaftlichen Artikel oder eine dichte technische Dokumentation verstehen.",
          "Die Ursache eines komplexen Problems finden, indem Sie Hypothesen systematisch ausschliessen.",
          "Statistik oder Mathematik auf ein reales Problem anwenden."],
    "A": ["Ein visuelles Design erstellen, das professionell aussieht.",
          "Einen Text schreiben, der Aufmerksamkeit weckt.",
          "Originelle Ideen haben, wenn andere nicht weiterkommen.",
          "Eine Idee durch Bild, Ton oder Bewegung ausdrücken."],
    "S": ["Einer Gruppe etwas so beibringen, dass alle es verstehen.",
          "Eine aufgebrachte Person beruhigen.",
          "Merken, was jemand fühlt, ohne dass die Person es sagt.",
          "Jemanden dabei unterstützen, ein persönliches Ziel zu erreichen."],
    "E": ["Eine skeptische Gruppe überzeugen.",
          "Eine Sitzung bis zu einem Entscheid führen.",
          "Eine für Sie gute Vereinbarung aushandeln.",
          "Ein Produkt oder eine Dienstleistung verkaufen."],
    "C": ["Ein Budget oder eine Buchhaltung fehlerfrei führen.",
          "Ein Ordnungssystem schaffen, das auch andere nutzen.",
          "Mit komplexen Excel-Tabellen arbeiten.",
          "Strikte Fristen und Abläufe einhalten."],
}

ANCHORS = [
    ("TF", "Technisch-funktionale Kompetenz",
     ["Ich möchte eine gefragte Expertin / ein gefragter Experte in meinem Fachgebiet werden.",
      "Am erfülltesten bin ich, wenn ich meine Fachkompetenz auf hohem Niveau einsetze.",
      "Ich würde eine Beförderung ablehnen, die mich aus meinem Fachgebiet herausführt."],
     "Die berufliche Identität entsteht daraus, in einem Gebiet sehr gut zu sein. Suchen Sie Expertenrollen und "
     "Fachlaufbahnen, nicht nur Führungslaufbahnen. Vorsicht bei Beförderungen ins reine Management."),
    ("GM", "Allgemeine Managementkompetenz",
     ["Ich möchte eines Tages eine ganze Organisation oder Abteilung leiten.",
      "Mich reizt die Verantwortung für die Ergebnisse eines ganzen Teams.",
      "Ich integriere lieber die Arbeit anderer, als Spezialist/in für eine einzige Sache zu sein."],
     "Sie motivieren Verantwortung, Integration und die Ergebnisse der Organisation. Suchen Sie Rollen mit Team "
     "und Budget. Vorsicht bei isolierten Spezialistenrollen."),
    ("AU", "Selbstständigkeit / Unabhängigkeit",
     ["Ich möchte selbst entscheiden, wie, wann und wo ich arbeite.",
      "Starre Regeln und Abläufe von Organisationen belasten mich.",
      "Für mehr Freiheit würde ich auf die Sicherheit einer Festanstellung verzichten."],
     "Sie brauchen Kontrolle über Ihre Arbeitsweise. Suchen Sie Freelancing, Beratung, Remote-Arbeit, klare Ziele "
     "mit Freiheit in der Umsetzung. Vorsicht bei Mikromanagement."),
    ("SE", "Sicherheit / Beständigkeit",
     ["Die Sicherheit von Arbeitsplatz und Einkommen ist mir sehr wichtig.",
      "Ich bevorzuge einen stabilen Arbeitgeber, auch wenn ich langsamer vorankomme.",
      "Es beruhigt mich zu wissen, was mich in den nächsten Jahren erwartet."],
     "Berechenbarkeit gibt Ihnen Ruhe und Energie. Suchen Sie grosse oder öffentliche Arbeitgeber, unbefristete "
     "Verträge, klare Leistungen. Vorsicht bei variablem Einkommen und riskanten Start-ups."),
    ("EC", "Unternehmerische Kreativität",
     ["Ich träume davon, etwas ganz Eigenes zu schaffen: eine Firma, ein Produkt.",
      "Es motiviert mich, eine Idee in ein funktionierendes Geschäft zu verwandeln.",
      "Ich bin bereit, Risiken einzugehen, um etwas Neues aufzubauen."],
     "Sie wollen etwas Eigenes schaffen. Suchen Sie Firmengründung, Intrapreneurship, Produkteinführungen. "
     "Vorsicht bei Rollen, in denen Sie nur pflegen, was andere geschaffen haben."),
    ("SV", "Dienst / Hingabe für eine Sache",
     ["Ich möchte, dass meine Arbeit zu einer Sache beiträgt, an die ich glaube.",
      "Ich würde eine schlechter bezahlte Stelle wählen, wenn sie Menschen oder der Umwelt hilft.",
      "Der Sinn meiner Arbeit zählt mehr als Titel oder Geld."],
     "Sinn und Wirkung zählen. Suchen Sie NGOs, den öffentlichen Sektor, Gesundheit, Bildung, Nachhaltigkeit oder "
     "Firmen mit einer klaren Mission. Vorsicht bei rein gewinnorientierten Umfeldern."),
    ("CH", "Totale Herausforderung",
     ["Mich reizen Probleme, die andere für unlösbar halten.",
      "Wenn die Arbeit zur Routine wird, langweile ich mich schnell.",
      "Wettbewerb und grosse Hindernisse geben mir Energie."],
     "Schwierige Probleme geben Ihnen Energie. Suchen Sie Transformationsprojekte, Beratung, Krisensituationen, "
     "ehrgeizige Ziele. Vorsicht bei Routine."),
    ("LS", "Lebensstilintegration",
     ["Ich möchte eine Laufbahn, die zu meinem Privatleben und meiner Familie passt, nicht umgekehrt.",
      "Ich würde einen Umzug oder eine Beförderung ablehnen, die mein Privatleben aus dem Gleichgewicht bringt.",
      "Flexible Arbeitszeiten sind für mich eine Bedingung, kein Bonus."],
     "Die Laufbahn muss sich ins Leben einfügen. Suchen Sie flexible Arbeitszeiten, Teilzeit, Remote-Arbeit, "
     "Arbeitgeber mit einer Kultur der Balance. Vorsicht bei Kulturen ständiger Erreichbarkeit."),
]

B5 = [  # Mini-IPIP (Donnellan et al., 2006), eigene Übersetzung, Originalreihenfolge
    ("E", "+", "Auf Partys stehe ich oft im Mittelpunkt."),
    ("A", "+", "Ich kann mich in die Gefühle anderer einfühlen."),
    ("C", "+", "Ich erledige Aufgaben sofort."),
    ("N", "+", "Meine Stimmung schwankt häufig."),
    ("O", "+", "Ich habe eine lebhafte Fantasie."),
    ("E", "−", "Ich rede nicht viel."),
    ("A", "−", "Die Probleme anderer interessieren mich nicht."),
    ("C", "−", "Ich vergesse oft, Dinge an ihren Platz zurückzulegen."),
    ("N", "−", "Ich bin die meiste Zeit entspannt."),
    ("O", "−", "Abstrakte Ideen interessieren mich nicht."),
    ("E", "+", "Auf Partys spreche ich mit vielen verschiedenen Leuten."),
    ("A", "+", "Ich spüre die Gefühle anderer."),
    ("C", "+", "Ich mag Ordnung."),
    ("N", "+", "Ich rege mich leicht auf."),
    ("O", "−", "Ich habe Mühe, abstrakte Ideen zu verstehen."),
    ("E", "−", "Ich halte mich meist im Hintergrund."),
    ("A", "−", "Andere Menschen interessieren mich nicht wirklich."),
    ("C", "−", "Ich bringe oft Dinge durcheinander."),
    ("N", "−", "Ich fühle mich selten niedergeschlagen."),
    ("O", "−", "Ich habe keine gute Vorstellungskraft."),
]
B5_NAME = {"E": "Extraversion", "A": "Verträglichkeit", "C": "Gewissenhaftigkeit", "N": "Neurotizismus",
           "O": "Intellekt / Offenheit"}

SDT = {
    "Autonomie": ["Ich konnte weitgehend selbst entscheiden, wie ich meine Arbeit organisiere.",
                  "Ich hatte das Gefühl, das zu tun, weil ich es wähle, nicht weil ich muss.",
                  "Meine Ideen und Meinungen wurden berücksichtigt."],
    "Kompetenz": ["Ich fühlte mich fähig und wirksam in dem, was ich tat.",
                  "Ich hatte Gelegenheit, Neues zu lernen und mich zu entwickeln.",
                  "Ich erhielt klare Rückmeldungen, dass ich gute Arbeit leiste."],
    "Verbundenheit": ["Ich fühlte mich als Teil eines Teams.",
                      "Ich hatte bei der Arbeit Menschen, denen ich vertraute.",
                      "Mir lag an meinen Kolleginnen und Kollegen, und ich spürte, dass ihnen auch an mir lag."],
}

CTX = [
    ("Ich arbeite am besten allein", "Ich arbeite am besten im Team"),
    ("Klare, genau definierte Aufgaben", "Offene, mehrdeutige Probleme"),
    ("Gleichmässiges, berechenbares Tempo", "Hohes Tempo mit Dringlichkeiten"),
    ("Im Büro oder zu Hause", "Im Aussendienst, unterwegs"),
    ("Wenig Kundenkontakt", "Täglicher Kundenkontakt"),
    ("Grosse, strukturierte Organisation", "Kleine, flexible Organisation"),
    ("Spezialist/in in der Tiefe", "Generalist/in mit vielen Themen"),
    ("Langfristige Ergebnisse", "Schnelle, sichtbare Ergebnisse"),
    ("Individuelle Fachperson", "Führungsperson"),
    ("Fester, berechenbarer Lohn", "Variables, leistungsabhängiges Einkommen"),
]

ADAPT = {
    "Planung (nach vorne schauen)": ["Ich denke darüber nach, wie meine Arbeit in fünf Jahren aussehen wird.",
                                     "Ich bereite meine nächsten Laufbahnschritte frühzeitig vor.",
                                     "Ich weiss, welche Kompetenzen in meinem Gebiet gefragt sein werden."],
    "Kontrolle (selbst entscheiden)": ["Ich treffe wichtige Entscheidungen über meine Laufbahn selbst.",
                                       "Ich übernehme die Verantwortung für meinen beruflichen Weg.",
                                       "Ich bleibe meinen Überzeugungen treu, wenn ich entscheide."],
    "Neugier (erkunden)": ["Ich erkunde aktiv neue berufliche Möglichkeiten.",
                           "Ich suche Lerngelegenheiten ausserhalb meiner Rolle.",
                           "Ich frage andere, wie in ihren Bereichen gearbeitet wird."],
    "Zuversicht (können)": ["Ich bringe Aufgaben zu Ende, auch wenn sie schwierig sind.",
                            "Ich lerne schnell neue Fähigkeiten, wenn es nötig ist.",
                            "Ich finde Lösungen, wenn es nicht nach Plan läuft."],
}

OPEN = [
    ("Vorbild", "Wen haben Sie als Kind oder Jugendliche/r bewundert (ausser Ihren Eltern)? Was genau haben Sie "
     "bewundert?", "das ideale Selbst: Eigenschaften, die Sie verkörpern möchten"),
    ("Lieblingsmedien", "Welche Zeitschriften, Websites, Kanäle oder Podcasts verfolgen Sie gern? Was zieht Sie "
     "daran an?", "Umfelder und Arten von Problemen, die Sie anziehen"),
    ("Lieblingsgeschichte", "Was ist Ihre Lieblingsgeschichte (Buch, Film, Serie)? Erzählen Sie sie kurz.",
     "das Drehbuch, dem Sie folgen könnten, um weiterzukommen"),
    ("Motto", "Haben Sie ein Motto oder einen Spruch, der Sie leitet?", "der Rat, den Sie sich selbst geben"),
    ("Flow", "Wann haben Sie zuletzt bei einer Tätigkeit die Zeit vergessen? Was haben Sie gemacht?",
     "eine Tätigkeit mit starker innerer Motivation"),
]

OCC = [
    ("Softwareentwickler/in", "ICR"), ("IT-/Solution-Architekt/in", "IEC"), ("DevOps / Cloud Engineer", "RIC"),
    ("Data Scientist", "ICA"), ("Data Engineer", "CIR"), ("IT-Security Specialist/in", "CIE"),
    ("System-/Netzwerkadministrator/in", "RCI"), ("Business Analyst/in", "ICE"), ("IT-Projektleiter/in", "ECI"),
    ("Product Owner / Product Manager/in", "EIA"), ("IT-Consultant/in", "EIC"), ("Scrum Master / Agile Coach", "SEI"),
    ("UX/UI Designer/in", "AIE"), ("Technische/r Redaktor/in", "AIC"),
    ("IT-Trainer/in, Erwachsenenbildner/in", "SIE"), ("Informatiklehrer/in", "SIA"),
    ("Qualitätsmanager/in", "CIR"), ("Elektroingenieur/in", "IRC"), ("Maschinenbauingenieur/in", "RIC"),
    ("Bauingenieur/in", "RIC"), ("Automationsingenieur/in", "RIC"), ("Mechatroniker/in", "RCI"),
    ("Elektroinstallateur/in", "RIC"), ("Energieberater/in", "IER"), ("Umweltingenieur/in", "IRS"),
    ("Laborant/in", "IRC"), ("Wissenschaftler/in", "IAR"), ("Architekt/in", "AIR"), ("Grafiker/in", "AER"),
    ("Fotograf/in / Videograf/in", "ARE"), ("Journalist/in", "AES"), ("Übersetzer/in", "AIC"),
    ("Musiker/in", "AES"), ("Lehrer/in", "SAE"), ("Sozialarbeiter/in", "SEA"), ("Laufbahnberater/in", "SAI"),
    ("Psychologe / Psychologin", "ISA"), ("Pflegefachfrau / Pflegefachmann", "SIR"), ("Physiotherapeut/in", "SRI"),
    ("Arzt / Ärztin", "ISR"), ("HR-Fachperson / Recruiter/in", "SEC"), ("Verkaufsberater/in", "ESC"),
    ("Key Account Manager/in", "ECS"), ("Unternehmer/in / Gründer/in", "EAI"), ("Marketingmanager/in", "EAC"),
    ("Buchhalter/in / Treuhänder/in", "CEI"), ("Controller/in", "CIE"), ("Sachbearbeiter/in", "CES"),
    ("Logistiker/in / Supply Chain Specialist", "CER"), ("Hotelfachfrau / Hotelfachmann", "ESC"),
    ("Koch / Köchin", "RAE"), ("Polizist/in", "RES"), ("Landschaftsgärtner/in", "RAC"), ("Schreiner/in", "RAC"),
    ("Förster/in", "RIS"), ("Pilot/in", "RIE"),
]

SC_LIKE = ["Gar nicht", "Wenig", "Neutral", "Gern", "Sehr gern"]
SC_CONF = ["Gar nicht sicher: noch nie gemacht", "Wenig: versucht, mit Mühe", "Mittel: mit etwas Hilfe",
           "Sicher: selbstständig gemacht", "Sehr sicher: andere fragen mich um Hilfe"]
SC_TRUE = ["Trifft gar nicht zu", "Trifft wenig zu", "Trifft teilweise zu", "Trifft weitgehend zu", "Trifft völlig zu"]
SC_DESC = ["Gar nicht", "Wenig", "Teilweise", "Weitgehend", "Sehr gut"]
SC_STR = ["Gar nicht", "Schwach", "Mittel", "Stark", "Sehr stark"]

n_int = sum(len(v) for v in INT.values())
n_conf = sum(len(v) for v in CONF.values())
n_anc = sum(len(a[2]) for a in ANCHORS)
n_sdt = sum(len(v) for v in SDT.values())
n_ad = sum(len(v) for v in ADAPT.values())
n_closed = n_int + n_conf + n_anc + len(B5) + n_sdt + len(CTX) + n_ad + 2

# ------------------------------------------------------------------ Dokument

P("Berufskompass", title)
P("Test zur beruflichen Orientierung: Fragen, Antwortoptionen und Auswertungsmethode · Version 1 (Entwurf zur "
  "Durchsicht) · Oktober 2026 · deutsche Fassung von «Busola Vocațională»", subtitle)

P("Zweck des Tests", h1)
P("Der Berufskompass verfolgt dasselbe Ziel wie das Laufbahn Mosaik: Er zeigt, welche beruflichen Richtungen zu "
  "Ihnen passen. Der Unterschied: Er stützt sich auf Modelle mit jahrzehntelanger Forschung und misst mehr als "
  "Interessen. Er betrachtet fünf Dinge: <b>was Sie gern tun</b> (Interessen), <b>was Sie sich zutrauen</b> "
  "(Selbstwirksamkeit), <b>worauf Sie nicht verzichten würden</b> (Karriereanker), <b>wie Sie sind und arbeiten</b> "
  "(Persönlichkeit, Arbeitsumfeld, psychologische Grundbedürfnisse) und <b>wie Sie Ihre Laufbahn steuern</b> "
  "(Anpassungsfähigkeit). Dazu kommen offene Fragen zu Ihrer Geschichte.")
P("Das Ergebnis ist kein Urteil. Es ist eine Reihe gut begründeter Hypothesen, die Sie danach mit kleinen "
  "Experimenten in der realen Welt prüfen: Informationsgespräche, Probeprojekte, kurze Kurse.")

P("Was er besser macht als das Laufbahn Mosaik", h1)
table([
    ["Was das Laufbahn Mosaik einschränkt", "Was der Berufskompass macht"],
    ["Eigenes Modell («Grundstreben») ohne veröffentlichte Validierung.",
     "Er nutzt breit erforschte Modelle: RIASEC (Holland), Big Five, die Karriereanker nach Schein, die "
     "sozial-kognitive Laufbahntheorie, die Selbstbestimmungstheorie, die Laufbahn-Anpassungsfähigkeit (Savickas)."],
    ["Nur 4 Fragen pro Berufsfeld, je eine pro Teilbereich: instabile Werte.",
     "8 Fragen pro Interessentyp, aus denen zuverlässigere Werte berechnet werden."],
    ["«Wie gut können Sie das?» ist eine vage Selbsteinschätzung, die man leicht über- oder unterschätzt.",
     "Die Antwortstufen beschreiben Tatsachen («selbstständig gemacht», «andere fragen mich um Hilfe»). Die "
     "verhaltensbezogene Verankerung verringert Verzerrungen."],
    ["Viele Tätigkeiten gehören zur Lehre oder zu Stereotypen (Mode, Kosmetik, Servieren).",
     "Tätigkeiten für Erwachsene, einschliesslich digitaler Arbeit, Führung, Beratung und Forschung."],
    ["Wie oft man Hobbys nachgeht, hängt von Zeit, Geld und Familie ab, nicht nur von Vorlieben.",
     "Das Interesse wird direkt gemessen; die Lebenssituation fliesst separat ein (Anker «Lebensstil», "
     "Arbeitsumfeld)."],
    ["Misst weder Werte, Motivation, Persönlichkeit noch Anpassungsfähigkeit.",
     "Eigene Module für jeden dieser Bereiche, dazu die Passung mit dem Arbeitsumfeld."],
    ["Prüft nicht, ob aufmerksam geantwortet wurde.",
     "Kontrollitems, Erkennung gleichförmiger Antworten, der Zustimmungstendenz und zu schneller Antworten."],
    ["Der Bericht zeigt Summen pro Berufsfeld, ohne die Form des Profils zu deuten.",
     "Holland-Code, Differenzierung, Konsistenz, Landkarte der Arbeitswelt, Matrix Interesse × Zutrauen, "
     "Berufsliste mit Passungsindex und Experimentierplan."],
    ["Lässt die Geschichte der Person ausser Acht.",
     "Fünf offene Fragen aus dem Career Construction Interview (Savickas) und aus der Flow-Forschung."],
], [70, 110])

P("Aufbau des Tests", h1)
table([
    ["Nr.", "Modul", "Was es misst", "Wissenschaftliche Grundlage", "Items", "Min."],
    ["1", "Interessen", "6 Interessentypen nach RIASEC", "Holland (1959, 1997); Format des O*NET Interest "
     "Profiler", f"{n_int} + 1 Kontrolle", "7"],
    ["2", "Zutrauen in die eigenen Fähigkeiten", "Selbstwirksamkeit in den 6 Typen", "Bandura (1977); Lent, Brown & "
     "Hackett (1994); Betz & Borgen (1996)", str(n_conf), "3"],
    ["3", "Karriereanker", "8 Anker + Wahl der 3 wichtigsten Aussagen", "Schein (1978, 1990)",
     f"{n_anc} + 3 Wahlen", "4"],
    ["4", "Persönlicher Stil", "Big Five", "Mini-IPIP, Donnellan et al. (2006); IPIP, Goldberg (1999)",
     f"{len(B5)} + 1 Kontrolle", "3"],
    ["5", "Was Ihnen gefehlt hat", "Bedürfnisse nach Autonomie, Kompetenz, Verbundenheit an der letzten Stelle",
     "Selbstbestimmungstheorie, Deci & Ryan (1985, 2000)", str(n_sdt), "1"],
    ["6", "Arbeitsumfeld", "10 Vorlieben, jeweils auf einer Achse mit zwei Polen", "Theorie der Arbeitsanpassung, "
     "Dawis & Lofquist (1984); O*NET Work Context", str(len(CTX)), "2"],
    ["7", "Anpassungsfähigkeit", "Planung, Kontrolle, Neugier, Zuversicht", "Savickas (2005); Savickas & Porfeli "
     "(2012)", str(n_ad), "2"],
    ["8", "Ihre Geschichte", "Lebensthemen, innere Motivation", "Savickas, Career Construction Interview; "
     "Csikszentmihalyi (1990)", "5 offen", "5"],
    ["", "<b>Total</b>", "", "", f"<b>{n_closed} geschlossen + 3 Wahlen + 5 offen</b>", "<b>~27</b>"],
], [9, 30, 45, 58, 26, 12])
SP(3)
P("Die Items jedes Moduls erscheinen gemischt: In jeder Runde kommt je ein Item jedes Typs, in zufälliger, aber "
  "für alle Befragten gleicher Reihenfolge. So sinkt der Positionseffekt, und man kann nicht erraten, welcher Typ "
  "gemessen wird. Unten sind die Items der Übersicht halber nach Typen gruppiert.", small)

# ---------------- Modul 1
P("Modul 1 · Interessen", h1)
P("<b>Frage:</b> «Wie gern würden Sie …» · <b>Anleitung:</b> Denken Sie nur daran, wie gern Sie die Tätigkeit "
  "ausüben würden. Ob Sie sie können oder was sie einbringt, spielt hier keine Rolle.")
scale_table(SC_LIKE)
for t in TYPES:
    P(f"<font color='{TYPE_COL[t]}'><b>{t}</b></font> · {TYPE_NAME[t]}: {TYPE_DESC[t]}", h3)
    table([["Code", "Tätigkeit"]] + [[f"{t}{i + 1}", x] for i, x in enumerate(INT[t])], [14, 166])
SP(4)
P("<b>Kontrollitem</b> (Position 29): «Bitte wählen Sie zur Kontrolle der Aufmerksamkeit in dieser Zeile ‹Gern›.» "
  "Richtige Antwort: 4.")

# ---------------- Modul 2
story.append(PageBreak())
P("Modul 2 · Zutrauen in die eigenen Fähigkeiten", h1)
P("<b>Frage:</b> «Wie sicher sind Sie, dass Sie das gut könnten?» · <b>Anleitung:</b> Antworten Sie aufgrund Ihrer "
  "tatsächlichen Erfahrung. Die Stufen beschreiben Tatsachen, keine Eindrücke.")
scale_table(SC_CONF)
table([["Code", "Typ", "Aufgabe"]] + [[f"K{t}{i + 1}", TYPE_NAME[t], x] for t in TYPES for i, x in enumerate(CONF[t])],
      [14, 30, 136])

# ---------------- Modul 3
P("Modul 3 · Karriereanker", h1)
P("<b>Frage:</b> «Wie sehr trifft das auf Sie zu?» · <b>Anleitung:</b> Ein Anker ist das, worauf Sie nicht "
  "verzichten würden, wenn Sie wählen müssten. Antworten Sie ehrlich, auch wenn manche Aussagen «schöner» klingen "
  "als andere.")
scale_table(SC_TRUE)
rows = [["Code", "Anker", "Aussage"]]
for code, name, items, _ in ANCHORS:
    for i, x in enumerate(items):
        rows.append([f"{code}{i + 1}", name if i == 0 else "", x])
table(rows, [14, 46, 120])
SP(4)
P("<b>Auswahlschritt.</b> Nach den 24 Aussagen sieht die befragte Person die Liste nach vergebenen Punkten geordnet "
  "und wählt <b>genau 3</b>, die am stärksten zutreffen. Die erzwungene Wahl trennt echte Anker von bloss "
  "«angenehmen» (Methode von Schein).")

# ---------------- Modul 4
story.append(PageBreak())
P("Modul 4 · Persönlicher Stil (Big Five)", h1)
P("<b>Frage:</b> «Wie gut beschreibt Sie die Aussage?» · <b>Anleitung:</b> Beschreiben Sie sich so, wie Sie "
  "gewöhnlich jetzt sind, nicht wie Sie gern wären.")
scale_table(SC_DESC)
table([["Nr.", "Aussage", "Merkmal", "Schlüssel"]] +
      [[str(i + 1), x, B5_NAME[t], "direkt" if k == "+" else "umgepolt"] for i, (t, k, x) in enumerate(B5)],
      [11, 107, 40, 22])
SP(3)
P("Mini-IPIP-Items aus dem International Personality Item Pool (gemeinfrei), eigene Übersetzung, in der "
  "Originalreihenfolge. <b>Kontrollitem</b> (nach Item 12): «Bitte wählen Sie zur Kontrolle der Aufmerksamkeit in "
  "dieser Zeile ‹Gar nicht›.» Richtige Antwort: 1.", small)

# ---------------- Modul 5
P("Modul 5 · Was Ihnen gefehlt hat (psychologische Grundbedürfnisse)", h1)
P("<b>Frage:</b> «Wenn Sie an Ihre letzte (oder aktuelle) Stelle denken:» · Skala: wie in Modul 3 (Trifft gar "
  "nicht zu … Trifft völlig zu).")
table([["Code", "Bedürfnis", "Aussage"]] +
      [[f"{n[0]}{i + 1}", n if i == 0 else "", x] for n, items in SDT.items() for i, x in enumerate(items)],
      [14, 30, 136])

# ---------------- Modul 6
P("Modul 6 · Arbeitsumfeld", h1)
P("<b>Frage:</b> «Wo stehen Sie zwischen den beiden Varianten?» · Skala: 1 = ganz die linke Variante, 3 = egal "
  "oder beides gleich, 5 = ganz die rechte Variante.")
table([["Code", "Pol 1", "1 · 2 · 3 · 4 · 5", "Pol 5"]] +
      [[f"U{i + 1}", l, "○ ○ ○ ○ ○", r] for i, (l, r) in enumerate(CTX)],
      [14, 66, 34, 66], style_extra=[("ALIGN", (2, 1), (2, -1), "CENTER")])

# ---------------- Modul 7
story.append(PageBreak())
P("Modul 7 · Laufbahn-Anpassungsfähigkeit", h1)
P("<b>Frage:</b> «Wie stark ist das bei Ihnen ausgeprägt?»")
scale_table(SC_STR)
rows = [["Code", "Dimension", "Aussage"]]
for j, (dim, items) in enumerate(ADAPT.items()):
    for i, x in enumerate(items):
        rows.append([f"L{j + 1}{i + 1}", dim if i == 0 else "", x])
table(rows, [14, 46, 120])

# ---------------- Modul 8
P("Modul 8 · Ihre Geschichte (offene, freiwillige Fragen)", h1)
P("Freie Antwort in einigen Sätzen. Die Fragen stammen aus dem Career Construction Interview (Mark Savickas) und "
  "aus der Flow-Forschung (Mihaly Csikszentmihalyi).")
table([["Code", "Frage", "Was sie zeigt"]] +
      [[f"G{i + 1}", f"<b>{n}.</b> {q}", w] for i, (n, q, w) in enumerate(OPEN)],
      [14, 104, 62])

# ---------------- Auswertung
story.append(PageBreak())
P("Auswertungsmethode", h1)

P("1. Allgemeine Bewertungsregeln", h2)
bullets([
    "Jede Antwort zählt 1–5 Punkte. Bei umgepolten Items (Big Five) wird der Wert zu 6 − Antwort.",
    "Der Wert einer Skala ist der Mittelwert ihrer Items. Für Vergleiche wird er auf 0–100 umgerechnet: "
    "(Mittelwert − 1) / 4 × 100.",
    "Kontrollitems fliessen nicht in die Werte ein; sie dienen nur der Prüfung der Datenqualität.",
])

P("2. Interessen: das RIASEC-Profil", h2)
bullets([
    "<b>Holland-Code</b> = die drei Typen mit den höchsten Interessenwerten (z. B. ICR). Bei Gleichstand "
    "entscheidet der Wert aus Modul 2.",
    "<b>Differenzierung</b> = höchster − tiefster Wert. ≥ 45: klares Profil; 25–45: mittel; &lt; 25: flach. Ein "
    "flaches Profil bedeutet entweder sehr breite Interessen oder noch unklare Vorlieben. In beiden Fällen sagen "
    "praktische Experimente mehr als Tests.",
    "<b>Konsistenz</b> = Abstand der beiden ersten Typen auf dem Hexagon R–I–A–S–E–C. Benachbarte Typen (1): hoch, "
    "sie finden leicht im selben Beruf zusammen. Abstand 2: mittel. Gegenüberliegende Typen (3): tief, eine "
    "seltene Kombination. Sie kann ein wertvolles Hybridprofil sein oder ein Zeichen, dass eine der Richtungen eher "
    "in die Freizeit gehört.",
    "<b>Niveau</b> = Mittelwert der 6 Werte. ≥ 65: breite Interessen; die Wahl erfolgt dann vor allem nach Werten "
    "(Ankern). ≤ 30: allgemein tiefes Niveau, das in Phasen von Stress, Erschöpfung oder Arbeitslosigkeit häufig "
    "vorkommt. Es bedeutet keinen Mangel an Potenzial; eine Wiederholung nach einigen Wochen lohnt sich.",
    "<b>Landkarte der Arbeitswelt</b> (Prediger, 1982). Die Werte werden zentriert (jeder Wert minus Mittelwert der "
    "6), dann: <b>Daten ↔ Ideen</b> = 1,73 × (E + C − I − A); <b>Menschen ↔ Dinge</b> = A + 2S + E − C − 2R − I. "
    "Person und Berufe erscheinen auf derselben Karte mit zwei Achsen: Arbeit mit Daten oder mit Ideen, mit "
    "Menschen oder mit Dingen.",
])

P("3. Interesse × Zutrauen (sozial-kognitive Laufbahntheorie)", h2)
P("Für jeden RIASEC-Typ wird das Interesse mit dem Zutrauen verglichen. Als Schwellen dienen die persönlichen "
  "Mittelwerte beider Werte, weil relativ zum eigenen Profil gedeutet wird.")
table([
    ["", "Zutrauen über Ihrem Mittel", "Zutrauen unter Ihrem Mittel"],
    ["<b>Interesse über Ihrem Mittel</b>", "<b>Eigenes Terrain.</b> Richtungen, die Sie sofort nutzen können.",
     "<b>Terrain zum Erobern.</b> Ein Kurs oder ein begleitetes Projekt stärkt die Selbstwirksamkeit, den "
     "wichtigsten Motor der Laufbahnwahl (Lent et al., 1994)."],
    ["<b>Interesse unter Ihrem Mittel</b>", "<b>Können ohne Lust.</b> Sie sind gut darin, aber eine Laufbahn, die "
     "nur darauf aufbaut, birgt das Risiko von Erschöpfung und Langeweile.",
     "<b>Abseits des Weges.</b> Lohnt jetzt keine Investition."],
], [44, 68, 68])

P("4. Karriereanker", h2)
bullets([
    "Ankerwert = (Summe der 3 Items + 4 × Anzahl seiner Items unter den gewählten Top 3) / 3. Bereich 1–9.",
    "Hauptanker = höchster Wert. Der Bericht beschreibt ihn und sagt, worauf bei einer Stelle zu achten ist und "
    "wovor man sich hüten sollte:",
])
table([["Anker", "Was das für die Stellenwahl bedeutet"]] + [[f"<b>{n}</b>", d] for _, n, _, d in ANCHORS], [48, 132])

P("5. Persönlicher Stil (Big Five)", h2)
bullets([
    "Mittelwert pro Merkmal auf der Skala 1–5, umgepolte Items umcodiert. Neurotizismus wird als <b>emotionale "
    "Stabilität</b> (6 − Wert) berichtet, eine Formulierung, die nicht pathologisiert.",
    "Bänder: &lt; 2,5 tief, 2,5–3,5 mittel, &gt; 3,5 hoch. Ohne Bevölkerungsnormen ist die Deutung absolut und "
    "vorsichtig. Jedes Band erhält eine Folgerung für die Arbeit, zum Beispiel: Gewissenhaftigkeit ist der "
    "beständigste Prädiktor der Arbeitsleistung (Barrick & Mount, 1991); Introversion begünstigt Rollen mit tiefer "
    "Konzentration.",
    "Die emotionale Stabilität wird von der momentanen Lage beeinflusst, etwa von der Stellensuche. Der Bericht "
    "sagt das ausdrücklich.",
])

P("6. Bedürfnisse, Arbeitsumfeld, Anpassungsfähigkeit", h2)
bullets([
    "<b>Bedürfnisse</b>: Mittelwert pro Bedürfnis. Unter 3 = an der letzten Stelle unerfülltes Bedürfnis. Es wird "
    "zum vorrangigen Kriterium für die nächste Stelle (z. B. fehlende Autonomie → Rollen mit Freiheit in der "
    "Umsetzung suchen).",
    "<b>Arbeitsumfeld</b>: 1–2 oder 4–5 = klare Vorliebe, 3 = flexibel. Klare Vorlieben werden zu Filtern bei der "
    "Beurteilung von Stellenangeboten.",
    "<b>Anpassungsfähigkeit</b>: Mittelwert pro Dimension. Die tiefste erhält eine konkrete Massnahme (z. B. tiefe "
    "Neugier → drei Informationsgespräche in zwei Wochen).",
])

P("7. Passung mit Berufen", h2)
bullets([
    "Jeder Beruf hat einen RIASEC-Code (angenähert nach O*NET; Liste im Anhang). Der Code wird zu einem Vektor: "
    "erster Buchstabe = 1,00; zweiter = 0,65; dritter = 0,40; die übrigen drei = 0,10.",
    "Berechnet wird die Pearson-Korrelation zwischen dem Berufsvektor und dem Interessenprofil (rI), dann dem "
    "Zutrauensprofil (rZ). Die Korrelation vergleicht die <b>Form</b> des Profils, nicht das Niveau. Es spielt also "
    "keine Rolle, ob jemand generell hohe oder tiefe Werte gibt.",
    "<b>Passungsindex</b> = (0,7 × rI + 0,3 × rZ + 1) / 2 × 100. Bänder: ≥ 80 sehr gut; 65–80 gut; 50–65 teilweise; "
    "&lt; 50 schwach. Das Interesse hat das grössere Gewicht, weil es Zufriedenheit und Leistung voraussagt "
    "(Nye et al., 2012).",
    "Danach wird die Liste nach Hauptanker und Umfeldvorlieben gefiltert. Beispiele: Der Anker «Selbstständigkeit» "
    "rückt Beratungs- oder Freelance-Varianten nach vorn; eine Vorliebe für Einzelarbeit kennzeichnet Rollen mit "
    "vielen Sitzungen.",
])

P("8. Datenqualität", h2)
table([
    ["Prüfung", "Regel", "Schweregrad"],
    ["Kontrollitems", "Jede falsche Antwort", "schwer"],
    ["Gleichförmige Antworten", "Mindestens 2 Seiten mit derselben Antwort bei allen Items", "schwer"],
    ["Tempo", "Im Schnitt unter 1,8 Sekunden pro Item", "schwer"],
    ["Zustimmungstendenz", "Rohmittelwert der Big-Five-Items ≥ 3,8 oder ≤ 2,2 (die Items sind in der Richtung "
     "ausgewogen, ein extremer Mittelwert deutet daher auf einen Antwortstil hin)", "Hinweis"],
], [38, 112, 30])
SP(3)
P("Urteil: <b>Gut</b> (keine Probleme), <b>Gut, mit Hinweisen</b> (nur Hinweise) oder <b>Mit Vorsicht deuten</b> "
  "(mindestens ein schweres Problem). Gestützt auf die Forschung zu unaufmerksamen Antworten (Meade & Craig, 2012).",
  small)

P("9. Die offenen Antworten", h2)
P("Sie werden qualitativ nach der Methode von Savickas ausgewertet. Das Vorbild zeigt das ideale Selbst. Die "
  "Lieblingsmedien zeigen, welche Arten von Problemen anziehen. Die Lieblingsgeschichte zeigt das Drehbuch, dem die "
  "Person folgen könnte. Das Motto ist der Rat, den sie sich selbst gibt, und der Flow-Moment zeigt die innere "
  "Motivation. Die gefundenen Themen werden mit dem quantitativen Profil verglichen. Wo sie übereinstimmen, ist die "
  "Schlussfolgerung solider; wo sie abweichen, entsteht eine Frage zum Erkunden, kein Fehler.")

P("Aufbau des Schlussberichts", h1)
bullets([
    "<b>Zusammenfassung</b>: Holland-Code, Hauptanker, die drei passendsten Berufe, Urteil zur Datenqualität.",
    "<b>Interessen</b>: RIASEC-Hexagon (Interesse und Zutrauen überlagert), Differenzierung, Konsistenz, Niveau.",
    "<b>Landkarte der Arbeitswelt</b>: Position der Person und der Berufe auf den Achsen Daten/Ideen und "
    "Menschen/Dinge.",
    "<b>Matrix Interesse × Zutrauen</b> mit den vier Feldern und dem, was in jedem zu tun ist.",
    "<b>Karriereanker</b>: Rangfolge der 8 Anker und Beschreibung der ersten zwei.",
    "<b>Persönlicher Stil</b>, <b>unerfüllte Bedürfnisse</b>, <b>bevorzugtes Umfeld</b>, "
    "<b>Anpassungsfähigkeit</b>: jeweils mit konkreten Folgerungen.",
    "<b>Passende Berufe</b>: Top 15 mit Bezeichnung (für die Suche auf Stellenportalen), Code, Passungsindex und "
    "Begründung.",
    "<b>Experimentierplan</b> für 2–4 Wochen zu den ersten Richtungen: Informationsgespräch, Probeprojekt, kurzer "
    "Kurs (Ibarra, 2003; Burnett & Evans, 2016).",
    "<b>Grenzen</b> und die gegebenen Antworten, zur Transparenz.",
])

P("Grenzen und Schritte zur Validierung", h1)
bullets([
    "Die Items sind neu, ausser den Mini-IPIP-Items. Die gemessenen Konstrukte sind in der Literatur validiert, "
    "diese Formulierung der Items jedoch noch nicht empirisch.",
    "Für eine Validierung braucht es: eine Pilotstudie mit mindestens 200 Personen; interne Konsistenz (Cronbachs "
    "Alpha ≥ 0,70 pro Skala); eine Faktorenanalyse, die die Struktur bestätigt; einen Test-Retest nach 4–6 Wochen; "
    "den Vergleich mit etablierten Instrumenten, etwa dem O*NET Interest Profiler; Normen nach Altersgruppen.",
    "Jede Selbsteinschätzung wird von der momentanen Stimmung und vom Selbstbild beeinflusst. Das Ergebnis ist ein "
    "Ausgangspunkt für die Erkundung, kein Urteil.",
])

P("Literatur", h1)
refs = [
    "Bandura, A. (1977). Self-efficacy: Toward a unifying theory of behavioral change. <i>Psychological Review, 84</i>(2).",
    "Barrick, M. R., & Mount, M. K. (1991). The Big Five personality dimensions and job performance: A meta-analysis. "
    "<i>Personnel Psychology, 44</i>(1).",
    "Betz, N. E., Borgen, F. H., & Harmon, L. W. (1996). <i>Skills Confidence Inventory</i>. Consulting Psychologists Press.",
    "Burnett, B., & Evans, D. (2016). <i>Designing Your Life</i>. Knopf.",
    "Csikszentmihalyi, M. (1990). <i>Flow: The Psychology of Optimal Experience</i>. Harper & Row.",
    "Dawis, R. V., & Lofquist, L. H. (1984). <i>A Psychological Theory of Work Adjustment</i>. University of Minnesota Press.",
    "Deci, E. L., & Ryan, R. M. (2000). The «what» and «why» of goal pursuits. <i>Psychological Inquiry, 11</i>(4).",
    "Donnellan, M. B., Oswald, F. L., Baird, B. M., & Lucas, R. E. (2006). The Mini-IPIP scales. "
    "<i>Psychological Assessment, 18</i>(2).",
    "Goldberg, L. R. (1999). A broad-bandwidth, public domain, personality inventory. In <i>Personality Psychology in "
    "Europe, 7</i>.",
    "Holland, J. L. (1997). <i>Making Vocational Choices</i> (3. Aufl.). Psychological Assessment Resources.",
    "Ibarra, H. (2003). <i>Working Identity</i>. Harvard Business School Press.",
    "Lent, R. W., Brown, S. D., & Hackett, G. (1994). Toward a unifying social cognitive theory of career and academic "
    "interest, choice, and performance. <i>Journal of Vocational Behavior, 45</i>(1).",
    "Meade, A. W., & Craig, S. B. (2012). Identifying careless responses in survey data. <i>Psychological Methods, 17</i>(3).",
    "Nye, C. D., Su, R., Rounds, J., & Drasgow, F. (2012). Vocational interests and performance: A quantitative summary "
    "of over 60 years of research. <i>Perspectives on Psychological Science, 7</i>(4).",
    "Prediger, D. J. (1982). Dimensions underlying Holland's hexagon. <i>Journal of Vocational Behavior, 21</i>(3).",
    "Savickas, M. L. (2005). The theory and practice of career construction. In Brown & Lent (Hrsg.), <i>Career "
    "Development and Counseling</i>. Wiley.",
    "Savickas, M. L., & Porfeli, E. J. (2012). Career Adapt-Abilities Scale. <i>Journal of Vocational Behavior, 80</i>(3).",
    "Schein, E. H. (1990). <i>Career Anchors: Discovering Your Real Values</i>. Pfeiffer.",
]
for r in refs:
    story.append(Paragraph(r, ParagraphStyle("ref", parent=small, leftIndent=12, firstLineIndent=-12, textColor=INK)))

story.append(PageBreak())
P("Anhang · Berufe und RIASEC-Codes", h1)
P("Die Codes sind nach O*NET angenähert (Reihenfolge der Buchstaben = Gewicht des Typs). Die Bezeichnungen eignen "
  "sich als Suchbegriffe auf Stellenportalen. Die Liste lässt sich erweitern, ohne die Methode zu ändern.", small)
table([["Nr.", "Beruf", "Code"]] + [[str(i + 1), de, f"<b>{c}</b>"] for i, (de, c) in enumerate(OCC)], [12, 140, 28])


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Arial", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(15 * mm, 9 * mm, "Berufskompass · v1 Entwurf")
    canvas.drawRightString(195 * mm, 9 * mm, f"Seite {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(OUT, pagesize=A4, topMargin=15 * mm, bottomMargin=16 * mm, leftMargin=15 * mm,
                        rightMargin=15 * mm, title="Berufskompass - Test")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("OK", OUT, "closed items:", n_closed, "occupations:", len(OCC))
