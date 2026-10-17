<div align="center">

# 🛡️ SENTINEX

**Anticipate the Risk. Act Before It Escalates.**

[![IBM Z Datathon 2026](https://img.shields.io/badge/IBM_Z_Datathon-2026-blue.svg)](https://www.ibm.com/)
[![Track](https://img.shields.io/badge/Track-Real--Time_AI_for_Critical_Decisions-purple.svg)]()
[![Platform](https://img.shields.io/badge/Platform-IBM_LinuxONE_(s390x)-black.svg)]()
[![Backend](https://img.shields.io/badge/Backend-FastAPI-009688.svg)]()

*Built by Team NEUROBOTS*

</div>

---

## 📖 Overview

**SENTINEX** is an AI-driven personal safety intelligence system. Unlike traditional safety apps that wait for an SOS button or a scream, SENTINEX continuously analyzes multimodal contextual data (motion, location, acoustics) to forecast emerging risks *before* they become critical. 

By utilizing **Conformal Prediction**, the system mathematically bounds its own uncertainty, ensuring it only triggers proportionate, consent-aware interventions when it is statistically confident.

---

## ⚙️ System Pipeline

Instead of a reactive trigger, SENTINEX uses a continuous six-stage analytical pipeline:

```text

[1. Observe] ──> [2. Analyze] ──> [3. Forecast] ──> [4. Assess Risk] ──> [5. Decide] ──> [6. Intervene]
   Sensors          Features          Risk Score        Uncertainty        Policy           Consent
```

✨ Key Features

Mathematically Bounded Uncertainty: Uses Adaptive Conformal Prediction to guarantee a strict False Alarm Rate (FAR) budget. No random guessing.

Proportionate Interventions: Decisions are gated by a consent state machine. Actions range from silent monitoring to discreet verification, avoiding overreactions.

Enterprise Security: Implements a secure, immutable audit logging system to track all decision states safely.

Mainframe Optimized: Architected specifically for high-throughput inference on IBM LinuxONE (s390x).

🛠️ Technology Stack

Domain	Technology
Language	Python 3.12
Backend API	FastAPI, Uvicorn
Machine Learning	Scikit-Learn (Isolation Forest), NumPy, Pandas
Environment	IBM LinuxONE Community Cloud (Ubuntu 24.04)
Development	JupyterLab, Git

📂 Repository Structure

```text
SENTINEX/
│
├── app/                        # FastAPI Backend Application
│   └── main.py                 # API endpoints (/health, /assess, /config)
│
├── docs/                       # Technical Documentation
│   ├── API_CONTRACT.md         # Request/Response schemas
│   └── DEPLOYMENT_GUIDE.md     # LinuxONE deployment steps
│
├── src/                        # Source Code
│   ├── monitoring/             # Audit logging configuration
│   ├── decision/               # Decision engine & policy rules
│   └── data/                   # Validation & preprocessing
│
├── data/                       # Dataset Storage
│   └── synthetic/              # SMSD (Synthetic Multimodal Safety Data)
│
└── NEXGUARD_AI.ipynb           # Baseline ML model & evaluation notebook
```

🚀 Quick Start (LinuxONE Environment)

Prerequisites: Python 3.12 installed on LinuxONE (s390x).

1. Activate the environment

bash
source ~/jupyter-env/bin/activate
2. Launch the Backend API

bash
uvicorn app.main:app --host 127.0.0.1 --port 8000
3. Verify System Health
Open a second terminal and run:

bash
curl http://127.0.0.1:8000/health
Expected Output: {"status":"healthy","architecture":"s390x LinuxONE"}

(For full deployment details, see docs/DEPLOYMENT_GUIDE.md)

📊 Development Status

☑ Backend API: FastAPI skeleton with validation stubs [Verified]
☑ Audit Logging: Secure logging configuration implemented [Verified]
☑ Machine Learning: Synthetic dataset generation & Isolation Forest baseline [Implemented]
☑ Conformal Prediction: Initial mathematical bounds applied to baseline [Implemented]
□ System Integration: Connecting frontend to live backend [In Progress]
□ Full Quantexa Integration: Graph-based threat resolution [Future Work]

<div align="center"> <i>"From reactive alerts to anticipatory intelligence."</i> </div> ```
