import objgraph
import arcpy

class MemUsage(object):
    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("---objects at start---")
        objgraph.show_growth(limit=3)
        self.f()
        print("---objects at end---")
        objgraph.show_growth()


@MemUsage
def search():   
    
    rows = arcpy.SearchCursor("C:/temp/address_point.shp", "", "", "STREET_NAM", "STREET_NAM A")
    
    current_street = ""
    i = 1
    for row in rows:
    
        if current_street != row.STREET_NAM:
            current_street = row.STREET_NAM        
            print(current_street)
            
    del rows   

    
search()
