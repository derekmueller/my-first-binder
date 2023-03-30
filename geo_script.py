import geopandas as gpd

# Import sample data
gdf = gpd.read_file("ne_110m_admin_0_countries.gpkg")

# Print column names
print(gdf.columns)

