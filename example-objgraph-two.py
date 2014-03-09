import objgraph
import arcpy


def search():   
    
    rows = arcpy.SearchCursor("C:/temp/address_point.shp", "", "", "STREET_NAM", "STREET_NAM A")
    
    current_street = ""
    i = 1
    for row in rows:
    
        if current_street != row.STREET_NAM:
            current_street = row.STREET_NAM        
            print(current_street)
            
    del rows   
    


print("---objects at start---")
objgraph.show_growth(limit=3)
    
search()

print("---objects at end---")
objgraph.show_growth()