# grass_reproject_to_albers
# r.proj - Re-projects a raster map from one location to the current location.
# NOT RUN

import os
import grass.script as grass

datadir = r'F:\__data\muylaert\___BASES\mapbiomas_30m'
citydir = r'F:\__data\muylaert\___BASES\municipios_IBGE'
outputdir = r'...'

# Create a location for re-projecting maps
# Datum SAD69 and Projection Albers
# Now run the code below within this new location !!!!!!!!!!!!!!!!!!!!!!!!

os.chdir(citydir)

# Import municipalities of Brazil in albers
grass.run_command('v.in.ogr', input='malha_mun_13_albers_area.shp', output='malha_mun_13_albers_area', overwrite = True)

# Define region based on shapefile of municipalities
grass.run_command('g.region', vector = 'malha_mun_13_albers_area', res = 5000, flags = 'ap')
# the flag -p shows the region after defining it

#r.proj
os.chdir(datadir)

year = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014']
files = os.listdir(datadir)
                   
for i in files:
    for k in year:
        if i[-8:] == k+'.tif':
            print(k)
            name = i.replace('.tif', '') # define the name of the map inside GRASS without '.tif'
            print(name)
    # Import map
        grass.run_command('r.in.gdal', input= i, output=name, overwrite = True)
    
        grass.run_command('r.proj', location = 'brasil_location_latlon', input = 'BR_'+year, output = name+'_albers' , flags = 'p', memory = 300, overwrite = True)
    #os.chdir(outputdir)
    #return for continuing loop
    #os.chdir(datadir) Maybe unnecessary, since files do not change as object
    
    
# output = Name for output raster map (default: input)
# method=string
# Interpolation method to use
# Options: nearest,bilinear,cubic
# Default: nearest
