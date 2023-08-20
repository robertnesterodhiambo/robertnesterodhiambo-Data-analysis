# Google Apps Script Document Functions

This repository contains a Google Apps Script file (`code.gs`) with three functions: `myFunction1`, `myFunction2`, and `myFunction3`. These functions are designed to interact with Google Docs using Google Apps Script.

## Purpose

The purpose of this script is to demonstrate various tasks related to Google Docs manipulation. Each function showcases a specific aspect of working with Google Docs through code.

## Functions

1. **myFunction1**
   - Creates a new Google Docs document titled 'Tester 1'.
   - Utilizes the `DocumentApp.create()` function.

2. **myFunction2**
   - Creates a new Google Docs document titled 'Test 2'.
   - Retrieves the document's body and logs it using the `Logger.log()` function.
   - Appends a paragraph containing the text "Hello Naruto" to the document's body.

3. **myFunction3**
   - Retrieves an existing Google Docs document using a known document ID.
   - Retrieves the document's body and appends a paragraph containing "HELLO NARUTO".
   - Logs the document to the script's logger.

## Usage

To use these functions:

1. Open a Google Docs document.
2. Go to "Extensions" > "Apps Script".
3. Paste the content of `script.gs` into the Apps Script editor.
4. Save and run each function by selecting its name and clicking the play button (▶️).

Keep in mind that these functions require the necessary permissions to access and manipulate Google Docs. When prompted, make sure to review and grant the required permissions.

For more details about Google Apps Script and its capabilities, refer to the [official documentation](https://developers.google.com/apps-script).

Feel free to modify and expand these functions to suit your specific needs.
