import jwt
import streamlit as st
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import pandas as pd
import csv
import re



payload = {
 "username": st.text_input(""),
 "role": "user",
 
}

st.subheader("This is your secret key")
token1 = jwt.encode(payload, 'AID', algorithm='HS256')
x = jwt.decode(token1, 'AID', algorithms=['HS256'])
st.write(token1)
st.write("You are authorized to use the app")
st.write("Role:", payload['role'])

st.divider()



max_attempts = 7

if 'text_entry_count' not in st.session_state:
    st.session_state['text_entry_count'] = 0


qa = pipeline("table-question-answering", model="microsoft/tapex-large-finetuned-wtq")

import json

csv = st.file_uploader("Choose a file")
from json import loads, dumps

if csv is not None:
    df = pd.read_csv(csv)
   
    
    



if token1:
    st.session_state['text_entry_count'] += 1

if st.session_state['text_entry_count'] > max_attempts:
    st.error(f"You have uploaded a file {max_attempts} times. You have exceeded the number of requests.")
    st.stop()
else:
    st.write(f"Text entry count: {st.session_state['text_entry_count']}")
    



def clear_question():
    st.session_state["question"] = ""

question = st.text_input("Ask a question:", key="question")    
st.button("Clear question", on_click=clear_question)




if st.button("Get Answer"):
    input_data = [{"table": df, "query": question}]
    answer = qa(input_data)
    st.json(answer)
   
    
