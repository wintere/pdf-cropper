# A Quick PDF Cropping Utility

This script uses the PyPDF library to crop batches of .pdf
files by using a cropbox to specify the new extent of the image.

## Contents
* `cropper.py` - crops a single PDF, designed for parallelization
* `pdf_cropper.sbatch` - Slurm script used on the University of Oregon's Talapas cluster

## Requirements
* uv
* Python 3.10+

## Usage 

### Installing `uv`

If you have not already installed uv, [follow the instructions
here](https://docs.astral.sh/uv/getting-started/installation/#installation-methods).

### Cropping a Single File

To crop a single file, run the command below in Terminal or Git Bash:

```bash
uv run cropper.py tests/input/Betterton-Mary-Bio.pdf tests/output/ 25 45 750 750
```

### Cropping a Folder of PDFs

As pages from the same book often have the same margins,
you may to prefer to crop an entire folder of PDFs using
the same cropping extent parameters.

```bash
uv run cropper.py tests/input/ tests/output/ 25 45 750 750
```

## Tips
* Do not make the input and folders the same directory.
* Point measurements can be adjusted through trial and error
or (more effectively) using gridlines in 
[Acrobat](https://helpx.adobe.com/acrobat/using/grids-guides-measurements-pdfs.html)
or the ruler tool in Mac's Preview application.