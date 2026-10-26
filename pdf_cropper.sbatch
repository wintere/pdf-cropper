#!/bin/bash

#SBATCH --account=library_it
#SBATCH --partition=preempt
#SBATCH --job-name=PDF_Cropper
#SBATCH --time=00:05:00            
#SBATCH --nodes=1                  
#SBATCH --mem=250M
#SBATCH --output=%x-%j-%a.out
#SBATCH --error=%x-%j-%a.err
#SBATCH --array=0-10

module purge
module load uv

INDIR=(/scratch/library_it/TLS/input_v2/*)
OUTDIR=/scratch/library_it/TLS/cropped_v2

subdir="${INDIR[$SLURM_ARRAY_TASK_ID]}/"
basedir="$(basename "$subdir")"
subout="$OUTDIR/$basedir"

# Make output directory if it does not exist
mkdir -p $OUTDIR 
mkdir -p $subout
uv run cropper.py $subdir $subout 65 65 725 750