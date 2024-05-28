
# Google PAA Scraper

The Google PAA Scraper is a tool developed in Python and Streamlit that allows users to extract "People Also Ask" (PAA) questions from Google for a set of specified queries. This tool can be particularly useful for SEO projects, helping to create editorial plans, optimize FAQs, and identify related keywords.

## Features

- **Query Input**: Enter up to 20 search queries separated by commas.
- **Language Selection**: Choose the language for the search from Italian, English, French, Spanish, and German.
- **PAA Questions Extraction**: Uses HTTP requests to fetch Google results and BeautifulSoup to parse the HTML and extract related questions.
- **Visualization and Download**: Extracted PAA questions are displayed in a table within the application, with an option to download the data as a CSV file.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/google-paa-scraper.git
   ```
2. Change to the project directory:
   ```bash
   cd google-paa-scraper
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
2. Enter up to 20 search queries, separated by commas, in the text area.
3. Select the language for the search.
4. Click the "Scrape PAA Questions" button to start the extraction process.
5. View the extracted PAA questions in the table displayed in the application.
6. Download the extracted data as a CSV file if needed.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or feedback, please contact **NUR® Digital Marketing** at (info@nur.it)[info@nur.it].
