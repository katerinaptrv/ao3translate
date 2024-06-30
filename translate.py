import requests
from bs4 import BeautifulSoup
import textwrap
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.environ.get("GOOGLE_API_KEY")


MAX_TOKENS_PER_REQUEST = 5000

def translate_text(text, language):

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")  

    chunks = [text[i:i+MAX_TOKENS_PER_REQUEST] for i in range(0, len(text), MAX_TOKENS_PER_REQUEST)]
    
    translated_chunks = []
    
    print('Total: '+str(len(chunks)))
    
    context = ""
    
    for chunk in chunks:
        prompt = f'Translate the following text to {language} formatting with paragraphs with spaces between them.You will also reiceive a context of the last 200 characters translate for better understanding of the text to translate.\nContext:{context}\nTEXT:\n\n{chunk}\n\nTranslation:'
        response = llm.invoke(prompt)
        context = response.content
        translated_chunk = response.content
        translated_chunks.append(translated_chunk)
    
    return '\n'.join(translated_chunks)
            


def translate_work(url, language):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    work_text = soup.find('div', {'class': 'userstuff'}).text
    
    return translate_text(work_text, language)
    


