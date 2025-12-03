# CODA Projekti Tagasiside ja Õppetunnid

**Kuupäev:** 2025-11-12
**Eesmärk:** Analüüsida CODA projekti protsessi, et luua paremad workflow'id ja template'id tulevasteks projektideks (nt. nirgu.ee redesign)

---

## Mida vaatasin

- README.md, TODO.md, PROGRESS_UPDATES.md
- TECH_STACK_DECISION.md, koosoleku protokoll
- Git commit history (20+ commiti)
- Kaustastruktuur (docs, research, lighthouse-tests)
- E-maili drafid ja TMC suhtlus
- GitHub issues ja milestones

---

## ✅ Mida tegid VÄGA HÄSTI

### 1. Dokumentatsioon ja struktuur

**README.md:**
- Selge projekti ülevaade koos badge'idega
- Tech stack selgelt välja toodud
- Lingid dokumentatsioonile
- Features ja nõuded loetletud

**TODO.md:**
- Väga detailne ja struktureeritud
- GitHub issue linkidega
- Milestone'id selgelt eraldatud
- Staatused tähistatud (⏸️ ootel, ⏳ käimas, ✅ valmis)
- Vastutajad märgitud

**PROGRESS_UPDATES.md:**
- SUUREPÄRANE lähenemine!
- Ajakulu dokumenteeritud
- Emotsioonid ja mõtted kirjas (väga väärtuslik tagasivaatamiseks)
- Impact sektsioon - mida saavutati
- Aus ja avatud peegeldus

**TECH_STACK_DECISION.md:**
- Põhjalik otsustusprotsess
- Alternatiivid kaalutud (Jekyll, 11ty, Hugo vs Astro)
- Riskid ja mitigatsioonid kirjas
- Selge põhjendus iga valiku kohta
- Tabel nõuete täitmise kohta

**docs/PROTOKOLLID/:**
- Koosoleku protokoll kohe pärast kohtumist
- Osalejad, eesmärk, otsused kirjas
- Tegevused ja vastutajad määratud
- Järgmised sammud selged

### 2. Protsess ja planeerimine

**Esimene kohtumine:**
- Kohe protokoll kirja pandud
- Otsused dokumenteeritud
- Vastutajad määratud

**Põhjalik uurimustöö:**
- Lighthouse testid CODA riikide lehtedele
- Python skript analüüsiks
- Platvormide võrdlus (WordPress, Wix, Google Sites)
- Research materjalid eraldi kaustas

**GitHub kasutamine:**
- Issues + milestones ADHD-friendly lähenemine
- Parent/child issue struktuur
- Selge vastutuste jaotus TODO-s
- Milestone progress tracking

**Välissuhtlus:**
- TMC e-mailid dokumenteeritud
- Follow-up'id jälgitud
- Vastuste ootamine TODO-s märgitud

### 3. Tehnilised aspektid

**Git:**
- Kasutamine algusest peale
- Regulaarsed commitid
- .gitignore korralikult seadistatud

**Automatiseerimine:**
- Python skriptid lighthouse testide analüüsiks
- Research/data eraldi kaustas

**Kaustastruktuur:**
- `/docs` - dokumentatsioon
- `/docs/PROTOKOLLID` - koosolekud
- `/research` - uurimustöö
- `/research/lighthouse-tests` - testid

---

## 💡 Mida PUUDUS coda projektis

Need punktid on võimalused tulevaste projektide parandamiseks.

### 1. PUUDUB: Esimese kohtumise ETTEVALMISTUS

**Olukord:**
Protokoll on olemas PÄRAST kohtumist, aga ette valmistumise dokumenti pole näha.

**Järgmiseks korraks:**
Fail `meeting-preparation.md` enne esimest kohtumist:
- Kellega kohtumine? (nimi, ettevõte, roll)
- Mis on nende praegune olukord? (olemasolev veebileht, probleemid)
- Mida nad tahavad saavutada? (eesmärgid, ootused)
- Küsimused kliendile:
  - Eelarve ja ajakava ootused?
  - Sihtrühm ja kasutajad?
  - Tehnilised nõuded (hosting, CMS, jms)?
  - Kes haldab pärast valmimist?
  - Mida peab kindlasti sisaldama?
  - Mida EI tohi sisaldada?

**Miks oluline:**
Struktureeritud küsimused aitavad kohtumist juhtida ja tagavad, et kõik oluline saab käsitletud. Ei unusta midagi ära küsida.

### 2. PUUDUB: UX Audit ENNE projekti

**Olukord:**
Lighthouse testid on tehtud (performance), aga kasutajakogemuse (UX) analüüsi ei ole.

**Järgmiseks korraks:**
Fail `ux-audit.md` olemasoleva lehe kohta:
- **Navigatsioon** - kas arusaadav? Kas leiab otsitava?
- **Visuaalne hierarhia** - mis on kõige olulisem? Kas see eristub?
- **Mobiili kasutajakogemus** - kas mugav? Kas nupud piisavalt suured?
- **Juurdepääsetavus** - kontrast, fondid, alt-tekstid
- **Sisu kvaliteet** - kas arusaadav? Kas piisavalt infot?
- **CTA elementide asetus** - kas selge, mida kasutaja peaks tegema?
- **Kasutajate teekond** (user journey) - kuidas tüüpiline kasutaja lehte kasutab?
- **Leitud probleemid** - mis ei tööta? Mis on segane?
- **Positiivsed aspektid** - mida säilitada redesignis?

**Miks oluline:**
Lighthouse mõõdab tehnilist kvaliteeti. UX audit mõõdab kasutaja kogemust. Mõlemad on olulised.

### 3. PUUDUB: Selge projekti faaside dokument

**Olukord:**
TODO.md on kohati segane (sa ise märkisid: "TODO.md vajab korrigeerimist - Sisu on läinud lappesse"). Milestoned on läbisegi. Ei ole selget "workflow" dokumenti.

**Järgmiseks korraks:**
Fail `project-workflow.md` mis kirjeldab üldist protsessi:

**FAAS 1: Discovery & Negotiation (01-discovery-negotiation/)**
- Meeting preparation (küsimuste ettevalmistus)
- First meeting (esimene kohtumine)
- UX audit (olemasoleva lehe analüüs kui redesign)
- Testing plan (millised brauserid, seadmed testida)
- Proposal/quote (hinnapakkumine ja scope)
- Decision (võtan vastu või mitte)

**FAAS 2: In Progress (02-in-progress/)**
- Tech setup (projekti alustamine)
- Design (visuaalne kujundus)
- Development (arendamine)
- Testing (testimine)

**FAAS 3: Delivered (04-delivered/)**
- Client review (kliendi ülevaatus)
- Adjustments (parandused)
- Final delivery (lõplik üleandmine)
- Handover (dokumentatsiooni üleandmine)

**FAAS 4: Ongoing Support (05-ongoing-support/)**
- Bug fixes (veaparandused)
- Minor updates (väikesed uuendused)
- Support requests (toe taotlused)

**Miks oluline:**
Selge workflow aitab aru saada, millises faasis projekt on ja mis on järgmine samm. TODO.md võib olla detailne, aga workflow annab suure pildi.

### 4. PUUDUB: Testimisplaan

**Olukord:**
Sa mainsid, et alustad testimisplaanist, aga coda projektis pole seda veel dokumenti.

**Järgmiseks korraks:**
Fail `testing-plan.md`:

**Browser compatibility:**
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

**Mobile devices:**
- iOS Safari (iPhone)
- Android Chrome (Android phone)
- Tablet (iPad või Android tablet)

**Accessibility testing:**
- Keyboard navigation (Tab, Enter, Esc)
- Screen reader testing (NVDA või VoiceOver)
- Color contrast (WCAG AA minimum)
- Focus states visible
- Alt texts for images

**Performance testing:**
- Lighthouse score targets (Performance 90+, Accessibility 90+, Best Practices 90+, SEO 90+)
- Mobile performance
- Desktop performance

**Content management testing:**
- CMS login (kas töötab?)
- Content editing (kas lihtne?)
- Image upload (kas toimib?)
- Preview function (kas näitab õigesti?)

**Functional testing:**
- All links working
- Forms submitting correctly
- Navigation working
- Search function (kui on)
- Contact form (kui on)

**Cross-device testing:**
- Layout breaks (kas kujundus jääb terveks?)
- Image sizing (kas pildid on õiges suuruses?)
- Text readability (kas tekst on loetav?)

**Miks oluline:**
Testimisplaan tagab, et midagi ei unustata testida. Eriti oluline redesigni puhul, kus on olemas ootused.

### 5. PUUDUB: Hinnapakkumise template

**Olukord:**
CODA oli vabatahtlik projekt, aga nirgu.ee on tasuline töö.

**Järgmiseks korraks:**
Fail `proposal-template.md`:

**Projekti kirjeldus:**
- Mis on projekt?
- Mis on eesmärk?
- Kellele on mõeldud?

**Scope of work (töömahu kirjeldus):**
- Mida TEEN (näiteks: UX audit, disain, arendus, testimine, üleandmine)
- Mida EI TEE (out of scope - näiteks: content writing, SEO optimeerimine, logo disain)

**Deliverables (tulemused):**
- Mis sa kliendile üle annad? (näiteks: valmis veebileht, lähtekood, kasutusjuhend, CMS juhend)

**Timeline (ajakava):**
- Faas 1: Disain (2 nädalat)
- Faas 2: Arendus (3 nädalat)
- Faas 3: Testimine ja üleandmine (1 nädal)
- Kokku: 6 nädalat

**Hind:**
- Koguhind või tunnitasu
- Maksegraafikud (näiteks: 50% alguses, 50% üleandmisel)
- Mida hind sisaldab?

**Mida EI sisaldu (out of scope):**
- SEO optimeerimine (saab lisada eraldi)
- Content writing (klient teeb ise)
- Logo disain (klient annab valmis logo)

**Tingimused:**
- Maksetingimused
- Autoriõigused (kes omab koodi?)
- Garantii (kui kaua pakud toe?)
- Muudatuste protsess (kuidas käsitleda scope muudatusi?)

**Miks oluline:**
Selge pakkumine hoiab ära arusaamatusi ja scope creep'i. Mõlemad osapooled teavad, mida oodata.

### 6. PUUDUB: Client communication log

**Olukord:**
TMC e-mailid on dokumenteeritud (suurepärane!), aga ei ole ühtset kohta kõigi kliendi suhtluste jaoks.

**Järgmiseks korraks:**
Fail `client-communication.md`:
- Kuupäev ja kellaaeg
- Suhtluse tüüp (kohtumine, e-mail, telefon, chat)
- Kokkuvõte (mis arutati? Mis otsustati?)
- Tegevused (kes teeb mida?)
- Järgmine kontakt (millal?)

**Miks oluline:**
Kõik suhtlus ühes kohas aitab meenutada, mis oli kokku lepitud. Eriti oluline, kui projekt kestab kaua või on palju tagasisidet.

---

## 🔧 Mida saaks PAREMINI teha

### 1. Git commitid võiksid olla paremad

**Praegused commitid:**
- ✅ Hea: "Add PROGRESS_UPDATES.md with personal reflections"
- ✅ Hea: "Reorganize project structure for Astro setup"
- ❌ Nõrk: "Uuenda TODO: TMC kohtumine ja disaini abi" (eesti keel, ebaselge)
- ❌ Nõrk: "Lisa TODO: Ootan grupi vastust koosoleku registreerimise kohta" (liiga spetsiifiline)

**Parim praktika (Conventional Commits):**
```
feat: Add meeting preparation document
fix: Correct TODO milestone structure
docs: Update README with project status
refactor: Reorganize docs folder structure
chore: Update .gitignore for lighthouse tests
```

**Miks oluline:**
Hea commit message aitab hiljem aru saada, mis muutus ja miks. Inglise keel on standard (kui projekt on avalik või on võimalik, et tulevikus tuleb teisi arendajaid).

### 2. TODO.md struktuur läks segaseks

**Probleem:**
Sa ise märkisid: "TODO.md vajab korrigeerimist - Sisu on läinud lappesse. Milestone 1, 2, 3 sisu on segamini."

**Lahendus:**
- Hoia TODO.md lihtne (ainult praegused tegevused ja järgmised sammud)
- Detailne planeerimine → GitHub issues
- Archive valmis tegevused → PROGRESS_UPDATES.md
- TODO.md on "praegune olukord", mitte kogu projekti ajalugu

**Struktuur:**
```markdown
# TODO - CODA Eesti

## ⏳ Käimas (In Progress)
- [x] Issue #13: Astro setup
- [ ] Issue #14: Tailwind CSS setup (started 2025-11-05)

## 📋 Järgmisena (Next Up)
- [ ] Issue #15: Shadcn/ui components
- [ ] Issue #2: Visual identity

## ⏸️ Ootan vastust (Blocked)
- Brenda vastus (TMC)
- Grupi otsus koosoleku registreerimise kohta
```

### 3. Research materjalid võiksid olla kompaktsemad

**Olukord:**
15+ MB lighthouse teste, pikad JSON failid.

**Soovitus:**
- Hoia ainult summary tulemused version control'is
- Täielikud JSON'id → .gitignore (või eraldi archive kaust)
- README.md research kaustas kirjeldab, kust täielikud tulemused leida

**Miks oluline:**
Väiksem repo, kiirem kloneerimine, lihtsam navigeerida.

---

## 🎯 KONKREETSED SOOVITUSED nirgu.ee jaoks

### Templates nirgu.ee projekti jaoks

Järgmised failid tuleks luua ENNE esimest kohtumist:

**1. `meeting-preparation.md`**
Küsimused esimeseks kohtumiseks (vt punkt 1 üleval)

**2. `ux-audit-checklist.md`**
UX hindamise kriteeriumid nirgu.ee olemasolevale lehele (vt punkt 2 üleval)

**3. `testing-plan-template.md`**
Testimisplaani mall (vt punkt 4 üleval)

**4. `project-workflow.md`**
Üldine projekti protsess (vt punkt 3 üleval) - see on reusable template, mida saad kasutada kõigile projektidele

**5. `proposal-template.md`**
Hinnapakkumise template (vt punkt 5 üleval)

**6. `client-communication.md`**
Kliendi suhtluste log (vt punkt 6 üleval)

### Workflow nirgu.ee projektile

**ENNE esimest kohtumist:**
1. Vaata nirgu.ee lehte läbi
2. Täida `ux-audit-checklist.md` (mis töötab? mis mitte?)
3. Täida `meeting-preparation.md` (küsimused)
4. Tee Lighthouse test nirgu.ee-le (performance baseline)

**Esimene kohtumine:**
1. Kasuta `meeting-preparation.md` küsimusi
2. Tee märkmeid kohtumise ajal
3. Kohe pärast kohtumist → `docs/PROTOKOLLID/2025-XX-XX.md`

**Pärast esimest kohtumist:**
1. Täida `testing-plan.md` (millised brauserid? seadmed?)
2. Koosta `proposal.md` (hind, scope, ajakava)
3. Saada kliendile üle vaatamiseks
4. Otsus: võtan vastu või mitte?

**Projekti käigus:**
1. Uuenda `client-communication.md` iga suhtluse järel
2. Uuenda TODO.md (kas on schedule'is?)
3. Uuenda PROGRESS_UPDATES.md (ajakulu, saavutused)

**Pärast valmimist:**
1. Tee retrospektiiv (mis läks hästi? mis paremini?)
2. Liiguta projekt → `04-delivered/`
3. Archive õppetunnid template'idesse

---

## 📚 Õppetunnid (Key Takeaways)

### Mida jätkata (Keep doing)

1. **Dokumenteeri kohe** - protokollid, otsused, suhtlus kohe pärast sündmust
2. **PROGRESS_UPDATES.md** - ajakulu + emotsioonid on väga väärtuslik
3. **Põhjalik uurimustöö** - lighthouse testid, alternatiivide võrdlus
4. **GitHub issues** - ADHD-friendly, väikesed sammud
5. **Tech stack põhjendused** - kirja panna, miks valisid selle, mitte teise

### Mida alustada (Start doing)

1. **Meeting preparation** - küsimused ENNE kohtumist valmis
2. **UX audit** - mitte ainult Lighthouse, ka kasutajakogemus
3. **Client communication log** - kõik suhtlus ühes kohas
4. **Testimisplaan** - enne arendamist, mitte pärast
5. **Selge workflow** - millised faasid? mis on järgmine samm?

### Mida muuta (Change)

1. **TODO.md** - hoia lihtsana, ainult praegune olukord
2. **Git commitid** - inglise keel, conventional commits format
3. **Research materjalid** - .gitignore suured failid

---

## 🚀 Järgmised sammud

**Nirgu.ee projekti jaoks:**

1. Loo template'id (meeting-preparation, ux-audit, testing-plan, proposal)
2. Vaata nirgu.ee lehte läbi (UX audit)
3. Tee Lighthouse test (baseline)
4. Valmista ette küsimused esimeseks kohtumiseks
5. Pärast esimest kohtumist → protokoll + proposal

**Üldised template'id:**

Pärast nirgu.ee projekti lõppu, tee üldised template'id:
- `~/Automation/templates/web-project-workflow.md`
- `~/Automation/templates/meeting-preparation.md`
- `~/Automation/templates/ux-audit-checklist.md`
- `~/Automation/templates/testing-plan.md`
- `~/Automation/templates/proposal-template.md`

Neid saad kasutada kõigile tulevastele veebi projektidele.

---

## 📝 Lõppmõtted

CODA projekt oli suurepärane õppimisvõimalus. Sa tegid palju asju väga hästi:
- Dokumenteerimine oli põhjalik
- GitHub kasutamine struktureeritud
- Välissuhtlus professionaalne
- Otsustusprotsess läbimõeldud

Peamised võimalused parandamiseks:
- Ettevalmistus ENNE kohtumist (mitte ainult pärast)
- UX audit lisaks Lighthouse testidele
- Selge workflow/faaside dokument
- Testimisplaan varakult
- Client communication log

Nirgu.ee projekt on võimalus neid õppetunde rakendada ja luua paremad töövood ja template'id tulevasteks projektideks.

---

**Dokumendi koostas:** Claude AI
**Kuupäev:** 2025-11-12
**Põhineb:** CODA projekti analüüsil (29. oktoober - 5. november 2025)
