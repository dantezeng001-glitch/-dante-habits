#!/usr/bin/env python3
"""
Markdown → PDF converter.

Usage:
    python md_to_pdf.py <input.md> [output.pdf]

If output path is omitted, writes to the same directory with .pdf extension.
"""

import sys
import os
from pathlib import Path

try:
    from markdown_pdf import MarkdownPdf, Section
except ImportError:
    print("Error: markdown-pdf package is not installed.")
    print("Please install it using: pip install markdown-pdf")
    sys.exit(1)

def convert(input_path: str, output_path: str):
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Create PDF with Table of Contents up to level 2
    pdf = MarkdownPdf(toc_level=2)
    pdf.add_section(Section(content))
    pdf.save(output_path)
    
    size = os.path.getsize(output_path)
    print(f"OK  {output_path}  ({size:,} bytes)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python md_to_pdf.py <input.md> [output.pdf]")
        sys.exit(1)

    src = sys.argv[1]
    if not os.path.isfile(src):
        print(f"Error: file not found: {src}")
        sys.exit(1)

    if len(sys.argv) >= 3:
        dst = sys.argv[2]
    else:
        dst = str(Path(src).with_suffix(".pdf"))

    convert(src, dst)
