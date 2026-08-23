#!/bin/bash

#SBATCH --account=library_it
#SBATCH --partition=compute
#SBATCH --job-name=PDF_Cropper
#SBATCH --time=00:05:00            
#SBATCH --nodes=1                  
#SBATCH --mem=500M
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.err

module purge
module load uv

# Navigate to project directory
cd ~/apptainer_proj

PDFS=(/scratch/library_it/TLS/input/*)
OUTDIR=/scratch/library_it/TLS/cropped/

# Make output directory if it does not exist
mkdir -p $OUTDIR 

for file in ${PDFS[@]};
do
    uv run cropper.py $file $OUTDIR 65 65 750 750
done