import os

# FIXME: Doesn't support RTL text
def write_file(file_path: str, text: str):
    directory = os.path.dirname(file_path)
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)