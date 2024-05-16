For setting up a Python script on a Windows device that uses Tesseract OCR to extract text from images in the clipboard and then copies the text back to the clipboard, follow this simplified guide tailored specifically for Windows.

### Step 1: Install Python
Make sure Python is installed on your Windows system. If not, you can download it from the official Python website:
- Go to [Python.org](https://www.python.org/downloads/)
- Download the latest Python installer for Windows.
- Run the installer, and make sure to check "Add Python to PATH" before clicking "Install Now".

### Step 2: Install Tesseract-OCR
Install Tesseract OCR, ensuring it's accessible from your system's PATH:
1. Download the Tesseract Windows installer from [UB Mannheim’s Tesseract page](https://github.com/UB-Mannheim/tesseract/wiki).
2. Run the installer. During installation, note the installation directory (commonly `C:\Program Files\Tesseract-OCR`).
3. Optionally, add Tesseract to your system PATH:
   - Right-click on 'This PC' and select 'Properties'.
   - Click on 'Advanced system settings' and then 'Environment Variables'.
   - Under 'System Variables', find and select 'Path', then click 'Edit'.
   - Click 'New' and add the path where Tesseract is installed (e.g., `C:\Program Files\Tesseract-OCR`).
   - Click 'OK' to save and exit all dialogs.

### Step 3: Install Required Python Libraries
Open Command Prompt and install the necessary libraries using pip:
```bash
pip install Pillow pytesseract pyperclip
```

### Step 4: Run the Python Script
Once you have cloned or downloaded the repository, you can run the `image_to_text.py` script whenever you have an image copied to your clipboard that contains text you want to extract.

The script will automatically extract the text from the clipboard image and copy the extracted text back to the clipboard, ready for you to paste anywhere you need.
```python
# This script extracts text from images in the clipboard using Tesseract OCR and copies the extracted text back to the clipboard.
# Specifically designed to run on Windows.

import pytesseract
from PIL import ImageGrab, Image
import pyperclip
import tempfile
import os

# Configure the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def image_to_text_clipboard():
    try:
        # Grab the image from the clipboard
        img = ImageGrab.grabclipboard()
        if isinstance(img, Image.Image):
            # Save the image to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp:
                img.save(tmp.name)
                # Ensure the file is closed before reading it again
                tmp.close()
            
            # Read the image back from the temporary file
            with Image.open(tmp.name) as img:
                # Use Tesseract to extract text from the image
                text = pytesseract.image_to_string(img)
                # Copy the extracted text back to the clipboard
                pyperclip.copy(text)
                print("Text copied to clipboard.")
            
            # Delete the temporary file after ensuring it's no longer in use
            os.unlink(tmp.name)
        else:
            print("No image found on the clipboard.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
image_to_text_clipboard()
```

### Step 5: Run the Script
- Open Command Prompt.
- Navigate to the folder where `clipboard_ocr.py` is saved.
- Execute the script by typing:
  ```bash
  python clipboard_ocr.py
  ```

### Notes:
- Ensure the path to the Tesseract executable in the script (`pytesseract.pytesseract.tesseract_cmd`) matches the actual install location on your system.
- You can test the script by first copying an image (that contains text) to the clipboard.

This setup provides a streamlined way for Windows users to leverage OCR technology using Python, handling images from the clipboard efficiently.
