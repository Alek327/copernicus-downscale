import geopandas as gpd
import pandas as pd
import numpy as np
from shapely.geometry import Polygon
import rasterio
from rasterio.transform import from_origin
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

# 1. Create GeoJSON
geometry = [
    Polygon([(13.35, 52.48), (13.36, 52.48), (13.36, 52.49), (13.35, 52.49)]),
    Polygon([(13.37, 52.49), (13.38, 52.49), (13.38, 52.50), (13.37, 52.50)]),
    Polygon([(13.34, 52.47), (13.35, 52.47), (13.35, 52.48), (13.34, 52.48)])
]
gdf = gpd.GeoDataFrame({
    "id": [1, 2, 3],
    "tag_landuse": ["urban", "urban", "urban"],
    "timestamp": ["2018-01-01", "2020-01-01", "2022-01-01"]
}, geometry=geometry, crs="EPSG:4326")
gdf.to_file("examples/mock_urban.geojson", driver="GeoJSON")

# 2. Create mock CLC raster
raster_data = np.random.choice([0, 1, 2], size=(100, 100), p=[0.8, 0.15, 0.05])
transform = from_origin(13.30, 52.52, 0.001, 0.001)
with rasterio.open(
    "examples/mock_clc.tif", "w", driver="GTiff", height=100, width=100, count=1,
    dtype=raster_data.dtype, crs="EPSG:4326", transform=transform
) as dst:
    dst.write(raster_data, 1)

# 3. Generate overlay image
fig, ax = plt.subplots(figsize=(8, 8))
with rasterio.open("examples/mock_clc.tif") as src:
    gdf = gdf.to_crs(src.crs)
    rasterio.plot.show(src, ax=ax, title="Mock OSM Urban Overlay on CORINE")
    gdf.plot(ax=ax, facecolor="none", edgecolor="red", linewidth=1)
plt.savefig("examples/copernicus_osm_overlay.png", dpi=300)
plt.close()

# 4. Add GitHub/DOI footer
img = Image.open("examples/copernicus_osm_overlay.png")
draw = ImageDraw.Draw(img)
footer = "📦 github.com/Alek327/copernicus-downscale | 🔖 DOI: 10.5281/zenodo.xxxxxxx"
font = ImageFont.load_default()
draw.rectangle([0, img.height - 25, img.width, img.height], fill="white")
draw.text((10, img.height - 20), footer, font=font, fill="black")
img.save("examples/copernicus_osm_overlay_with_footer_final.png")

print("\n✅ Files created in 'examples/':")
print(" - mock_urban.geojson")
print(" - mock_clc.tif")
print(" - copernicus_osm_overlay_with_footer_final.png")

