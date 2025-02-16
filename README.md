# Data science tutor Ai

This is a Streamlit application that uses Google's Generative AI to provide answers to data science-related questions. The AI model is configured to act as a helpful data science tutor.

# Features

User-friendly interface to input queries.
Generates detailed answers to data science-related questions.
Politely declines to answer questions outside the scope of data science.
Installation

Clone the repository:

git clone (https://github.com/gokul-19/Data-science-tutor-Ai-)
cd your-repo-name
Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

pip install -r requirements.txt
Usage

Navigate to the directory containing chintu.py:

cd streamlit_tutor_app
Run the Streamlit application:

streamlit run chintu.py
Open your web browser and go to http://localhost:8501 to access the application.

# Configuration

Replace the placeholder API key in chintu.py with your valid Google Generative AI API key:
genai.configure(api_key="YOUR_VALID_API_KEY")
File Structure

Data-Science-Tutor-App/ │ ├── chintu.py # ├── requirements.txt # List of required packages └── venv/ # Virtual environment directory
