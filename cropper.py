import argparse
from pathlib import Path
import os
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject

# PDF processing function
def process_pdf(filepath, left, bottom, right, top, outdir):
    # Generate output path
    path_str = str(filepath)
    print("Procesing file", os.path.basename(path_str))
    output = os.path.join(outdir, os.path.basename(path_str))
    reader = PdfReader(path_str)
    writer = PdfWriter()
    for page in reader.pages:
        # Origin [0, 0] in the bottom left corner of the PDF
        page.cropbox = RectangleObject((left, bottom, right, top))
        writer.add_page(page)  # Add adjusted pages
    writer.write(output)

# Main for processing command-line arguments
def main():
    parser = argparse.ArgumentParser() # get command line arguments (one file per job, designed for Slurm array processing)
    parser.add_argument("input", help="filepath of a .pdf file or folder to be processed")
    parser.add_argument("output", help="output directory path")
    # Positional args for cropbox coordinates
    parser.add_argument("left", type=float) # Points from left edge to bottom left corner
    parser.add_argument("bottom", type=float) # Points from bottom edge to bottom left corner
    parser.add_argument("right", type=float) # Points from right edge to upper right corner
    parser.add_argument("top", type=float) # Points from top edge to upper right corner
    args = parser.parse_args()

    input_path = Path(args.input)
    if input_path.is_dir(): # Folder of PDFs
        for cur_file in input_path.glob("*.pdf", case_sensitive=False):
            process_pdf(cur_file, args.left, args.bottom, args.right, args.top,
                        args.output)
    else: # Single file
        process_pdf(input_path, args.left, args.bottom, args.right, args.top,
                    args.output)


if __name__ == "__main__":
    main()
