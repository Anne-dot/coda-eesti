# TODO - CODA Eesti Veebileht

**Viimati uuendatud:** 2025-10-30

---

## ⏳ Käimasolevad

*Hetkel puuduvad*

---

## ⏸️ Ootel / Planeeritud

### PRIORITEET 1: Tõlkimisdokumendi läbivaatamine ja suhtlus coda.org-ga

- [ ] **Vaata läbi tõlkimisdokument** - `docs/CODA_TOLKIMISE_PROTSESS.md`
  - [ ] Loe dokument läbi
  - [ ] Jaga info rühmaliikmetega
  - [ ] Kontrolli üle, kas midagi on puudu

- [ ] **Arutage grupis läbi:**
  - [ ] Kes saab/tahab mida teha (vastutuste jaotus)
  - [ ] Kellel on õigus kasutada grupi e-maili aadressi?
  - [ ] Kes räägib piisavalt hästi inglise keelt vormide täitmiseks?
  - [ ] Kas taotleme $1000 USD toetust või mitte?
  - [ ] **Veebiannetused: kas ja kuidas saaksime annetusi koguda?**
    - Kas tahame üldse annetusi koguda?
    - Milliseid platvorme kasutada? (Stripe, PayPal, Wise, pangalink?)
    - Kas võimaldada rahvusvahelisi annetusi? (veebikoosolekul osalejad võivad tahta toetada)
    - Kes haldab rahalisi tehinguid?
    - Läbipaistvus ja aruandlus
    - Milleks annetusi kasutada? (hosting, domeeninimi, materjalide trükkimine?)

- [ ] **Registreerige koosolek coda.org lehel** (PRIORITEET KÕRGE)
  - Link: https://coda.org/find-a-meeting/add-new-meeting/
  - Vastutaja: [Määrata koosolekul]
  - Märkus: See tuleb teha ENNE tõlkimisloa taotlemist (vaja group number'it)

- [ ] **Vana Eesti lehe sulgemine** (PRIORITEET KÕRGE)
  - E-mail tmc@coda.org ja/või [email protected]
  - Teema: codaestonia.wordpress.com eemaldamine
  - Vastutaja: [Määrata koosolekul - vajab e-maili õigust]

- [ ] **Tõlkimisloa taotlemine** (PRIORITEET KESKMINE-KÕRGE)
  - Link: https://coda.org/service-info/translation-mgmt-main-page/ ("Start Here")
  - Vastutaja: [Määrata koosolekul - peab rääkima inglise keelt]
  - Märkus: Tehke PÄRAST koosoleku registreerimist!

### Uurimistöö ja Kommunikatsioon

- [ ] **Lighthouse testimine** - Testi teiste CODA riikide lehti
  - [ ] codauk.org
  - [ ] coda-deutschland.de
  - [ ] codacanada.ca
  - [ ] codaireland.com
  - [ ] codependentsanonymous.org.au
  - [ ] Analüüsi tulemused ja tee kokkuvõte

- [ ] **Jaga uurimustööd** - Saada Facebook gruppi AI tehtud uurimustöö

### PRIORITEET 2: Veebilehe Tehniline Alustamine (EI VAJA coda.org nõusolekut)

**Võid alustada kohe paralleelselt konsultatsioonidega!**

- [ ] **Projekti kausta struktuur**
  - [ ] Korrasta olemasolevad failid loogiliselt
  - [ ] Määra kaustade struktuur (docs, src, public jne)
  - [ ] Liiguta failid õigetesse kaustadesse
  - **Märkus:** Tee enne Astro setupi!

- [ ] **Astro projekti setup**
  - [ ] npm init astro
  - [ ] Tailwind CSS seadistamine
  - [ ] Shadcn/ui integreerimine
  - [ ] Projekti struktuur
  - **Märkus:** Tehniline setup ei vaja CoDA luba

- [ ] **CODA.org disaini analüüs**
  - [ ] Värvikoodid
  - [ ] Fondid
  - [ ] Paigutus ja komponendid
  - **Märkus:** Disaini uurimine ja inspireerimine on OK

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
- [ ] **Lisa koosolek coda.org lehele** - Vastutaja määramata

---

## ✅ Tehtud

- [x] GitHub repo loomine (coda-eesti)
- [x] Koosoleku protokoll (2025-10-29)
- [x] Tech stack otsus
- [x] README.md
- [x] .gitignore
- [x] Uurimustöö dokumentatsioon
- [x] CoDA tõlkimise protsessi ja autoriõiguste uurimine (2025-10-30)
- [x] Voting Entity nõuete uurimine
- [x] Eesti konkreetsete sammude dokumenteerimine
- [x] E-maili draft koostamine coda.org-le (ei olnud palutud - kaassõltlaslik AI omalooming abiks)

---

## 📝 Märkmed

- Backup tech-inimese leidmine tutvusringkonnast (tulevikus)
- Domeeninime valik (kui vaja oma domeeni)

---

**Projekti staatus:** 🟡 Planeerimine ja setup faas
