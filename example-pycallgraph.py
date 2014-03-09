from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
import arcpy


def search():
    rows = arcpy.SearchCursor("C:/temp/address_point.shp", "", "", "STREET_NAM", "STREET_NAM A")

    current_street = ""

    for row in rows:
        if current_street != row.STREET_NAM:
            current_street = row.STREET_NAM        
            print(current_street)
            
with PyCallGraph(output=GraphvizOutput()):
    search()