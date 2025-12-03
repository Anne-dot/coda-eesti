# Progress Updates

**Total time invested:** 7.5 hours

---

## 2025-11-02

**Time:** 11:00 - 15:30 (~4.5 hours)

**Completed:**
- Reorganized project folder structure
  - Created `/research` folder for research materials
  - Moved `lighthouse-testid` → `research/lighthouse-tests` (English naming)
  - Moved Python scripts and research documents
  - Deleted duplicate files (DRY principle)
  - Enhanced `parse_all_lighthouse.py` with comprehensive analysis
  - Created `/research/README.md` with navigation links
  - Fixed Python script paths
- Renamed `TECH_STACK_OTSUS.md` → `TECH_STACK_DECISION.md` (English naming)
- Created Issue #4: Reorganize project folder structure → Closed
- Created Issue #5: Document tech stack decisions (parent issue)
- Created and closed Issues #6-#11 with detailed documentation:
  - #6: Astro framework choice
  - #7: Tailwind CSS choice
  - #8: Shadcn/ui component library choice
  - #9: Sveltia CMS choice
  - #10: GitHub Pages hosting choice
  - #11: CI/CD pipeline approach
- Documented CI/CD pipeline decisions:
  - PR-based deployment workflow
  - Full build process with lint, type checking, and caching
  - Lighthouse CI in soft mode (PR + post-deployment)
- Updated permissions (reduced automatic permissions, keep WebSearch/WebFetch/Read)

**Impact:**
- **Milestone 0 progress:** Significant advancement in "Structure and Decisions" milestone
- **Issue #1 sub-tasks:** Completed folder structure (#4) and tech stack documentation (#5)
- **Documentation quality:** All tech stack decisions documented with rationale, alternatives, risks, and exit strategies
- **Best practices alignment:** Confirmed all decisions align with official documentation (Astro, GitHub Actions, Lighthouse CI)
- **DRY principle applied:** Removed duplicate files and scripts, single source of truth established
- **GitHub workflow established:** Parent/child issue structure working well for ADHD-friendly task management
- **Foundation ready:** Project structure and tech decisions documented, ready for Astro setup (Milestone 1)

**Tunded ja mõtted:**

Mul on suitsunälg. Mul on hea meel, et see oluline osa sai tehtud ja samas nagu ikka ma tahaks juba palju kaugemal olla. Mul on hea meel, et ma olin selleks piisavalt eeltööd teinud, et sain vormilisele poolele keskenduda ega pidanud liiga palju otsuseid enam vastu võtma. Ma olen enda üle uhke, sest ma olen õppinud dokumenteerima ja sellele viitama, enne edasi minekut. Ma tean, et see töö võimaldab edaspidi kiiremini ja kvaliteetsemalt projekti teha ja kokkuvõttes säästab aega, mitte ei kuluta. ATH jaoks on lihtsalt siin vist liiga vähe dopamiini.

---

**Time:** 22:30 - 00:00 (~1.5 hours)

**Completed:**
- Discovered and reported Bash permissions bug in Claude Code
  - Tested `gh issue create` executing without permission prompt
  - Found workaround: added "Bash" to "ask" list in settings.local.json
  - Created detailed bug report with reproduction steps
  - Posted Issue #10874 to anthropics/claude-code repository (first external bug report!)
  - Added to TODO.md "Jälgimist vajavad asjad" section for tracking
- Milestone 1 planning started
  - Reviewed Issue #5 structure (grouped sub-issues approach)
  - Planned Issue #12 sub-issues structure (6 tasks in 3 groups)
  - Created Issue #13: Initialize and configure Astro project
  - Updated Issue #12 with TASKS structure and Issue #13 link
  - Updated TODO.md with Milestone 1 structure and GitHub links

**Impact:**
- **Security improvement:** Bash permissions now properly prompt for confirmation
- **First external contribution:** Bug report to Claude Code helps improve the tool
- **Milestone 1 planning complete:** Clear structure with grouped sub-issues ready for implementation
- **ADHD-friendly workflow:** Small, focused issues (#13 created) following established pattern from Milestone 0
- **TODO.md tracking:** External issues now tracked in dedicated section
- **Ready for tomorrow:** Issue #13 ready to implement, remaining 5 sub-issues planned

**Tunded ja mõtted:**

Ma tunnen üheaegselt uhkust ja ärritust. Uhkust, et ma märkasin ja võtsin midagi bugi osas ette. St et ma muutsin oma claude seadistust ja kaitsesin ennast selle eest ja siis ka andsin sellest välismaailmale teada, sest see on minu meelest oluline. Ja ma tunnen ärritust, sest ai tehnoloogia on küll palju arenenud ja mulle on sellest palju kasu minu ath aju nõrkuste kompenseerimisel, kuid ma ei saanud bugiga tegelemise arvelt oma projektiga tegeleda. Samas ma ka tean, et homseks heaks stardiks on juba päris head tööd tehtud ning kõik on dokumenteeritud ja sellega seoses on ka lihtne jätkata täpselt siit, kus ma praegu pooleli jäin.

---

## 2025-12-03

**Time:** 22:00 - 23:31 (~1.5 hours)

**Completed:**
- Koosolek registreeritud coda.org lehel: https://coda.org/meeting/coda-kuressaare/
  - Ajavööndi parandus saadetud (GMT+3)
- Hosting muudetud GitHub Pages → Cloudflare Pages (privaatne repo OK)
- Repo muudetud privaatseks
- Dokumentatsioon uuendatud (DRY, single source of truth)
- **Tehniline setup VALMIS (Issue #12):**
  - #13: Astro v5.16.4 initsialiseeritud
  - #14: Tailwind CSS 4 (Vite plugin)
  - #15: Shadcn/ui + React integratsioon
  - #16: Prettier (Astro + Tailwind plugins)
  - #17: ESLint (recommended + jsx-a11y)
  - #18: Folder structure
- CLAUDE.md uuendatud tööstiili reeglitega

**Impact:**
- **Milestone 1 tehniline osa valmis** - dev keskkond töötab
- **Koosolek ametlikult registreeritud** - saab tõlkimisluba taotleda
- **Repo privaatne** - Cloudflare Pages võimaldab tasuta

**Tunded ja mõtted:**

Ma olen väsinud. Vahepeal kaob tasuliste uute projektidega seoses mott ära. Samas ma tean, et see on oluline ja kasulik paljudele inimestele. Lisaks on ka detsembris mõlema lapse sünnipäevad ja mitu jõulupidu.
