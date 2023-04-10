import openai
import time
openai.api_key = '' # please enter your key

question = input('Enter your question: ')
## output is a list of question responses from the AI
output = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": question}
    ]
)
mc = "McDonald"
num = 0
first = []
burgers = []
fries = []
nuggets = []
misc = []

while True:
    ## as while loop starts, you can either exit or break into questions
    if question.lower() == 'exit':
        print('Goodbye!')
        time.sleep(1)
        quit()
    elif mc.lower() in question.lower():
        response = output['choices'][0]['message']['content']
        first.append(question)
        first.append(response)
        print(response)
        question = input('Enter your question: ')
        output = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": question}])
        while True:
            if 'burger' in question.lower():
                ## sort responses into burger list
                output = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}])
                response = output['choices'][0]['message']['content']
                burgers.append(question) # adds question asked
                burgers.append(response) # adds response recieved
                print(response)
                question = input('Enter your question: ')
            elif 'fries' in question.lower():
                ## sort responses into fries list
                output = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}])
                response = output['choices'][0]['message']['content']
                fries.append(question) # adds question asked
                fries.append(response) # adds response recieved
                print(response)
                question = input('Enter your question: ')
            elif 'nugget' in question.lower():
                ## sort responses into nuggets list
                output = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}])
                response = output['choices'][0]['message']['content']
                nuggets.append(question) # adds question asked
                nuggets.append(response) # adds response recieved
                print(response)
                question = input('Enter your question: ')
            elif question.lower() == 'exit':
                while True:
                    summary = input('Would you like a chat summary?: ')
                    if summary.lower() == 'yes':
                        print('CHAT SUMMARY')
                        print('Initial result:')
                        if len(first) == 0:
                            print('No questions asked.')
                        else:
                            for i in range(len(first)):
                                if i % 2 == 0:
                                    print(num + 1, 'User:', first[i])
                                    num += 1
                                else:
                                    print('  System:', first[i])
                                print('') # adds space for cleaner output
                        print('Burgers:')
                        if len(burgers) == 0:
                            print('No burger questions asked.')
                        else:
                            for i in range(len(burgers)):
                                if i % 2 == 0:
                                    print(num + 1, 'User:', burgers[i])
                                    num += 1
                                else:
                                    print('  System:', burgers[i])
                                print('') # adds space for cleaner output
                        print('Fries:')
                        if len(fries) == 0:
                            print('No fry questions asked.')
                        else:
                            for i in range(len(fries)):
                                if i % 2 == 0:
                                    print(num + 1, 'User:', fries[i])
                                    num += 1
                                else:
                                    print('  System:', fries[i])
                                print('') # adds space for cleaner output
                        print('Nuggets:')
                        if len(nuggets) == 0:
                            print('No nugget questions asked.')
                        else:
                            for i in range(len(nuggets)):
                                if i % 2 == 0:
                                    print(num + 1, 'User:', nuggets[i])
                                    num += 1
                                else:
                                    print('  System:', nuggets[i])
                                print('') # adds space for cleaner output
                        print('Other Questions:')
                        if len(misc) == 0:
                            print('No other questions asked.')
                        else:
                            for i in range(len(misc)):
                                if i % 2 == 0:
                                    print(num + 1, 'User:', misc[i])
                                    num += 1
                                else:
                                    print('  System:', misc[i])
                                print('') # adds space for cleaner output
                        time.sleep(1)
                        quit() # auto quits after summary is given
                    elif summary.lower() == 'no':
                        break # goes back up to the goodbye
                    else:
                        print('Please enter yes or no')
                        ## will keep asking for a yes or no repsonse till satisfied
                        continue
                break
            else:
                ## stores unrelated question answers
                output = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}])
                response = output['choices'][0]['message']['content']
                misc.append(question) # adds question asked
                misc.append(response) # adds response recieved
                print(response)
                question = input('Enter your question: ')
            continue
    else:
        # first question needed to contain mcdonald's, will ask you restart and input
        print("Ask about Mcdonald's")
        break