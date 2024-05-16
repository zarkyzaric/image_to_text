import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    # List of packages to install
    packages = ['Pillow', 'pytesseract', 'pyperclip']

    # Install each package using pip
    for package in packages:
        try:
            print(f"Installing {package}...")
            install(package)
            print(f"{package} installed successfully.")
        except Exception as e:
            print(f"Failed to install {package}. Error: {e}")

if __name__ == "__main__":
    main()
