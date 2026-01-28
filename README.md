# 🚀 Project Spike BDD con pytest-bdd

Questo repository contiene un framework di test automatizzati basato su **pytest-bdd** (Python BDD).  
Il progetto è configurato per essere universale (Windows, macOS, Linux) e integra strumenti per la reportistica e l'analisi della copertura del codice.

---

## 🛠️ Configurazione Ambiente

### 1. Installazione Virtual Environment

Il progetto utilizza `pipenv` per gestire le dipendenze in modo isolato.  
Per creare l'ambiente virtuale e installare tutti i pacchetti necessari (inclusi quelli di sviluppo e testing):

```bash
pipenv install --dev
```

### 2. Installazione Estensioni VS Code

Per il corretto funzionamento del Test Explorer e del **Go to Definition** (F12), installa queste estensioni direttamente in Visual Studio Code:

#### Cucumber (Gherkin) Full Support

Necessaria per l'evidenziazione della sintassi nei file `.feature`.

---


## 📂 Struttura del Progetto

- `tests/features/`  
  Contiene i file Gherkin (`.feature`)

- `tests/steps/`  
  Contiene le implementazioni degli step in Python

- `reports/`  
  Cartella autogenerata con i report HTML di esecuzione e copertura

- `support/` 
  Librerie che vengono utilizzate dentro ai vari steps 
  ---
## 🏃 Comandi per Eseguire i Test

Puoi gestire l'esecuzione tramite i comandi configurati nel `Pipfile`.  
Questi comandi utilizzano script Python interni per garantire la compatibilità su ogni sistema operativo.

### 1. Esecuzione Test Standard

Esegue tutti i test e mostra i risultati nel terminale:

```bash
pipenv run test
```

### 2. Generazione Report HTML

Esegue i test e apre automaticamente il browser con il report grafico dettagliato:

```bash
pipenv run report
```

### 3. Analisi della Coverage (Copertura)

Calcola la percentuale di codice coperta dai test e apre il report HTML interattivo:

```bash
pipenv run coverage-report
```

---

## 🔍 Esecuzione dal Test Explorer

Oltre ai comandi da terminale, puoi utilizzare l'interfaccia grafica di VS Code per una gestione più visuale:

- Apri la tab **Testing** (icona del becher nella barra laterale sinistra)
- Qui trovi l'elenco di tutte le **Feature** e gli **Scenario** rilevati nel progetto
- Puoi avviare singoli test o intere cartelle cliccando sull'icona ▶️

---