import sys
import os
import numpy as np
from os import listdir, system
from os.path import isfile, join


if len(sys.argv) > 1:
    N = int(sys.argv[1])
else:
    N = 10

rootpath = str(os.path.dirname(os.path.abspath(__file__)))
pypath = f'{rootpath}/timing'
jobpath = f'{rootpath}/jobs'
shjob = f'{jobpath}/jobs_all.sh'
shrun = f'{jobpath}/runjobs_all.sh'
scripts = [f for f in listdir(pypath) if isfile(join(pypath, f)) and ('ctools' in f or 'gammapy' in f) and ('cumulative' not in f and 'lima' not in f)]

print(scripts)

for script in scripts:
    shname = f'{jobpath}/{script.replace(".py", ".sh")}'
    sh = open(shname, 'w+')
    sh.write('#!/bin/bash\n')
    sh.write('\nsource activate scitools')

    for i in range(N):
        if i == 0:
            sh.write(f'\n\tpython3 {pypath}/{script} 1000 {True}')
            sh.write(f'\n\tpython3 {pypath}/{script} 100 {False}')
            sh.write(f'\n\tpython3 {pypath}/{script} 10 {False}')
        else:
            sh.write(f'\n\tpython3 {pypath}/{script} 1000 {False}')
            sh.write(f'\n\tpython3 {pypath}/{script} 100 {False}')
            sh.write(f'\n\tpython3 {pypath}/{script} 10 {False}')

    sh.write('\n')
    sh.close()

sh = open(shjob, 'w+')
sh.write('#!/bin/bash\n')
for script in scripts:
    sh.write(f'echo {script.replace(".py", ".sh")}\n')
    sh.write(f'bash {jobpath}/{script.replace(".py", ".sh")}\n')

sh = open(shrun, 'w+')
sh.write('#!/bin/bash\n')
sh.write(f'\n#SBATCH --job-name=ambra')
#sh.write(f'\n#SBATCH --output=slurm-allscripts.out')
sh.write(f'\n#SBATCH --account=ambra')
sh.write(f'\n#SBATCH --nodes=1')
sh.write(f'\n#SBATCH --cpus-per-task=1\n\n')
sh.write(f'exec sh {shjob}\n')
sh.close()