# Multi-Genre Movie Classifier

## Overview
This project aims to classify movies into multiple genres using machine learning techniques. By leveraging metadata (e.g., cast, crew) and textual data (e.g., plot summaries), the system can predict relevant genres for movies with high accuracy. The project demonstrates the use of Natural Language Processing (NLP) techniques such as TF-IDF and embeddings.

## Objectives
- Build a model capable of classifying movies into one or more genres.
- Utilize plot summaries and metadata features like actors and directors for classification.
- Provide insights that can aid businesses in content personalization and market analysis.

## Business Applications
1. **Content Personalization**: Streaming platforms can recommend movies tailored to user preferences.
2. **Market Trends**: Studios can identify popular genres for targeted content creation.
3. **Search Optimization**: Improved discovery features for movie databases.

## Dataset
We use the **IMDb Movies Dataset**, which contains:
- Plot summaries
- Genre labels
- Additional metadata like cast and directors

## Project Structure
```
movie-genre-classifier/
├── data/
│   ├── raw/                # Raw IMDb dataset
│   ├── processed/          # Preprocessed data
│   └── test/               # Test data for predictions
├── notebooks/
│   ├── exploratory_analysis.ipynb  # Exploratory Data Analysis (EDA)
│   └── model_experiments.ipynb     # Model training and evaluation experiments
├── src/
│   ├── __init__.py
│   ├── data_loader.py      # For loading and preprocessing data
│   ├── feature_engineer.py # TF-IDF or embeddings implementation
│   ├── train_model.py      # Training the classifier
│   ├── predict.py          # For predicting genres of new movies
│   └── utils.py            # Helper functions (e.g., evaluation metrics)
├── models/
│   └── saved_model.pkl     # Trained model file
├── README.md               # Project description
├── requirements.txt        # Dependencies (e.g., spaCy, scikit-learn, numpy)
├── setup.py                # Installation script
└── tests/
    ├── test_data_loader.py
    ├── test_feature_engineer.py
    └── test_train_model.py
```
