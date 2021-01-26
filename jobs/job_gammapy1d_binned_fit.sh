#!/bin/bash

#SBATCH --job-name=ambra
#SBATCH --output=slurm-/home/ambra/Desktop/CTA/projects/cta-sag-sci/jobs/job_gammapy1d_binned_fit.sh.out
#SBATCH --account=ambra
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1

exec sh /home/ambra/Desktop/CTA/projects/cta-sag-sci/jobs/gammapy1d_binned_fit.sh
