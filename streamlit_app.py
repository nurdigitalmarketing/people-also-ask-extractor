import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_paa_questions(query, hl='it', num_results=10):
    url = f"https://www.google.com/search?q={query}&hl={hl}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all related questions
    paa_questions = [question.get_text() for question in soup.find_all('div', class_='related-question-pair')][:num_results]
    
    # If not enough questions found, look for additional ones
    if len(paa_questions) < num_results:
        additional_questions = [question.get_text() for question in soup.find_all('div', class_='BVG0Nb')][:num_results - len(paa_questions)]
        paa_questions.extend(additional_questions)
    
    return paa_questions

def capture_paa_questions(header, query, all_questions, hl, num_results):
    questions = get_paa_questions(query, hl, num_results)
    all_questions[header].extend(questions)

def main():
    st.title("Google PAA Scraper")
    
    queries = st.text_area("Enter up to 20 search queries, separated by commas:")
    hl = st.selectbox("Select language for search:", ['it', 'en', 'fr', 'es', 'de'])
    num_results = st.slider("Number of PAA questions to retrieve per query:", min_value=1, max_value=20, value=10)
    
    all_questions = {"People Also Ask questions": []}
    
    if st.button("Scrape PAA Questions"):
        if queries:
            query_list = [q.strip() for q in queries.split(',')[:20]]
            for query in query_list:
                capture_paa_questions("People Also Ask questions", query, all_questions, hl, num_results)
            
            st.success("Scraping complete!")
            
            if all_questions["People Also Ask questions"]:
                df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in all_questions.items()]))
                st.dataframe(df)
                
                csv_filename = "paa_questions.csv"
                st.download_button(label="Download CSV", data=df.to_csv(index=False).encode('utf-8'), file_name=csv_filename, mime='text/csv')
        else:
            st.error("Please enter at least one search query.")

if __name__ == "__main__":
    main()
