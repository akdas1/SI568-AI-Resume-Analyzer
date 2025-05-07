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
            ## user can choose to exit at any point in this loop
            elif filepath.lower() == 'exit':
                    print('Goodbye!')
                    quit()
            else: ## if the file is not a PDF
                filepath = input('Enter your file as a pdf: ')
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
