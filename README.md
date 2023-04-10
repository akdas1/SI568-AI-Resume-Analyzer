# What you need to know before starting:

## What users may need to know:
I made the interface simple enough to give users ideas of what needs to be input if a wrong value is given. For example, the first question needs to contain “McDonald’s”. If you do not ask about McDonald’s, you will be told to “Ask about McDonald’s.” However, you need to rerun the code to try again. I had issues with adding another input for it letting users re-ask the questions without rerunning.

## What technical members may need to know:
The AI may be computationally heavy, but code comments are illuminating how each part works. In short, we are going through several while loops based on user input, and will continuously run and store data until the user exits. Upon exit, users will be given a question input on if they want to have a chat summary, and a yes would give a sorted chat transcript for simple access. For technical requirements, please seek the requirements.txt file as stated below.

### Instructions

1. First, input your personal key in the commented line 'openai.api_key ='.
1. Run the code. You will be asked to input a question. Please start by asking a question about (containing) McDonald's.
1. If you do not ask about McDonald's, you will be told to ask about McDonald's. Rerun the terminal and try again.
1. After, you can ask any questions you'd like. Keep in mind, questions containing, 'burgers', 'nuggets' or 'fries' will be stored in appropriate lists, with others being generally stored in a separate section.
1. You can ask any amount of questions, but please keep in mind that the AI has fees for me and usage has a capacity.
1. At the end, you will be asked if you want an ordered chat summary, a yes or no response will exit the system and give you a summary if you said yes. If you said no, it will simply exit. If you enter another response, you will be able to respond until the input is fulfilled.
1. Connecting to the AI may be computationally heavy and will depend on your system, the API, and your Wifi. Please read the requirements.txt for further information.



