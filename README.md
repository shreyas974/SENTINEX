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
