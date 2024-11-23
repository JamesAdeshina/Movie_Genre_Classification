import pandas as pd
import os

# def load_and_combine_data(data_folder):
#     dataframes = []
#     for genre_file in os.listdir(data_folder):
#         if genre_file.endswith(".csv"):
#             genre = genre_file.replace(".csv", "")
#             df = pd.read_csv(os.path.join(data_folder, genre_file))
#             df['genre'] = genre  # Add genre label
#             dataframes.append(df)
#     combined_df = pd.concat(dataframes, ignore_index=True)
#     return combined_df

# def preprocess_and_save_data(combined_df, save_path):
#     # Example preprocessing: lowercase, drop NA
#     combined_df['plot'] = combined_df['plot'].str.lower().fillna('')
#     combined_df.to_csv(save_path, index=False)

# if __name__ == "__main__":
#     data_folder = "./data/raw/"
#     save_path = "./data/processed/combined_movies.csv"
#     combined_df = load_and_combine_data(data_folder)
#     preprocess_and_save_data(combined_df, save_path)


# import pandas as pd
# import pandas as pd
# from sklearn.preprocessing import MultiLabelBinarizer
#
# def load_and_preprocess_data(raw_data_path, processed_data_path):
#     """
#     Load the dataset, preprocess the genres, and save processed data.
#     """
#     # Load raw data
#     data = pd.read_csv(raw_data_path)
#
#     # Process genres (convert string to list)
#     data['genres'] = data['genres'].apply(eval)
#
#     # Save processed data
#     data.to_csv(processed_data_path, index=False)
#
#     # Get unique genres
#     mlb = MultiLabelBinarizer()
#     y = mlb.fit_transform(data['genres'])
#     data['genres_binary'] = list(y)
#     return data, mlb.classes_
