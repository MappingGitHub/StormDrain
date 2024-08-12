import arcpy

# Path to the feature class
feature_class_path = r"D:\LACounty_GIS\SDN_Python_Tools\SDN_Python_Tools.gdb\GravityMain"

# Initialize an empty set to store unique names
unique_names = set()

# Create a Search Cursor to iterate through the feature class
with arcpy.da.SearchCursor(feature_class_path, ['MAINTAINED_BY', 'NAME']) as cursor:
    for row in cursor:
        if row[0] == "PROPOSED":  # Check if MAINTAINED_BY is 'PROPOSED'
            unique_names.add(row[1])  # Add the NAME to the set to ensure uniqueness

# Convert the set to a list
unique_names_list = list(unique_names)

# Print the results
print("List of unique names where MAINTAINED_BY is 'PROPOSED':")
for name in unique_names_list:
    print(name)
