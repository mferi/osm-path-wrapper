# Retrieving OSM path feautures (including tracks) and load it in a postgres db
# http://wiki.openstreetmap.org/wiki/Map_Features#Paths
import overpy

BINDING = "(50.7,7.1,50.8,7.25)"
api = overpy.Overpass()

# fetch all ways and nodes
result = api.query("""
    (
    way["highway"="footway"]%s;
    way["highway"="path"]%s;
    way["highway"="track"]%s;
    way["highway"="cycleway"]%s;
    way["highway"="steps"]%s;
    way["highway"="bridleway"]%s;
    );
    (._;>;);
    out body;
    """ % (BINDING, BINDING, BINDING, BINDING, BINDING, BINDING))

for way in result.ways:
    print("Name: %s" % way.tags.get("name", "n/a"))
    print("   Highway: %s" % way.tags.get("highway", "n/a"))
    print("   Nodes:")
    for node in way.get_nodes(resolve_missing=True):
        print("    Lat: %f, Lon: %f" % (node.lat, node.lon))
