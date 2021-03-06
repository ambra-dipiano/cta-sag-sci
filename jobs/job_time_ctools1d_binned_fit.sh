#!/bin/bash

#SBATCH --job-name=ambra
#SBATCH --output=slurm-time_ctools1d_binned_fit.out
#SBATCH --account=ambra
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1

exec sh /data01/homes/cta/gammapy_integration/cta-sag-sci/jobs/time_ctools1d_binned_fit.sh
