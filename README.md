# 🧾 PDF Renamer by Tracking Code

A Python-based GUI tool to automatically rename PDF files based on tracking codes (starting with `WS`) found on the **first page** of the document. Ideal for processing 300–1000 PDFs quickly. 🖥️📄

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)]()

---

## 🚀 Features

- 🔍 Scans first page of PDF for codes starting with `WS` (case-insensitive)
- 📝 Renames files using tracking code
- 📄 Logs successfully renamed codes in a `.txt` file
- 🔁 Reverts names if an error occurs during processing
- 🖼️ Visual feedback during processing
- 🧩 Suffixes added to handle duplicates (`_1`, `_2`, etc.)
- 🖱️ Drag-and-drop GUI interface

---

## 📂 Folder Structure

pdf-renamer-by-tracking-code/
├── main.py # Launches GUI
├── renamer.py # Handles PDF renaming logic
├── utils.py # Logging and helper functions
├── assets/
│ └── icon.ico # (Optional) Custom icon
├── dist/
│ └── exe-version.exe # Compiled Windows app
├── logs/
│ ├── renamed.txt # Tracking codes
│ └── errors.txt # Failed renames
├── screenshot.png
├── README.md
├── LICENSE
└── requirements.txt


---

## 🛠️ How to Use

1. **Download** the latest `.exe` file from [Releases](https://github.com/arvinbalinado/pdf-renamer-by-tracking-code/releases).
2. **Prepare PDF files** in a folder.
3. **Run the application**, drag PDFs into the GUI, and click **Rename**.
4. A `renamed.txt` log will be generated.
5. If no `WS` code is found or if errors occur, details are logged in `errors.txt`.

---

## 💻 Tech Stack

- **Python 3.13**
- `PyMuPDF` (`fitz`)
- `Tkinter`
- `os`, `re`, `shutil`

---

## 📦 Installation (Developers)

```bash
git clone https://github.com/arvinbalinado/pdf-renamer-by-tracking-code.git
cd pdf-renamer-by-tracking-code
pip install -r requirements.txt
python main.py

📬 Contact
For feedback or support, reach me at: arvin.balinado@yahoo.com

📄 License
This project is licensed under the MIT License.

