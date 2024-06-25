# PubMed Article Summarizer

This Flask web application summarizes PubMed articles using natural language processing techniques. It allows users to input text directly or upload PDF/TXT files, and generates both brief and detailed summaries.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Features

- Summarize articles from text input or file upload (PDF/TXT)
- Generate brief (50-70 words) or detailed (150 words) summaries
- Display word count for original article and summary
- Export summary as PDF
- Responsive web design

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository:
git clone https://github.com/MK61395/PubMed-Article-Summarizer.git
cd PubMed-Article-Summarizer

2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

3. Install the required packages:
pip install -r requirements.txt

## Usage

1. Run the Flask application:
python app.py

2. Open a web browser and navigate to `http://127.0.0.1:5000/`

3. Enter text or upload a PDF/TXT file, choose the summary type, and click "Summarize"

4. View the original article and its summary, along with word counts

5. Optionally, export the result as a PDF

## Project Structure

- `app.py`: Main Flask application file
- `templates/index.html`: HTML template for the web interface
- `preprocessing.ipynb`: Jupyter notebook for dataset preprocessing
- `requirements.txt`: List of Python dependencies

## How It Works

1. **Data Preprocessing**: The `preprocessing.ipynb` notebook demonstrates how to preprocess the PubMed dataset:
- Load the dataset using the `datasets` library
- Preprocess the text by tokenizing, removing stopwords, and cleaning special characters
- Save the preprocessed dataset for later use

2. **Web Application**: The Flask app (`app.py`) handles the main functionality:
- Accepts user input (text or file upload)
- Summarizes the text using the LSA (Latent Semantic Analysis) algorithm
- Renders the results using the HTML template
- Allows exporting the summary as a PDF

3. **User Interface**: The `index.html` file provides a responsive web interface for easy interaction with the summarizer.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
