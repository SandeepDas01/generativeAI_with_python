from transformers import pipeline
import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def chat_with_llm(text):
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
    print("Welcome to the PDF Chat! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        else:
            answer = qa_pipeline(question=user_input, context=text)
            print("Answer: ", answer['answer'])

if __name__ == "__main__":
    pdf_path = "linkedin.pdf"  # Replace with the path to your PDF file
    extracted_text = extract_text_from_pdf(pdf_path)
    chat_with_llm(extracted_text)
