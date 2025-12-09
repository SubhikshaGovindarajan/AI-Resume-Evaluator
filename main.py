from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
#from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
def prompt(resume_text,jd_text):
    prompt_template=ChatPromptTemplate.from_template(
    '''
    you are an expert career consultant. Compare the following resume and job description.
    Resume:
    {resume}
    JobDescription:
    {jd}

    Analyse and provide a structured JSON response with the following fields:
    1. Job Title Match: Describe how well the job title aligns.  
    2. Roles and Responsibilities: See if the candidate's duties align with the job requirements.
    3. Years of Experience: Verify if the candidate meets the required experience. 
    4. Keyword Match: Identify whether key JD skills appear in the resume. 
    5. Overall Match Score: Give a score showing the overall alignment. 
    6. Summary Fit: Write a brief summary of how suitable the candidate seems for the role. 
    7. Suggestions: Add short tips on what can be improved or highlighted better.


    return your result in valid JSON format only
'''
    

    )

    llm=ChatOllama(
        model="llama3.2:3b",
        temperature=0.1
    )
    parser=StrOutputParser()

    chain=prompt_template | llm | parser
    response = chain.invoke({"resume": resume_text, "jd": jd_text})

    print(response)
    return(response)

