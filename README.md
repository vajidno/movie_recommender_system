# Movie Recommender System(Content based)

## Overview

Welcome to the Movie Recommender System! This system is designed to provide personalized movie recommendations based on user preferences and content features.

## Features

- **Content-Based Recommendation:** Utilizes the following movie features to recommend similar movies:
  - **Genres**
  - **ID**
  - **Keywords**
  - **Title**
  - **Overview**
  - **Cast**
  - **Crew**

### Data Source

The dataset used in this project is sourced from [TMDB 5000 Movie Dataset on Kaggle].

### Data Preparation

During the data preprocessing stage, handling string data was a significant challenge. The following steps were taken to overcome this challenge:

1. **Conversion to Lists:** String data was converted into lists for more effective processing.
2. **Whitespace Management:** Spaces and other whitespace characters were managed to ensure consistency in the data.
3. **Text Vectorization:** Techniques such as text vectorization were employed to represent text data numerically.
4. **Cosine Similarity:** The cosine distance metric was used to calculate the similarity between textual data, aiding in content-based recommendations.
5. **Stemming:** Porter Stemmer was applied to reduce words to their base form, enhancing the efficiency of text-based algorithms.

After these preprocessing steps, a new column named **Tags** was created, consolidating information for simplified representation.

### Web App and API Integration

The movie recommender system is now accessible through a web app created with Streamlit. The web app allows users to interactively explore movie recommendations and view movie posters fetched through an API.

### File Compression

Due to the large size of the similarity file, it has been compressed using the `gzip` module. The compressed file is named `similarity.pkl.gz`.

**Explore the Movie Recommender System:** [Movie Recommender Web App](https://movierecommendersystem-5zw3bq7qhkeuci4iw2eerv.streamlit.app/)








