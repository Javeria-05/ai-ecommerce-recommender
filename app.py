import pandas as pd
import joblib
import gradio as gr
from sklearn.metrics.pairwise import cosine_similarity


# Load files
data = pd.read_pickle(
    "../E-commerce_recommendation_system/myApp/dataset/data.pkl"
)

preprocessor = joblib.load(
    "../E-commerce_recommendation_system/myApp/models/preprocessor.joblib"
)

kmeans = joblib.load(
    "../E-commerce_recommendation_system/myApp/models/kmeans_model.joblib"
)


# Create feature matrix
feature_matrix = preprocessor.fit_transform(data)

# Similarity
cosine_sim = cosine_similarity(
    feature_matrix,
    feature_matrix
)


def recommend(product_name):

    search_results = data[
        data['Title'].str.contains(
            product_name,
            case=False,
            na=False
        )
    ]

    if search_results.empty:
        return "No products found."

    cluster_label = kmeans.labels_[
        search_results.index[0]
    ]

    cluster_indices = [
        i for i, label in enumerate(kmeans.labels_)
        if label == cluster_label
    ]

    sim_scores = [
        (i, cosine_sim[search_results.index[0]][i])
        for i in cluster_indices
    ]

    sim_scores = sorted(
        sim_scores,
        key=lambda x: x[1],
        reverse=True
    )[:5]

    result = ""

    for item in sim_scores:

        idx = item[0]

        result += f"""
Product: {data.iloc[idx]['Title']}
Category: {data.iloc[idx]['Category']}
Price: ${data.iloc[idx]['Price']}

"""

    return result


demo = gr.Interface(
    fn=recommend,
    inputs="text",
    outputs="text",
    title="AI Ecommerce Recommendation System"
)

demo.launch()