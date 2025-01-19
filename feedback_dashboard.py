import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Adding custom phrases with negative sentiment to improve accuracy
custom_words = {
    "encountered a bug": -2.5,
    "froze the dashboard": -2.5,
    "wasn't very informative": -2.0,
    "not helpful": -2.5,
    "needs improvement": -2.0,
    "could use improvement": -2.0
}
analyzer.lexicon.update(custom_words)

# Post-processing function to detect specific negative phrases
def adjust_sentiment(comment, initial_sentiment, color):
    negative_phrases = ["encountered a bug", "froze the dashboard", "crashed", "doesn't work", "not working", "issue"]
    if any(phrase in comment.lower() for phrase in negative_phrases):
        return 'Negative', 'red'
    return initial_sentiment, color

# Function to classify a single comment using adjusted VADER and post-processing
def classify_comment(comment):
    scores = analyzer.polarity_scores(comment)
    compound_score = scores['compound']
    
    # Initial classification based on compound score
    if compound_score >= 0.1:
        initial_sentiment = 'Positive'
        color = 'green'
    elif compound_score <= -0.1:
        initial_sentiment = 'Negative'
        color = 'red'
    else:
        initial_sentiment = 'Neutral'
        color = 'yellow'
    
    # Adjust sentiment based on specific phrases
    sentiment, adjusted_color = adjust_sentiment(comment, initial_sentiment, color)
    return sentiment, adjusted_color

# Streamlit app setup
st.title("Enhanced Comment Sentiment Analysis")
st.write("Enter a comment or multiple comments (each on a new line) to determine if they’re positive, negative, or neutral.")

# Input box for user to enter one or multiple comments
user_comments = st.text_area("Type your comment(s) here (one per line):")

# Initialize counters for sentiment categories
sentiments = {"Positive": 0, "Negative": 0, "Neutral": 0}

# Process comments if any are entered
if user_comments:
    comments = user_comments.splitlines()  # Split input into individual comments
    results = []
    
    for comment in comments:
        sentiment, color = classify_comment(comment)
        sentiments[sentiment] += 1
        results.append({"Comment": comment, "Sentiment": sentiment})
        
        # Display each comment's sentiment with appropriate color
        if color == 'green':
            st.success(f"Sentiment: {sentiment} - {comment}")
        elif color == 'red':
            st.error(f"Sentiment: {sentiment} - {comment}")
        elif color == 'yellow':
            st.warning(f"Sentiment: {sentiment} - {comment}")

    # Display overall sentiment summary in a DataFrame
    df = pd.DataFrame(results)
    st.write("### Sentiment Analysis Summary")
    st.dataframe(df)

    # Display a bar chart of sentiment distribution
    st.write("### Sentiment Distribution Chart")
    fig, ax = plt.subplots()
    ax.bar(sentiments.keys(), sentiments.values(), color=['green', 'red', 'yellow'])
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Number of Comments")
    ax.set_title("Sentiment Distribution of Comments")
    st.pyplot(fig)

    # Optionally display a pie chart of sentiment distribution
    st.write("### Sentiment Distribution Pie Chart")
    fig, ax = plt.subplots()
    ax.pie(sentiments.values(), labels=sentiments.keys(), autopct='%1.1f%%', colors=['green', 'red', 'yellow'])
    ax.set_title("Sentiment Distribution of Comments")
    st.pyplot(fig)
