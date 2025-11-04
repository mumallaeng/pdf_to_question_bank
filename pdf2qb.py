#!/usr/bin/env python3
"""
PDF to Question Bank Converter

This script converts PDF files containing question banks into individual question images.
It splits pages into columns and then separates questions based on whitespace detection.
"""

import os
import argparse
from pdf2image import convert_from_path
from PIL import Image


def is_white(pixel):
    """
    Check if a pixel is white (RGB value >= 250 for all channels).

    Args:
        pixel: Pixel value (can be tuple for RGB/RGBA or int for grayscale)

    Returns:
        bool: True if pixel is white, False otherwise
    """
    # RGB mode
    if isinstance(pixel, tuple) and len(pixel) == 3:
        return all(channel >= 250 for channel in pixel)
    # RGBA mode
    elif isinstance(pixel, tuple) and len(pixel) == 4:
        return all(channel >= 250 for channel in pixel[:3])
    # Grayscale mode
    elif isinstance(pixel, int):
        return pixel >= 250
    return False


def split_col_by_height_rgb(cols, crop_height=40):
    """
    Split columns into segments based on whitespace detection.

    Args:
        cols: List of column images
        crop_height: Height of each scanning segment (default: 40 pixels)

    Returns:
        list: List of column segments for each column
    """
    cols_segments = []

    for col in cols:
        width, height = col.size
        segments = []
        current_segment = None
        flag = 0

        for y in range(0, height, crop_height):
            # Define box (left, top, right, bottom)
            box = (0, y, width, min(y + crop_height, height))
            crop_segment = col.crop(box)
            pixels = list(crop_segment.getdata())

            # Check if this is a white segment
            is_white_segment = all(pixel == (255, 255, 255) for pixel in pixels)

            if is_white_segment:
                # White segment detected
                if flag == 1 and current_segment:
                    # If flag was 1 and white segment appears, add current segment
                    segments.append(current_segment)
                    current_segment = None
                flag = 0
            else:
                # Non-white segment
                if flag == 0:
                    # Start new segment
                    current_segment = crop_segment.copy()
                else:
                    # Merge consecutive non-white segments
                    new_height = current_segment.height + crop_segment.height
                    combined_segment = Image.new('RGB', (width, new_height))
                    combined_segment.paste(current_segment, (0, 0))
                    combined_segment.paste(crop_segment, (0, current_segment.height))
                    current_segment = combined_segment

                flag = 1

        # Note: Last segment (usually page number) is excluded
        # if current_segment:
        #     segments.append(current_segment)

        cols_segments.append(segments)

    return cols_segments


def split_image_by_columns(image, col_count=2):
    """
    Split an image into vertical columns.

    Args:
        image: PIL Image object
        col_count: Number of columns to split into (default: 2)

    Returns:
        list: List of cropped column images
    """
    width, height = image.size
    # Exclude 3px border between columns
    column_width = (width - (col_count - 1) * 3) // col_count

    cropped_col_images = []

    for i in range(col_count):
        left = i * (column_width + 3)
        right = left + column_width
        cropped_col_image = image.crop((left, 0, right, height))
        cropped_col_images.append(cropped_col_image)

    return cropped_col_images


def pdf_to_images(pdf_path, output_folder):
    """
    Convert PDF pages to images.

    Args:
        pdf_path: Path to the PDF file
        output_folder: Folder to save output images

    Returns:
        list: List of PIL Image objects
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    images = convert_from_path(pdf_path)

    return images


def pdf_to_split_boxes(pdf_path, output_folder, col_count):
    """
    Convert PDF to split box images (individual questions).

    Args:
        pdf_path: Path to the PDF file
        output_folder: Folder to save output images
        col_count: Number of columns per page

    Returns:
        dict: Dictionary containing page, column, and box information
    """
    images = pdf_to_images(pdf_path, output_folder)
    pdf_dict = {}

    for page_num, image in enumerate(images):
        page_key = f'page_{page_num + 1}'
        pdf_dict[page_key] = {
            'image': image,
        }

        col_images = split_image_by_columns(image, col_count)
        cols_box_images = split_col_by_height_rgb(col_images)

        for col_num, col_val in enumerate(col_images):
            col_key = f'col_{col_num + 1}'

            pdf_dict[page_key][col_key] = {
                'col_image': col_val
            }

            col_box_images = cols_box_images[col_num]
            for box_num, box_val in enumerate(col_box_images):
                box_key = f'box_{box_num + 1}'

                pdf_dict[page_key][col_key][box_key] = {
                    'box_image': box_val
                }

                format_nums = f"C{col_num + 1:02d}B{box_num + 1:04d}"
                box_path = os.path.join(output_folder, f'{page_key}_{format_nums}.png')
                box_val.save(box_path, 'PNG')

    return pdf_dict


def convert_all_pdfs_in_folder(folder_path, col_count=2):
    """
    Convert all PDF files in a folder to question images.

    Args:
        folder_path: Path to folder containing PDF files
        col_count: Number of columns per page (default: 2)
    """
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, file_name)
            output_folder = os.path.join(folder_path, os.path.splitext(file_name)[0])

            print(f"Processing: {pdf_path}")
            pdf_dict = {
                "pdf_name": file_name,
                "pdf_val": pdf_to_split_boxes(pdf_path, output_folder, col_count)
            }

            print(f"Completed: {file_name}")
            print(f"Output folder: {output_folder}")
            print(f"Pages processed: {len(pdf_dict['pdf_val'])}")
            print("-" * 50)


def main():
    """Main function with command-line argument parsing."""
    parser = argparse.ArgumentParser(
        description='Convert PDF question banks to individual question images'
    )
    parser.add_argument(
        'folder_path',
        type=str,
        help='Path to folder containing PDF files'
    )
    parser.add_argument(
        '--columns',
        '-c',
        type=int,
        default=2,
        help='Number of columns per page (default: 2)'
    )

    args = parser.parse_args()

    if not os.path.exists(args.folder_path):
        print(f"Error: Folder '{args.folder_path}' does not exist")
        return 1

    convert_all_pdfs_in_folder(args.folder_path, args.columns)
    return 0


if __name__ == "__main__":
    exit(main())
