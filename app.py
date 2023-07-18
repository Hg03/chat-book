import streamlit as st
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import pinecone
import os
from markdownlit import mdlit

st.set_page_config(layout='wide',page_icon='📟',page_title='Chatbook')
mdlit('#Chat - [blue]book[/blue] ✉️ 🔥')

with_or_without = st.selectbox('How do you want your chatbot',['Using your API key','Local Chatbot(without key)'])

if with_or_without is 'Using your API key':
  open_api_key = st.text_input('Enter your API key',type='password')
elif with_or_without is 'Local Chatbot(without key)':
  st.info('No key is required ')
