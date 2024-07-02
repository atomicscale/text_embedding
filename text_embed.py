import os
import openai
from scipy.spatial import distance
import plotly.express as px
from sklearn.cluster import KMeans
from umap import UMAP
openai.api_key = "your_api_key"
def get_embedding(text_to_embed):
	# Embed a line of text
	response = openai.Embedding.create(
    	model= "text-embedding-ada-002",
    	input=[text_to_embed]
	)
	# Extract the AI output embedding as a list of floats
	embedding = response["data"][0]["embedding"]
    
	return embeddin

import pandas as pd
data_URL =  "https://raw.githubusercontent.com/keitazoumana/Experimentation-Data/main/Musical_instruments_reviews.csv"

review_df = pd.read_csv(data_URL)
review_df.head()
review_df = review_df[['reviewText']]
print("Data shape: {}".format(review_df.shape))
review_df = review_df.sample(100)
review_df["embedding"] = review_df["reviewText"].astype(str).apply(get_embedding)

# Make the index start from 0
review_df.reset_index(drop=True)

review_df.head(10)

