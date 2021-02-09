import yaml
import sys
import os
from os.path import join

# configure
cfgfile = sys.argv[1]
pypath = str(os.path.dirname(os.path.abspath(__file__)))  
configuration = open(os.path.join(pypath, cfgfile))
cfg = yaml.load(configuration, Loader=yaml.FullLoader)

if cfg['options']['extract_data'] and cfg['setup']['simtype'].lower() == 'grb':
    print('Preparing GRB catalog...\n')
    os.system(f'python3 simGRBpreparation.py -f {cfgfile}')
elif cfg['setup']['simtype'].lower() == 'bkg':
    print('Computing BKG-ONLY simulations is work in progress')
else:
    raise ValueError('Ivalid "simtype" value')

print('\n\nExit\n\n')