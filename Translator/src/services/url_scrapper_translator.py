import requests
from bs4 import BeautifulSoup
from langchain_openai.chat_models.azure import AzureChatOpenAI
from utils.config import Config

def extract_text_from_url(url):
    #Parei em 7:08
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()
               
        text = soup.get_text(separator=' ')
        #Limpar Texto
        linhas = (line.strip() for line in text.splitlines())
        parts = (phrase.strip() for line in linhas for phrase in line.split(" "))   
        texto_limpo = '\n'.join(part for part in parts if part)
        return texto_limpo
    else:
        print(f"failed to fetch the URL. Status code: {response.status_code}")
        return None
    
def extract_text_from_url_raw(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    return text

client = AzureChatOpenAI(
    azure_endpoint = Config.OAI_ENDPOINT,
    api_key = Config.OAI_KEY,
    api_version = Config.OAI_VERSION,
    deployment_name = Config.OAI_DEPLOYMENT_NAME,
    max_retries = 0
)

def translate_article(text, lang):
    messages = [
        ("system" , "Você atua como tradutor de textos"),
        ("user", f"Traduza o {text} para o idioma {lang}. A resposta deve ser em Markdown e não conter nenhuma informação além do texto traduzido")
    ]
    response = client.invoke(messages)
    print(response.content)
    return response.content