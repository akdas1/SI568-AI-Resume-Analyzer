# What you need to know before starting:
**This mini project was made for educational purposes for SI 568 at the University of Michigan School of Information.**

*This repository and its code are intended solely as a demo to showcase academic work. You may download and run it locally. As this is an academic project and **not a product**, the code is provided without any warranty.*

**You will need your own OpenAI API key**, which can be referenced on their site. You can input your key into the "yourkey.py" file (avoiding hard coding). You will also need to pip install PyPDF2 to access your PDF resumes. 

- The function defaults to using PDFs for simplicity, although future adjustments to the if-elif-else statements referenced can bring in more file types.
- Please read the "requirements.txt" for the recommended system requirements to run. Note: they are based on my computer for testing.

## Overall Function
I attempted to make the interface simple enough so that when you run either script, you will be given directions on what to input or follow responses. Both scripts use while loops to cross-check inputs. It will let you run (or simply exit) until you get that step right! For example, both scripts ask for PDF inputs, and if the file doesn't exist, is misspelled, or isn't a PDF, the window will let you retry until a valid PDF resume is input. You can either exit the terminal window manually or by typing "exit."
Detailed instructions for both types of users are below:

## What applicants may need to know:
When you input your resume, the AI will give you a list of jobs that match your skill set. You may ask additional follow-up questions if you'd like. You can also exit at any point just by typing 'exit'. The intent behind this was to experiment with how
AI can help with the application process and preparation, especially with resume uploading directly within Python.

## What employers may need to know:
When you input an applicant's resume, the AI will give you a summary of the applicant's resume. You can then input other applicants' resumes to get additional resume summaries. You can also exit at any point just by typing 'exit'. The intent behind this was to experiment with speed and how AI can help with hiring strategies.

### Notes
1. I originally referenced and sampled several generic resumes from BeamJobs to test the code. These were removed to avoid sharing. However, you can view the AI-generated / transformed sample outputs within the "sampleoutput.pdf" for both the applicant and employer scripts.
1. Connecting to the AI may be computationally heavy and depend on your system, the API (calls and other third-party limits), and Wifi speeds. Please take a look at the "requirements.txt" for more info.
1. Applicants can ask open-ended questions after getting their list of matching jobs. However, there is no limit on what type of questions you can ask, although the AI will learn from previous context in your questions, answers, and input resume. This essentially makes it a resume-focused "chatbot". Updated Note: AI has file uploads
1. Employers are not currently able to ask open questions to the AI, but can consistently get resume summaries to assist in the hiring process.

## Data & Privacy
1. While this uses Generative AI, it is important to note that it can be inaccurate. This code was used experimentally to see how it may work in a business setting.
1. Be cautious when submitting sensitive information to Generative AI resources. This code utilizes external APIs like OpenAI. While the code does not collect or store data, information sent to external services may be collected or used. You may refer to OpenAI's privacy policies to see what they collect here: https://openai.com/policies/row-privacy-policy/

## References
OpenAI. ChatGPT. 2023. OpenAI, https://openai.com/blog/chatgpt.
