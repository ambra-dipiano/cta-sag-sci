#!/bin/bash

#SBATCH --job-name=ambra
#SBATCH --output=slurm-/home/ambra/Desktop/CTA/projects/cta-sag-sci/jobs/job_ctools3d_blindfit.sh.out
#SBATCH --account=ambra
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1

exec sh /home/ambra/Desktop/CTA/projects/cta-sag-sci/jobs/ctools3d_blindfit.sh
