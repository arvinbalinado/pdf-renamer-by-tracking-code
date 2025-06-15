import os

def log_tracking_code(code, log_file="tracking_codes.txt"):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{code}\n")

def log_error(filename, error_msg, log_file="error_log.txt"):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{filename}: {error_msg}\n")

def generate_unique_name(directory, base_name):
    counter = 1
    new_name = base_name
    while os.path.exists(os.path.join(directory, new_name)):
        name, ext = os.path.splitext(base_name)
        new_name = f"{name}_{counter}{ext}"
        counter += 1
    return new_name
