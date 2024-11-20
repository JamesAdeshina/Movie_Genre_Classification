import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

def predict_genres(movie_plot, model_save_path):
    """
    Predict genres for a given movie plot using the trained model.
    """
    # Load model and vectorizer
    with open(model_save_path, 'rb') as f:
        model_data = pickle.load(f)

    model = model_data['model']
    vectorizer = model_data['vectorizer']
    class_labels = model_data['class_labels']

    # Transform the movie plot
    X_new = vectorizer.transform([movie_plot])

    # Predict genres
    y_pred = model.predict(X_new)[0]
    predicted_genres = [class_labels[i] for i, pred in enumerate(y_pred) if pred == 1]

    return predicted_genres
