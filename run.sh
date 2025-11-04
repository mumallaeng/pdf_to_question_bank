#!/bin/bash
# Run script for PDF to Question Bank Converter

set -e  # Exit on error

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Error: Virtual environment not found!"
    echo "Please run './setup.sh' first to set up the environment."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Check if folder path is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <folder_path> [--columns N]"
    echo ""
    echo "Example:"
    echo "  $0 sample"
    echo "  $0 sample --columns 3"
    exit 1
fi

# Run the Python script with all arguments
echo "Running PDF to Question Bank Converter..."
echo "=========================================="
python3 pdf2qb.py "$@"
echo "=========================================="
echo "✓ Processing completed!"
