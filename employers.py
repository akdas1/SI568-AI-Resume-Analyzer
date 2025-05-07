# Please pip install PyPDF2 before you start
import openai
import os
from yourkey import key
from PyPDF2 import PdfReader
openai.api_key = key # go to yourkey.py and enter your key

model_engine = "gpt-3.5-turbo" # changed from text-davinci-002 due to depreciation

## we are just choosing the PDF format for simplicity
def get_resume(filepath):
    '''
    Takes in a filepath and returns the text of the resume

    Parameters:
    -----------
    filepath: str
        file path of the input resume

    Returns:
        resume: str
            extracted text from the resume
    '''
    while True:
        ## check if the file exists
        if os.path.isfile(filepath) == True:
            ## check if the file is a PDF
            if filepath.endswith('.pdf'):
                reader = PdfReader(filepath)
                resume = reader.pages[0].extract_text()
            else: ## if the file is not a PDF
                filepath = input('Enter the file as a pdf: ')
        ## users can choose to exit at any point in this loop
        elif filepath.lower() == 'exit':
                    print('Goodbye!')
                    quit()
        else:
            filepath = input('Enter a valid pdf file path: ')
            continue
        return resume

def ask_question(question, history):
    '''
    Takes in a question and retrieves an answer from the AI.
    Stores the question, answer, and previous history.

    Parameters:
    -----------
    question: str
        input question from the user
    history: list
        list of previous questions and answers

    Returns:
        answer: str
        response from the AI
    '''
 
    # exits if chosen
    if question.lower() == 'exit':
        print('Goodbye!')
        quit() # will immediately quit and ignore the rest
    # stores question, answer, and history
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = history + [{"role": "user", "content": question}])

    # gets the response from the AI
    answer = response['choices'][0]['message']['content']
    return answer

def main():
    '''
    Runs the program, then stores questions and answers.
    Initially returns some summary based on the
    resume. Then, gave the option to input additional.

    Parameters:
    -----------
        None

    Returns:
        None
    '''
    filepath = input("Enter the applicant's resume filepath in pdf format: ")
    text = get_resume(filepath)
    history = []
    question = f"Here is a resume: \n{text} Can you summarize it for me?"
    answer = ask_question(question, history)
    print(answer) # prints the initial response
    ## stores question and responses
    history.append({"role": "user", "content": question})
    history.append({"role": "assistant", "content": answer})
    while True:
        filepath = input("Enter the next applicant's resume or exit: ")
        text = get_resume(filepath)
        question = f"Here is a resume: \n{text} Can you summarize it for me?"
        answer = ask_question(question, history)
        print(answer) # prints the initial response
        ## stores question and responses
        history.append({"role": "user", "content": question})
        history.append({"role": "assistant", "content": answer})
        continue
if __name__ == "__main__":
    main()
