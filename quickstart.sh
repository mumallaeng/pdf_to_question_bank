#!/bin/bash
# Quick start script - Setup and run in one command

set -e  # Exit on error

echo "=========================================="
echo "PDF to Question Bank Converter"
echo "Quick Start"
echo "=========================================="
echo ""

# Run setup if venv doesn't exist
if [ ! -d "venv" ]; then
    echo "Setting up for the first time..."
    ./setup.sh
else
    echo "Virtual environment found. Skipping setup."
    echo "To reinstall dependencies, run: ./setup.sh"
    echo ""
fi

# Check if folder path is provided
if [ $# -eq 0 ]; then
    echo ""
    echo "Usage: $0 <folder_path> [--columns N]"
    echo ""
    echo "Example:"
    echo "  $0 sample"
    echo "  $0 sample --columns 3"
    exit 1
fi

# Run the program
./run.sh "$@"
