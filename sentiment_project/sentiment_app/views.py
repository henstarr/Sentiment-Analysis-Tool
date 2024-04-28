from django.shortcuts import render
from transformers import pipeline
import re

model_path = "cardiffnlp/twitter-roberta-base-sentiment-latest"
sentiment_task = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)

def home(request):
    word_sentiments = []
    sentiment = None    

    if request.method == 'POST':
        text = request.POST.get('text')
        words = text.split()
        results = sentiment_task(text)

       #print(results)
        
        rege = re.compile("^ +$")
        if rege.search(text) or text == "":
            return render(request, 'home.html', {'sentiment': None, 'word_sentiments': None})

            

        for word in words:
            result = sentiment_task(word)
            sentiment = result[0]['label']
            score = round(result[0]['score'],2)

            word_sentiments.append((word, sentiment, score))

        # Use the sentiment_task pipeline to analyze the text

        # Since the results will be a list of dictionaries like [{'label': 'LABEL', 'score': SCORE}], we can take the first result
        sentiment = results[0]['label']
        score = results[0]['score']  # You can use the score for further customization of your output


        if sentiment == 'negative':  
            sentiment = 'Negative'
        elif sentiment == 'neutral': 
            sentiment = 'Neutral'
        elif sentiment == "positive":
            sentiment = 'Positive'
        else:
            sentiment = None

    return render(request, 'home.html', {'sentiment': sentiment, 'word_sentiments': word_sentiments})

# Create your views here.
