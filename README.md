# What you need to know before starting:
You need to type your OpenAI key to the yourkey.py file. You will also need to pipinstall PyPDF2 to access your pdf resumes. You can read the requirements.txt for clarity on what system requirements are recommended to use this on.

I made the interface simple enough to when you run either scripts, users will be given a general idea of what needs to be input. If a wrong value is input, you can correct this until corrected or simply exit! In both scripts, you are asked to input a filepath of your resume in pdf format. If you do not enter a correct filepath or incorrect file type, you will be give the oppurtunity to re-enter a filepath. This will run until you enter a valid path or you exit. Detailed instructions for both types of users are below:

You can view and use sample resumes attached. You can also view sample outputs within the sampleoutput.pdf for both types of scripts.

## What applicants may need to know:
When you input your resume, the AI will give you a list of jobs that match your skillset. You can then ask any additional followup questions you want. You can exit at any point just by typing 'exit'.

## What employers may need to know:
When you input an applicant's resume, the AI will give you a summary of the applicant's resume. You can then input other applicant's resumes to get their resume summaries. You can exit at any point just by typing 'exit'.

### Notes

1. Connecting to the AI may be computationally heavy and will depend on your system, the API, and your Wifi. Please read the requirements.txt for further information.
1. Applicants are able to ask open ended questions after getting their list of matching jobs. However, there is no limit on what type of questions you can ask, although the AI will learn previous context in your questions and answers.
1. Employers are not currently able to ask open questions to the AI, but are able to consistently get resume summaries to assist in the hiring process.


