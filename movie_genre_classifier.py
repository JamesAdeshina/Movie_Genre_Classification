from src.data_loader import load_and_preprocess_data
from src.feature_engineer import generate_features
from src.train_model import train_classifier, save_model
from src.predict import predict_genres
import os


# Main execution script
def main():
    # Paths
    raw_data_path = os.path.join("data", "raw", "movies.csv")
    processed_data_path = os.path.join("data", "processed", "processed_data.csv")
    model_save_path = os.path.join("models", "saved_model.pkl")

    # Step 1: Load and preprocess data
    print("Loading and preprocessing data...")
    data, class_labels = load_and_preprocess_data(raw_data_path, processed_data_path)

    # Step 2: Generate features
    print("Generating features...")
    X_train, X_test, y_train, y_test, vectorizer = generate_features(data)

    # Step 3: Train the model
    print("Training the model...")
    model = train_classifier(X_train, y_train)

    # Step 4: Save the trained model
    print("Saving the trained model...")
    save_model(model, vectorizer, class_labels, model_save_path)

    # Step 5: Predict genres for test data
    print("Predicting genres for test data...")
    test_movie = "A thrilling story of survival in space with deep human emotions."
    predictions = predict_genres(test_movie, model_save_path)
    print(f"Predicted genres for test movie: {predictions}")


if __name__ == "__main__":
    main()
