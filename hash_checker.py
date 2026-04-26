import hashlib
import os

def calculate_file_hash(file_path):
    """
    Calculates the SHA-256 hash of a given file.
    This is essential in Digital Forensics to ensure data integrity.
    """
    sha256_hash = hashlib.sha256()
    
    try:
        # We use 'rb' (Read Binary) to read the file in its raw format
        with open(file_path, "rb") as f:
            # Read the file in chunks of 4096 bytes to optimize memory usage
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    
    except FileNotFoundError:
        return "Error: File not found. Please check the path."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# --- Tool Interface ---
print("--- Digital Forensics: File Integrity Tool ---")
path = input("Enter the full path of the file to analyze: ")

# Execute analysis
result = calculate_file_hash(path)

print("-" * 45)
print(f"Analysis Result for: {os.path.basename(path)}")
print(f"SHA-256 Hash: {result}")
print("-" * 45)
