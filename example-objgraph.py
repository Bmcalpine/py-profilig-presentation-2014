import objgraph
import arcpy


def search():
    
    print("---objects at start---")
    objgraph.show_growth(limit=3)
    
    rows = arcpy.SearchCursor("C:/temp/address_point.shp", "", "", "STREET_NAM", "STREET_NAM A")
    
    objgraph.show_refs([rows], filename='objgraph.png')
    
    objgraph.show_backrefs([rows], filename='objgraph-backrefs.png')
    
    current_street = ""

    print("---objects before---")
    objgraph.show_growth()
    
    for row in rows:
        if current_street != row.STREET_NAM:
            current_street = row.STREET_NAM        
            print(current_street)
            

    print("--objects after loop---")
    objgraph.show_growth()
    
    del rows
    
    print("---objects after cursor delete---")
    objgraph.show_growth()
    
search()