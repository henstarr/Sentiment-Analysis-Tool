# Sentiment Analysis Web Application

This project is a web-based sentiment analysis tool developed with Django. It analyzes text input by the user to determine the sentiment behind the text (positive, neutral, or negative).

## Features

- User-friendly web interface for submitting text.
- Real-time sentiment analysis display.
- Visual feedback for sentiment intensity.

## Technologies Used

- **Django**: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **Bootstrap**: For responsive UI design.
- **html/css: For styling and creating static UI.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What you need to install the software:

- Python 3.8 or higher
- pip
- Virtualenv (recommended)

### Installing

A step-by-step series of examples that tell you how to get a development env running:

1. Clone the repository:
   
   ```
   git clone https://github.com/yourusername/sentiment-analysis-webapp.git
   ```
3. Create virtual environment
    ```
    cd sentiment_project
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
    ```
Now, visit http://127.0.0.1:8000/ in your web browser to see the application in action.

### Acknowledgments
- CardiffNLP for their roBERTa NLP model: https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest


