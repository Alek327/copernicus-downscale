# Streamlit dashboard

import streamlit as st
import geopandas as gpd
import rasterio
import matplotlib.pyplot as plt
import rasterio.plot

st.set_page_config(layout="wide")
st.title("🌍 Copernicus + OSM Hybrid Demo")

st.markdown("This live dashboard visualizes mock urban features over CORINE-style land cover.")

col1, col2 = st.columns(2)

with col1:
    st.header("Urban GeoJSON")
    try:
        gdf = gpd.read_file("examples/mock_urban.geojson")
        st.map(gdf)
        st.dataframe(gdf)
    except Exception as e:
        st.error(f"Error loading GeoJSON: {e}")

with col2:
    st.header("CORINE-style Raster")
    try:
        with rasterio.open("examples/mock_clc.tif") as src:
            fig, ax = plt.subplots(figsize=(6, 6))
            rasterio.plot.show(src, ax=ax, title="Mock CLC Raster")
            st.pyplot(fig)
    except Exception as e:
        st.error(f"Error loading raster: {e}")

st.markdown("---")
st.header("Final Overlay with GitHub + Zenodo Footer")
st.image("examples/copernicus_osm_overlay_with_footer_final.png", caption="Mock overlay visualization", use_column_width=True)

st.success("Streamlit dashboard connected to Copernicus mock demo")
