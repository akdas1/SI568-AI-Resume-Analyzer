# Mini Project: AI Resume Analyzer & Summarizer
# Author: Amit Das
# Course: SI 568 Applied Data Science
# University of Michigan School of Information
# Date: April 18, 2023
# Revision Date: May 7, 2025

# Description: Connects to OpenAI's API and asks the user to input a resume. This lets 
#              users retrieve resume summaries for the input file. Then, they are asked
#              to input another resume and repeat the process, repeating this process
#              until the user exits.


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
                filepath = input('Enter the file as a PDF: ')
        ## users can choose to exit at any point in this loop
        elif filepath.lower() == 'exit':
                    print('Goodbye!')
                    quit()
        else:
            filepath = input('Enter a valid PDF file path: ')
            continue
        return resume

def ask_question(question):
    '''
    Takes in a question and retrieves an answer from the AI.

    Parameters:
    -----------
    question: str
        input question from the user

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
        messages = [{"role": "user", "content": question}])

    # gets the response from the AI
    answer = response['choices'][0]['message']['content']
    return answer

def main():
    '''
    Runs the program, then returns questions and answers.
    Summarizes input resume by calling the get_resume
    function, and connects to the model via the 
    ask_question function. It will repeat the process 
    each time for the remaining applicants until the user 
    exits. The user can also exit at any point 
    by typing "exit".

    Parameters:
    -----------
        None

    Returns:
        None
    '''
    ## question and responses
    while True:
        # loop to continuously summarize inputs
        filepath = input("Enter the applicant's resume filepath in PDF format: ")
        ## users can exit during this continuous loop
        if 'exit' in filepath.lower():
            print("Goodbye!")
            break
        text = get_resume(filepath)
        question = f"Here is a resume: \n{text} Can you summarize it for me?"
        answer = ask_question(question)
        print(answer) # prints the response
        continue
if __name__ == "__main__":
    main()
