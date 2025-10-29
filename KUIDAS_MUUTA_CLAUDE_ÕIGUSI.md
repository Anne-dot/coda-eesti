# Kuidas Muuta Claude'i Õigusi Projektis

**Kuupäev**: 2025-10-29
**Projekt**: /home/d0021/Automation/coda

---

## Kui Andsid Claude'ile Automaatsed Õigused

Kui valisid valikud nagu:
- "Yes, and don't ask again for Web Search commands in /home/d0021/Automation/coda"
- "Yes, and don't ask again for WebFetch commands in /home/d0021/Automation/coda"
- Või muu "don't ask again" valik

Siis need õigused salvestati projekti konfiguratsioonifaili.

---

## Kuidas Õigusi Tagasi Võtta või Muuta

### Variant 1: Kustuta Projekti Kaust (Lihtne)

```bash
rm -rf ~/.claude/projects/coda/
```

**Mõju**: Kõik selle projekti automaatsed õigused kustutatakse. Claude küsib järgmisel korral uuesti.

**Märkus**: See ei kustuta sinu töökausta `/home/d0021/Automation/coda`, ainult Claude'i projekti seadeid.

---

### Variant 2: Muuda Konfiguratsioonifaili (Täpsem)

1. **Leia projekti konfiguratsioon**:
```bash
ls -la ~/.claude/projects/
```

2. **Otsi "coda" nimelist kausta**:
```bash
ls -la ~/.claude/projects/coda/
```

3. **Vaata, millised failid seal on**:
Tõenäoliselt leidub fail nagu `permissions.json` või `config.json`

4. **Ava fail redaktoriga**:
```bash
nano ~/.claude/projects/coda/permissions.json
# või
cat ~/.claude/projects/coda/permissions.json
```

5. **Kustuta või muuda read**, mis sisaldavad:
   - `WebSearch`
   - `WebFetch`
   - Või muid tööriistu, mille õigusi tahad tagasi võtta

6. **Salvesta fail** (Nano puhul: Ctrl+O, Enter, Ctrl+X)

---

### Variant 3: Kontrolli .claude Kausta Struktuuri

```bash
# Vaata kõiki Claude'i seadeid
ls -la ~/.claude/

# Vaata projektide kausta
ls -la ~/.claude/projects/

# Vaata selle konkreetse projekti seadeid
find ~/.claude/projects/ -name "*coda*"
```

---

## Kuidas Kontrollida, Kas Õigused on Antud?

```bash
# Otsi "coda" projekti seadeid
find ~/.claude -type f -name "*" | xargs grep -l "coda" 2>/dev/null

# Vaata projekti kausta sisu
tree ~/.claude/projects/coda/
# või
ls -laR ~/.claude/projects/coda/
```

---

## Kui Midagi Läheb Valesti

**OHUTU MEETOD**: Kustuta kogu projekti kaust ja alusta puhtalt lehelt:

```bash
# 1. Varunda (kui soovid)
cp -r ~/.claude/projects/coda ~/.claude/projects/coda_backup_$(date +%Y%m%d)

# 2. Kustuta projekti seaded
rm -rf ~/.claude/projects/coda/

# 3. Järgmisel Claude'i käivitamisel küsib ta uuesti õigusi
```

---

## Kiire Käsud

### Kustuta kõik "coda" projekti õigused:
```bash
rm -rf ~/.claude/projects/coda/
```

### Vaata, millised õigused on antud:
```bash
cat ~/.claude/projects/coda/permissions.json 2>/dev/null || echo "Faili ei leitud"
```

### Varunda enne kustutamist:
```bash
cp -r ~/.claude/projects/coda ~/.claude/projects/coda_backup_$(date +%Y%m%d_%H%M%S)
```

---

## Märkused

- **Töökaust** (`/home/d0021/Automation/coda/`) **EI KUSTUTATA** - see jääb alles
- Kustutatakse ainult Claude'i **projekti seaded** (`~/.claude/projects/coda/`)
- Pärast kustutamist küsib Claude järgmisel korral uuesti õigusi
- See on täiesti ohutu operatsioon

---

**Viimati uuendatud**: 2025-10-29
