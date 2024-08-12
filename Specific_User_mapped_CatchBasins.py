import arcpy

# Define the input feature class and output layer name
input_feature_class = r"D:\LACounty_GIS\SDN_Python_Tools\SDN_Python_Tools.gdb\CatchBasin"
output_layer_name = "Sarmen_mapped_CBs"

# Set the workspace to the geodatabase
arcpy.env.workspace = r"D:\LACounty_GIS\SDN_Python_Tools\SDN_Python_Tools.gdb"

# Define the SQL expression for selecting records
sql_expression = "CREATED_User = 'SBAJARI'"

# Create a feature layer with the selection
arcpy.management.MakeFeatureLayer(input_feature_class, output_layer_name, sql_expression)

# If desired, you can save the new feature layer permanently as a new feature class
output_feature_class = r"D:\LACounty_GIS\SDN_Python_Tools\SDN_Python_Tools.gdb\Sarmen_mapped_CatchBasins"
arcpy.management.CopyFeatures(output_layer_name, output_feature_class)

print("Filtered records have been exported to:", output_feature_class)
