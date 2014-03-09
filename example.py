import arcpy

rows = arcpy.SearchCursor("C:/temp/address_point.shp", "", "", "STREET_NAM", "STREET_NAM A")

current_street = ""

for row in rows:
    if current_street != row.STREET_NAM:
        current_street = row.STREET_NAM        
        print(current_street)