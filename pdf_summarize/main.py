import fitz  # PyMuPDF
import openai

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to summarize text using ChatGPT API
def summarize_text_with_gpt(text, max_tokens=150):
    openai.api_key = ''  
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=text,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text'].strip()


# Path to your PDF file
pdf_path = 'Terraform_course.pdf'


# Extract text from PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Summarize text using ChatGPT API
summary = summarize_text_with_gpt(pdf_text)


# Print the summary
print("Summary:")
print(summary)







