import geopandas as gpd

# Load the GeoJSON file
npc_boundaries = gpd.read_file('resources\singapore-npc-boundaries\SingaporePoliceForceNPCBoundary.geojson')

# Display the first few rows
print(npc_boundaries.head())
print(type(npc_boundaries))
#print length of the dataframe
print(len(npc_boundaries))
