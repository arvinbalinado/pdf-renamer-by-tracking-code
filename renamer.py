import os
import re
import fitz  # PyMuPDF
from utils import log_tracking_code, log_error, generate_unique_name

def extract_tracking_code_from_pdf(pdf_path):
    try:
        with fitz.open(pdf_path) as doc:
            first_page_text = doc[0].get_text()
        match = re.search(r'(WS\d+)', first_page_text, re.IGNORECASE)
        return match.group(1).upper() if match else None
    except Exception as e:
        raise RuntimeError(f"Error reading {pdf_path}: {e}")

def rename_pdfs_in_folder(folder_path, log_area=None):
    renamed_count = 0
    seen_codes = set()

    for filename in os.listdir(folder_path):
        if not filename.lower().endswith(".pdf"):
            continue

        original_path = os.path.join(folder_path, filename)

        try:
            tracking_code = extract_tracking_code_from_pdf(original_path)

            if not tracking_code:
                log_error(f"{filename}: No WS code found")
                if log_area:
                    log_area.insert("end", f"❌ {filename}: No WS code found\n")
                continue

            # Check for duplicates and generate unique filename
            if tracking_code in seen_codes:
                new_filename = generate_unique_name(tracking_code, folder_path)
            else:
                new_filename = f"{tracking_code}.pdf"

            seen_codes.add(tracking_code)

            new_path = os.path.join(folder_path, new_filename)
            os.rename(original_path, new_path)

            log_tracking_code(tracking_code)

            if log_area:
                log_area.insert("end", f"✅ Renamed {filename} → {new_filename}\n")

            renamed_count += 1

        except Exception as e:
            error_msg = f"{filename}: {str(e)}"
            log_erro_
