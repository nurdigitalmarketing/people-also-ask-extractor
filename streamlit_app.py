import streamlit as st
import requests
from bs4 import BeautifulSoup

# Funzione per estrarre le domande "People Also Ask"
def extract_questions(query):
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        questions = []
        for question in soup.select('.related-question-pair .BVG0Nb'):
            questions.append(question.get_text())
        return questions
    else:
        return ["Error: Unable to fetch questions. Please try again later."]

# Funzione principale per l'app Streamlit
def main():
    st.title("People Also Ask Extractor")
    
    query = st.text_input("Enter your query:")
    
    if st.button("Extract"):
        if query:
            questions = extract_questions(query)
            st.write("Extracted Questions:")
            for question in questions:
                st.write(question)
        else:
            st.write("Please enter a query.")

if __name__ == "__main__":
    main()
