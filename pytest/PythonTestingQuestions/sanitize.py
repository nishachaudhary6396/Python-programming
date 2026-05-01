import re

class InputSanitizationError(Exception):
    pass

def sanitize_input(text):
    cleaned_text = re.sub(r"[^a-zA-Z0-9 -]", "", text)

    if cleaned_text.strip() == "":
        raise InputSanitizationError("emptyyy text")
    
    return cleaned_text