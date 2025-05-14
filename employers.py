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
    Takes in a filepath and returns the text of the resume.

    Parameters:
    -----------
    filepath: str
        file path of the input resume

    Returns:
        resume: str
            extracted text from the resume
    '''
    while True:
        ## checks the exit condition
        ## users can choose to exit at any point in this loop
        if filepath.lower() == 'exit':
            print("Goodbye!")
            quit() # quits the code
        ## check if the file exists
        if not os.path.isfile(filepath):
            print("That file does not exist.")
        ## checks if the file is a PDF or not
        elif not filepath.endswith('.pdf'):
            print("This is not a PDF file.")
        # if the PDF does exist:
        else:
            try:
                ## reads in the PDF file
                reader = PdfReader(filepath)
                ## filters to the first page for resumes
                resume = reader.pages[0].extract_text()
                if not resume or resume.strip() == "":
                    print("File is empty.")
                else:
                    return resume  # returns immediately once a valid PDF exists
            except Exception as e: # corrupt file error or unreadable
                print(f"Error reading the PDF: {e}")
        # asks the user to input a new file path for the above reasons
        filepath = input('Enter a valid PDF file path or type "exit" to quit: ')

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
        text = get_resume(filepath)
        question = f"Here is a resume: \n{text} Can you summarize it for me?"
        answer = ask_question(question)
        print(answer) # prints the response
        continue
if __name__ == "__main__":
    main()
