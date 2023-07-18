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
mdlit('# Chat - [blue]book[/blue] ✉️ 🔥')

