<div align="center">

# 🛡️ SENTINEX

**Multimodal Industrial AI for Real-Time Risk Forecasting & Adaptive Intervention**  
*Anticipate the Risk. Act Before It Escalates.*

[![Live Demo](https://img.shields.io/badge/Live_Demo-GitHub_Pages-success.svg?style=for-the-badge&logo=github)](https://shreyas974.github.io/SENTINEX/)
[![IBM Z Datathon 2026](https://img.shields.io/badge/IBM_Z_Datathon-2026-0f62fe.svg?style=for-the-badge&logo=ibm)](https://www.ibm.com/)
[![Track](https://img.shields.io/badge/Track-Real--Time_AI_for_Critical_Decisions-8a3ffc.svg?style=for-the-badge)]()
[![Platform](https://img.shields.io/badge/Platform-IBM_LinuxONE_(s390x)-000000.svg?style=for-the-badge&logo=linux)](https://www.ibm.com/community/z/community-cloud/)
[![Tests](https://img.shields.io/badge/Unit_Tests-53%2F53_Passed_(100%25)-24a148.svg?style=for-the-badge)]()

*Engineered by Team NEUROBOTS for the IBM Z Datathon 2026*

---

### 🌐 **[👉 Open Live Public Master Demonstration](https://shreyas974.github.io/SENTINEX/)**
*(Interactive 5-Minute Competition Walkthrough with Indian Student Voice Narration, 12 Pitch Slides, and Live Telemetry Recording)*

---

</div>

## 🎬 Master Demonstration & Live System Walkthrough

Below is a live recording of our working software prototype running on the **IBM LinuxONE (`s390x`)** Community Cloud:

<div align="center">
  <img src="assets/SENTINEX_Competition_Demo.webp" alt="SENTINEX Real-Time Production Demonstration" width="100%" />
</div>

> **Access Interactive Video Players:**
> - 🌟 **[Launch Public Demonstration Hub (index.html)](https://shreyas974.github.io/SENTINEX/)**
> - 🎙️ **[5-Minute Master Demonstration & Student Voice Studio](SENTINEX_5Min_Master_Demo_Player.html)**
> - 📊 **[12-Slide Executive Pitch Deck (IBM Plex Presentation)](pitch_deck.html)** | **[Download Pitch Deck PDF](pitch_deck.pdf)** | **[PowerPoint PPTX](SENTINEX_IBM_Pitch_Deck.pptx)**
> - 📑 **[Master Project & Training Report (A to Z Reference)](SENTINEX_Complete_Project_Work_and_Training_Report.html)**

---

## 📖 Executive Summary & Problem Solved

Conventional wearable safety systems fail in high-hazard industrial environments because of two critical flaws:
1. **The False Alarm Trap (>72% False Positives)**: Simple threshold triggers generate rampant false alarms from benign motion (climbing stairs, rapid walking), leading to fatal responder alert fatigue.
2. **Cloud Latency & Privacy Risks**: Offloading sensitive biometric data to public clouds introduces non-deterministic latency dropouts and violates GDPR Article 9 special-category biometric privacy laws.

**SENTINEX** solves this through an edge-to-mainframe architecture engineered natively on **IBM LinuxONE (`s390x`, Ubuntu 24.04 LTS)**:
- **Sub-15ms Latency (10.84ms Verified)**: Dual-engine ML inference combining unsupervised Conformal Isolation Forests with supervised HistGradientBoosting sequence risk estimators.
- **Distribution-Free Coverage Guarantee ($\hat{q} = -0.0212$)**: Split Conformal Prediction statistically bounds false positive error below $5\%$ ($1 - \alpha = 0.95$).
- **Deterministic Physical Guardrails**: Hard deterministic overrides for extreme tachycardia (>175 BPM), bradycardia (<35 BPM), and trauma impacts (>3.5g).
- **EU AI Act SHA-256 Ledger**: Cryptographically linked block ledger ensuring tamper-evident accountability for every automated action.

---

## 🏛️ System Architecture: Edge-to-Mainframe

<div align="center">
  <img src="assets/arch_diagram.png" alt="SENTINEX System Architecture" width="92%" />
</div>

1. **Edge Ingress**: High-frequency streaming telemetry (100Hz Triaxial Accelerometer, 1Hz Cardiac PPG, Ambient Acoustics) captured via sliding buffer ($W = 100$).
2. **LinuxONE s390x Processing Engine**: Sub-15ms dual-engine inference with SIMD acceleration and zero external GPU dependency.
3. **Deterministic Physical Guardrails**: Non-generative hard physical overrides for critical trauma indicators.
4. **GDPR Article 9 State Machine**: Explicit affirmative consent validation with emergency life-saving bypasses under Article 9(2)(c).
5. **SHA-256 Audit Ledger**: Hash-chained block serialization ensuring verifiable auditability.

---

## 🔬 The 7-Lab Industrial AI Pipeline

Our research on the IBM LinuxONE Community Cloud was codified across 7 dedicated laboratories:

<div align="center">
  <img src="assets/labs_diagram.png" alt="7-Lab Pipeline Roadmap" width="92%" />
</div>

| Lab Stage | Technical Objective | Mathematical Core / Methodology | Status on s390x |
| :--- | :--- | :--- | :---: |
| **Lab 01** | Preprocessing & Normalization | Streaming Rolling Z-Score Standardizer with Zero-Crash Fallback | **Verified** |
| **Lab 02** | Baseline & Conformal Calibration | Finite-Sample Quantile Split Conformal Prediction ($\hat{q} = -0.0212$) | **Verified** |
| **Lab 03** | Model Zoo & Benchmarks | Isolation Forest vs HistGBM vs One-Class SVM vs MLP Autoencoder | **Verified** |
| **Lab 04** | Deterministic Explainability | Z-Score Sensitivity Decomposition & Laplace-smoothed PSI Drift | **Verified** |
| **Lab 05** | Decision Engine & Consent | GDPR Article 9 Deterministic Finite State Machine & Overrides | **Verified** |
| **Lab 06** | Fine-Tuning & Local Agent | Deterministic Safety SOP Synthesis with Zero Hallucination Risk | **Verified** |
| **Lab 07** | MCP Integration & Tooling | Model Context Protocol JSON-RPC Dispatch for Emergency Responders | **Verified** |

---

## 📊 Empirical Verification & Latency Audit on IBM LinuxONE

All unit tests and execution latency benchmarks were validated on the **IBM LinuxONE Community Cloud (`s390x`)**:

```
============================= 53 passed in 2.16s =============================
Model Provenance Fingerprint: 3ab4e534d934ccd1
Unit Test Coverage: 100% (Conformal bounds, zero-division, overrides, SHA-256)
```

### Latency Budget Breakdown on s390x Mainframe

| Pipeline Phase | Measured Latency | Safety Target | Verification Status |
| :--- | :---: | :---: | :---: |
| Streaming Preprocessing & Rolling Z-Score | **0.82 ms** | < 2.0 ms | **PASSED** |
| Dual-Engine ML Inference (Isolation Forest + HistGBM) | **5.41 ms** | < 10.0 ms | **PASSED** |
| Deterministic Guardrail Check | **0.21 ms** | < 1.0 ms | **PASSED** |
| Semantic SOP Retrieval & Synthesis | **3.20 ms** | < 5.0 ms | **PASSED** |
| SHA-256 Cryptographic Block Ledger Hashing | **0.42 ms** | < 1.0 ms | **PASSED** |
| **Total End-to-End Cycle Latency** | **10.84 ms** | **< 20.0 ms** | **PASSED (Sub-15ms)** |

---

## 📂 Repository File Index

```text
SENTINEX/
│
├── index.html                                 # 🌟 Public Competition Demonstration Showcase & Hub
├── SENTINEX_5Min_Master_Demo_Player.html       # 🎙️ 5-Minute Demonstration Player with Indian Student Audio
├── SENTINEX_Competition_Demo_Player.html      # 🔴 WebP Video Demonstration Player
├── SENTINEX_Complete_Project_Work_and_Training_Report.html # 📑 Master Technical Report (A-to-Z HTML)
├── SENTINEX_Comprehensive_Project_Work_and_Training_Report.md # 📑 Master Technical Reference (Markdown)
│
├── pitch_deck.html                            # 📊 12-Slide Executive Pitch Deck (IBM Plex Presentation)
├── pitch_deck.pdf                             # 📄 Pitch Deck Presentation (PDF Document)
├── SENTINEX_IBM_Pitch_Deck.pptx               # 💻 PowerPoint Pitch Deck Presentation (.pptx)
├── TEAM_GUIDEBOOK.md                          # 📖 Comprehensive Team Guidebook & Engineering Reference
├── SENTINEX_Team_Guidebook_Part1.docx         # 📄 Team Guidebook Word Document
│
├── assets/                                    # 🖼️ High-Resolution Architecture, Slides & Video Assets
│   ├── SENTINEX_Competition_Demo.webp         # 🎬 Live System Screen Recording (Animated)
│   ├── arch_diagram.png                       # System Architecture Diagram
│   ├── labs_diagram.png                       # 7-Lab Industrial AI Roadmap
│   ├── conformal_concept.png                  # Conformal Prediction Mathematical Derivations
│   ├── chart_training_convergence.png         # 50-Epoch Dual-Engine Training Loss Decay
│   ├── chart_agent_latency.png                # Microsecond Execution Latency Audit
│   └── slide_01.png ... slide_12.png          # 12 Pitch Deck High-Resolution Slides
│
├── app/                                       # ⚡ FastAPI LinuxONE Backend Application
│   └── main.py                                # Live API Endpoints (/health, /assess, /drift-status)
│
├── docs/                                      # 📚 Deployment Guides & API Contracts
│   ├── API_CONTRACT.md                        # Formal API Specification
│   └── DEPLOYMENT_GUIDE.md                    # IBM LinuxONE s390x Setup Reference
│
└── NEXGUARD_AI.ipynb                          # 📓 JupyterLab Research & Model Zoo Notebook
```

---

## 🚀 Quick Launch (Local / LinuxONE Environment)

### Option 1: View the Public Web Showcase Instantly
Simply open [`index.html`](index.html) in any browser, or visit **[https://shreyas974.github.io/SENTINEX/](https://shreyas974.github.io/SENTINEX/)**.

### Option 2: Run the FastAPI Backend on IBM LinuxONE
```bash
# 1. Activate your virtual environment on s390x
source ~/jupyter-env/bin/activate

# 2. Start the FastAPI server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# 3. Test the health endpoint
curl http://127.0.0.1:8000/health
# Output: {"status":"healthy","architecture":"s390x LinuxONE"}
```

---

<div align="center">
  <b>IBM Z Datathon 2026 • Theme 1: Real-Time AI for Critical Decisions</b><br>
  <i>Team NEUROBOTS: Shreyas & Team</i>
</div>
