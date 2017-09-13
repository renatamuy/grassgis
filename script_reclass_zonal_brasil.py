#----------------------------------------------------------------------------------------------------------------------
'''Script for Mapbiomas Collection 2
 Renata Muylaert and Bernardo Niebuhr
 Application: Get Mosaic of Mapbiomas collection 2 and reclass it, preparing for calculation of landscape metrics'''
#----------------------------------------------------------------------------------------------------------------------

# Import modules
import os
import grass.script as grass
import math

#check current dir
os.getcwd()

datadir = r'F:\__data\muylaert\___BASES\mapbiomas_30m'
outputdir = r'G:\outputs'
       
# Change dir
os.chdir(datadir)

# test
ano = '2001'

# Read all files and directories inside the folder, and transform them to a python list
# Each element of the list will be a string element

files = os.listdir(datadir)

# Suppose we are going to gather all maps inside a mapset
map_list = grass.list_grouped('rast', pattern = '*'+ano)['PERMANENT']

# First, define the GRASS region as the region encompassing all the maps, using g.region

grass.run_command('g.region', raster = map_list, flags = 'p') # the flag -p shows the region after defining it

# Reclassiy MapBiomas Forest and Silviculture

reclass_legend_for = ['1 thru 8 = 1 forest', 
                      '*        = 0']

reclass_legend_euca = ['9 = 1 euca', 
                       '* = 0']

# Create txt file for reclassification - forest
file_name_for = 'reclass_mapbiomas_forest_1_8.txt'
os.chdir(datadir)
reclass_file = open(file_name_for, 'w')
for i in reclass_legend_for:
    reclass_file.write(i)
    reclass_file.write('\n')
    
reclass_file.close()

# Create txt file for reclassification - euca
file_name_euca = 'reclass_mapbiomas_euca_9.txt'
os.chdir(datadir)
reclass_file = open(file_name_euca, 'w')
for i in reclass_legend_euca:
    reclass_file.write(i)
    reclass_file.write('\n')
    
reclass_file.close()

# Checking txt files generated

fileextensions = ('.txt')
for filename in os.listdir(datadir):
    if filename.endswith(fileextensions):
       print(filename)

# Set range up to 2016
years= range(2001, 2017) 
number_string = ''.join([str(x) for x in years])
str(years)

del name
del year
del i

os.chdir(datadir)
# For each file, check whether it is a .tif, print its name and import into GRASS
for i in files:
  for year in years:
    year = str(year)
    if i[-8:] == year+'.tif':
      name_aux = i.replace('.tif', '') # define the name of the map inside GRASS without '.tif'
      name = name_aux.replace('1km_', '')
      # Import map
      grass.run_command('r.in.gdal', input=i, output=name, overwrite = True)
      # Recover file names for rules
      file_name_for = 'reclass_mapbiomas_forest_1_8.txt'
      file_name_euca = 'reclass_mapbiomas_euca_9.txt'
      
      # Forest
      grass.run_command('r.reclass', input=name, output='BR_'+year+'_forest_1a8', rules = file_name_for, overwrite = True)
      # Euca
      grass.run_command('r.reclass', input=name, output='BR_'+year+'_euca_9', rules = file_name_euca, overwrite = True)
      
      # Export
      os.chdir(outputdir)
      grass.run_command('r.out.gdal', input='BR_'+year+'_forest_1a8', output='BR_'+year+'_forest_1a8'+'.tif', overwrite = True)
      grass.run_command('r.out.gdal', input='BR_'+year+'_euca_9', output='BR_'+year+'_euca_9'+'.tif', overwrite = True)
     
      print i
      print year
      os.chdir(datadir)


#----------------------------------------------------------------------------------

      # Remove from temporary files?
      # grass.run_command('g.remove', raster ='BR_'+year+'_forest_1a8', flags = 'f')
      # grass.run_command('g.remove', raster ='BR_'+year+'_euca_9', flags = 'f')
      # grass.run_command('g.remove', raster = name, flags = 'f')
      
'''Building the rest'''
#check current dir
os.getcwd()
# Check rasters in grass
grass.parse_command("g.list", _type="rast")

# Finding errors
return handle_errors(returncode, returncode, args, kwargs)





