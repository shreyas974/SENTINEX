# SENTINEX — Complete Build & Deployment Manual
## IBM LinuxONE (s390x) & Production Deployment Guide

**Target Hardware**: IBM LinuxONE Community Cloud  
**Architecture**: `s390x` (IBM z/Architecture Enterprise Mainframe)  
**Operating System**: Ubuntu 24.04 LTS  
**Python Runtime**: Python 3.12+  
**Target SLAs**: Sub-15ms Latency (`10.84ms` Verified), 99.999% Availability  
**GitHub Repository**: `https://github.com/shreyas974/SENTINEX`  
**Live Public Showcase**: `https://shreyas974.github.io/SENTINEX/`  

---

## 1. Quick Start & Architecture Overview

SENTINEX is an edge-to-mainframe industrial safety intelligence platform. The backend service and machine learning model zoo run natively on **IBM LinuxONE (`s390x`)**, while the public demonstration and web UI execute on modern web engines.

```text
[Wearable Sensors] --(BLE / TLS 1.3)--> [Edge Buffer W=100] --(REST)--> [IBM LinuxONE s390x]
                                                                                │
                                                                   ┌────────────┴────────────┐
                                                                   ▼                         ▼
                                                            [FastAPI:8000]            [JupyterLab:8888]
                                                            (ML + Guardrails)         (Research & Tests)
```

---

## 2. IBM LinuxONE Server Provisioning & Setup

### Step 1: Connect to LinuxONE Instance
```bash
ssh linux1@<your-linuxone-ip>
```

### Step 2: Update System Packages
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip python3-venv git curl build-essential
```

### Step 3: Clone the Repository
```bash
cd ~
git clone https://github.com/shreyas974/SENTINEX.git
cd SENTINEX
```

### Step 4: Configure Virtual Environment
```bash
python3 -m venv ~/jupyter-env
source ~/jupyter-env/bin/activate
pip install --upgrade pip
```

### Step 5: Install Project Dependencies
```bash
pip install fastapi uvicorn scikit-learn numpy pandas matplotlib pytest httpx jupyterlab
```

---

## 3. Launching Services on IBM LinuxONE

### Launching the Asynchronous FastAPI Backend:
Start the production API server with 4 worker processes:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

Verify service health:
```bash
curl http://127.0.0.1:8000/health
# Expected Output:
# {"status":"healthy","architecture":"s390x LinuxONE"}
```

### Launching the JupyterLab Research Server:
In a separate terminal or screen session:
```bash
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser
```

Access the JupyterLab interface at:
`http://<your-linuxone-ip>:8888/lab`

---

## 4. Running the Automated Test Suite (53/53 Tests)

To verify model calibration, rolling statistics, deterministic guardrails, and cryptographic ledger integrity on `s390x`:
```bash
pytest tests/ -v
```

Expected output:
```text
============================= test session starts =============================
platform linux -- Python 3.12.3, pytest-8.1.1, pluggy-1.4.0
rootdir: /home/linux1/SENTINEX
collected 53 items

tests/test_sentinex.py::test_calibrator_init PASSED                      [  1%]
...
tests/test_sentinex.py::test_total_end_to_end_latency_sla PASSED         [ 98%]
tests/test_sentinex.py::test_total_unit_test_count PASSED                [100%]

============================= 53 passed in 0.16s ==============================
```

---

## 5. Systemd Service Deployment (Production Daemon)

To keep the SENTINEX backend running 24/7 across server reboots on LinuxONE:

1. Create a systemd service file:
```bash
sudo nano /etc/systemd/system/sentinex.service
```

2. Add the following configuration:
```ini
[Unit]
Description=SENTINEX Industrial AI Backend Service on s390x
After=network.target

[Service]
User=linux1
WorkingDirectory=/home/linux1/SENTINEX
ExecStart=/home/linux1/jupyter-env/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

3. Enable and start the service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable sentinex
sudo systemctl start sentinex
sudo systemctl status sentinex
```

---

## 6. Hosting the Public Showcase on GitHub Pages

The interactive public demonstration hub, 5-minute video studio with Indian student narration, and 12-slide pitch presentation are configured for zero-dependency static deployment via GitHub Pages:

1. Go to your GitHub repository: `https://github.com/shreyas974/SENTINEX`
2. Click **Settings** $\to$ **Pages** (left navigation)
3. Under **Build and deployment**:
   - Source: **Deploy from a branch**
   - Branch: `main`
   - Folder: `/ (root)`
4. Click **Save**
5. Within 60 seconds, your public site is live at:
   **`https://shreyas974.github.io/SENTINEX/`**
