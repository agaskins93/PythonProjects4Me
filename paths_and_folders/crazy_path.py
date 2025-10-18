from pathlib import Path
from datetime import datetime


#if else to see if file path exist
crazy_path = Path.home() / 'I' / 'dont' / 'exist.csv'
print(crazy_path)

if crazy_path.exists():

    with open(crazy_path, 'r') as file:
        print(file.read())

else:
    print('file does not exisit')

# iterates over multiple folders
path2 = Path.home() / 'PycharmProjects' / 'PythonProject'
for item in path2.iterdir():
    if item.is_file() and item.suffix == '.py':
        print(f' {item.stem} is a  python file')
        stats = item.stat()
        print('size:', stats.st_size)
        print('last modified:', datetime.fromtimestamp(stats.st_mtime))
    if item.is_dir():
        print(f' {item.name} is a directory')
    if 'read' in item.name.lower():
        print(f' contains the word \'read\'')

path3 = Path.home() / 'Documents' / 'PythonProject'

