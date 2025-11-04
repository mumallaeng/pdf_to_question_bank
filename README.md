English | [한국어](README.ko.md)

# PDF to Question Bank Converter

A tool that extracts individual question images from PDF files. It splits each PDF page into columns, then separates individual questions within each column based on whitespace and saves them as image files.
Built to make it easy to create flashcard question banks for tools like Anki.

## Quick Start

### Method 1: Using the `pdf2qb` command (recommended)

```bash
# One-time setup
./scripts/setup.sh

# Activate the virtual environment, then use
source venv/bin/activate
pdf2qb sample
pdf2qb sample --columns 3
```

### Method 2: Using shell scripts

```bash
# Setup and run in one command
./scripts/quickstart.sh sample

# Split into 3 columns
./scripts/quickstart.sh sample --columns 3
```

On first run, it automatically creates a virtual environment and installs the required packages.
For other usage methods, see [setup](docs/setup.md).

## Preview and Usage Example




<table>
<tr>
<td>

Place your PDF files in the specified path and run the script

<img alt="preview_1" src="https://github.com/user-attachments/assets/ba8eb71b-9554-48fa-a9b4-dc8d7d52c6e1" />
</td>
<td>

Result: individual question images are extracted and saved

<img alt="preview_2" src="https://github.com/user-attachments/assets/19c08be1-8ddb-4a3b-850e-a96e1e53f999" />
</td>
</tr>
<tr>
<td>
Usage example: <br/>
Import the extracted image files into Anki to build a question bank
    <img alt="preview_3" src="https://github.com/user-attachments/assets/8728a109-4f00-4aac-9211-61db7b857355" />
</td>
<td>
    <img alt="preview_4" src="https://github.com/user-attachments/assets/20ba421c-0acb-4447-9c4c-6d309d960348" />
</td>
</tr>
</table>



<br/><br/><br/>


# Planned Improvements

- Titles, page numbers, and other non-question/answer images are sometimes extracted along with actual content
- Improve handling of question images that don't have a white background
- Add a feature to output a CSV (`number,question_path,answer_path`) that matches question and answer PDFs by question number
- Add direct conversion to an Anki deck file (.apkg)

<br/><br/><br/>

---

**License**

[MIT](LICENSE)
