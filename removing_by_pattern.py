#Removing existing raster files in GRASS environment by some pattern

#Removing all rasters finishing with the term  _AreaHA

grass.run_command('g.remove', type='raster', pattern='*_AreaHA', flags= 'f')


''':)'''

