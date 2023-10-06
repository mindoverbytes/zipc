# ZIP File Password Cracker

## Overview

This Python script provides a straightforward yet effective password brute-force tool for opening password-protected ZIP files. It utilizes the Python `zipfile` module to systematically test potential passwords from a user-provided word list, attempting to extract the contents of a ZIP archive.

## Features

- Brute-force approach for unlocking password-protected ZIP files.
- Support for traditional ZIP encryption (legacy encryption).
- Flexibility to specify the encrypted ZIP file and a word list containing potential passwords.
- Real-time progress updates and results displayed in the console.

## Requirements

- Python 3.x
- A word list file with potential passwords (e.g., `wordlist.txt`).

## Installation

1. Clone or download this repository to your local machine.

   ```bash
   git clone https://github.com/mindoverbytes/zipc.git
   ```

2. Open a terminal or command prompt.

## Usage

1. Run the script by executing the following command:

    ```bash
    python zipc.py zip_file wordlist_file
    ```

2. The script will initiate the brute-force process, systematically trying each password from the word list until it successfully unlocks the ZIP file or exhausts all possibilities.

## Note

- This script is designed for educational and legitimate purposes only. Unauthorized use of this script to gain unauthorized access to password-protected files is illegal and unethical.
