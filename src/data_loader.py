import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

def load_and_preprocess_data(raw_data_path, processed_data_path):
    """
    Load the dataset, preprocess the genres, and save processed data.
    """
    # Load raw data
    data = pd.read_csv(raw_data_path)

    # Process genres (convert string to list)
    data['genres'] = data['genres'].apply(eval)

    # Save processed data
    data.to_csv(processed_data_path, index=False)

    # Get unique genres
    mlb = MultiLabelBinarizer()
    y = mlb.fit_transform(data['genres'])
    data['genres_binary'] = list(y)
    return data, mlb.classes_
