import docx
import os
from datetime import date
from tkinter import filedialog

filepath = filedialog.askopenfilename()

if filepath:
    print(f"Selected file: {filepath}")
    file_name = os.path.basename(filepath)
    file_path = os.path.dirname(filepath);
    print(file_path)
    doc = docx.Document(filepath)

    replace_date = "{Date}"
    replace_company = "{Company}"
    replace_role = "{Role}"

    today = date.today().strftime("%B %d, %Y")
    company = input("Company: ")
    role = input("Role: ")

    for paragraph in doc.paragraphs:
        if replace_date in paragraph.text:
            paragraph.text = paragraph.text.replace(replace_date, today)
        
        if replace_company in paragraph.text:
            paragraph.text = paragraph.text.replace(replace_company, company)

        if replace_role in paragraph.text:
            paragraph.text = paragraph.text.replace(replace_role, role)
    
    doc.save(f"{file_path}/{company}-{file_name}")
    print(f"Successfully saved file to {file_path}")
    
else :
    print("No File Selected")
