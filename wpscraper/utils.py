import re


# unused function to remove characters before JSON response, might be useful later
def remove_leading_scripts(response_text):
    cleaned_text = re.search(r'(\[.*)', response_text)
    return cleaned_text.group(1)
