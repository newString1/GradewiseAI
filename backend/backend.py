# extract_pdf_files

import zipfile
import os
import shutil
import os
import PyPDF2
from backend import gemini


def analysis(file, reference):
    
# Define the path to the zip file
    if len(file) == 1 and file[0].type == "application/x-zip-compressed":
        zip_file_path = file[0]
        # Define the folder where you want to extract the PDF files
        output_folder = "backend/extracted_folder"

        # Ensure the output folder exists, if not, create it
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Extract the contents of the zip file
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(output_folder)

        # Move PDF files to the output folder
        for filename in os.listdir(output_folder):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(output_folder, filename)
                # Move the PDF file to the output folder
                shutil.move(pdf_path, os.path.join(output_folder, filename))

        # Extract text from PDF files

        def extract_text_from_pdf(pdf_path):
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ''
                for page in pdf_reader.pages:
                    text += page.extract_text()
                return text

        def main(folder_path):
            for filename in os.listdir(folder_path):
                if filename.endswith('.pdf'):
                    pdf_path = os.path.join(folder_path, filename)
                    text = extract_text_from_pdf(pdf_path)
                    print(f"Text from {filename}:")
                    resp = gemini.prompt(text, filename, reference)
                    print(resp)
                    # print(text+"\n")

        # folder_path = 'C:\\Users\\God\\OneDrive\\Documents\\file extraction'
        # print('backend/extracted_folder/'+file[0].name[:-4])
        main('backend/extracted_folder/'+file[0].name[:-4])
