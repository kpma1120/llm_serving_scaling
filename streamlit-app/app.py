import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain_openai import ChatOpenAI

# 1. Generate a Summary of the Text
def prediction_pipeline(text):
    print("Inside prediction pipeline")
    text_splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size=1000,
        chunk_overlap=20
    )
    text_chunks = text_splitter.split_text(text)
    print(len(text_chunks))

    # Connect to vLLM server (OpenAI API compatible)
    llm = ChatOpenAI(
        model="Qwen/Qwen2.5-1.5B-Instruct",   # replace with the model you launched via `vllm serve`
        api_key="EMPTY",                      # vLLM does not require a real API key
        base_url="http://localhost:8000/v1"   # change to public IP if vLLM server is running on a remote machine
    )

    docs = [Document(page_content=t) for t in text_chunks]
    chain = load_summarize_chain(llm=llm, chain_type='map_reduce', verbose=True)
    summary = chain.run(docs)
    
    return summary


# Streamlit UI
user_input = st.text_area("Enter Text To summarize")
button = st.button("Generate Summary")
if user_input and button:
    summary = prediction_pipeline(user_input)
    st.write("Summary : ", summary)
