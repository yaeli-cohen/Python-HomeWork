import os
import shutil

def create_folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)



def delete_folder(directory):
    empty = True
    for _ in os.scandir(directory):
        empty = False
        break

    if empty:
        shutil.rmtree(directory, ignore_errors=True)
    else:
        raise OSError(f"התיקייה '{directory}' אינה ריקה ולכן לא ניתן למחוק אותה.")

# def create_directory(directory):
#     if not os.path.exists(directory):
#         os.makedirs(directory)

def delete_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)

def create_file(file_path):
    with open(file_path, "x") as new_file:
        new_file.write("")


def write_file(file_path, content):
    with open(file_path, "x") as new_file:
        new_file.write(content)


def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)



def list_files(directory):
    if os.path.exists(directory):
        files = os.listdir(directory)
        return files
    else:
        raise OSError(f"<UNK> '{directory}' <UNK> <UNK> <UNK> <UNK> <UNK>.")


def show_path(path):
    if os.path.exists(path):
        print(path)
