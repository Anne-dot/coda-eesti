# Tech Stack Otsus - CODA Eesti Veebileht

**Kuupäev:** 2025-10-29
**Otsustaja:** Anne (nooremtarkvararendaja)
**Kontekst:** Pärast koosolekut, kus WordPress.com reklaamid ei vaimustanud ja Google Sites disainipiirangud ei sobinud

---

## Lõplik Tech Stack

- **Static Site Generator:** Astro
- **CMS:** Sveltia CMS
- **Styling:** Tailwind CSS
- **UI Components:** Shadcn/ui
- **Hosting:** GitHub Pages
- **CI/CD:** GitHub Actions

---

## Otsustusprotsess

### Algne olukord

Koosolekul tutvustati tasuta platvorme (WordPress.com, Wix, Google Sites, Weebly). Peamised probleemid:
- **WordPress.com** - reklaamid lehel (tasuta plaanil)
- **Wix** - väga silmatorkavad reklaamid
- **Google Sites** - liiga suured disainipiirangud (ei saa kasutada CODA.org värvikoode ja fonte)
- **Weebly** - keeruline üleandmine, ebaselge mitme administraatori tugi

### Nõuded

**Funktsionaalsed:**
- Tasuta lahendus
- Reklaamideta
- Mitme administraatori tugi (3+ inimest)
- Lihtne sisu haldamine mittetehnilisele kasutajale
- Haldamise üleandmine võimalik

**Tehnilised:**
- Mobile-first lähenemine
- Kõrge accessibility (Lighthouse 90-100)
- CODA.org disaini järgimine (täpsed värvikoodid ja fondid)
- Kiire laadimisaeg

**Arendaja vaatenurk:**
- Portfoolio väärtus (modernne tehnoloogia)
- Õppimisvõimalus
- Tulevikukindel (ei ole "legacy" teel)
- Komponentide taaskasutamine

---

## Static Site Generator Valik

### Kaalutud variandid

**Jekyll:**
- ✅ GitHub Pages native support (zero config)
- ✅ Suur community, palju ressursse
- ✅ Stabiilne ja usaldusväärne
- ❌ Ruby dependency (aeglasem setup)
- ❌ Aeglasem build
- ❌ "Legacy" staatuses (ei kasva enam)
- ❌ Kaotab turuosa uutele SSG-dele
- ❌ 5 aasta pärast tuleb ikkagi õppida midagi uut

**11ty (Eleventy):**
- ✅ Modernne (2018+)
- ✅ Kõige kiirem SSG
- ✅ Lihtne õppida
- ✅ Hea portfoolio väärtus
- ❌ Väiksem community kui Jekyll
- ❌ Vähem valmis teemasid

**Hugo:**
- ✅ Kõige kiirem build (Go-based)
- ✅ Populaarne, suur community
- ❌ Go templating keerulisem õppida
- ❌ Järsem õppimiskõver

**Astro:** ⭐ **VALITUD**
- ✅ **Kõige modernisem** (2021+)
- ✅ **Kõige kiiremini kasvav** SSG turul (TOP 3)
- ✅ **Parim portfoolio väärtus** (näitab kursis olemist tänapäevaste trendidega)
- ✅ **Islands Architecture** (ainult vajalik JS laetakse)
- ✅ **Zero JS by default** (kiire lehekülg)
- ✅ **Komponentide tugi** (React, Vue, Svelte)
- ✅ **Valmis komponendid** (Shadcn/ui) - ei pea ise leiutama
- ✅ **Tulevikukindel** (aktiivne development, kasvav populaarsus)
- ✅ **Lihtne õppida** (kui oskad HTML ja JS)
- ✅ Töötab hästi GitHub Pages'iga (GitHub Actions)
- ⚠️ Vajab GitHub Actions workflow (1 fail, 10 rida)

### Põhjendus

Astro valiti, sest:
1. Anne on programmeerija ja tunneb GitHub Actions'it juba (kasutas Discord boti jaoks)
2. Portfoolio projekt on oluline - Astro on kõige modernisem ja näitab kursis olemist
3. Komponentide taaskasutamine (Shadcn/ui) kiirendab arendust
4. Tulevikukindel - 5 aasta pärast on standard, mitte "uus fancy asi"
5. Jekyll oleks "legacy" õppimine - tuleks ikkagi hiljem Astro õppida

---

## CMS Valik

### Nõue: 3+ kasutajat (rühma liikmed)

**Tina CMS:**
- ✅ Parim UX ("edit in place")
- ✅ Modernne
- ❌ **Tasuta ainult 2 kasutajat** (ei sobi - vajame 3+)
- ❌ $9/kuu per kasutaja pärast

**Decap CMS (endine Netlify CMS):**
- ✅ 100% tasuta
- ✅ Piiramatu kasutajate arv
- ✅ Git-based (kõik GitHub'is)
- ✅ Suur community
- ❌ Aegunud UX
- ❌ Development aeglustunud (community fork)

**Sveltia CMS:** ⭐ **VALITUD**
- ✅ **100% tasuta**
- ✅ **Piiramatu kasutajate arv**
- ✅ **Git-based** (kõik muudatused GitHub'is)
- ✅ **Decap CMS drop-in replacement** (kasutab sama config faili)
- ✅ **Parem UX** kui Decap
- ✅ **Kiirem** kui Decap
- ✅ **Saab lihtsalt switchida** Decap CMS-ile kui probleeme (1 rea muudatus)
- ⚠️ Uus projekt (2023) - väike community

### Põhjendus

Sveltia CMS valiti, sest:
1. Tasuta ja piiramatu kasutajate arv (Tina oleks kallis)
2. Parem kasutajakogemus kui Decap (rühma liikmetele lihtsam)
3. Modernne (sobib Astro'ga hästi kokku)
4. Fallback võimalus Decap CMS-ile (riskivaba valik)

---

## Styling & UI

### Tailwind CSS ⭐ **VALITUD**

**Põhjused:**
- ✅ Kõige populaarsem CSS framework 2025
- ✅ Suurepärane portfoolio väärtus
- ✅ Utility-first = kiire development
- ✅ Mobile-first built-in
- ✅ Väike bundle size (PurgeCSS)
- ✅ Astro'ga hästi integreeritud

**Alternatiivid:**
- Vanilla CSS/SASS - aeglasem development, vähem trendy
- Bootstrap - generic välimus, raske bundle

### Shadcn/ui ⭐ **VALITUD**

**Põhjused:**
- ✅ Valmis accessible komponendid
- ✅ Tailwind-based (sobib stackiga)
- ✅ Kiire prototüüpimine
- ✅ WCAG standarditele vastav (accessibility)
- ✅ Ei pea ise komponente leiutama

---

## Hosting

### GitHub Pages ⭐ **VALITUD**

**Põhjused:**
- ✅ **100% tasuta**
- ✅ **Reklaamideta**
- ✅ **Oma domeen võimalik** (tasuta)
- ✅ **HTTPS vaikimisi**
- ✅ **Git versioonikontroll**
- ✅ **Piiramatu arv collaborators**
- ✅ Anne tunneb GitHub Actions'it juba

**Alternatiivid:**
- Netlify - tasuta, aga lisateenused pole vajalikud
- Vercel - sama mis Netlify
- Cloudflare Pages - hea, aga GitHub on tuttavam

---

## Kokkuvõte

**Valitud stack vastab KÕIGILE nõuetele:**

| Nõue | Lahendus |
|------|----------|
| Tasuta | ✅ Kõik komponendid 100% tasuta |
| Reklaamideta | ✅ GitHub Pages pole reklaame |
| Mitme admini | ✅ Piiramatu (Sveltia CMS) |
| CODA.org disain | ✅ Täielik kontroll (Tailwind) |
| Mobile-first | ✅ Tailwind built-in |
| Accessibility | ✅ Shadcn/ui + Astro |
| Kiire | ✅ Astro zero JS |
| Portfoolio | ✅ Modernne stack |
| Tulevikukindel | ✅ Astro kasvab |
| Õppimine | ✅ Uued oskused |

**Lisaboonused:**
- Git versioonikontroll (kõik muudatused jälgitavad)
- Lihtne backup (kõik GitHub'is)
- CI/CD (GitHub Actions automaatne deploy)
- Skaleeruv (static = kiire ka palju külastajatega)

---

## Riskid ja Mitigatsioonid

### Risk 1: Sveltia CMS on uus (2023)
**Mitigatsioon:** Kasutab Decap CMS config formaati. 1 rea muudatusega saab minna Decap CMS-ile üle.

### Risk 2: Rühma liikmed peavad õppima CMS-i
**Mitigatsioon:** Teen põhjaliku kasutajajuhendi screenshotidega. Sveltia UX on lihtne.

### Risk 3: Anne lahkub projektist
**Mitigatsioon:** Kõik on GitHub'is, dokumenteeritud. Leiab backup tech-inimese tutvusringkonnast.

### Risk 4: Astro muutub
**Mitigatsioon:** Astro on stabiilne ja kasvav. Static output töötab alati (HTML/CSS/JS).

---

**Otsuse tegi:** Anne
**Kinnitatud:** 2025-10-29
**Järgmine review:** Pärast prototüübi valmimist
