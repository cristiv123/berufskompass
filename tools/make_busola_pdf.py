# -*- coding: utf-8 -*-
import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, KeepTogether)
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

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "busola_vocationala_test.pdf")

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


def table(rows, widths, header=True, style_extra=None, font=cell):
    data = [[c if not isinstance(c, str) else Paragraph(c, cellb if (header and r == 0) else font)
             for c in row] for r, row in enumerate(rows)]
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
    rows = [["Punctaj"] + [str(i + 1) for i in range(len(options))], ["Variantă"] + options]
    table(rows, [20] + [32] * len(options), header=True)


# ------------------------------------------------------------------ content

TYPES = ["R", "I", "A", "S", "E", "C"]
TYPE_NAME = {"R": "Realist", "I": "Investigativ", "A": "Artistic", "S": "Social", "E": "Întreprinzător",
             "C": "Convențional"}
TYPE_DESC = {
    "R": "lucru cu mâinile, unelte, mașini, natură; rezultate concrete",
    "I": "analiză, cercetare, înțelegerea felului în care funcționează lucrurile",
    "A": "creație, expresie, design, lucru fără reguli fixe",
    "S": "a învăța, a sprijini, a îngriji și a consilia oameni",
    "E": "a convinge, a conduce, a vinde, a-ți asuma riscuri",
    "C": "structură, date, proceduri, precizie și control",
}

INT = {
    "R": ["Să repari sau să întreții echipamente, mașini sau aparate.",
          "Să montezi, să conectezi și să pui în funcțiune o instalație tehnică.",
          "Să lucrezi cu unelte într-un atelier (lemn, metal, electronică).",
          "Să lucrezi în aer liber: pe un șantier, într-o pădure sau la o fermă.",
          "Să conduci sau să operezi vehicule, drone sau utilaje.",
          "Să construiești ceva fizic de la zero, după un plan.",
          "Să afli de ce nu funcționează un dispozitiv și să-l repari cu mâinile tale.",
          "Să îngrijești plante, animale sau un teren."],
    "I": ["Să analizezi date ca să găsești o tendință sau o cauză ascunsă.",
          "Să înțelegi în profunzime cum funcționează un sistem complex.",
          "Să faci experimente și să testezi ipoteze.",
          "Să citești studii științifice sau tehnice din domeniul tău.",
          "Să rezolvi o problemă logică dificilă pentru care nu există încă o soluție.",
          "Să construiești un model matematic sau statistic.",
          "Să investighezi cauza principală a unei defecțiuni sau a unui incident.",
          "Să înveți singur(ă) o tehnologie sau o teorie nouă, până o stăpânești."],
    "A": ["Să proiectezi aspectul vizual al unui produs, al unei aplicații sau al unui spațiu.",
          "Să scrii texte, povești sau articole.",
          "Să compui, să cânți sau să produci muzică.",
          "Să fotografiezi, să filmezi sau să montezi video.",
          "Să inventezi un concept sau o idee complet nouă.",
          "Să joci un rol, să prezinți sau să improvizezi în fața unui public.",
          "Să lucrezi fără reguli fixe, acolo unde stilul personal contează.",
          "Să desenezi, să pictezi sau să creezi obiecte decorative."],
    "S": ["Să explici ceva complicat cuiva care abia începe.",
          "Să ajuți o persoană să treacă printr-o perioadă dificilă.",
          "Să ții un curs sau un workshop.",
          "Să îngrijești persoane bolnave, în vârstă sau cu dizabilități.",
          "Să mediezi un conflict între două persoane.",
          "Să fii mentor pentru un coleg mai tânăr.",
          "Să lucrezi la un proiect care îmbunătățește viața unei comunități.",
          "Să asculți și să consiliezi oameni care îți cer sfatul."],
    "E": ["Să convingi un client să aleagă soluția ta.",
          "Să conduci o echipă spre un obiectiv ambițios.",
          "Să pornești propria afacere sau propriul proiect.",
          "Să negociezi un contract, un preț sau un salariu.",
          "Să prezinți o idee în fața conducerii ca să obții buget.",
          "Să iei decizii rapide cu informații incomplete.",
          "Să-ți construiești o rețea de contacte profesionale.",
          "Să concurezi pentru rezultate măsurabile (vânzări, cotă de piață)."],
    "C": ["Să ții evidența exactă a cifrelor, documentelor sau stocurilor.",
          "Să verifici dacă un proces respectă regulile și standardele.",
          "Să organizezi informații în tabele, baze de date sau arhive.",
          "Să întocmești bugete, facturi sau rapoarte financiare.",
          "Să urmezi o procedură clară, pas cu pas, fără greșeli.",
          "Să planifici calendare, termene și resurse.",
          "Să controlezi calitatea unui produs sau a unei documentații.",
          "Să pui ordine într-un sistem haotic de fișiere, date sau procese."],
}

CONF = {
    "R": ["Să depanezi un aparat electric sau electronic.",
          "Să folosești în siguranță scule electrice.",
          "Să citești un plan tehnic și să lucrezi după el.",
          "Să montezi mobilier sau o instalație simplă fără instrucțiuni detaliate."],
    "I": ["Să analizezi un set de date și să tragi concluzii corecte.",
          "Să înțelegi un articol științific sau o documentație tehnică densă.",
          "Să găsești cauza unei probleme complexe, eliminând sistematic ipotezele.",
          "Să folosești statistica sau matematica pentru o problemă reală."],
    "A": ["Să creezi un design vizual care arată profesionist.",
          "Să scrii un text care captează atenția.",
          "Să vii cu idei originale când ceilalți sunt blocați.",
          "Să exprimi o idee prin imagine, sunet sau mișcare."],
    "S": ["Să predai ceva unui grup astfel încât toți să înțeleagă.",
          "Să calmezi o persoană supărată.",
          "Să-ți dai seama ce simte cineva fără să ți-o spună.",
          "Să sprijini pe cineva să-și atingă un obiectiv personal."],
    "E": ["Să convingi un grup sceptic.",
          "Să conduci o ședință până la o decizie.",
          "Să negociezi un acord bun pentru tine.",
          "Să vinzi un produs sau un serviciu."],
    "C": ["Să ții un buget sau o evidență fără erori.",
          "Să creezi un sistem de organizare pe care îl folosesc și alții.",
          "Să lucrezi cu tabele Excel complexe.",
          "Să respecți termene și proceduri stricte."],
}

ANCHORS = [
    ("TF", "Competență tehnică / funcțională",
     ["Vreau să ajung un expert căutat în specialitatea mea.",
      "Mă simt cel mai împlinit(ă) când îmi folosesc la nivel înalt abilitățile de specialitate.",
      "Aș refuza o promovare care m-ar scoate din domeniul meu de expertiză."],
     "Identitatea profesională vine din a fi foarte bun(ă) într-un domeniu. Caută roluri de expert și căi de "
     "carieră tehnice, nu doar manageriale. Atenție la promovările spre management pur."),
    ("GM", "Management general",
     ["Vreau să ajung să conduc o organizație sau un departament întreg.",
      "Mă atrage responsabilitatea pentru rezultatele unei echipe întregi.",
      "Prefer să integrez munca altora decât să fiu specialist într-un singur lucru."],
     "Te motivează responsabilitatea, integrarea și rezultatele organizației. Caută roluri cu echipă și buget. "
     "Atenție la rolurile de specialist izolat."),
    ("AU", "Autonomie / independență",
     ["Vreau să decid singur(ă) cum, când și unde îmi fac munca.",
      "Regulile și procedurile rigide ale organizațiilor mă apasă.",
      "Aș renunța la siguranța unui post fix pentru mai multă libertate."],
     "Ai nevoie să-ți controlezi modul de lucru. Caută freelancing, consultanță, remote, obiective clare cu "
     "libertate în execuție. Atenție la microcontrol."),
    ("SE", "Securitate / stabilitate",
     ["Siguranța locului de muncă și a venitului este foarte importantă pentru mine.",
      "Prefer un angajator stabil, chiar dacă avansez mai încet.",
      "Mă liniștește să știu la ce să mă aștept în următorii ani."],
     "Predictibilitatea îți dă liniște și energie. Caută angajatori mari sau publici, contracte pe durată "
     "nedeterminată, beneficii clare. Atenție la venitul variabil și la startup-urile riscante."),
    ("EC", "Creativitate antreprenorială",
     ["Visez să creez ceva complet al meu: o firmă, un produs.",
      "Mă motivează să transform o idee într-o afacere care funcționează.",
      "Sunt dispus(ă) să risc ca să construiesc ceva nou."],
     "Vrei să creezi ceva al tău. Caută fondarea unei firme, intraprenoriat, lansări de produse. Atenție la "
     "rolurile în care doar întreții ce au creat alții."),
    ("SV", "Serviciu / dedicare unei cauze",
     ["Vreau ca munca mea să contribuie la o cauză în care cred.",
      "Aș alege un post mai prost plătit dacă ar ajuta oamenii sau mediul.",
      "Sensul a ceea ce fac contează mai mult decât titlul sau banii."],
     "Contează sensul și impactul. Caută ONG-uri, sectorul public, sănătate, educație, sustenabilitate sau "
     "companii cu o misiune clară. Atenție la mediile orientate exclusiv spre profit."),
    ("CH", "Provocare pură",
     ["Mă atrag problemele pe care alții le consideră imposibile.",
      "Mă plictisesc repede când munca devine rutină.",
      "Competiția și obstacolele mari îmi dau energie."],
     "Te energizează problemele grele. Caută proiecte de transformare, consultanță, situații de criză, ținte "
     "ambițioase. Atenție la rutină."),
    ("LS", "Stil de viață",
     ["Vreau o carieră care se potrivește cu viața mea personală și cu familia, nu invers.",
      "Aș refuza o mutare sau o promovare care mi-ar dezechilibra viața privată.",
      "Flexibilitatea programului este pentru mine o condiție, nu un bonus."],
     "Cariera trebuie să se integreze în viață. Caută program flexibil, part-time, remote, angajatori cu o "
     "cultură a echilibrului. Atenție la culturile de tip „mereu disponibil”."),
]

B5 = [  # Mini-IPIP (Donnellan et al., 2006), traducere proprie; ordinea originală de administrare
    ("E", "+", "Sunt adesea sufletul petrecerilor."),
    ("A", "+", "Rezonez cu sentimentele celorlalți."),
    ("C", "+", "Îmi fac treburile imediat."),
    ("N", "+", "Am des schimbări bruște de dispoziție."),
    ("O", "+", "Am o imaginație bogată."),
    ("E", "−", "Nu vorbesc mult."),
    ("A", "−", "Nu mă interesează problemele altora."),
    ("C", "−", "Uit des să pun lucrurile la locul lor."),
    ("N", "−", "Sunt relaxat(ă) aproape tot timpul."),
    ("O", "−", "Nu mă interesează ideile abstracte."),
    ("E", "+", "La petreceri vorbesc cu mulți oameni diferiți."),
    ("A", "+", "Simt emoțiile celorlalți."),
    ("C", "+", "Îmi place ordinea."),
    ("N", "+", "Mă supăr ușor."),
    ("O", "−", "Îmi e greu să înțeleg ideile abstracte."),
    ("E", "−", "De obicei stau în plan secund."),
    ("A", "−", "Nu mă interesează cu adevărat ceilalți."),
    ("C", "−", "Încurc des lucrurile."),
    ("N", "−", "Rareori mă simt abătut(ă)."),
    ("O", "−", "Nu am o imaginație prea bună."),
]
B5_NAME = {"E": "Extraversie", "A": "Agreabilitate", "C": "Conștiinciozitate", "N": "Nevrotism",
           "O": "Intelect / imaginație"}

SDT = {
    "Autonomie": ["Puteam decide în mare parte cum îmi organizez munca.",
                  "Simțeam că fac ce fac pentru că aleg, nu pentru că sunt obligat(ă).",
                  "Ideile și opiniile mele erau luate în seamă."],
    "Competență": ["Mă simțeam capabil(ă) și eficient(ă) în ceea ce făceam.",
                   "Aveam ocazia să învăț lucruri noi și să cresc.",
                   "Primeam semnale clare că îmi fac treaba bine."],
    "Relaționare": ["Mă simțeam parte dintr-o echipă.",
                    "Aveam la muncă oameni în care aveam încredere.",
                    "Țineam la colegi și simțeam că și lor le pasă de mine."],
}

CTX = [
    ("Lucrez cel mai bine singur(ă)", "Lucrez cel mai bine în echipă"),
    ("Sarcini clare, bine definite", "Probleme deschise, ambigue"),
    ("Ritm constant, previzibil", "Ritm alert, cu urgențe"),
    ("La birou sau de acasă", "Pe teren, în mișcare"),
    ("Puțin contact cu clienții", "Contact zilnic cu clienții"),
    ("Organizație mare, structurată", "Organizație mică, flexibilă"),
    ("Specialist(ă) în profunzime", "Generalist(ă), multe subiecte"),
    ("Rezultate pe termen lung", "Rezultate rapide, vizibile"),
    ("Contribuitor individual", "Conducător de oameni"),
    ("Salariu fix, previzibil", "Venit variabil, legat de performanță"),
]

ADAPT = {
    "Preocupare (privești înainte)": ["Mă gândesc la cum va arăta munca mea peste cinci ani.",
                                      "Îmi pregătesc din timp pașii următori în carieră.",
                                      "Știu ce competențe vor fi cerute în domeniul meu."],
    "Control (decizi tu)": ["Iau singur(ă) deciziile importante despre cariera mea.",
                            "Îmi asum responsabilitatea pentru drumul meu profesional.",
                            "Rămân fidel(ă) convingerilor mele atunci când decid."],
    "Curiozitate (explorezi)": ["Explorez activ opțiuni profesionale noi.",
                                "Caut ocazii de a învăța în afara rolului meu.",
                                "Îi întreb pe alții cum se lucrează în domeniile lor."],
    "Încredere (poți)": ["Duc sarcinile la capăt chiar și când sunt grele.",
                         "Învăț repede competențe noi când e nevoie.",
                         "Găsesc soluții când lucrurile nu merg cum am plănuit."],
}

OPEN = [
    ("Model de rol", "Pe cine admirai când erai copil sau adolescent (în afară de părinți)? Ce anume admirai?",
     "eul ideal: calitățile pe care vrei să le întruchipezi"),
    ("Medii preferate", "Ce reviste, site-uri, canale sau podcasturi urmărești cu plăcere? Ce te atrage la ele?",
     "mediile și tipurile de probleme care te atrag"),
    ("Povestea preferată", "Care e povestea ta preferată (carte, film, serial)? Povestește-o pe scurt.",
     "scenariul pe care l-ai putea urma ca să mergi mai departe"),
    ("Motto", "Ai un motto sau o zicală care te ghidează?", "sfatul pe care ți-l dai singur(ă)"),
    ("Flow", "Când ai uitat ultima dată de timp lucrând la ceva? Ce făceai?",
     "activitatea cu motivație intrinsecă puternică"),
]

OCC = [
    ("Dezvoltator(oare) software", "Softwareentwickler/in", "ICR"),
    ("Arhitect(ă) de soluții IT", "IT-/Solution-Architekt/in", "IEC"),
    ("Inginer(ă) DevOps / cloud", "DevOps / Cloud Engineer", "RIC"),
    ("Data scientist", "Data Scientist", "ICA"),
    ("Inginer(ă) de date", "Data Engineer", "CIR"),
    ("Specialist(ă) securitate IT", "IT-Security Specialist/in", "CIE"),
    ("Administrator(oare) sisteme și rețele", "System-/Netzwerkadministrator/in", "RCI"),
    ("Analist(ă) de business", "Business Analyst/in", "ICE"),
    ("Manager(ă) de proiect IT", "IT-Projektleiter/in", "ECI"),
    ("Product owner / manager de produs", "Product Owner / Product Manager/in", "EIA"),
    ("Consultant(ă) IT", "IT-Consultant/in", "EIC"),
    ("Scrum master / agile coach", "Scrum Master / Agile Coach", "SEI"),
    ("Designer UX/UI", "UX/UI Designer/in", "AIE"),
    ("Redactor(ă) tehnic(ă)", "Technische/r Redaktor/in", "AIC"),
    ("Formator(oare) IT pentru adulți", "IT-Trainer/in, Erwachsenenbildner/in", "SIE"),
    ("Profesor(oară) de informatică", "Informatiklehrer/in", "SIA"),
    ("Auditor(oare) / manager(ă) de calitate", "Qualitätsmanager/in", "CIR"),
    ("Inginer(ă) electrotehnist(ă)", "Elektroingenieur/in", "IRC"),
    ("Inginer(ă) mecanic(ă)", "Maschinenbauingenieur/in", "RIC"),
    ("Inginer(ă) constructor(oare)", "Bauingenieur/in", "RIC"),
    ("Inginer(ă) automatizări", "Automationsingenieur/in", "RIC"),
    ("Tehnician(ă) mecatronist(ă)", "Mechatroniker/in", "RCI"),
    ("Electrician(ă)", "Elektroinstallateur/in", "RIC"),
    ("Consultant(ă) în energie", "Energieberater/in", "IER"),
    ("Inginer(ă) de mediu", "Umweltingenieur/in", "IRS"),
    ("Laborant(ă) chimie / biologie", "Laborant/in", "IRC"),
    ("Cercetător(oare) științific(ă)", "Wissenschaftler/in", "IAR"),
    ("Arhitect(ă)", "Architekt/in", "AIR"),
    ("Designer grafic", "Grafiker/in", "AER"),
    ("Fotograf(ă) / videograf(ă)", "Fotograf/in / Videograf/in", "ARE"),
    ("Jurnalist(ă)", "Journalist/in", "AES"),
    ("Traducător(oare)", "Übersetzer/in", "AIC"),
    ("Muzician(ă)", "Musiker/in", "AES"),
    ("Profesor(oară)", "Lehrer/in", "SAE"),
    ("Asistent(ă) social(ă)", "Sozialarbeiter/in", "SEA"),
    ("Consilier(ă) de carieră", "Laufbahnberater/in", "SAI"),
    ("Psiholog(ă)", "Psychologe / Psychologin", "ISA"),
    ("Asistent(ă) medical(ă)", "Pflegefachfrau / Pflegefachmann", "SIR"),
    ("Fizioterapeut(ă)", "Physiotherapeut/in", "SRI"),
    ("Medic", "Arzt / Ärztin", "ISR"),
    ("Specialist(ă) HR / recrutare", "HR-Fachperson / Recruiter/in", "SEC"),
    ("Consultant(ă) vânzări", "Verkaufsberater/in", "ESC"),
    ("Key account manager", "Key Account Manager/in", "ECS"),
    ("Antreprenor(oare) / fondator(oare)", "Unternehmer/in / Gründer/in", "EAI"),
    ("Manager(ă) de marketing", "Marketingmanager/in", "EAC"),
    ("Contabil(ă) / fiduciar(ă)", "Buchhalter/in / Treuhänder/in", "CEI"),
    ("Controller financiar", "Controller/in", "CIE"),
    ("Specialist(ă) administrativ(ă)", "Sachbearbeiter/in", "CES"),
    ("Specialist(ă) logistică / supply chain", "Logistiker/in / Supply Chain Specialist", "CER"),
    ("Specialist(ă) în ospitalitate", "Hotelfachfrau / Hotelfachmann", "ESC"),
    ("Bucătar(easă)", "Koch / Köchin", "RAE"),
    ("Polițist(ă)", "Polizist/in", "RES"),
    ("Peisagist(ă) / grădinar(ă)", "Landschaftsgärtner/in", "RAC"),
    ("Tâmplar(ă)", "Schreiner/in", "RAC"),
    ("Silvicultor(oare)", "Förster/in", "RIS"),
    ("Pilot(ă)", "Pilot/in", "RIE"),
]

SC_LIKE = ["Deloc", "Puțin", "Neutru", "Mult", "Foarte mult"]
SC_CONF = ["Deloc sigur(ă): n-am făcut niciodată", "Puțin: am încercat, cu greu", "Moderat: cu puțin ajutor",
           "Sigur(ă): am făcut-o singur(ă)", "Foarte sigur(ă): alții îmi cer ajutorul"]
SC_TRUE = ["Deloc adevărat", "Puțin adevărat", "Parțial adevărat", "În mare parte adevărat", "Complet adevărat"]
SC_DESC = ["Deloc", "Puțin", "Parțial", "În mare măsură", "Foarte bine"]
SC_STR = ["Deloc", "Slab", "Moderat", "Puternic", "Foarte puternic"]

n_int = sum(len(v) for v in INT.values())
n_conf = sum(len(v) for v in CONF.values())
n_anc = sum(len(a[2]) for a in ANCHORS)
n_sdt = sum(len(v) for v in SDT.values())
n_ad = sum(len(v) for v in ADAPT.values())
n_closed = n_int + n_conf + n_anc + len(B5) + n_sdt + len(CTX) + n_ad + 2

# ------------------------------------------------------------------ document

P("Busola Vocațională", title)
P("Test de orientare profesională: întrebări, variante de răspuns și metoda de analiză · versiunea 1 (ciornă de "
  "revizuit) · octombrie 2026", subtitle)

P("Scopul testului", h1)
P("Busola Vocațională urmărește același scop ca Laufbahn Mosaik: să arate ce direcții profesionale ți se potrivesc. "
  "Diferența este că pornește de la modele cu zeci de ani de cercetare în spate și măsoară mai mult decât "
  "interesele. Se uită la cinci lucruri: <b>ce îți place</b> (interese), <b>la ce te simți capabil(ă)</b> "
  "(auto-eficacitate), <b>la ce nu ai renunța</b> (valori de carieră), <b>cum ești și cum lucrezi</b> "
  "(personalitate, mediu de lucru, nevoi psihologice) și <b>cum îți conduci cariera</b> (adaptabilitate). Le "
  "completează cu întrebări deschise despre povestea ta.")
P("Rezultatul nu este o sentință. Este un set de ipoteze bine argumentate pe care le verifici apoi prin experimente "
  "mici în lumea reală: interviuri informaționale, proiecte de probă, cursuri scurte.")

P("Ce face mai bine decât Laufbahn Mosaik", h1)
table([
    ["Ce limitează Laufbahn Mosaik", "Ce face Busola Vocațională"],
    ["Model propriu („Grundstreben”), fără validare publicată.",
     "Folosește modele cu cercetare extinsă: RIASEC (Holland), Big Five, ancorele lui Schein, teoria social-cognitivă "
     "a carierei, teoria autodeterminării, adaptabilitatea în carieră (Savickas)."],
    ["Doar 4 întrebări pe domeniu, câte una pe subdomeniu: scoruri instabile.",
     "8 întrebări pe fiecare tip de interes, din care se calculează scoruri mai fiabile."],
    ["„Wie gut können Sie das?” este o autoevaluare vagă, ușor de umflat sau de subestimat.",
     "Treptele de răspuns descriu fapte („am făcut-o singur(ă)”, „alții îmi cer ajutorul”). Ancorarea "
     "comportamentală reduce distorsiunile."],
    ["Multe activități țin de ucenicie sau de stereotipuri (modă, cosmetică, servire la mese).",
     "Activități pentru adulți, inclusiv munca digitală, conducerea, consultanța, cercetarea."],
    ["Frecvența hobby-urilor depinde de timp, bani și familie, nu doar de preferințe.",
     "Interesul se măsoară direct, iar contextul de viață intră separat (ancora „stil de viață”, mediul de lucru)."],
    ["Nu măsoară valori, motivație, personalitate sau adaptabilitate.",
     "Module dedicate pentru fiecare, plus potrivirea cu mediul de lucru."],
    ["Nu verifică dacă răspunsurile sunt date cu atenție.",
     "Itemi de control, detectarea răspunsurilor uniforme, a tendinței de a fi de acord și a răspunsurilor prea "
     "rapide."],
    ["Raportul arată sume pe domenii, fără interpretarea formei profilului.",
     "Cod Holland, diferențiere, consistență, harta lumii muncii, matricea interes × încredere, listă de meserii "
     "cu indice de potrivire și plan de experimente."],
    ["Ignoră povestea persoanei.",
     "Cinci întrebări deschise din Interviul de construcție a carierei (Savickas) și din cercetarea despre flow."],
], [70, 110])

P("Structura testului", h1)
table([
    ["Nr.", "Modul", "Ce măsoară", "Bază științifică", "Itemi", "Min."],
    ["1", "Interese", "6 tipuri de interese RIASEC", "Holland (1959, 1997); formatul O*NET Interest Profiler",
     f"{n_int} + 1 control", "7"],
    ["2", "Încredere în abilități", "Auto-eficacitatea pe cele 6 tipuri", "Bandura (1977); Lent, Brown & Hackett (1994); "
     "Betz & Borgen (1996)", str(n_conf), "3"],
    ["3", "Ancore de carieră", "8 ancore + alegerea celor mai importante 3 afirmații", "Schein (1978, 1990)",
     f"{n_anc} + 3 alegeri", "4"],
    ["4", "Stil personal", "Big Five", "Mini-IPIP, Donnellan și colab. (2006); IPIP, Goldberg (1999)",
     f"{len(B5)} + 1 control", "3"],
    ["5", "Ce ți-a lipsit", "Nevoile de autonomie, competență, relaționare la ultimul job",
     "Teoria autodeterminării, Deci & Ryan (1985, 2000)", str(n_sdt), "1"],
    ["6", "Mediul de lucru", "10 preferințe de context, pe axe cu doi poli", "Teoria adaptării la muncă, Dawis & "
     "Lofquist (1984); O*NET Work Context", str(len(CTX)), "2"],
    ["7", "Adaptabilitate", "Preocupare, control, curiozitate, încredere", "Savickas (2005); Savickas & Porfeli (2012)",
     str(n_ad), "2"],
    ["8", "Povestea ta", "Teme de viață, motivație intrinsecă", "Savickas, Interviul de construcție a carierei; "
     "Csikszentmihalyi (1990)", "5 deschise", "5"],
    ["", "<b>Total</b>", "", "", f"<b>{n_closed} închise + 3 alegeri + 5 deschise</b>", "<b>~27</b>"],
], [9, 30, 45, 58, 26, 12])
SP(3)
P("Itemii fiecărui modul se prezintă amestecați: în fiecare rundă apare câte un item din fiecare tip, în ordine "
  "aleatoare, dar aceeași pentru toți respondenții. Astfel scade efectul de poziție și nu se poate ghici ce tip se "
  "măsoară. Mai jos itemii sunt grupați pe tipuri, pentru claritate.", small)

# ---------------- Module 1
P("Modulul 1 · Interese", h1)
P("<b>Întrebare:</b> „Cât de mult ți-ar plăcea să…” · <b>Instrucțiune:</b> gândește-te doar la cât de mult ți-ar "
  "plăcea activitatea, nu la dacă o știi face sau la cât se câștigă.")
scale_table(SC_LIKE)
for t in TYPES:
    story.append(KeepTogether([
        Paragraph(f"<font color='{TYPE_COL[t]}'><b>{t}</b></font> · {TYPE_NAME[t]}: {TYPE_DESC[t]}", h3),
    ]))
    table([["Cod", "Activitate"]] + [[f"{t}{i + 1}", x] for i, x in enumerate(INT[t])], [14, 166])
SP(4)
P("<b>Item de control</b> (poziția 29): „Pentru verificarea atenției, alege «Mult» la acest rând.” Răspuns corect: 4.")

# ---------------- Module 2
story.append(PageBreak())
P("Modulul 2 · Încredere în abilități", h1)
P("<b>Întrebare:</b> „Cât de sigur(ă) ești că ai putea face asta bine?” · <b>Instrucțiune:</b> răspunde după "
  "experiența reală. Treptele descriu fapte, nu impresii.")
scale_table(SC_CONF)
table([["Cod", "Tip", "Sarcină"]] + [[f"K{t}{i + 1}", TYPE_NAME[t], x] for t in TYPES for i, x in enumerate(CONF[t])],
      [14, 28, 138])

# ---------------- Module 3
P("Modulul 3 · Ancore de carieră", h1)
P("<b>Întrebare:</b> „Cât de adevărat este pentru tine?” · <b>Instrucțiune:</b> o ancoră e lucrul la care nu ai "
  "renunța dacă ar trebui să alegi. Răspunde sincer, chiar dacă unele afirmații sună mai „frumos” decât altele.")
scale_table(SC_TRUE)
rows = [["Cod", "Ancoră", "Afirmație"]]
for code, name, items, _ in ANCHORS:
    for i, x in enumerate(items):
        rows.append([f"{code}{i + 1}", name if i == 0 else "", x])
table(rows, [14, 46, 120])
SP(4)
P("<b>Pasul de alegere.</b> După cele 24 de afirmații, respondentul vede lista lor ordonată după punctajul dat și "
  "alege <b>exact 3</b> care sunt cele mai adevărate pentru el sau ea. Alegerea forțată desparte ancorele reale de "
  "cele doar „plăcute” (metoda lui Schein).")

# ---------------- Module 4
story.append(PageBreak())
P("Modulul 4 · Stil personal (Big Five)", h1)
P("<b>Întrebare:</b> „Cât de bine te descrie afirmația?” · <b>Instrucțiune:</b> descrie-te cum ești de obicei acum, "
  "nu cum ți-ai dori să fii.")
scale_table(SC_DESC)
table([["Nr.", "Afirmație", "Trăsătură", "Cheie"]] +
      [[str(i + 1), x, B5_NAME[t], "directă" if k == "+" else "inversată"] for i, (t, k, x) in enumerate(B5)],
      [11, 107, 40, 22])
SP(3)
P("Itemi Mini-IPIP din International Personality Item Pool (domeniu public), traducere proprie, în ordinea originală "
  "de administrare. <b>Item de control</b> (după itemul 12): „Pentru verificarea atenției, alege «Deloc» la acest "
  "rând.” Răspuns corect: 1.", small)

# ---------------- Module 5
P("Modulul 5 · Ce ți-a lipsit (nevoi psihologice de bază)", h1)
P("<b>Întrebare:</b> „Gândindu-te la ultimul tău loc de muncă (sau la cel actual):” · Scala: aceeași ca la modulul 3 "
  "(Deloc adevărat … Complet adevărat).")
table([["Cod", "Nevoie", "Afirmație"]] +
      [[f"{n[0]}{i + 1}", n if i == 0 else "", x] for n, items in SDT.items() for i, x in enumerate(items)],
      [14, 30, 136])

# ---------------- Module 6
P("Modulul 6 · Mediul de lucru", h1)
P("<b>Întrebare:</b> „Unde te așezi între cele două variante?” · Scala: 1 = complet varianta din stânga, 3 = mi-e "
  "indiferent sau ambele la fel, 5 = complet varianta din dreapta.")
table([["Cod", "Polul 1", "1 · 2 · 3 · 4 · 5", "Polul 5"]] +
      [[f"M{i + 1}", l, "○ ○ ○ ○ ○", r] for i, (l, r) in enumerate(CTX)],
      [14, 66, 34, 66], style_extra=[("ALIGN", (2, 1), (2, -1), "CENTER")])

# ---------------- Module 7
story.append(PageBreak())
P("Modulul 7 · Adaptabilitate în carieră", h1)
P("<b>Întrebare:</b> „Cât de puternic este acest lucru la tine?”")
scale_table(SC_STR)
rows = [["Cod", "Dimensiune", "Afirmație"]]
for j, (dim, items) in enumerate(ADAPT.items()):
    for i, x in enumerate(items):
        rows.append([f"D{j + 1}{i + 1}", dim if i == 0 else "", x])
table(rows, [14, 46, 120])

# ---------------- Module 8
P("Modulul 8 · Povestea ta (întrebări deschise, opționale)", h1)
P("Răspuns liber, câteva propoziții. Întrebările vin din Interviul de construcție a carierei (Mark Savickas) și din "
  "cercetarea despre flow (Mihaly Csikszentmihalyi).")
table([["Cod", "Întrebare", "Ce dezvăluie"]] +
      [[f"P{i + 1}", f"<b>{n}.</b> {q}", w] for i, (n, q, w) in enumerate(OPEN)],
      [14, 104, 62])

# ---------------- Analysis
story.append(PageBreak())
P("Metoda de analiză", h1)

P("1. Reguli generale de scorare", h2)
bullets([
    "Fiecare răspuns valorează 1–5 puncte. La itemii inversați (Big Five) punctajul devine 6 − răspuns.",
    "Scorul unei scale este media itemilor ei. Pentru comparații se transformă în 0–100: (medie − 1) / 4 × 100.",
    "Itemii de control nu intră în scoruri; servesc doar la verificarea calității datelor.",
])

P("2. Interese: profilul RIASEC", h2)
bullets([
    "<b>Codul Holland</b> = primele trei tipuri după scorul de interes (de exemplu ICR). La egalitate decide "
    "scorul de încredere din modulul 2.",
    "<b>Diferențierea</b> = scorul cel mai mare − scorul cel mai mic. ≥ 45: profil clar; 25–45: moderat; "
    "&lt; 25: plat. Un profil plat înseamnă fie interese foarte largi, fie preferințe încă neclare. În ambele "
    "cazuri, experimentele practice spun mai mult decât testele.",
    "<b>Consistența</b> = distanța pe hexagonul R–I–A–S–E–C dintre primele două tipuri. Tipuri vecine (1): "
    "ridicată, se regăsesc ușor în aceeași meserie. Distanța 2: medie. Tipuri opuse (3): scăzută, o combinație "
    "rară. Poate fi un profil hibrid valoros sau un semn că una dintre direcții ține de timpul liber.",
    "<b>Elevația</b> = media celor 6 scoruri. ≥ 65: interese largi, iar alegerea se va face mai ales după valori "
    "(ancore). ≤ 30: nivel general scăzut, care apare des în perioade de stres, oboseală sau șomaj. Nu înseamnă "
    "lipsă de potențial; merită refăcut testul peste câteva săptămâni.",
    "<b>Harta lumii muncii</b> (Prediger, 1982). Scorurile se centrează (fiecare minus media celor 6), apoi: "
    "<b>Date ↔ Idei</b> = 1,73 × (E + C − I − A); <b>Oameni ↔ Lucruri</b> = A + 2S + E − C − 2R − I. Persoana "
    "și meseriile apar pe aceeași hartă, cu două axe: lucru cu date sau cu idei, cu oameni sau cu lucruri.",
])

P("3. Interes × încredere (teoria social-cognitivă a carierei)", h2)
P("Pentru fiecare tip RIASEC se compară interesul cu încrederea. Pragurile sunt mediile personale ale celor două "
  "scoruri, fiindcă interpretarea se face relativ la propriul profil.")
table([
    ["", "Încredere peste media ta", "Încredere sub media ta"],
    ["<b>Interes peste media ta</b>", "<b>Teren propriu.</b> Direcții de folosit imediat.",
     "<b>Teren de cucerit.</b> Un curs sau un proiect ghidat crește auto-eficacitatea, principalul motor al "
     "alegerilor de carieră (Lent și colab., 1994)."],
    ["<b>Interes sub media ta</b>", "<b>Competență fără chef.</b> Bun(ă) la asta, dar o carieră construită doar pe ea "
     "riscă epuizarea și plictiseala.", "<b>În afara drumului.</b> Nu merită investiție acum."],
], [44, 68, 68])

P("4. Ancore de carieră", h2)
bullets([
    "Scorul ancorei = (suma celor 3 itemi + 4 × numărul itemilor ei aleși în top 3) / 3. Intervalul este 1–9.",
    "Ancora principală este cea cu scorul cel mai mare. Raportul o descrie, spune ce să cauți într-un job și la "
    "ce să fii atent(ă):",
])
table([["Ancoră", "Ce înseamnă pentru alegerea jobului"]] + [[f"<b>{n}</b>", d] for _, n, _, d in ANCHORS], [48, 132])

P("5. Stil personal (Big Five)", h2)
bullets([
    "Media pe trăsătură, pe scala 1–5, cu itemii inversați recodați. Nevrotismul se raportează ca "
    "<b>stabilitate emoțională</b> (6 − scor), o formulare care nu patologizează.",
    "Benzi: &lt; 2,5 scăzut, 2,5–3,5 mediu, &gt; 3,5 ridicat. Fără norme populaționale, interpretarea este absolută "
    "și prudentă. Fiecare bandă primește o implicație pentru muncă, de exemplu: conștiinciozitatea este cel mai "
    "constant predictor al performanței (Barrick & Mount, 1991); introversia avantajează rolurile de concentrare "
    "profundă.",
    "Stabilitatea emoțională este influențată de situația de moment, de exemplu de căutarea unui loc de muncă. "
    "Raportul o spune explicit.",
])

P("6. Nevoi psihologice, mediu de lucru, adaptabilitate", h2)
bullets([
    "<b>Nevoi</b>: media pe nevoie. Sub 3 = nevoie nesatisfăcută la ultimul job. Ea devine criteriu prioritar "
    "pentru următorul (de exemplu, lipsa autonomiei → caută roluri cu libertate în execuție).",
    "<b>Mediul de lucru</b>: 1–2 sau 4–5 = preferință clară, 3 = flexibil. Preferințele clare devin filtre la "
    "evaluarea ofertelor de muncă.",
    "<b>Adaptabilitatea</b>: media pe dimensiune. Cea mai scăzută primește o acțiune concretă (de exemplu "
    "curiozitate scăzută → trei interviuri informaționale în două săptămâni).",
])

P("7. Potrivirea cu meseriile", h2)
bullets([
    "Fiecare meserie are un cod RIASEC (aproximat după O*NET; lista e în anexă). Codul devine un vector: prima "
    "literă = 1,00; a doua = 0,65; a treia = 0,40; celelalte trei = 0,10.",
    "Se calculează corelația Pearson dintre vectorul meseriei și profilul de interese (rI), apoi profilul de "
    "încredere (rC). Corelația compară <b>forma</b> profilului, nu nivelul, deci nu contează dacă cineva dă în "
    "general scoruri mari sau mici.",
    "<b>Indicele de potrivire</b> = (0,7 × rI + 0,3 × rC + 1) / 2 × 100. Benzi: ≥ 80 foarte bună; 65–80 bună; "
    "50–65 parțială; &lt; 50 slabă. Interesul are ponderea mai mare: prezice satisfacția și performanța "
    "(Nye și colab., 2012).",
    "Lista finală se filtrează apoi după ancora principală și preferințele de context. Exemple: ancora "
    "„autonomie” scoate în față variantele de consultanță sau freelancing; preferința pentru lucru individual "
    "semnalează rolurile cu multe ședințe.",
])

P("8. Calitatea datelor", h2)
table([
    ["Verificare", "Regulă", "Gravitate"],
    ["Itemi de control", "Fiecare răspuns greșit", "serioasă"],
    ["Răspunsuri uniforme", "Cel puțin 2 pagini cu același răspuns la toți itemii", "serioasă"],
    ["Viteză", "Sub 1,8 secunde în medie pe item", "serioasă"],
    ["Tendința de acord", "Media brută a itemilor Big Five ≥ 3,8 sau ≤ 2,2 (itemii sunt echilibrați ca direcție, "
     "deci o medie extremă indică un stil de răspuns)", "observație"],
], [38, 112, 30])
SP(3)
P("Verdict: <b>Bună</b> (nicio problemă), <b>Bună, cu observații</b> (doar observații) sau <b>De interpretat cu "
  "prudență</b> (cel puțin o problemă serioasă). Bazat pe cercetarea despre răspunsurile neatente (Meade & Craig, "
  "2012).", small)

P("9. Răspunsurile deschise", h2)
P("Se analizează calitativ, după metoda lui Savickas. Modelul de rol arată eul ideal. Mediile preferate arată "
  "tipul de probleme care atrag. Povestea preferată arată scenariul pe care persoana l-ar putea urma. Motto-ul "
  "este sfatul pe care și-l dă singură, iar momentul de flow arată motivația intrinsecă. Temele găsite se "
  "compară cu profilul cantitativ. Unde se potrivesc, concluzia e mai solidă; unde diferă, apare o întrebare de "
  "explorat, nu o eroare.")

P("Structura raportului final", h1)
bullets([
    "<b>Rezumat</b>: codul Holland, ancora principală, primele trei meserii, verdictul de calitate a datelor.",
    "<b>Interese</b>: hexagonul RIASEC (interes și încredere suprapuse), diferențiere, consistență, elevație.",
    "<b>Harta lumii muncii</b>: poziția persoanei și a meseriilor pe axele date/idei și oameni/lucruri.",
    "<b>Matricea interes × încredere</b>, cu cele patru zone și ce faci în fiecare.",
    "<b>Ancore de carieră</b>: clasamentul celor 8 și descrierea primelor două.",
    "<b>Stil personal</b>, <b>nevoi nesatisfăcute</b>, <b>mediul preferat</b>, <b>adaptabilitate</b>: fiecare cu "
    "implicații concrete.",
    "<b>Meserii potrivite</b>: top 15, cu numele în română și în germană (pentru căutarea pe platformele de joburi), "
    "cod, indice de potrivire și motiv.",
    "<b>Plan de experimente</b> pe 2–4 săptămâni pentru primele direcții: interviu informațional, proiect de probă, "
    "curs scurt (Ibarra, 2003; Burnett & Evans, 2016).",
    "<b>Limite</b> și răspunsurile date, pentru transparență.",
])

P("Limite și pașii de validare", h1)
bullets([
    "Itemii sunt noi, cu excepția celor Mini-IPIP. Construcțiile măsurate sunt validate în literatură, dar această "
    "formulare a itemilor nu este încă validată empiric.",
    "Pentru validare ar fi nevoie de: un studiu pilot cu cel puțin 200 de persoane; consistență internă "
    "(alfa Cronbach ≥ 0,70 pe scală); analiză factorială care să confirme structura; test-retest la 4–6 "
    "săptămâni; comparație cu instrumente stabilite, de exemplu O*NET Interest Profiler; norme pe grupe de "
    "vârstă.",
    "Orice autoevaluare este influențată de dispoziția de moment și de imaginea de sine. Rezultatul e un punct de "
    "plecare pentru explorare, nu un verdict.",
])

P("Bibliografie", h1)
refs = [
    "Bandura, A. (1977). Self-efficacy: Toward a unifying theory of behavioral change. <i>Psychological Review, 84</i>(2).",
    "Barrick, M. R., & Mount, M. K. (1991). The Big Five personality dimensions and job performance: A meta-analysis. "
    "<i>Personnel Psychology, 44</i>(1).",
    "Betz, N. E., Borgen, F. H., & Harmon, L. W. (1996). <i>Skills Confidence Inventory</i>. Consulting Psychologists Press.",
    "Burnett, B., & Evans, D. (2016). <i>Designing Your Life</i>. Knopf.",
    "Csikszentmihalyi, M. (1990). <i>Flow: The Psychology of Optimal Experience</i>. Harper & Row.",
    "Dawis, R. V., & Lofquist, L. H. (1984). <i>A Psychological Theory of Work Adjustment</i>. University of Minnesota Press.",
    "Deci, E. L., & Ryan, R. M. (2000). The „what” and „why” of goal pursuits. <i>Psychological Inquiry, 11</i>(4).",
    "Donnellan, M. B., Oswald, F. L., Baird, B. M., & Lucas, R. E. (2006). The Mini-IPIP scales. "
    "<i>Psychological Assessment, 18</i>(2).",
    "Goldberg, L. R. (1999). A broad-bandwidth, public domain, personality inventory. În <i>Personality Psychology in "
    "Europe, 7</i>.",
    "Holland, J. L. (1997). <i>Making Vocational Choices</i> (ed. a 3-a). Psychological Assessment Resources.",
    "Ibarra, H. (2003). <i>Working Identity</i>. Harvard Business School Press.",
    "Lent, R. W., Brown, S. D., & Hackett, G. (1994). Toward a unifying social cognitive theory of career and academic "
    "interest, choice, and performance. <i>Journal of Vocational Behavior, 45</i>(1).",
    "Meade, A. W., & Craig, S. B. (2012). Identifying careless responses in survey data. <i>Psychological Methods, 17</i>(3).",
    "Nye, C. D., Su, R., Rounds, J., & Drasgow, F. (2012). Vocational interests and performance: A quantitative summary "
    "of over 60 years of research. <i>Perspectives on Psychological Science, 7</i>(4).",
    "Prediger, D. J. (1982). Dimensions underlying Holland's hexagon. <i>Journal of Vocational Behavior, 21</i>(3).",
    "Savickas, M. L. (2005). The theory and practice of career construction. În Brown & Lent (ed.), <i>Career "
    "Development and Counseling</i>. Wiley.",
    "Savickas, M. L., & Porfeli, E. J. (2012). Career Adapt-Abilities Scale. <i>Journal of Vocational Behavior, 80</i>(3).",
    "Schein, E. H. (1990). <i>Career Anchors: Discovering Your Real Values</i>. Pfeiffer.",
]
for r in refs:
    story.append(Paragraph(r, ParagraphStyle("ref", parent=small, leftIndent=12, firstLineIndent=-12, textColor=INK)))

story.append(PageBreak())
P("Anexă · Meserii și coduri RIASEC", h1)
P("Codurile sunt aproximate după O*NET (ordinea literelor = importanța tipului). Numele în germană ajută la "
  "căutarea pe platformele de joburi din spațiul germanofon. Lista se poate extinde fără să se schimbe metoda.", small)
table([["Nr.", "Meserie", "Denumire în germană", "Cod"]] +
      [[str(i + 1), ro, de, f"<b>{c}</b>"] for i, (ro, de, c) in enumerate(OCC)], [11, 74, 75, 20])


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Arial", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(15 * mm, 9 * mm, "Busola Vocațională · v1 ciornă")
    canvas.drawRightString(195 * mm, 9 * mm, f"pagina {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(OUT, pagesize=A4, topMargin=15 * mm, bottomMargin=16 * mm, leftMargin=15 * mm,
                        rightMargin=15 * mm, title="Busola Vocationala - test")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("OK", OUT, "closed items:", n_closed, "occupations:", len(OCC))
