
# Behave + Playwright Testprojekt

Projektet innehåller tester skrivna i **Behave BDD** tillsammans med **Playwright för Python**.<br>

## 📋 Projektbeskrivning

Projektet innehåller automatiserade tester skrivna med Behave (BDD-ramverk) och Playwright för Python. Testerna validerar följande funktionalitet:

- ✅ Navigering i applikationen
- ✅ Tillägg av böcker
- ✅ Favoritmarkering av böcker
- ✅ Borttagning av favoritmarkering
- ✅ Hovring vid favoritikoner

**Testmiljö:** [Läslistan](https://tap-vt25-testverktyg.github.io/exam--reading-list/)

---

## 📁 Projektstruktur

```
Behave_playwright_project/
├── src/                        # Källkod
│   ├── features/               # Gherkin feature-filer (.feature)
│   │   └── steps/              # Stepdefinitioner och environment.py
│   ├── pages/                  # Page Object Model-klasser
│── README.md                   # Denna fil
│── STORIES.md                  # User stories med acceptanskriterier
└── requirements.txt            # Python-beroenden
```

---
### Viktiga filer

- **`STORIES.md`** – Innehåller alla user stories med acceptanskriterier. Varje feature-fil refererar till sin user story.
- **`features/environment.py`** – Konfiguration för testmiljön (webbläsare, hooks, etc.)
- **`pages/`** – Page Object-klasser för strukturerad och underhållbar testkod
---
## Komma igång

### Förutsättningar
Innan du börjar, se till att du har följande installerat:

- Python 3.9 eller senare
- pip (Python package manager)
- Git (eller liknande för att klona projektet)
- venv (virtuell miljö), <i>inte ett krav</i>


### Installera projektet

#### 1. Klona projektet (om tillämpligt)

```bash
git clone <repository-url>
cd Tentamen_Behave_Playwright_project
```

#### 2. Skapa och aktivera den virtuella miljön (om du använder det)

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 3. Installera beroenden

```bash
pip install -r requirements.txt
```

Alternativt installera manuellt om `requirements.txt` inte helt fungerar:

```bash
pip install pytest-playwright
playwright install
pip install behave
```
> **OBS:** Kommandot `playwright install` laddar ner nödvändiga webbläsare (Chromium, Firefox, WebKit), om ditt system inte har browsers måste playwright install köras även när requirements installerar resten.
---
## ▶️ Köra tester

### Navigera till src-mappen

Alla Behave-kommandon måste köras från `src`-mappen:

```bash
cd src
```
### Kör alla tester

```bash
behave
```

### Kör specifik feature-fil

```bash
behave features/catalogue.feature
```

### Kör med detaljerad output

```bash
behave -v
```
---
## 🔧 Konfiguration

### Testmiljö

- **Webbläsare:** Chromium (headless mode)
- **Test-URL:** https://tap-vt25-testverktyg.github.io/exam--reading-list/
- **Konfigurationsfil:** `features/environment.py`

### Ändra webbläsare eller headless-läge

Redigera `features/environment.py` för att anpassa inställningar:

```python
# Exempel: Kör med synlig webbläsare
browser = playwright.chromium.launch(headless=False)
Inställningen är "True" i projektet
```

---

## 🧪 Testramverk och tekniker

| Teknik | Beskrivning |
|--------|-------------|
| **Behave** | BDD-ramverk för Python som använder Gherkin-syntax |
| **Playwright** | Modern automation-bibliotek för webbläsartestning |
| **Page Object Model** | Designmönster för underhållbar och återanvändbar testkod |
| **Gherkin** | Given/When/Then-syntax för läsbara testscenarier |

---