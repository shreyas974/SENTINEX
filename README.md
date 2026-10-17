SENTINEX: Temporal Conformal Safety Intelligence
Tagline: Anticipate the Risk. Act Before It Escalates.

Team: NEUROBOTS
Competition: IBM Z Datathon 2026
Track: Theme 1 — Real-Time AI for Critical Decisions

1. Executive Summary
Conventional personal-safety applications are inherently reactive, relying on manual SOS triggers or post-incident detection. Such architectures lack the capacity to forecast emerging risks, resulting in insufficient warning lead time and high false-alarm rates.

SENTINEX is an anticipatory decision-support prototype configured to process multimodal temporal data, estimate emerging risk with mathematically bounded uncertainty, and recommend proportionate, consent-aware interventions prior to the onset of a critical event.

2. System Architecture & Pipeline
The system executes a six-stage analytical pipeline:
Observe → Analyze → Forecast → Assess Risk → Decide → Intervene

The architecture comprises:

Data Ingestion & Validation: Strict schema and timestamp validation (FastAPI).

Temporal Inference Engine: Transparent baseline models (Isolation Forest) for anomaly detection.

Conformal Prediction Module: Statistically bounded risk prediction sets (guaranteeing false-alarm budgets).

Decision Engine: Uncertainty-gated policy escalation formalized as a Constrained Markov Decision Process (CMDP).

Audit Ledger: Immutable, secure logging of all decision states (IBM Z / LinuxONE aligned).

3. Core Technical Innovations
Adaptive Conformal Prediction: The system does not output raw point estimates. It outputs prediction sets 
Γ
α
(
x
)
Γ 
α
 (x) with a mathematically guaranteed error rate (
α
=
0.05
α=0.05), effectively bounding the False Alarm Rate (FAR).

Proportionate Intervention: Automated actions are strictly gated by a consent state machine. The system recommends actions ranging from silent monitoring to user verification, avoiding overreaction to benign anomalies.

Enterprise Integration: Designed for deployment on IBM LinuxONE (s390x architecture), ensuring high-throughput secure inference.

4. Repository Structure
text
SENTINEX/
├── app/                  # FastAPI backend application (main.py)
├── docs/                 # API Contract and Deployment Guides
├── src/
│   ├── monitoring/       # Secure audit logging
│   ├── decision/         # Decision engine logic
│   └── data/             # Validation and preprocessing
├── data/synthetic/       # Synthetic Multimodal Safety Dataset (SMSD)
└── NEXGUARD_AI.ipynb     # Prototype model and evaluation notebook
5. Evaluation Metrics (Verified)
Our baseline prototype on IBM LinuxONE demonstrates the following capabilities:

False Alarm Rate (FAR): ~4.96% (Mathematically aligned with our 
α
=
0.05
α=0.05 conformal bound).

Warning Lead Time: Predictive alerts successfully trigger prior to the ground-truth critical event.

Backend Health: GET /health verified returning s390x LinuxONE architecture status.

6. Getting Started (LinuxONE Environment)
Prerequisites: Python 3.12, Ubuntu 24.04.5 LTS, s390x architecture.

bash
# 1. Activate environment
source ~/jupyter-env/bin/activate

# 2. Launch the backend API
uvicorn app.main:app --host 127.0.0.1 --port 8000

# 3. Verify health (in a separate terminal)
curl http://127.0.0.1:8000/health
(For full documentation, refer to docs/DEPLOYMENT_GUIDE.md and docs/API_CONTRACT.md).

7. Development Status
[Implemented] FastAPI backend skeleton with validation and audit logging.

[Implemented] Synthetic Multimodal Safety Dataset (SMSD) generator.

[Implemented] Conformal prediction baseline notebook.

[Verified] End-to-end backend deployment on IBM LinuxONE (s390x).

[Future Work] Integration of real-time sensor telemetry and full Quantexa graph resolution.
