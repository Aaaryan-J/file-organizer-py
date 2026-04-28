from pathlib import Path

p = Path(r"C:\Users\ASUS\OneDrive\Documents\programming\python\file_organizer")
choice = input("Are you sure you want to organize the files by filetype? (Y/N): ").lower()
if choice == 'y':
    for f in p.iterdir():
        if f.is_file():
            filetype = f.suffix[1:]
            folder_path = p / f"{filetype}_files"
            folder_path.mkdir(exist_ok=True)
            new_location = folder_path / f.name
            f.replace(new_location)
else:
    print("Exiting...")