import os
#from dotenv import load_dotenv
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
#from langchain.agents import create_pandas_dataframe_agent
from langchain_experimental.agents import create_pandas_dataframe_agent
import streamlit as st
import json
import pandas as pd
import numpy as np

#client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")



st.title('Analítica de datos con Agentes 🤖🔍')
ke = st.text_input('Ingresa tu Clave')
os.environ['OPENAI_API_KEY'] = ke


uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
   df=pd.read_csv(uploaded_file, on_bad_lines='skip') #on_bad_lines='skip'
   st.write(df)

st.write('Te ayduaré a analizar los datos que cargues.')

user_question = st.text_input("Que desesas saber de los datos?:")
if user_question :
    # user_question=user_question+', una vez resuelto responde siempre en español, si es un número escribe el número no uses letras'
  try:

        #if user_question:
    agent = create_pandas_dataframe_agent(OpenAI(model_name="gpt-4o",temperature=0), df, verbose=True)
    with get_openai_callback() as cb:
        response = agent.run(user_question)
       #print(cb)
      st.write(response)
  except:
    pass    
