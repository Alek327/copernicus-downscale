# 🌍 Copernicus + OpenStreetMap (OSM) Hybrid Toolkit

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15175397.svg)](https://doi.org/10.5281/zenodo.15175397)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Streamlit App](https://img.shields.io/badge/Launch-Dashboard-green)](https://copernicus-downscale.streamlit.app)

---

## 🧭 Overview
An open-source hybrid toolkit to analyze urban land cover change and water stress using:
- 🛰 Copernicus Earth observation (CORINE, GHSL, ERA5)
- 🌍 OpenStreetMap history data (via ohsome-planet → GeoParquet)

Supports reproducible sustainability science and SDG 6.4.2 monitoring (water stress).

---

## ✨ Features
- CORINE and GHSL land cover analysis
- ERA5 precipitation + evapotranspiration extraction
- Urban feature growth from OSM (landuse/buildings)
- EWEI modeling with sectoral water coefficients
- Streamlit dashboard + CLI + Jupyter workflows
- Compatible with MRIO, EEIO, and policy reporting needs

---

## 🚀 Quickstart
```bash
pip install -r requirements.txt
streamlit run streamlit_map_dashboard.py
```

Or explore:
```bash
notebooks/osm_integration.ipynb
```

---

## 🔄 OSM + Copernicus Integration Example
```bash
# Convert OSM PBF → GeoParquet with ohsome-planet
java -jar ohsome-planet.jar contributions \
  --pbf berlin.osh.pbf \
  --output data/osm_geo \
  --overwrite

# Analyze growth
python ohsome_to_downscale.py --dir data/osm_geo/latest \
  --bbox 13.1,52.3,13.8,52.6
```

---

## 🧪 Structure
```
copernicus_downscale/
├── landcover.py
├── hydro_timeseries.py
├── water_stress_model.py
├── osm_geo.py
notebooks/
└── osm_integration.ipynb
streamlit_map_dashboard.py
ohsome_to_downscale.py
```

---

## 🛰️ Use Cases
- Urban expansion monitoring
- Water resource planning (EWEI)
- Regional SDG 6.4.2 analysis
- Climate and sustainability policy support

---

## 📖 Citation
```bibtex
@software{galychyn2025copernicus,
  author       = {Oleksandr Galychyn},
  title        = {Copernicus + OpenStreetMap Hybrid Toolkit},
  year         = 2025,
  doi          = {10.5281/zenodo.15175397},
  publisher    = {Zenodo},
  url          = {https://github.com/Alek327/copernicus-downscale}
}
```

---

## 🛰️ License
MIT License — reusable for research, education, and development.

Built by Oleksandr Galychyn | University of Ghent
