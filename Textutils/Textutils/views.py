# ================================
# views.py
# Author: Arpit Katiyar
# Purpose: Define the views (functions) that handle requests
# ================================

# Importing required modules from Django
from django.http import HttpResponse      # For sending simple HTTP responses (not used much here, but useful for debugging)
from django.shortcuts import render       # For rendering templates (HTML files)


# ---------------------------
# Home Page View
# ---------------------------
def home(request):
    """
    This function will handle requests for the homepage.
    It will simply render and return the 'home.html' template.
    """
    return render(request, 'home.html')   # Render = combine template + optional data


# ---------------------------
# Analyze Text View
# ---------------------------
def analyze(request):
    """
    This function processes the input text based on user selection.
    Right now, it removes punctuation if the 'removepunch' option is ON.
    """

    # 1. Get text input from the request (using GET method for now).
    #    If no text is provided, use 'DefaultText' as fallback.
    text = request.GET.get('text', 'DefaultText')

    # 2. Check if the 'Remove Punctuation' option was selected.
    #    If the checkbox is not selected, it will be 'off'.
    removepunch = request.GET.get('removepunch', 'off')

    # 3. Initialize an empty string for storing the analyzed text.
    analyzed_text = ''

    # 4. Define a list of punctuations to remove.
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

    # 5. If 'removepunch' is ON, loop through the input text and build a new string
    #    without punctuation characters.
    if removepunch == 'on':
        for char in text:
            if char not in punctuations:
                analyzed_text += char
    else:
        # If option is not ON, just keep the text as it is.
        analyzed_text = text

    # 6. Prepare parameters (dictionary) to pass to the template.
    #    These variables can be displayed in the HTML file.
    params = {
        'purpose': 'Removed Punctuations' if removepunch == 'on' else 'No Changes',
        'text': text,                       # Original text
        'removepunch': removepunch,         # Status of checkbox
        'analyzed_text': analyzed_text      # Final processed text
    }

    # 7. Render the 'analyze.html' template and send params to it.
    return render(request, 'analyze.html', params)
