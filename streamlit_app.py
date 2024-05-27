# File: streamlit_paa_extractor.py

import streamlit as st
from bs4 import BeautifulSoup
import requests
import re

def extract_paa(question, num_results=5):
    """
    Funzione per estrarre i risultati 'People Also Ask' da Google.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    query = question.replace(' ', '+')
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Estrarre le domande e le risposte
    questions = []
    answers = []
    for result in soup.find_all('div', class_='related-question-pair', limit=num_results):
        q = result.find('span', class_='match-mod-horizontal-padding').get_text()
        questions.append(q)
        a = result.find('div', class_='s').get_text()
        answers.append(a)
    
    return list(zip(questions, answers))

def main():
    st.title("People Also Ask Extractor")
    
    question = st.text_input("Enter your question:")
    num_results = st.slider("Number of results:", 1, 10, 5)
    
    if st.button("Extract"):
        if question:
            results = extract_paa(question, num_results)
            st.write("### Results:")
            for i, (q, a) in enumerate(results, 1):
                st.write(f"**Q{i}:** {q}")
                st.write(f"**A{i}:** {a}")
        else:
            st.error("Please enter a question.")

if __name__ == "__main__":
    main()
