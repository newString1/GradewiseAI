import streamlit as st
# import uploaded_pdf from 2_Step1️⃣ - Upload student data and essay📄.py
# import 2_Step1️⃣ - Upload student data and essay📄
from backend import backend
import pandas as pd
import numpy as np
import csv
from email.message import EmailMessage
import ssl
import smtplib


roll_email_dict = {}
st.markdown("### Upload Student Roll Number and their respective email in CSV file")
uploaded_csv = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_csv:
    bytes_data = uploaded_file.read().decode("utf-8")  # Decode bytes to string
    st.write("filename:", uploaded_file.name)
    # Parse CSV data
    csv_reader = csv.reader(bytes_data.splitlines())

# Skip the header row
    next(csv_reader)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Extract roll number and email from the row
        roll_no = row[1]  # Assuming Roll No is the second column (index 1)
        email = row[2]    # Assuming Email is the third column (index 2)

        # Add roll number and email to the dictionary
        roll_email_dict[roll_no] = email

    # Print the dictionary
        # print("Roll Number and Email Dictionary:")
        # for roll_no, email in roll_email_dict.items():
            # print(f"Roll No: {roll_no}, Email: {email}")

# st.markdown("## Great!🙌 The essays have been evaluated successfully.")
# st.markdown("### Here are the results:")

# df = pd.DataFrame([['sst', '100'],['can','500']], columns=['model','0'])
# st.bar_chart(df)  # Replace ?? with the appropriate argument(s) for the bar_chart function

st.markdown("### You can download the results as a CSV file.")

with open("responses.csv", "rb") as file:
    btn = st.download_button(
            label="Download Results",
            data=file,
            file_name="responses.csv",
            mime="csv"
          )


# Function to load data
def load_data(csv_file):
    df = pd.read_csv(csv_file)
    return df

# Main function

# Title
st.title('Rating Distribution Analysis')
# Load data
df = load_data('responses.csv')  # Change 'rating.csv' to the name of your CSV fil
# Create a DataFrame to store the counts of each rating
ratings_counts = pd.DataFrame({'Rating': range(1, 10), 'Count': 0})
# Count occurrences of each rating from the loaded data
for rating in range(0, 10):
    ratings_counts.loc[rating - 1, 'Count'] = (df['Rating'] == rating).sum()
# Display bar chart
st.write('### Distribution of Ratings')
st.bar_chart(ratings_counts.set_index('Rating'))



# Email forwarding
stud_len = len(roll_email_dict)
saved_time = (4*stud_len)/60 - (stud_len)/60
st.markdown(f"# WOW! You just have saved {saved_time} hours of manual work!🎉")

st.markdown('### Send feedback to students based on the results.')
send = st.button("Send Feedback through Email")
if send:
  email_sender = "gradewiseai@gmail.com"
  email_password = "aefk ncoz kajz abtc"
  subject = "Your Essay feedback"

  responses = {}
  with open(r'responses.csv', 'r') as responses_file:
      response_reader = csv.DictReader(responses_file)
      for row in response_reader:
          responses[row['Roll Number']] = {
              'rating': row['Rating'],
              'feedback': row['Feedback']
          }
  # stud_upload = backend.stud_data
  print(roll_email_dict)
  for roll_number, email_receiver in roll_email_dict.items():
      # roll_number = student_row['Roll Number']
      # email_receiver = student_row['Email']
      # name_receiver = student_row['Name']
      roll_number = roll_number+".pdf"
      # print(roll_number)
      if roll_number in responses:
          rating = responses[roll_number]['rating']
          feedback = responses[roll_number]['feedback']
          body = f"The evaluation of your essay has been completed.\nYour Rating for the essay is: {rating}/10\nFeedback: {feedback}\n\nThank you!\nNote: This is an automated email. Please do not reply."
      else:
          body = "There hasn't been any submission of essays so rating is provided as 0."
      em = EmailMessage()
      em["From"] = email_sender
      em["To"] = email_receiver
      em["Subject"] = subject
      em.set_content(body)
      context = ssl.create_default_context()
      with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
          smtp.login(email_sender, email_password)
          smtp.sendmail(email_sender, email_receiver, em.as_string())
  print("Emails sent successfully to all students.")
  st.success('Emails sent successfully to all students.', icon="✅")
