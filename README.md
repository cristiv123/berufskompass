# Busola Vocațională · Berufskompass

Test de orientare profesională care rulează complet în browser, în română și germană. Răspunsurile rămân pe
dispozitivul utilizatorului (salvare automată în `localStorage`, export și import `.json`). Nu există server și
nu se trimit date nicăieri.

*Ein Test zur beruflichen Orientierung, der vollständig im Browser läuft (Rumänisch und Deutsch). Die Antworten
bleiben auf dem Gerät der Person.*

## Ce măsoară

| Modul | Model |
|---|---|
| Interese (48 de itemi) | RIASEC, Holland (1997) |
| Încredere în abilități (24) | Auto-eficacitate, Bandura (1977); SCCT, Lent, Brown & Hackett (1994) |
| Ancore de carieră (24 + 3 alegeri) | Schein (1990) |
| Stil personal (20) | Big Five, Mini-IPIP, Donnellan et al. (2006) |
| Nevoi psihologice (9) | Teoria autodeterminării, Deci & Ryan (2000) |
| Mediul de lucru (10) | Theory of Work Adjustment, Dawis & Lofquist (1984) |
| Adaptabilitate (12) | Savickas & Porfeli (2012) |
| Povestea ta (5 întrebări deschise) | Career Construction Interview, Savickas |

Raportul arată:
- codul Holland, cu diferențierea și consistența profilului;
- hexagonul RIASEC și harta lumii muncii (Prediger, 1982);
- matricea interes × încredere;
- ancorele, profilul Big Five, nevoile, mediul preferat și adaptabilitatea;
- top 15 meserii, cu indice de potrivire;
- un plan de experimente;
- o verificare a calității răspunsurilor.

Raportul se poate salva ca PDF din butonul „Salvează ca PDF”, care deschide fereastra de printare a browserului.

## Publicare pe GitHub Pages

1. Creează un repository pe GitHub, de exemplu `berufskompass`.
2. Încarcă fișierele din acest folder:
   ```bash
   git remote add origin https://github.com/<utilizator>/berufskompass.git
   git push -u origin main
   ```
3. Pe GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch**. Alege `main` și `/ (root)`, apoi **Save**.
4. După un minut, aplicația e disponibilă la `https://<utilizator>.github.io/berufskompass/`.

## Rulare locală

Aplicația folosește module JavaScript, care nu se încarcă din `file://`. Pornește un server static:

```bash
python -m http.server 8765
```

Apoi deschide `http://localhost:8765`.

## Teste

```bash
node tests/scoring.test.mjs
```

## Structură

- `index.html`, `css/style.css`: pagina și stilurile, inclusiv tema întunecată și stilul pentru printare.
- `js/data.js`: itemii, scalele și meseriile în ambele limbi, generați din sursele documentului PDF.
- `js/model.js`: modulele, ordinea itemilor și paginile.
- `js/scoring.js`: toate calculele, ca funcții pure.
- `js/charts.js`: graficele SVG.
- `js/report.js`: raportul final.
- `js/i18n.js`: textele interfeței și ale raportului.
- `js/app.js`: fluxul testului, salvarea, importul și exportul.
- `js/demo.js`: răspunsurile pentru raportul exemplu.
- `docs/`: documentul testului, în PDF, în română și germană.
- `tools/`: scripturile care generează PDF-urile și `js/data.js`. Ca să schimbi o întrebare, editeaz-o în
  `tools/make_busola_pdf.py` și `tools/make_busola_pdf_de.py`, apoi rulează:
  ```bash
  python tools/extract_data.py tools/make_busola_pdf.py tools/make_busola_pdf_de.py js/data.js
  ```

## Limite

Itemii sunt noi, cu excepția celor Mini-IPIP, și nu au fost încă validați empiric. Rezultatul este un punct de
plecare pentru explorare, nu un diagnostic.
