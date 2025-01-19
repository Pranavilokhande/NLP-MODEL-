**Feedback Classification Dashboard**

This repository contains a project for building an interactive feedback classification dashboard using machine learning and natural language processing (NLP) techniques. The dashboard allows users to classify text-based feedback as positive or negative.

**Features**

**Data Preprocessing:**

Handles text cleaning and preprocessing using regular expressions and manual stop words.

Detailed Explanation: This step ensures that the input text is clean and ready for analysis. Regular expressions are used to remove unwanted characters, such as punctuation, numbers, and special symbols. Stop words, which are common words like "and" or "the" that do not contribute significantly to the analysis, are manually defined and removed to improve the model's focus on meaningful words.

**Sentiment Analysis:**

Implements sentiment analysis using TextBlob and a Naive Bayes classifier.

Detailed Explanation: Sentiment analysis determines whether the feedback text conveys a positive, negative, or neutral sentiment. TextBlob provides a simple and effective way to analyze text polarity (positive or negative sentiment) and subjectivity. The Naive Bayes classifier complements this by learning from labeled examples to classify new feedback based on word occurrences and patterns.

**Machine Learning Pipeline:**

Utilizes scikit-learn for feature extraction (CountVectorizer) and model training.

Detailed Explanation: A machine learning pipeline is created using scikit-learn to streamline the processing and classification tasks. The CountVectorizer transforms text into a numeric representation by counting word occurrences, making it suitable for model training. The Naive Bayes algorithm is then trained on this representation to predict the sentiment of new feedback accurately.

**Interactive Dashboard:**

Built with Streamlit for real-time classification and visualization.

Detailed Explanation: The dashboard is a user-friendly interface allowing users to interact with the model in real-time. Users can upload datasets, view processed feedback, and obtain instant sentiment classifications. The Streamlit framework simplifies the creation of interactive web applications, offering dynamic updates and visualizations.

**Technologies Used**

Programming Language: Python

**Libraries:**

pandas for data manipulation

scikit-learn for machine learning

textblob for sentiment analysis

streamlit for dashboard development

re for text preprocessing

**How to Run the Project**

**Clone the Repository:**

git clone https://github.com/your-username/feedback-dashboard.git
cd feedback-dashboard

**Install Dependencies:**
Use the requirements file to install all necessary libraries.

pip install -r requirements.txt

**Run the Streamlit App:**
Launch the dashboard using the following command:

streamlit run feedback_dashboard.py

**Interact with the Dashboard:**
Upload a dataset, analyze feedback, and visualize classification results interactively.

