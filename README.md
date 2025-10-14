# 🛰️ Mobley CMB Anomaly Cluster (MCAC)

**Author:** L. Soren Mobley  
**Date:** October 2025  
**Environment:** Termux + Python 3.13 (Healpy, Astropy, NumPy)  
**Dataset:** *Planck SMICA CMB Map* — `COM_CMB_IQU-smica-field-Int_2048_R2.01_full.fits`

---

## 📘 Overview

This repository contains the code and analysis pipeline used to detect and characterize statistically significant temperature anomalies in the **Cosmic Microwave Background (CMB)** using *Planck* mission data.  

The study introduces the **Mobley Anomaly Cluster (MAC)** — a compact region of anomalous sigma deviations located near the **Orion–Eridanus boundary** of the Galactic plane.  

Analysis was performed entirely on-device within the **Termux mobile Linux environment**, demonstrating portable, reproducible cosmological analysis workflows.

---

## ⚙️ Workflow

1. Load *Planck* SMICA full-sky map using `healpy.read_map()`.  
2. Compute mean and standard deviation of temperature field.  
3. Identify pixels with |σ| > 3.0 (three-sigma deviations).  
4. Convert anomalous pixel indices to spherical coordinates (θ, φ).  
5. Export coordinate set and summary statistics.  

Example run:
```bash
~/healpy.sh ~/downloads/cmb_anomalies.py
