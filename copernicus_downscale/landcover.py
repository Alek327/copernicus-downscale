# copernicus_downscale/landcover.py
import rasterio
import rasterio.mask
import geopandas as gpd
import numpy as np
import os
import requests
from zipfile import ZipFile

def calculate_urban_percentage(corine_raster_path, region_shapefile_path, urban_classes=[111, 112, 121, 122, 123, 124]):
    region_gdf = gpd.read_file(region_shapefile_path)
    with rasterio.open(corine_raster_path) as src:
        region_gdf = region_gdf.to_crs(src.crs)
        out_image, _ = rasterio.mask.mask(src, region_gdf.geometry, crop=True)
        out_image = out_image[0]
        urban_mask = np.isin(out_image, urban_classes)
        urban_pixels = np.sum(urban_mask)
        total_pixels = np.count_nonzero(out_image != src.nodata)
        urban_percent = (urban_pixels / total_pixels) * 100 if total_pixels > 0 else 0
        return round(urban_percent, 2)

def download_corine_clc(destination_folder="data", year="2018"):
    base_url = f"https://land.copernicus.eu/land-files/CLMS/Landcover/CLC/CLC{year}/raster/CLC{year}_V2020_20u1.tif.zip"
    local_zip = os.path.join(destination_folder, f"CLC{year}.zip")
    os.makedirs(destination_folder, exist_ok=True)
    r = requests.get(base_url)
    with open(local_zip, "wb") as f:
        f.write(r.content)
    with ZipFile(local_zip, 'r') as zip_ref:
        zip_ref.extractall(destination_folder)
    os.remove(local_zip)

def download_ghsl_raster(destination_folder="data", product="GHS_BUILT_S_E", year="2018"):
    os.makedirs(destination_folder, exist_ok=True)
    fname = f"{product}_{year}_GLOBE_R2023A_54009_1000_V1_0.tif.zip"
    base_url = f"https://cidportal.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_BUILT_C/BUILT_S_E2018_GLOBE_R2023A/GHS_BUILT_S_E/GHS_BUILT_S_E{year}_GLOBE_R2023A_54009_1000_V1_0.tif.zip"
    local_zip = os.path.join(destination_folder, fname)
    r = requests.get(base_url)
    with open(local_zip, "wb") as f:
        f.write(r.content)
    with ZipFile(local_zip, 'r') as zip_ref:
        zip_ref.extractall(destination_folder)
    os.remove(local_zip)
