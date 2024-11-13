import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analyse_credit_card

def configureInterface():
    st.title("Upload de arquivos DIO - Desafio 2 - Azure - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        fileName = uploaded_file.name
        
        #Enviar para o BLOB

        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url:
            st.write(f"Arquivo {fileName} foi enviado com sucesso para o Azure Blob Storage")
            credit_card_info = analyse_credit_card(blob_url) #Chamar funcao de cartao de credito
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Erro ao enviar o arquivo {fileName} para o Azure Blob Storage")


def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem Enviada!", use_column_width=True)
    st.write("Resultado da validação:")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color: green;'>Cartão Válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do Titular: {credit_card_info['card_name']}")
        st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
        st.write(f"Data de Validade: {credit_card_info['expiry_date']}")
    else:
        st.markdown(f"<h1 style='color: red;'>Cartão Inválido</h1>", unsafe_allow_html=True)
        st.write("Este não é um cartão de crédito válido")


if __name__ == "__main__":
    configureInterface()