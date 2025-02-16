# Data Science Tutor AI

This is a Streamlit application that uses Google's Generative AI to provide answers to data science-related questions. The AI model is configured to act as a helpful data science tutor.

## Features

### User-friendly interface to input queries.
### Generates detailed answers to data science-related questions.
### Politely declines to answer questions outside the scope of data science.

## Installation

Clone the repository:
git clone (https://github.com/gokul-19/Data-science-tutor-Ai-.git)
cd Data-science-tutor-Ai-

Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:
pip install -r requirements.txt

## Usage

Navigate to the project directory:
cd python_code_reviewer

Run the Streamlit application:
streamlit run app.py

Access the application:
Open your web browser and go to http://localhost:8501.

# Configuration

Replace the placeholder API key in app.py with your valid Google Generative AI API key:
import genai

genai.configure(api_key="YOUR_VALID_API_KEY")

# File Structure

Data-Science-Tutor-AI/
│── streamlit-app(Data science tutor Ai).webm  # Web media file
│── task4(Data_science_tutor_AI_).ipynb        # Jupyter Notebook
│── Image.png                                  # Image file
│── README.md                                  # Documentation file
│── app.py                                     # Main Streamlit application


