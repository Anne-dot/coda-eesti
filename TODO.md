# TODO - CODA Eesti Veebileht

---

## ⏳ Käimasolevad

- **TODO.md vajab korrigeerimist** - Sisu on läinud lappesse
  - Milestone 1, 2, 3 sisu on segamini
  - Vajab ülevaatamist vastavalt GitHubi milestone definitsioonidele
  - Vajab koosoleku protokolli ülevaatamist (millised lehed on kokku lepitud)
  - Prioriteet: KÕRGE (enne uute issue'de loomist)

- **Ootan Brenda (tmc@coda.org) vastust** - Videokõne toimus 3. novembril
  - Algne aeg lükati edasi
  - Videokõne toimus ja oli väga informatiivne
  - Saatsin follow-up e-maili täiendavate küsimustega (2025-11-04)
  - Ootan vastust:
    - Autoriõiguse täpne formaat veebilehel ("fair use")
    - Visuaalse identiteedi kontakt (Laurie C.)
    - Daily Meditations kasutamine veebilehel ja e-mailiga
    - Kirjanduse müük ja levitamine

- **Ootan ajavööndi parandust coda.org lehel** - Saatsin paranduse (2025-12-03)
  - Koosolek: https://coda.org/meeting/coda-kuressaare/
  - Probleem: Ajavöönd oli vale (GMT +2 Kaliningrad/South Africa)
  - Õige: GMT +3 (Baghdad, Riyadh, Moscow) - Eesti aeg

- **Ande K lubas aidata** - Disaini tagasiside (2025-11-02)
  - Ta kujundab raamatuid
  - Annab tagasisidet mockup'ile koos teiste CODA liikmetega

- **Ootan CoDA Eesti rühma tagasisidet** - Saatsin TMC vestluse kokkuvõtte (2025-11-04)
  - Fail: [TMC_VESTLUSE_KOKKUVOTE.docx](docs/TMC_VESTLUSE_KOKKUVOTE.docx)
  - Ootan:
    - Kes on teine inimene translation agreement'i allkirjastamiseks (peab rääkima inglise keelt)
    - Millised materjalid tahame legaliseerida ja tulevikus tõlkida

---

## 🔍 Jälgimist vajavad asjad

- **Claude Code bug report** - [Issue #10874](https://github.com/anthropics/claude-code/issues/10874)
  - Bash permissions bug: `gh` write commands executesid ilma promptita
  - Postitatud: 2025-11-02
  - Duplicate analüüs tehtud: 2025-11-03
    - Sarnane #6608-le (sama root cause - default-allow behavior)
    - Erinev #6527 ja #8961-st (erinevad stsenaariumid)
    - Kommentaar GitHubis postitatud
  - Staatus: Ootan meeskonna vastust
  - Workaround: Bash on `ask` listis

- **CoDA.org performance recommendations** - [EMAIL_DRAFT_LIGHTHOUSE.html](docs/EMAIL_DRAFT_LIGHTHOUSE.html)
  - Lighthouse test tulemused (Mobile: 3/100, Desktop: 33/100)
  - WordPress quick fixes soovitused (3 tasuta pluginat)
  - Saadetud Brendale edastamiseks tech meeskonnale: 2025-11-04
  - Ootan: vastust või implementeerimise tagasisidet

---

## ⏸️ Ootel / Planeeritud

### PRIORITEET 1: Milestone 0 - Structure and Decisions

**GitHub:** See [Milestone 0 - Structure and Decisions](https://github.com/Anne-dot/coda-eesti/milestone/1)

**Parent Issue:** [#1 - Project technical foundations](https://github.com/Anne-dot/coda-eesti/issues/1)

- [x] **[Issue #4](https://github.com/Anne-dot/coda-eesti/issues/4): Projekti kausta struktuur** ✅ VALMIS
  - Loodud `/research` kaust
  - Liigutatud lighthouse testid ja Python skriptid
  - Eemaldatud duplikaadid (DRY)
  - Loodud README.md lingidega

- [x] **[Issue #5](https://github.com/Anne-dot/coda-eesti/issues/5): Tech stack dokumenteerimine** ✅ VALMIS
  - [#6: Astro framework](https://github.com/Anne-dot/coda-eesti/issues/6) ✅
  - [#7: Tailwind CSS](https://github.com/Anne-dot/coda-eesti/issues/7) ✅
  - [#8: Shadcn/ui](https://github.com/Anne-dot/coda-eesti/issues/8) ✅
  - [#9: Sveltia CMS](https://github.com/Anne-dot/coda-eesti/issues/9) ✅
  - [#10: GitHub Pages](https://github.com/Anne-dot/coda-eesti/issues/10) ✅
  - [#11: CI/CD pipeline](https://github.com/Anne-dot/coda-eesti/issues/11) ✅

- [ ] **[Issue #2](https://github.com/Anne-dot/coda-eesti/issues/2): Visual identity and design system**
  - CODA.org disaini analüüs
  - Värvikoodid
  - Fondid
  - Paigutus ja komponendid

- [ ] **[Issue #3](https://github.com/Anne-dot/coda-eesti/issues/3): UX & Accessibility planning**
  - Lehekülgede struktuur
  - Navigatsioon
  - Mobile-first approach
  - Accessibility requirements

- [ ] **[Issue #20](https://github.com/Anne-dot/coda-eesti/issues/20): Update global.css with color palette**
  - Sõltub: Issue #2, #3
  - CSS muutujate uuendamine meie värvidega

- [ ] **[Issue #19](https://github.com/Anne-dot/coda-eesti/issues/19): Create mockup**
  - Sõltub: Issue #2, #3, #20
  - Tagasiside: Ande K + CODA liikmed

---

### PRIORITEET 1.5: Milestone 1 - MVP Static Site

**GitHub:** See [Milestone 1 - MVP Static Site](https://github.com/Anne-dot/coda-eesti/milestone/2)

**Parent Issue:** [#12 - Technical setup - Astro + Tailwind + Shadcn](https://github.com/Anne-dot/coda-eesti/issues/12)

- [x] **[Issue #12](https://github.com/Anne-dot/coda-eesti/issues/12): Technical setup - Astro + Tailwind + Shadcn** ✅ VALMIS (2025-12-03)
  - [x] [#13: Initialize and configure Astro project](https://github.com/Anne-dot/coda-eesti/issues/13)
  - [x] [#14: Integrate Tailwind CSS](https://github.com/Anne-dot/coda-eesti/issues/14)
  - [x] [#15: Make Shadcn/ui components available](https://github.com/Anne-dot/coda-eesti/issues/15)
  - [x] [#16: Set up Prettier for code formatting](https://github.com/Anne-dot/coda-eesti/issues/16)
  - [x] [#17: Set up ESLint for code linting](https://github.com/Anne-dot/coda-eesti/issues/17)
  - [x] [#18: Create project folder structure](https://github.com/Anne-dot/coda-eesti/issues/18)

- [ ] **Leheküljed, mis EI VAJA CoDA materjale:**
  - [ ] Kontaktide leht (ainult koosoleku info - saame pärast registreerimist)
  - [ ] "Meist" / "About" leht (üldine info grupi kohta)
  - [ ] FAQ leht (üldised küsimused)
  - [ ] Navigatsioon ja struktuuri
  - [ ] Footer ja header
  - **Märkus:** Need lehed võid teha valmis ja deployda kohe

- [ ] **Leheküljed, mis VAJAVAD CoDA materjale (oota luba!):**
  - [ ] ❌ 12 Sammu leht (vajab tõlkimisluba)
  - [ ] ❌ 12 Traditsiooni leht (vajab tõlkimisluba)
  - [ ] ❌ Päevatekstid / meditations (vajab tõlkimisluba)
  - [ ] ❌ Kirjanduse tsitaadid (vajab tõlkimisluba)
  - **Märkus:** Need jäta placeholder'iteks või "Coming soon", kuni saad loa

- [ ] **Sveltia CMS paigaldamine**
  - [ ] Config fail (admin/config.yml)
  - [ ] GitHub OAuth setup
  - [ ] Kasutajate õigused
  - **Märkus:** CMS setup ei vaja CoDA luba

- [ ] **GitHub Actions CI/CD**
  - [ ] Deploy workflow
  - [ ] Lighthouse CI
  - **Märkus:** Deploy'mist võid teha kohe, kui on midagi näidata

### Dokumentatsioon

- [ ] **Kasutajajuhend** - CMS-i kasutamine rühma liikmetele
  - [ ] Screenshotidega juhend
  - [ ] Kuidas sisu muuta
  - [ ] Kuidas uudiseid lisada

- [ ] **Portfolio kirjeldus**
  - [ ] Projekti kirjeldus (eesti + inglise)
  - [ ] Screenshots
  - [ ] Tehnilised väljakutsed ja lahendused

### Pärast Valmimist

- [ ] **Teata coda.org-ile** - Eesti veebilehe valmimisest

---

### PRIORITEET 2: Tõlkimisdokumendi läbivaatamine ja suhtlus coda.org-ga

- [ ] **Vaata läbi tõlkimisdokument** - `docs/CODA_TOLKIMISE_PROTSESS.md`
  - [x] Loe dokument läbi
  - [x] Kontrolli üle, kas midagi on puudu
  - [x] Saatsin küsimused TMC-le (2025-10-31)
  - [ ] Jaga info rühmaliikmetega PÄRAST TMC vastust (täielik pilt)

- [ ] **Arutage grupis läbi:**
  - [ ] Kes saab/tahab mida teha (vastutuste jaotus)
  - [ ] Kellel on õigus kasutada grupi e-maili aadressi?
  - [ ] Kes räägib piisavalt hästi inglise keelt vormide täitmiseks?
  - [ ] Kas taotleme $1000 USD toetust või mitte?
  - [ ] **Veebiannetused: kas ja kuidas saaksime annetusi koguda?**
    - Kas tahame üldse annetusi koguda?
    - Milliseid platvorme kasutada? (Stripe, PayPal, Wise, pangalink?)
    - Veebikoosolekul osalejad (eesti inimesed, kes ei saa Kuressaarde) võivad tahta toetada
    - Kes haldab rahalisi tehinguid?
    - Läbipaistvus ja aruandlus
    - Milleks annetusi kasutada? (hosting, domeeninimi, materjalide trükkimine?)

- [x] **Registreerige koosolek coda.org lehel** ✅ TEHTUD (2025-12-03)
  - Link: https://coda.org/meeting/coda-kuressaare/
  - Ajavööndi parandus saadetud (ootel)

- [ ] **Tõlkimisloa taotlemine** (PRIORITEET KESKMINE-KÕRGE)
  - Link: https://coda.org/service-info/translation-mgmt-main-page/ ("Start Here")
  - Vastutaja: [Määrata koosolekul - peab rääkima inglise keelt]
  - Märkus: Tehke PÄRAST koosoleku registreerimist!

---

## ⏸️ Edasi Lükatud / Madal Prioriteet

- [ ] **Vana Eesti lehe eemaldamine** (PRIORITEET MADAL - edasi lükatud)
  - **Staatus:** Edasi lükatud kuni uue lehe valmimiseni
  - **Põhjus:** Vana codaestonia.wordpress.com leht (2016) sisaldab vähemalt eestikeelset infot kaassõltuvuse kohta. Kuni uus leht valmis saab, on parem midagi kui mitte midagi.
  - **Coda.org staatus:** Tallinna koosolek on coda.org lehel juba märgitud "Meeting No Longer Active" (uuendatud 15.07.2025)
  - **Tulevikus:** Kui uus leht on valmis ja live, saada e-mail meetings@coda.org või info@coda.org palvega eemaldada vana WordPress leht
  - Vastutaja: [Määrata hiljem]

---

## ✅ Tehtud

**Milestone 0 Progress (50%):**
- [x] [Issue #4](https://github.com/Anne-dot/coda-eesti/issues/4): Projekti kausta struktuur ✅
- [x] [Issue #5](https://github.com/Anne-dot/coda-eesti/issues/5): Tech stack dokumenteerimine ✅
- [ ] Issue #2: Visual identity (järgmine)
- [ ] Issue #3: UX & Accessibility (järgmine)

**Eelnevad:**
- [x] GitHub repo loomine (coda-eesti)
- [x] Koosoleku protokoll (2025-10-29)
- [x] Tech stack otsus
- [x] README.md
- [x] .gitignore
- [x] Uurimustöö dokumentatsioon
- [x] CoDA tõlkimise protsessi ja autoriõiguste uurimine (2025-10-30)
- [x] Voting Entity nõuete uurimine
- [x] Eesti konkreetsete sammude dokumenteerimine
- [x] E-maili draft koostamine TMC-le (2025-10-31)
- [x] E-maili saatmine tmc@coda.org (2025-10-31) - 7 küsimust tõlkimise ja materjalide kohta
- [x] Lighthouse testimine CODA riikide lehtedele (2025-10-29) - Teise AI agendi poolt
- [x] Uurimustöö CODA rahvusvahelistest lehtedest ja tasuta platvormidest (2025-10-29)
- [x] Koosoleku registreerimine coda.org lehel (2025-12-03) - https://coda.org/meeting/coda-kuressaare/

---

## 📝 Märkmed

- Backup tech-inimese leidmine tutvusringkonnast (tulevikus)
- Domeeninime valik (kui vaja oma domeeni)

---

**Projekti staatus:** 🟡 Planeerimine ja setup faas
