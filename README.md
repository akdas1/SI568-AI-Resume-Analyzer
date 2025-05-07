# AI Resume Analyzer & Summarizer, SI 568 Mini Project

## Course
SI 568 Applied Data Science  
University of Michigan, School of Information

## Author
Amit Das

Original Date: April 18, 2023 

**Revision Date**: May 7, 2025 

## What you need to know before starting:
**This mini project was made for educational purposes for SI 568 at the University of Michigan School of Information.**

*This repository and its code are intended solely as a demo to showcase academic work. You may download and run it locally. As this is an academic project and **not a product**, the code is provided without any warranty.*

## Install Dependencies 
**You will need your own OpenAI API key**, which can be referenced on their [site](https://openai.com/api/). You can input your key into the "**yourkey.py**" file (avoiding hard coding for security). It's not recommended to share your key publicly or with others.

**Library Dependencies can be installed via:**
pip install -r requirements.txt

Python Version 3.10.0+ *preferred*

## Overall Function
I attempted to create a simple interface so that when you run either script, you will be given directions on what to input or follow responses. Both scripts use while loops to cross-check inputs. It will let you run (or exit) until you get that step right! For example, both scripts ask for PDF inputs, and if the file doesn't exist, is misspelled, or isn't a PDF, the window will let you retry until a valid PDF resume is input. You can either manually exit the terminal window or type "exit."

Detailed instructions for both types of users are below:

## What applicants may need to know:
When you input your resume, the AI will give you a list of jobs that match your skill set. You can also ask additional follow-up questions or exit at any point just by typing 'exit'. You may also quit the terminal. The intent behind this was to experiment with how AI can help with the application process and preparation, especially with resume uploading directly within Python for context. 

## What employers may need to know:
When you input an applicant's resume, the AI will give you a summary of the applicant's resume. You can then input other applicants' resumes to get additional resume summaries. You can also exit at any point just by typing 'exit'. The intent behind this was to experiment with speed and how AI can help with hiring strategies.

## Some thoughts for optimization:
- The function defaults to using PDFs for simplicity, although future adjustments to the if-elif-else statements referenced can bring in more file types.
  
**For the employers.py**: I realized that though there is a file limit to PDF, the summarizer may still work if it has readable text within it, regardless of the content’s topic. This partially covers any issues if the file wasn’t a resume, since the responses would process and be non-resume-related summaries. I do not have a simple thought process on how to limit this as of yet, that doesn’t involve reading the file contents **until after it is read in.** However, an option is to use the AI to print out a simple response of judgment, similar to natural language processing and machine learning classifications. This concept is that after the file is accepted, the AI reads it, decides it is not a resume, and then exists via a chat response variable. If "yes", it would exit, Python would print out "Sorry. This file is not a resume. Please upload a **one-page PDF resume.**"

For clarity, **the AI model is not what decides to quit.** It decides what classification the input file is, and based on that, the code preemptively responds. There currently isn’t a page limit in the PDF file reader function. If a user abuses the code by uploading irrelevant pages, inaccurate summaries will be produced. This is a flaw of the current project, but a way I thought about fixing this was to limit the page numbers submitted to one via if statements, which is the standard. This would solve the case of irrelevant pages, and the above AI decision-making idea would solve instances where it is one page and not a resume. The same can be said if the page were blank.

**for the applicants.py**:

### Notes
1. I originally referenced and sampled several generic resumes from **BeamJobs** to test the code. These were removed to avoid sharing. However, you can view the AI-generated / transformed sample outputs within the "sampleoutput.pdf" for both the applicant and employer scripts.
1. Connecting to the AI may be computationally heavy and depend on your system, the API (calls and other third-party limits), and Wifi speeds. Please take a look at the "requirements.txt" for more info.
1. Applicants can ask open-ended questions after getting their list of matching jobs. However, there is no limit on what type of questions you can ask, although the AI will learn from previous context in your questions, answers, and input resume. This essentially makes it a resume-focused "chatbot". *Updated Note: AI has file uploads now, but this was still experimental.*
1. Employers are not currently able to ask open questions to the AI, but can consistently get resume summaries to assist in the hiring process.

## Data & Privacy
1. While this uses Generative AI, it is important to note that it can be inaccurate. This code was used experimentally to see how it may work in a business setting.
1. Be cautious when submitting sensitive information to Generative AI resources. This code utilizes external APIs like OpenAI. While the code does not collect or store data, information sent to external services may be collected or used. You may refer to OpenAI's privacy policies to see what they collect here: https://openai.com/policies/row-privacy-policy/

## Acknowledgements

This project uses **OpenAI's API** and publicly available resume templates from **BeamJobs** to test whether my code's AI-generated feedback and resume summaries were accurate. The templates were used only for academic, educational, non-commercial, and testing purposes. They have since been removed from this repository.

OpenAI's API was used for
[OpenAI API](https://openai.com/api/)

Resume templates used for testing were sourced from the following BeamJobs pages. In each case, I used the *first downloadable template on each page* (unless updated):

- [Sample 1: 9 Data Scientist Resume Examples for 2023](https://www.beamjobs.com/resumes/data-science-resume-example-guide)
- [Sample 2: 5 Business Resume Examples That Got the Job in 2023](https://www.beamjobs.com/resumes/business-resume-examples)
- [Sample 3: 7 Attorney Resume Examples That Got the Job in 2023](https://www.beamjobs.com/resumes/attorney-resume-examples)
- [Sample 4: 11 Data Analyst Resume Examples for 2023](https://www.beamjobs.com/resumes/data-analyst-resume-examples#writing-your-data-analyst-resume)
- [Sample 5: 5 Dentist Resume Examples Guaranteed to Work in 2023](https://www.beamjobs.com/resumes/dentist-resume-examples)
