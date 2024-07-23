import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
# import zipfile
# import os
# import shutil
from backend import backend
# from backend import gemini

# def analysis(csv, file):
#     if len(file) == 1 and file.type == "application/zip":
#         zip_file_path = file.name
#         # Define the folder where you want to extract the PDF files
#         output_folder = "extracted"
#         # Ensure the output folder exists, if not, create it
#         if not os.path.exists(output_folder):
#             os.makedirs(output_folder)
#         # Extract the contents of the zip file
#         with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#             zip_ref.extractall(output_folder)
#         # Move PDF files to the output folder
#         for filename in os.listdir(output_folder):
#             if filename.endswith(".pdf"):
#                 pdf_path = os.path.join(output_folder, filename)
#                 # Move the PDF file to the output folder
#                 shutil.move(pdf_path, os.path.join(output_folder, filename))





st.markdown("### Upload Student Essays in pdf format or zip file containing pdf files")
uploaded_pdf = st.file_uploader("Upload pdfs or zip file",accept_multiple_files=True)
# print(type(uploaded_csv))
# print(type(uploaded_pdf))
# if uploaded_pdf != [] and uploaded_csv == []:
#   st.error("Please upload CSV file")
# else:
for up_pdf in uploaded_pdf:
    bytes_data = up_pdf.read()
    st.write("filename:", up_pdf.name)
    print(up_pdf.name)

import streamlit as st

refer_txt = st.text_area(
    "Reference : ",
    )

# st.write(f'You wrote {len(txt)} characters.')


submit = st.button("Submit")
if submit:
    # import time
#  import streamlit as st

    with st.spinner('Loading...'):
        backend.analysis(uploaded_pdf,refer_txt)
        # backend.upload_file(uploaded_csv)
    st.success('Done!')
    switch_page("step2️⃣ - download and save results")