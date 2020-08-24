import os
import re
import json

def ensure_file_directory(file):
    inception(os.path.dirname(os.path.realpath(file)))

def inception(directory):
    parent_directory = os.path.dirname(directory)
    if not os.path.exists(parent_directory):
        inception(parent_directory)
    if not os.path.exists(directory):
        os.makedirs(directory)

def dump_json(json_object,output_file):
    ensure_file_directory(output_file)
    with open(output_file, 'w') as f:
        f.write(json.dumps(json_object))

def remove_leading_scripts(response_text):
    cleaned_text = re.search(r'(\[.*)', response_text)
    return cleaned_text.group(1)
