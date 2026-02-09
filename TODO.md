# TODO - CoDA Eesti Veebileht

---

## ⏳ Käimasolevad

- **Deploy** - Sait vajab deploymist, et rühm saaks tagasisidet anda
  - Cloudflare Pages või GitHub Pages
  - Prioriteet: KÕRGE

- **Ande K lubas aidata** - Disaini tagasiside (2025-11-02)
  - Ta kujundab raamatuid
  - Annab tagasisidet mockup'ile koos teiste CoDA liikmetega

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
  - Staatus: Ootan meeskonna vastust
  - Workaround: Bash on `ask` listis

- **CoDA.org performance recommendations** - [EMAIL_DRAFT_LIGHTHOUSE.html](docs/EMAIL_DRAFT_LIGHTHOUSE.html)
  - Lighthouse test tulemused (Mobile: 3/100, Desktop: 33/100)
  - Saadetud Brendale edastamiseks tech meeskonnale: 2025-11-04
  - Ootan: vastust või implementeerimise tagasisidet

---

## ⏸️ Ootel / Planeeritud

### Milestone 0 - Structure and Decisions

**GitHub:** See [Milestone 0](https://github.com/Anne-dot/coda-eesti/milestone/1)

- [ ] **[Issue #2](https://github.com/Anne-dot/coda-eesti/issues/2): Visual identity and design system**
  - Töö tehtud, ootab rühma tagasisidet

- [ ] **[Issue #3](https://github.com/Anne-dot/coda-eesti/issues/3): UX & Accessibility planning**
  - Töö tehtud, ootab tagasisidet + Lighthouse teste (target: 90+)

- [ ] **[Issue #20](https://github.com/Anne-dot/coda-eesti/issues/20): Update global.css with color palette**
  - Töö tehtud, ootab Issue #3 sulgemist

- [ ] **[Issue #19](https://github.com/Anne-dot/coda-eesti/issues/19): Create mockup**
  - Sait ise on mockup, ootab deployd ja rühma tagasisidet

### Milestone 1 - MVP Static Site

**GitHub:** See [Milestone 1](https://github.com/Anne-dot/coda-eesti/milestone/2)

- [ ] **Leheküljed, mis EI VAJA CoDA materjale:**
  - [ ] Kontaktide leht (ainult koosoleku info)
  - [ ] "Meist" / "About" leht (üldine info grupi kohta)
  - [ ] FAQ leht (üldised küsimused)
  - **Märkus:** Need lehed võid teha valmis ja deployda kohe

- [ ] **Leheküljed, mis VAJAVAD CoDA materjale (oota luba!):**
  - [ ] ❌ 12 Sammu leht (vajab tõlkimisluba)
  - [ ] ❌ 12 Traditsiooni leht (vajab tõlkimisluba)
  - [ ] ❌ Päevatekstid / meditations (vajab tõlkimisluba)
  - [ ] ❌ Kirjanduse tsitaadid (vajab tõlkimisluba)
  - **Märkus:** Need jäta placeholder'iteks kuni saad loa

- [ ] **Sveltia CMS paigaldamine**
  - [ ] Config fail (admin/config.yml)
  - [ ] GitHub OAuth setup
  - [ ] Kasutajate õigused

- [ ] **GitHub Actions CI/CD**
  - [ ] Deploy workflow
  - [ ] Lighthouse CI

### Dokumentatsioon

- [ ] **Kasutajajuhend** - CMS-i kasutamine rühma liikmetele

- [ ] **Portfolio kirjeldus**
  - [ ] Projekti kirjeldus (eesti + inglise)
  - [ ] Screenshots
  - [ ] Tehnilised väljakutsed ja lahendused

### Pärast Valmimist

- [ ] **Teata coda.org-ile** - Eesti veebilehe valmimisest

---

### Tõlkimisdokumendi läbivaatamine ja suhtlus coda.org-ga

- [ ] **Jaga info rühmaliikmetega** PÄRAST TMC vastust (täielik pilt)

- [ ] **Arutage grupis läbi:**
  - [ ] Kes saab/tahab mida teha (vastutuste jaotus)
  - [ ] Kellel on õigus kasutada grupi e-maili aadressi?
  - [ ] Kes räägib piisavalt hästi inglise keelt vormide täitmiseks?
  - [ ] Kas taotleme $1000 USD toetust või mitte?
  - [ ] **Veebiannetused: kas ja kuidas?**

- [ ] **Tõlkimisloa taotlemine**
  - Link: https://coda.org/service-info/translation-mgmt-main-page/
  - Vastutaja: [Määrata koosolekul]
  - Märkus: Tehke PÄRAST koosoleku registreerimist!

---

## ⏸️ Edasi Lükatud / Madal Prioriteet

- [ ] **Vana Eesti lehe eemaldamine**
  - Staatus: Edasi lükatud kuni uue lehe valmimiseni
  - Põhjus: codaestonia.wordpress.com (2016) sisaldab eestikeelset infot
  - Tulevikus: Kui uus leht on live, saada e-mail meetings@coda.org palvega eemaldada

---

## 📝 Märkmed

- Backup tech-inimese leidmine tutvusringkonnast (tulevikus)
- Domeeninime valik (kui vaja oma domeeni)

---

**Projekti staatus:** 🟡 MVP arendus - ootab deployd ja tagasisidet
