from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_classifier(X_train, y_train):
    """
    Train a multi-label classifier using Random Forest.
    """
    model = MultiOutputClassifier(RandomForestClassifier(n_estimators=100, random_state=42))
    model.fit(X_train, y_train)
    return model

def save_model(model, vectorizer, class_labels, model_save_path):
    """
    Save the trained model and TF-IDF vectorizer to a file.
    """
    with open(model_save_path, 'wb') as f:
        pickle.dump({'model': model, 'vectorizer': vectorizer, 'class_labels': class_labels}, f)
