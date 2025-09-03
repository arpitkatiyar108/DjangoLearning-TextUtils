# ================================
# views.py
# Author: Arpit Katiyar
# Purpose: Define the views (functions) that handle requests
# ================================

# Importing required modules from Django
from django.http import HttpResponse      # For sending plain text responses (not used much here)
from django.shortcuts import render       # For rendering templates (HTML files)


# ---------------------------
# Home Page View
# ---------------------------
def home(request):
    """
    Handles requests for the homepage.
    It simply renders and returns the 'home.html' template.
    """
    return render(request, 'home.html')   # Render = combine template + optional data


# ---------------------------
# Analyze Text View
# ---------------------------
def analyze(request):
    """
    This function processes the input text based on user selections.
    Current options:
        - Remove Punctuations
        - Convert to Uppercase
        - Remove Newlines
        - Remove Spaces
        - Character Count
    """

    # 1. Get text input from the request (from the POST method).
    #    If no text is provided, 'No Text Found!' will be used.
    text = request.POST.get('text', 'No Text Found!')

    # 2. Get all checkbox values (ON/OFF switches).
    removepunch = request.POST.get('removepunch', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremoval = request.POST.get('newlineremoval', 'off')
    spaceremoval = request.POST.get('spaceremoval', 'off')
    charcount = request.POST.get('charcount', 'off')

    # 3. Initialize required variables.
    analyzed_text = text   # Start with original text
    purpose_text_list = [] # Keep track of transformations applied

    # 4. Define list of punctuation characters.
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

    # 5. Apply transformations in sequence (order matters).
    if removepunch == 'on':
        analyzed_text = ''.join(char for char in analyzed_text if char not in punctuations)
        purpose_text_list.append("Punctuations Removed")

    if uppercase == 'on':
        analyzed_text = analyzed_text.upper()
        purpose_text_list.append("Converted to Uppercase")

    if newlineremoval == 'on':
        analyzed_text = analyzed_text.replace("\n", " ").replace("\r", " ")
        purpose_text_list.append("New Lines Removed")

    if spaceremoval == 'on':
        analyzed_text = analyzed_text.replace(" ", "")
        purpose_text_list.append("Spaces Removed")

    if charcount == 'on':
        # Character count is informational → doesn’t modify text
        purpose_text_list.append(f"Character Count: {len(analyzed_text)}")

    # 6. Prepare context (dictionary) to pass to template.
    params = {
        'purpose_list': purpose_text_list,  # List of applied operations
        'text': text,                       # Original input text
        'analyzed_text': analyzed_text      # Final processed text
    }

    # 7. Render 'analyze.html' and pass the context.
    return render(request, 'analyze.html', params)
