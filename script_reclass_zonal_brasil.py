# Import modules
import os
import grass.script as grass


os.getcwd()

datadir = r'F:\__data\muylaert\___BASES\mapbiomas_30m'
outputdir = r'F:\__data\muylaert\___BASES\outputs'

       
# Change dir
os.chdir(datadir)

#test
year = '2000'

# Read all files and directories inside the folder, and transform them to a python list
# Each element of the list will be a string element
files = os.listdir(datadir)


# For each file, check whether it is a .tif, print its name and import into GRASS

for i in files:
  
  if i[-8:] == year+'.tif':
    print i
    name = i.replace('.tif', '') # define the name of the map inside GRASS without '.tif'
    
    # Import map
    grass.run_command('r.in.gdal', input=i, output=name, overwrite = True)
  
    '''FAZER LISTA COM NAMESSSSS'''

# Suppose we are going to gather all maps inside a mapset
map_list = grass.list_grouped('rast', pattern = '*'+year)['PERMANENT']

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

#Checking txt files

fileextensions = ('.txt')
for filename in os.listdir(os.curdir):
    if filename.endswith(fileextensions):
       print(filename)


# Reclassify
# Forest
del i

#Botar em um for
names = grass.parse_command("g.list", _type="rast")
grass.run_command('g.remove', raster="MATAATLANTICA_2012")

for i in NAMES:
    os.chdir(datadir)
    grass.run_command('r.reclass', input=name, output='BR_'+year+'_forest_1a8', rules = file_name_for, overwrite = True)
# Euca
    grass.run_command('r.reclass', input=name, output='BR_'+year+'_euca_9', rules = file_name_euca, overwrite = True)

# Can I Change dir INSIDE THE LOOP?

os.chdir(outputdir)

grass.run_command('r.out.gdal', input='BR_'+year+'_forest_1a8', output='BR_'+year+'_forest_1a8'+'.tif', type=Byte)
   
grass.run_command('r.out.gdal', input='BR_'+year+'_euca_9', output='BR_'+year+'_euca_9'+'.tif', type=Byte)
    

############################
#area flor
#forest.sum * 1000*1000/10000
#grass.run_command('v.rast.stats', map=munic_teste, raster='BR_'+year+'_forest_1a8', column_prefix=forest method=sum [percentile=integer]

###################
#r.out.gdal input=BR_2012_mask out=BR_2012_mask type=Byte

# Import municipalities of Brazil
#grass.run_command('v.in.ogr', input='malha_mun_13_albers_area.shp', output='malha_mun_13_albers_area', overwrite = True)

# Define region based on shapefile of municipalities
#grass.run_command('g.region', vector = 'malha_mun_13_albers_area', res = 5000, flags = 'ap') # the flag -p shows the region after defining it



