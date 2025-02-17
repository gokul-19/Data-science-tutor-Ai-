# Data Science Tutor (AI) - README
Welcome to the Data Science Tutor (AI) application! This tool is designed to assist users with data science-related queries using a conversational AI model. Below, you'll find instructions on how to set up and use the application.

## Overview
This application leverages Streamlit for the user interface and Google's Generative AI for generating responses to user queries. The AI model is configured to respond only to data science-related questions, ensuring focused and relevant interactions.

## Features
- *Interactive User Interface:* Built with Streamlit, providing a simple and intuitive way to interact with the AI.
- *Data Science Focus:* The AI is specifically tuned to handle data science queries, making it a valuable tool for learners and professionals alike.
- *Real-time Response Generation:* Get instant answers to your questions with the click of a button.

## Prerequisites
Before running the application, ensure you have the following:

- Python 3.7 or later installed on your machine.
- An API key from Google Generative AI. You can obtain this by signing up for access to Google's AI services.

## Installation
### 1. Clone the Repository:
```ruby
git clone <repository-url>
cd <repository-directory>
```

### 2.Install Required Packages:
Make sure you have streamlit and google-generativeai installed. You can install them using pip:
```ruby
pip install streamlit google-generativeai
```

### 3. Configure API Key:
Replace "YOUR_GOOGLE_API_KEY" in the code with your actual Google API key.

## Usage
### 1. Run the Application:
Start the Streamlit server by running the following command in your terminal:
```ruby
streamlit run <script-name>.py
```
Replace <script-name>.py with the name of the Python file containing the code

### 2. Interact with the AI:

Open your web browser and navigate to the local URL provided by Streamlit *(usually http://localhost:8501)*.
Enter your data science-related query in the text input field.
Click the "Generate Response" button to receive an AI-generated answer.

## System Prompt
The AI model is initialized with a system prompt that instructs it to act as a helpful data science tutor. It is programmed to handle only data science-related queries and will politely redirect users if they ask unrelated questions.

## Contributing
Contributions to improve the application are welcome! Feel free to fork the repository and submit pull requests with enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For any questions or feedback, please contact [Your Name] at [Your Email].

# Enjoy your journey into data science with the help of AI!

