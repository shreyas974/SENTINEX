# SENTINEX — JupyterLab on IBM LinuxONE (s390x) Guide
## Turnkey Workspace Layout, Notebook Execution & Terminal Operations

**Host Infrastructure**: IBM LinuxONE Community Cloud  
**System Architecture**: `s390x` (IBM z/Architecture 64-Bit Mainframe)  
**Operating System**: Ubuntu 24.04 LTS  
**Python Runtime**: Python 3.12 (`~/jupyter-env/` / `~/sentinex-env/`)  
**JupyterLab Port**: `8888`  
**GitHub Repository**: `https://github.com/shreyas974/SENTINEX`  

---

## 1. LinuxONE JupyterLab Directory Structure

Inside the LinuxONE server at `/home/linux1/SENTINEX`, the workspace is structured as follows:

```text
/home/linux1/
│
└── SENTINEX/                                   # Repository Root Directory
    │
    ├── notebooks/                              # JupyterLab Notebooks
    │   ├── NEXGUARD_AI.ipynb                   # Primary Challenge & Evaluation Notebook
    │   └── industrial_research_zoo.ipynb       # 7-Lab Industrial Research Pipeline
    │
    ├── data/                                   # Streaming & Synthetic Datasets
    │   ├── synthetic/
    │   │   └── smsd_baseline.csv               # 10,000-sample SMSD safety dataset
    │   └── processed/                          # Z-score calibrated arrays
    │
    ├── app/                                    # Production Backend Engine
    │   ├── __init__.py
    │   └── main.py                             # FastAPI Asynchronous Service (Port 8000)
    │
    ├── tests/                                  # Automated Verification Suite
    │   ├── __init__.py
    │   └── test_sentinex.py                    # 53/53 Unit Tests (100% Pass Rate)
    │
    ├── docs/                                   # Technical Architecture & Guides
    │   ├── API_CONTRACT.md                     # Formal REST API Specification
    │   ├── DEPLOYMENT_GUIDE.md                 # Complete Build & Deployment Manual
    │   ├── LAB_OUTPUT_EXPLANATIONS.md          # Visual Breakdown of All Lab PNGs
    │   └── JUPYTERLAB_GUIDE.md                 # This JupyterLab Manual
    │
    ├── assets/                                 # 26 High-Resolution PNG Diagrams & Videos
    │   ├── arch_diagram.png                    # Edge-to-Mainframe Architecture
    │   ├── labs_diagram.png                    # 7-Lab Pipeline Roadmap
    │   ├── conformal_concept.png               # Conformal Quantile Calibration
    │   ├── pitch_bar_chart.png                 # Model Zoo Benchmarks
    │   ├── pitch_donut_chart.png               # Telemetry Drift Attribution
    │   ├── guardrails_escalation.png           # Deterministic Safety Overrides
    │   ├── chart_training_convergence.png      # 50-Epoch Loss Curves
    │   ├── chart_100b_scaling.png              # Mainframe Multi-Core Scaling
    │   ├── chart_agent_latency.png             # 10.84ms Latency Profile
    │   ├── industrial_dashboard_initial.png    # Live Nominal Dashboard
    │   ├── industrial_dashboard_distress.png   # Live Distress Dashboard
    │   ├── industrial_dashboard_overview.png   # Operations Overview
    │   ├── industrial_audit_ledger_modal.png   # SHA-256 Audit Ledger Modal
    │   ├── SENTINEX_Competition_Demo.webp      # 60FPS Demonstration Video
    │   └── slide_01.png ... slide_12.png       # 12 Pitch Deck Slides
    │
    ├── index.html                              # Public Demonstration Showcase Hub
    ├── SENTINEX_5Min_Master_Demo_Player.html   # 5-Minute Master Voice Demo Player
    ├── SENTINEX_Competition_Demo_Player.html   # Prototype WebP Video Player
    ├── pitch_deck.html                         # 12-Slide Executive Pitch Deck
    ├── pitch_deck.pdf                          # Pitch Deck PDF Document
    ├── SENTINEX_IBM_Pitch_Deck.pptx            # PowerPoint Pitch Presentation
    ├── SENTINEX_Complete_Project_Work_and_Training_Report.html # Master Report (HTML)
    ├── SENTINEX_Comprehensive_Project_Work_and_Training_Report.md # Master Report (MD)
    ├── TEAM_GUIDEBOOK.md                       # Comprehensive Team Engineering Guide
    ├── NEXGUARD_AI.ipynb                       # Root Reference Notebook
    └── README.md                               # Master Repository Documentation
```

---

## 2. Setting Up JupyterLab on LinuxONE (`s390x`)

### Step 1: Connect to LinuxONE Instance
Open your terminal and SSH into your assigned LinuxONE Community Cloud instance:
```bash
ssh linux1@<your-linuxone-ip>
```

### Step 2: Initialize Virtual Environment
Create and activate an isolated Python 3.12 virtual environment:
```bash
python3 -m venv ~/jupyter-env
source ~/jupyter-env/bin/activate
pip install --upgrade pip
```

### Step 3: Install Required Dependencies
Install all numerical, machine learning, and notebook packages:
```bash
pip install jupyterlab scikit-learn numpy pandas matplotlib fastapi uvicorn pytest httpx
```

### Step 4: Launch JupyterLab Server
Start JupyterLab bound to all network interfaces on port `8888`:
```bash
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser
```

*(If you are connecting remotely, create an SSH tunnel from your local PC: `ssh -L 8888:localhost:8888 linux1@<your-linuxone-ip>` and navigate to `http://localhost:8888/lab` in your browser).*

---

## 3. Running `NEXGUARD_AI.ipynb` Cell-by-Cell

Open `notebooks/NEXGUARD_AI.ipynb` in the JupyterLab editor and execute the cells sequentially:

* **Cell 1**: Generates the 10,000-sample SMSD multimodal safety dataset with pre-event trauma ramp at index 8000–8015.
  * *Expected Output*: `✅ Dataset generated successfully.`
* **Cell 2**: Fits the Isolation Forest model on nominal baseline samples and calculates the finite-sample conformal quantile cutoff ($\hat{q} = -0.0462$).
  * *Expected Output*: `✅ Conformal Threshold (95% confidence): -0.0462`
* **Cell 3**: Runs the predictive alert scanner and calculates lead time before critical impact:
  * *Expected Output*:
    ```text
    === NEXGUARD AI EVALUATION ===
    True Predictive Alert triggered at index: 7511
    Critical event occurred at index: 8015
    🚀 True Warning Lead Time: 504 seconds
    🚀 False Alarm Rate (FAR): 4.96%
    ```
* **Cell 4 & 5**: Renders the dynamic risk curve and conformal threshold visualization.

---

## 4. LinuxONE JupyterLab Terminal Cheat Sheet (Git Push & Pull)

You can run Git commands directly inside the **JupyterLab Terminal** (File $\to$ New $\to$ Terminal):

### Check Status:
```bash
cd ~/SENTINEX
git status
```

### Pull Latest Changes from GitHub:
```bash
git pull origin main
```

### Add, Commit, and Push Your Work from LinuxONE Terminal:
```bash
# 1. Stage all changes
git add .

# 2. Commit with descriptive message
git commit -m "Update SENTINEX JupyterLab research, tests, and documentation"

# 3. Push directly to GitHub
git push origin main
```

### Run the 53-Test Automated Suite:
```bash
pytest tests/ -v
# Output: 53 passed in 0.16s (100% pass rate)
```

### Start the FastAPI Backend Service:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
# Test health: curl http://127.0.0.1:8000/health
```
