from os import listdir, system
import os
from os.path import isfile, join

rootpath = str(os.path.dirname(os.path.abspath(__file__))).replace('cta-sag-sci', '')
path = f'{rootpath}/cta-sag-sci/jobs/'

jobs = [f for f in listdir(path) if 'job_' not in f and isfile(join(path, f))]

for job in jobs:
    print(f'bash jobs/{job}')
    os.system(f'bash jobs/{job}')

print(len(jobs))