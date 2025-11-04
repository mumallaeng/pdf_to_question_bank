#!/bin/bash
# Setup script for PDF to Question Bank Converter

set -e  # Exit on error

echo "=========================================="
echo "PDF to Question Bank Converter - Setup"
echo "=========================================="
echo ""

# Check for poppler installation
echo "Checking system dependencies..."
if ! command -v pdfinfo &> /dev/null; then
    echo "⚠️  WARNING: poppler is not installed!"
    echo ""
    echo "This program requires poppler to convert PDFs."
    echo ""
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "On macOS, install with Homebrew:"
        echo "  brew install poppler"
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "On Ubuntu/Debian, install with:"
        echo "  sudo apt-get install poppler-utils"
    fi
    echo ""
    read -p "Do you want to continue setup anyway? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Setup cancelled. Please install poppler and try again."
        exit 1
    fi
else
    echo "✓ poppler is installed"
fi
echo ""

# Check if venv already exists
if [ -d "venv" ]; then
    echo "Virtual environment already exists."
    read -p "Do you want to recreate it? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Removing existing virtual environment..."
        rm -rf venv
    else
        echo "Using existing virtual environment."
    fi
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Install package in editable mode
echo "Installing pdf2qb package..."
pip install -e .

echo ""
echo "=========================================="
echo "✓ Setup completed successfully!"
echo "=========================================="
echo ""
echo "You can now run the program in multiple ways:"
echo ""
echo "1. Using the pdf2qb command (recommended):"
echo "   source venv/bin/activate"
echo "   pdf2qb <folder_path>"
echo ""
echo "2. Using the shell script:"
echo "   ./run.sh <folder_path>"
echo ""
echo "3. Using quickstart (auto-activates venv):"
echo "   ./quickstart.sh <folder_path>"
echo ""
