"""
When geoprocessing history is recorded in an item's metadata,
and geoprocessing tools are constantly used to analyze, evaluate,
and manage data as with utility networks and parcel datasets, over
time the geoprocessing history can grow to be very large in size.
Metadata documents containing years of geoprocessing history have
been known to be 2 GB in size. When all the items in an enterprise
geodatabase contain metadata documents of this size, performance of
the database as a whole is affected. To optimize performance, you
may want to delete the geoprocessing history from the metadata of
every item in the database.The options provided with this method allow
you to remove unwanted content from an item's metadata and reduce the
overall size of a metadata document as much as possible.

"""

# Link 1: https://pro.arcgis.com/en/pro-app/latest/arcpy/metadata/what-is-the-metadata-module.htm
# Link 2: https://pro.arcgis.com/en/pro-app/latest/arcpy/metadata/metadata-class.htmimport arcpy

from arcpy import metadata as md

# Get the target item's Metadata object
poles_path = r'C:\SARMEN_WORK\For_Metadata_Presentation_08_12_2024\LA_County_Proclaimed_Forests.gdb\USNF_DPW_NATIONAL_FOREST_PROCLAINED'
tgt_item_md = md.Metadata(poles_path)

# Delete all geoprocessing history and any enclosed files from the item's metadata
if not tgt_item_md.isReadOnly:
    tgt_item_md.deleteContent('GPHISTORY')
    tgt_item_md.deleteContent('ENCLOSED_FILES')
    tgt_item_md.save()



