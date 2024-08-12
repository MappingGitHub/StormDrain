import arcpy

def calculate_total_length_by_maintainer(feature_class, maintained_value):
    try:
        # Initialize the total length
        total_length = 0
        
        # Use a search cursor to iterate through the feature class
        with arcpy.da.SearchCursor(feature_class, ["SHAPE@", "Maintained_BY"]) as cursor:
            for row in cursor:
                geometry = row[0]  # First field is the geometry (SHAPE@)
                maintained = row[1]  # Second field is the Maintained field
                
                # Check if the maintained field matches the specified value
                if maintained == maintained_value:
                    # Calculate length
                    length = geometry.length  # geometry is a SpatialReference object
                    total_length += length

        return total_length
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Path to the GravityMain feature class (make sure to specify the feature class name)
    feature_class = r"D:\LACounty_GIS\SDN_Python_Tools\SDN_Python_Tools.gdb\GravitYMain"  # Replace with your actual feature class name

    # Specify the maintained value
    maintained_value = "LACFCD"

    # Calculate total length
    total_length = calculate_total_length_by_maintainer(feature_class, maintained_value)

    # Output the result if the total length is calculated
    if total_length is not None:
        print(f"Total length of GravityMains maintained by {maintained_value}: {total_length:.2f} feet")
