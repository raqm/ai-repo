# AI Sentiment Dashboard

Welcome to the **AI Sentiment Dashboard** built with **Streamlit** and powered by the **Hugging Face Transformers** library! This simple web app allows you to input text and analyze the sentiment (positive or negative) of the content in real-time using a pre-trained sentiment analysis model.

## Features
- **Text Input**: Enter any text you'd like to analyze.
- **Sentiment Prediction**: The model predicts if the sentiment of the text is positive or negative.
- **Confidence Score**: Displays the model's confidence level in its prediction.

## 🧑‍💻 Getting Started

### Prerequisites
- **Python 3.7+** (though the environment is set up in GitHub Codespaces automatically).
- **Streamlit**: To run the app and create the interactive interface.
- **Hugging Face Transformers**: The library used to load pre-trained models for sentiment analysis.

### Running Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/raqm/ai-repo.git
   cd ai-repo/ai-sentiment-dashboard
 
2.	Install dependencies:
pip install -r requirements.txt
 
3.	Run the Streamlit app:
streamlit run app.py
 
4.	Open your browser and go to http://localhost:8501 to see the dashboard in action!
Running in GitHub Codespaces
1.	Go to the GitHub repo.
2.	Click on the "Code" button and select "Open with Codespaces".
3.	Codespaces will automatically set up the environment.
4.	In the terminal, run:
streamlit run ai-sentiment-dashboard/app.py
 
5.	Open the Streamlit app by clicking the "Open in Browser" link provided by Codespaces.
