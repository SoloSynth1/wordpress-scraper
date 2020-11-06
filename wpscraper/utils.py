import re


def remove_leading_scripts(response_text):
    cleaned_text = re.search(r'(\[.*)', response_text)
    return cleaned_text.group(1)
