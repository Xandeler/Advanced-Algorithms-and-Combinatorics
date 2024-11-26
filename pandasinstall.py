import os
import sys
import subprocess

# Function to install packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install required packages
install("pandas")

print("Pandas installed successfully!")
