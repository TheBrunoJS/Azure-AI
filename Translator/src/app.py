from services.translator_service import translate_text, translate_document
from services.url_scrapper_translator import extract_text_from_url, translate_article
from docx import Document

target_language = "pt-br"

# Tests from the document and text translate
input_file = "./content/musica.docx"
#translate_document(input_file, target_language)
#print(translate_text("I want to break free", target_language))


# Tests from url translate 
url = "https://dev.to/arindam_1729/9-open-source-libraries-to-supercharge-your-next-project-c71"
text = extract_text_from_url(url)
article = translate_article(text, target_language)

print(article)