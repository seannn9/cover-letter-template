# Cover Letter Editor

A customizable python script that asks for two inputs (company name, role you are applying for), then automatically edits the cover letter template with those information.

### Dependecy:

-   `python-docx` - a Python library for creating and updating Microsoft Word (.docx) files

Install required packages in git bash

```
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

### How-To:

You can edit this code block to add custom variables.

```python
replace_date = "{Date}"
replace_company = "{Company}"
replace_role = "{Role}"

today = date.today().strftime("%B %d, %Y")
company = input("Company name: ")
role = input("What role are you applying for? ")

#finds instances of the given strings in the whole document, then replaces them with the user's inputs.
for paragraph in doc.paragraphs:
    if replace_date in paragraph.text:
        paragraph.text = paragraph.text.replace(replace_date, today)

    if replace_company in paragraph.text:
        paragraph.text = paragraph.text.replace(replace_company, company)

    if replace_role in paragraph.text:
        paragraph.text = paragraph.text.replace(replace_role, role)
```

Example cover letter template:

```
Your Details

{Company Name}
{Company Address}

Dear Hiring Manager,

I am very excited to apply for the position of {Position} at {Company Name}.
```
