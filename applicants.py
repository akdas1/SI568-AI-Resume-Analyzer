# Mini Project: AI Resume Analyzer & Summarizer
# Author: Amit Das
# Course: SI 568 Applied Data Science
# University of Michigan School of Information
# Date: April 18, 2023
# Revision Date: May 7, 2025

# Description: Connects to OpenAI's API and lets users upload a resume file to 
#              receive job suggestions, followed by optional conversational 
#              feedback until they exit.

# Please pip install PyPDF2 before you start
import openai
import os
from yourkey import key
from PyPDF2 import PdfReader
openai.api_key = key # go to yourkey.py and enter your key

## we are just choosing the PDF format
filepath = input('Enter the file path of your resume in pdf format: ')

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
        quit() # immediately quits and ignores the rest of the code
        
    else: # stores question, answer, and history
    response = openai.ChatCompletion.create(
                model ="gpt-3.5-turbo", messages = history + 
                [{"role": "user", "content": question}])
    
    # retrieves the answer
    answer = response['choices'][0]['message']['content']
    return answer
def main():
    '''
    Runs the program, then stores questions and answers.
    Initially returns some job suggestions based on the
    resume. Then, gave the option for the user to ask
    additional questions.

    Parameters:
    -----------
        None

    Returns:
        None
    '''
    text = get_resume(filepath) # gets the resume text
    ## initial question
    question = f"Here is my resume. What jobs could I get with this?\n{text}"
    history = []
    answer = ask_question(question, history)
    print(answer) # prints the initial response
    ## stores question and responses
    history.append({"role": "user", "content": question})
    history.append({"role": "assistant", "content": answer})
    while True:
        # asks the user if they have any follow-up questions
        question = input('Ask a follow up question or exit: ')
        answer = ask_question(question, history)
        print(answer)
        ## stores question and responses
        history.append({"role": "user", "content": question})
        history.append({"role": "assistant", "content": answer})
if __name__ == "__main__":
    main()
