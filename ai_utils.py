import openai 
from openai import OpenAI
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_ats_score(resume_text, job_desc):
    documents = [resume_text.lower(), job_desc.lower()]
    vectorizer = CountVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()

    cosine_sim = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
    return round(cosine_sim * 100, 2)  # Return as a percentage

openai.api_key = "your api key "

def generate_cover_letter(job_desc, resume_text):
    prompt = f"""You are an expert career coach. Given the job description and resume below, write a personalized cover letter:\n\n
    Job Description:\n{job_desc}\n\nResume:\n{resume_text}\n\nCover Letter:"""
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']


def generate_resume_summary(resume_text, job_desc):
    prompt = f"Given the following resume:\n{resume_text}\n\nAnd this job description:\n{job_desc}\n\nGenerate a summary matching the resume to the job."
    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
