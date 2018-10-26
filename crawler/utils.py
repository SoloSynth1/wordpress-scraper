import os


def ensure_file_directory(file):
    inception(os.path.dirname(os.path.realpath(file)))

def inception(directory):
    parent_directory = os.path.dirname(directory)
    if not os.path.exists(parent_directory):
        inception(parent_directory)
    if not os.path.exists(directory):
        os.makedirs(directory)