# Spam Email Classifier&#x20;

##### **Project Type:** Classification

##### **Industry:** Codec Technologies 

##### **Contribution:** Individual

##### **Name:** Ayesha Nikhat

## 1. Project Overview

The **Spam Email Classifier** is a Machine Learning project that predicts whether an email is **Spam** or **Ham (Not Spam)**. It uses Natural Language Processing (NLP) techniques to process email text and a Multinomial Naive Bayes algorithm to classify messages.

The project includes data exploration, text vectorization, model training and evaluation, a terminal-based prediction program, and an interactive web application built using Streamlit.

**GitHub Link:** 

## 2. Project Objectives

- Develop a Machine Learning model to classify emails as Spam or Ham.
- Explore and analyze a labelled email dataset.
- Convert email text into numerical features using TF-IDF.
- Train and evaluate a classification model.
- Build a user-friendly interface for predicting email categories.

## 3. Dataset Description

The project uses a labelled email dataset containing **5,171 email records**.

- **Ham emails:** 3,672
- **Spam emails:** 1,499
- **Missing values:** None found during initial exploration.
- **Target variable:** Email label, represented as Ham = 0 and Spam = 1.

Pandas is used to load and explore the dataset, including its structure, class distribution, missing values, and duplicate records.

## 4. Technologies and Libraries Used

| Technology              | Purpose                                            |
| ----------------------- | -------------------------------------------------- |
| Python                  | Main programming language                          |
| Pandas                  | Data loading and exploration                       |
| Scikit-learn            | Feature extraction, model training, and evaluation |
| TF-IDF                  | Converts email text into numerical features        |
| Multinomial Naive Bayes | Classifies emails as Spam or Ham                   |
| Streamlit               | Creates the interactive web application            |
| Joblib                  | Saves and loads the trained model and vectorizer   |

## 5. Project Workflow

1. **Data Exploration:** Load the dataset and examine its structure and quality.
2. **Text Vectorization:** Use TF-IDF to convert email text into numerical features, with a maximum of 5,000 features.
3. **Train-Test Split:** Divide the dataset into 80% training data and 20% testing data.
4. **Model Training:** Train a Multinomial Naive Bayes classifier.
5. **Model Evaluation:** Evaluate the model using accuracy, precision, recall, F1-score, and a confusion matrix.
6. **Model Saving:** Save the trained model and TF-IDF vectorizer for reuse.
7. **Prediction:** Classify new email messages using the Python script or Streamlit web application.

## 6. Model Performance

The model achieved approximately **95.27% test accuracy** on the evaluated test split.

| Evaluation Metric | Result |
| ----------------- | -----: |
| Accuracy          | 95.27% |
| Ham Precision     |    97% |
| Ham Recall        |    96% |
| Ham F1-score      |    97% |
| Spam Precision    |    90% |
| Spam Recall       |    94% |
| Spam F1-score     |    92% |

These results represent performance on the evaluated dataset. Actual predictions may vary when the model encounters new email messages.

## 7. Key Features

- Classifies email messages as Spam or Ham.
- Provides terminal-based email predictions.
- Includes an interactive Streamlit web interface.
- Displays prediction results clearly.
- Reuses saved model files without retraining for every prediction.
- Applies Machine Learning rather than relying on manually defined keyword rules.

## 8. Project Structure

```text
Spam Email Classifier/
├── data/
│   └── spam_ham_dataset.csv
├── models/
│   ├── spam_model.pkl
│   └── tfidf_vectorizer.pkl
├── app.py
├── predict.py
├── train_model.py
├── data_exploration.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 9. Installation and Execution

**Step 1: Install the required libraries**

```bash
pip install -r requirements.txt
```

**Step 2: Run the terminal classifier**

```bash
python predict.py
```

Enter an email message when prompted to receive a Spam or Ham prediction. Type `exit` to stop the program.

**Step 3: Launch the Streamlit application**

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal to use the web application.

**Note:** The saved model and vectorizer files must be present in the `models/` directory. If they have not been generated, run `python train_model.py` first.

## 10. Limitations and Future Enhancements

### Limitations

- The model may misclassify unfamiliar or ambiguous email messages.
- Performance depends on the quality and representativeness of the dataset.
- The classifier analyzes email text but does not independently verify links, attachments, or sender identity.
- The model does not guarantee perfect predictions.

### Future Enhancements

- Improve text preprocessing and feature engineering.
- Evaluate additional Machine Learning algorithms.
- Test the model on a wider variety of emails.
- Add more detailed evaluation visualizations.
- Deploy the application online for broader access.

## 11. Conclusion

The Spam Email Classifier demonstrates how Machine Learning and Natural Language Processing can be used to automate email classification. By combining TF-IDF vectorization, Multinomial Naive Bayes, and Streamlit, the project provides a practical example of building, evaluating, and using a text classification model.

## Streamlit Web Application
Displays the interactive interface used to enter email text and view prediction results.
### 1. Ham Email Prediction
![Ham Email Prediction](https://github.com/ayeshanikhat12/Spam-Email-Classifier/blob/cdce3a209b78e939e5ef63590630d74e8964d709/ham.png)

### 2. Spam Email Prediction
![Spam Output](https://github.com/ayeshanikhat12/Spam-Email-Classifier/blob/b3bc1da2ff41b32a32b9ee69f74a307f80bba6a4/spam.png)


## 👩‍💻 Author

**Ayesha Nikhat**

- GitHub: https://github.com/ayeshanikhat12
- LinkedIn: https://www.linkedin.com/in/ayesha-nikhat-12a4aa305/
