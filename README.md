# Busola Vocațională · Berufskompass · Career Compass · Boussole de carrière · Bussola professionale

Test de orientare profesională care rulează complet în browser, în cinci limbi: română, germană, engleză,
franceză și italiană. Răspunsurile rămân pe dispozitivul utilizatorului (salvare automată în `localStorage`,
export și import `.json`). Nu există server și nu se trimit date nicăieri. Numele persoanei, dacă e introdus,
apare doar în raport și în fișierul descărcat.

*Ein Test zur beruflichen Orientierung, der vollständig im Browser läuft (RO, DE, EN, FR, IT). Die Antworten
bleiben auf dem Gerät der Person.*

*A career orientation test that runs entirely in the browser (RO, DE, EN, FR, IT). Answers stay on the person's
device.*

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
- `js/data.js`: itemii, scalele și meseriile în cele cinci limbi, generați din sursele din `tools/`.
- `js/model.js`: modulele, ordinea itemilor și paginile.
- `js/scoring.js`: toate calculele, ca funcții pure.
- `js/charts.js`: graficele SVG.
- `js/report.js`: raportul final.
- `js/i18n.js`: textele interfeței și ale raportului în română și germană; `js/ui_en.js`, `js/ui_fr.js`,
  `js/ui_it.js` pentru engleză, franceză și italiană.
- `js/app.js`: fluxul testului, salvarea, importul și exportul.
- `js/demo.js`: răspunsurile pentru raportul exemplu.
- `docs/`: documentul testului, în PDF, în română și germană.
- `tools/`: sursele itemilor și scripturile care generează PDF-urile și `js/data.js`. Ca să schimbi o
  întrebare, editeaz-o în toate sursele: `make_busola_pdf.py` (RO), `make_busola_pdf_de.py` (DE),
  `lang_en.py`, `lang_fr.py`, `lang_it.py`. Apoi rulează:
  ```bash
  python tools/extract_data.py js/data.js
  ```
  Scriptul verifică faptul că toate limbile au aceeași structură și aceleași coduri de meserii.

## Limite

Itemii sunt noi, cu excepția celor Mini-IPIP, și nu au fost încă validați empiric. Rezultatul este un punct de
plecare pentru explorare, nu un diagnostic.
