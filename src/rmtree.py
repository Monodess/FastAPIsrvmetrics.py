import os
import shutil


def smart_cleanup(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in dirs:
            full_path = os.path.join(root, name)

            # Get the contents once to save processing time
            try:
                content = os.listdir(full_path)
            except FileNotFoundError:
                continue

            # Case 1: Folder is truly empty
            if not content:
                print(f"Removing empty folder: {full_path}")
                os.rmdir(full_path)

            # Case 2: Folder only contains __pycache__
            elif len(content) == 1 and "__pycache__" in content:
                print(f"Removing cache-heavy folder: {full_path}")
                shutil.rmtree(full_path)

            # Case 3 (Optional): Delete __pycache__ folders themselves
            elif name == "__pycache__":
                print(f"Nuking cache: {full_path}")
                shutil.rmtree(full_path)


smart_cleanup('app')