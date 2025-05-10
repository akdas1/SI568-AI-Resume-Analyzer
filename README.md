# AI Resume Analyzer & Summarizer, SI 568 Mini Project

## Course
SI 568 Applied Data Science  
University of Michigan, School of Information

## Author
Amit Das

Original Date: April 18, 2023 

**Revision Date**: May 10, 2025 

## Description:
**This mini project was made for educational purposes for SI 568 at the University of Michigan School of Information.**

## Install Dependencies 
**You will need your own OpenAI API key**, which can be referenced on their [site](https://openai.com/api/). You can input your key into the "**yourkey.py**" file (avoiding hard coding for security). It's not recommended to share your key publicly or with others.

**Library Dependencies can be installed via:**
> pip install -r requirements.txt

Python Version 3.10.0+ *preferred*

## Overall Function
I created a simple interface so that when you run either script, you will be given directions on what to input or follow responses. Both scripts use while loops to cross-check inputs. It will let you run (or exit) until you get that step right! For example, both scripts ask for PDF inputs, and if the file doesn't exist, is misspelled, or isn't a PDF, the window will let you retry until a valid PDF resume is input. You can either manually exit the terminal window or type "exit."

Detailed instructions for both types of users are below:

## What applicants may need to know:
When you input your resume, the AI will give you a list of jobs that match your skill set. You can also ask additional follow-up questions or exit at any point just by typing 'exit'. You may also quit the terminal. The intent was to experiment with how AI can help with the application process and preparation, especially with resume uploading directly within Python for context. 

## What employers may need to know:
When you input an applicant's resume, the AI will give you a summary of the applicant's resume. You can then input other applicants' resumes to get additional resume summaries. You can also exit at any point just by typing 'exit'. The intent was to experiment with speed and how AI can help with hiring strategies.

## Considerations & Optimizations:
> The function defaults to using PDFs for simplicity, although future adjustments to the if-elif-else statements referenced can bring in more file types.

**For both scripts**: Though both scripts limit the input files to one-page PDFs, the summarizer may still work if it has readable text within it, regardless of the content’s topic. Results could vary depending on the questions, file contents, and model used, if modified. It may be important to limit this to content-based resumes, in case there are areas for computational abuse.

One theoretical way to handle non-resume inputs safely could involve searching for specific resume terms like “education”, “work experience”, “skills”, and/or “projects” after a valid PDF is uploaded, but before it’s returned and processed by the AI. The code then validates the content by parsing through the extracted text, and prompts the user to upload a new resume file if the text doesn't match most of the common resume terms.

**May 4, 2025 Revision: fixed nested while loops**

Corrected a redundant while loop in the question receiver functions, since it was not needed. The main function’s while loop included the question.

**May 9, 2025 Revision: fixed blank and corrupted inputs**

One thing I have revised was the addition of a blank page filter in the file uploading steps. After the input file is extracted, the code will check if the text string is empty. It also strips empty white spaces just in case. If the PDF file does not work, I revised the validated PDF path file to run in a try/ except statement. Similarly, whether the file is corrupted or blank, the user will be able to upload another file or exit.

### Notes
1. I originally referenced and sampled several generic resumes from **BeamJobs** to test code. These were removed to avoid sharing. However, you can view the AI-generated / transformed sample outputs within the "sampleoutput.pdf" for both the applicant and employer scripts.
1. Connecting to the AI may be computationally heavy and depend on your system, the API (calls and other third-party limits), and Wifi speeds. Please take a look at the "requirements.txt" for more info.
1. Applicants can ask open-ended questions after getting their list of matching jobs. However, there is no limit on what type of questions you can ask, although the AI will learn from previous context in your questions, answers, and input resume. This essentially makes it a resume-focused "chatbot". *Updated Note: AI has file uploads now, but this was still experimental.*
1. Employers are not currently able to ask open questions to the AI, but can consistently get resume summaries to assist in the hiring process.

## Data & Privacy
1. While this uses Generative AI, it is important to note that it can be inaccurate. This code was used experimentally to see how it may work in a business setting.
1. Be cautious when submitting sensitive information to Generative AI resources. This code utilizes external APIs like OpenAI. While the code does not collect or store data, information sent to external services may be collected or used. You may refer to OpenAI's privacy policies to see what they collect here: https://openai.com/policies/row-privacy-policy/

## License & Usage

This project was created as part of academic coursework and is shared solely for demonstration and testing purposes. It is not intended for production or commercial use. The software is provided "as-is" with no warranty of any kind. 

You may explore, modify, and run the project locally for personal or non-commercial purposes. Please do not use, modify, or distribute this code for commercial purposes.

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
