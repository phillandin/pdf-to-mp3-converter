import pdfplumber
import requests
import os

api_key = os.environ.get("API_KEY")
url = "https://api.voicerss.org/"

pdf_pages_text = []

pdf = input("Please enter the full file path of the pdf you'd like to convert to audio.\n")

file_name = pdf.split(".pdf")[0]

with pdfplumber.open(pdf) as file:
    for page in file.pages:
        page_text = page.extract_text()
        pdf_pages_text.append(page_text)

full_text = "\n".join(pdf_pages_text)

parameters = {
    "key": api_key,
    "src": full_text,
    "hl": "en-us",
}

response = requests.post(url=url, params=parameters)

with open(f"{file_name}.mp3", "wb") as file:
    file.write(response.content)
