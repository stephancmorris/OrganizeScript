import os
import shutil
from pathlib import Path

# The path to the directory you want to organize
downloads_dir = Path.home() / 'Downloads'

for item in downloads_dir.iterdir():
    # Check if it's a file
    if item.is_file():
        # Get the file extension
        file_extension = item.suffix.lstrip('.')
        
        if file_extension:  # if file has an extension
            new_dir = downloads_dir / file_extension
            
            # Create a new directory if it doesn't exist
            new_dir.mkdir(exist_ok=True)
            
            # Construct the new file path
            new_file_path = new_dir / item.name
            
            # Move the file
            shutil.move(str(item), str(new_file_path))
