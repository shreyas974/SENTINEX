# SENTINEX — IBM LinuxONE (s390x) Deployment Guide

**Target Runtime:** IBM LinuxONE Community Cloud  
**OS:** Ubuntu 24.04 LTS (`s390x`)  
**Python Version:** Python 3.12+  

---

## 1. Connecting to LinuxONE Community Cloud
Connect to your assigned LinuxONE instance over SSH:
```bash
ssh linux1@<your-linuxone-ip>
```

---

## 2. Environment Setup
Create and activate an isolated Python 3.12 virtual environment:
```bash
python3 -m venv ~/sentinex-env
source ~/sentinex-env/bin/activate
pip install --upgrade pip
```

Install backend dependencies:
```bash
pip install fastapi uvicorn scikit-learn numpy pandas pytest
```

---

## 3. Launching the Backend Service
From the repository root:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

Verify that the service is running:
```bash
curl http://localhost:8000/health
# Expected: {"status":"healthy","architecture":"s390x LinuxONE"}
```

---

## 4. Running the Automated Test Suite
Execute the 53-test verification suite:
```bash
pytest tests/ -v
# Expected: 53 passed in ~2.16s (100% test pass rate)
```

---

## 5. Hosting the Public Showcase on GitHub Pages
1. Go to your GitHub repository: `https://github.com/shreyas974/SENTINEX`
2. Navigate to **Settings** $\to$ **Pages**
3. Under **Branch**, select `main` and root `/`
4. Click **Save**
5. Your public interactive demonstration will be live at:
   `https://shreyas974.github.io/SENTINEX/`
