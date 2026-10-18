# SENTINEX — Formal API Contract & Specification

**Target Platform:** IBM LinuxONE Community Cloud (`s390x`, Ubuntu 24.04 LTS)  
**Protocol:** RESTful JSON over HTTPS (Port 8000)  
**Provenance Fingerprint:** `3ab4e534d934ccd1`  

---

## 1. Health & Mainframe Telemetry
### `GET /health`
Returns system status, active host architecture, and model provenance.

**Response (200 OK):**
```json
{
  "status": "healthy",
  "architecture": "s390x LinuxONE",
  "provenance_fingerprint": "3ab4e534d934ccd1",
  "uptime_seconds": 84210,
  "hardware_simd": true
}
```

---

## 2. Real-Time Telemetry Assessment
### `POST /api/v1/industrial/assess`
Ingests streaming worker telemetry (100Hz kinematics, 1Hz cardiac rhythms, acoustics) and returns fused dual-engine risk scores with conformal uncertainty bounds.

**Request Body:**
```json
{
  "worker_id": "WRK-9042",
  "timestamp": "2026-10-18T14:30:00Z",
  "heart_rate_bpm": 74.5,
  "gait_variance": 0.14,
  "impact_g": 1.02,
  "acoustic_db": 58.2,
  "consent_granted": true
}
```

**Response (200 OK — Nominal State):**
```json
{
  "worker_id": "WRK-9042",
  "fused_risk_score": 0.041,
  "conformal_uncertainty_interval": [0.021, 0.065],
  "escalation_level": 0,
  "status": "NOMINAL",
  "action_recommended": "SILENT_MONITORING",
  "feature_attribution": {
    "kinematics": 0.40,
    "cardiac": 0.25,
    "acoustics": 0.20,
    "context": 0.15
  },
  "block_hash": "a4f89d3c52e89b2110c9d74a72d418193ac49826d9e187263910ab38c471092a",
  "execution_latency_ms": 10.84
}
```

---

## 3. Telemetry Drift Status (PSI)
### `GET /api/v1/industrial/drift-status`
Returns empirical Bayes Laplace-smoothed Population Stability Index across sliding windows ($W=100$).

**Response (200 OK):**
```json
{
  "psi_value": 0.042,
  "classification": "STABLE",
  "recalibration_required": false,
  "telemetry_health_score": 98.5,
  "sliding_window_size": 100
}
```

---

## 4. Cryptographic Audit Ledger
### `GET /api/v1/industrial/audit-ledger`
Returns the recent SHA-256 tamper-evident block chain for EU AI Act compliance.

**Response (200 OK):**
```json
{
  "chain_valid": true,
  "total_blocks": 15,
  "recent_blocks": [
    {
      "index": 14,
      "timestamp": "2026-10-18T14:30:00Z",
      "prev_hash": "b2c918274091823acdeff9018273645129847162534128937162543918273645",
      "action": "SILENT_MONITORING",
      "fused_risk": 0.041,
      "consent_valid": true,
      "hash": "a4f89d3c52e89b2110c9d74a72d418193ac49826d9e187263910ab38c471092a"
    }
  ]
}
```
