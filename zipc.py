import argparse
import logging
from zipfile import ZipFile

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')  # Removed %(levelname)s
logger = logging.getLogger(__name__)

# Use a method to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password.encode())
        return True  # The password was correct
    except Exception as e:
        return False  # The password was incorrect

def main():
    parser = argparse.ArgumentParser(description='Bruteforce ZIP file password.')
    parser.add_argument('zip_file', help='Path to the encrypted ZIP file')
    parser.add_argument('wordlist_file', help='Path to the word list file')

    args = parser.parse_args()

    logger.info(f'[+] Beginning bruteforce for {args.zip_file}')
    
    with ZipFile(args.zip_file) as zf:
        with open(args.wordlist_file, 'r', encoding='latin-1') as f:
            passwords = f.read().splitlines()
            for password in passwords:
                password = password.strip()  # Remove leading/trailing whitespaces
                logger.info(f'Trying password: {password}')
                if attempt_extract(zf, password):
                    logger.info(f'[+] Password found: {password}')
                    break
            else:
                logger.info('[+] Password not found in list')

if __name__ == "__main__":
    main()
