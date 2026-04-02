# spam-detector-app

A machine learning web application that classifies SMS messages as Spam or Not Spam using 
natural language processing.

Try it here:
https://spam-detector-app-v1.streamlit.app

- The model is trained on a dataset of SMS messages
- Text is converted into numerical features using TF-IDF (Term Frequency–Inverse Document Frequency)
- A machine learning model predicts whether a message is spam or not

Technologies used:
	•	Python
	•	scikit-learn
	•	Streamlit
	•	Pandas

Features
	•	Enter any message and get instant spam classification
	•	Displays prediction result (Spam / Not Spam)
	•	Shows model confidence score
	•	Simple and interactive web interface

File structure:
spam-detector-app/
│── app.py
│── spam.csv
│── requirements.txt
│── README.md

Installation (Run Locally)
	1.	Clone the repository
	2.	Install dependencies:
pip install -r requirements.txt
streamlit run app.py

Performance: 
	•	Accuracy: ~97% (depending on dataset split)
	•	Model: Logistic Regression
	•	Feature Extraction: TF-IDF

What I Learned
	•	How to clean and process real-world datasets
	•	How to train and evaluate a machine learning model
	•	How to convert text into numerical features
	•	How to deploy a web app using Streamlit

Future Improvements
	•	Improve model accuracy with advanced NLP models
	•	Add support for email or social media messages
	•	Enhance UI/UX design
	•	Add user authentication
  

  
