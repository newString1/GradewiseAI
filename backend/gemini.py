"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai
import csv
import re
with open('responses.csv', 'w', newline='',  encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Roll Number", "Rating", "Feedback"])

genai.configure(api_key="API-KEY-OF-GEMINI-1.0-PRO")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# convo = model.start_chat(history=[
# ])
# convo.send_message("What architectures are used in Gemini and ChatGPT?")
# print(convo.last.text)
def prompt(essay, rollno, reference):
    # start_time = time.time()
    messages_chatgpt=[{"role": "system", "content": "you are an essay evaluator. You need to give rating from 1 to 10 under the rating heading and then give feedback and suggestions for improvement as points line by line to students clearly under the feedback. These are the reference essay give rating based on how close the essay is to the reference essay . If the essay is not at all related to reference essay give 0  and give 10 if all the points from reference essay are covered in the essay. Give feedback points. These are the reference essay "+reference+"  This is the actual essay to be rated and reviewed "+essay},
                  {"role": "user", "content": essay} ]
    def transform_to_gemini(messages_chatgpt):
        messages_gemini = []
        system_promt = ''
        for message in messages_chatgpt:
            if message['role'] == 'system':
                system_promt = message['content']
            elif message['role'] == 'user':
                messages_gemini.append({'role': 'user', 'parts': [message['content']]})
            elif message['role'] == 'assistant':
                messages_gemini.append({'role': 'model', 'parts': [message['content']]})
        if system_promt:
            messages_gemini[0]['parts'].insert(0, f"*{system_promt}*")

        return messages_gemini
    messages = transform_to_gemini(messages_chatgpt)
    response = model.generate_content(messages)
    print(response.text)
    # response_text = response.text
    response_text = re.sub(r'\*', '', response.text)


    # Extract rating and feedback
    rating_index = response_text.find("Rating: ") + len("Rating: ")
    rating_end_index = response_text.find("\n", rating_index)
    rating_str = response_text[rating_index:rating_end_index]
    # Extract numerator of fraction rating if exists
    # if '/' in rating_str:
    #     rating = rating_str.split('/')[0]
    # else:
    #     rating = rating_str
    # extracted_digits = [re.match(r'^\d+', string).group() if re.match(r'^\d+', string) else None for string in sample_strings]
    rating = re.match(r'^\d+', rating_str).group()
    if not rating:
        rating = 0
    # Find feedback content
    feedback_start_index = response_text.find(":", rating_end_index) + 1
    feedback_content = response_text[feedback_start_index:].strip()

    print("Rating:", rating)
    # print("Feedback:")
    print(feedback_content)
    with open('responses.csv', 'a', newline='',  encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([rollno, rating, feedback_content])
