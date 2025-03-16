import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture
from scipy.cluster.hierarchy import linkage, fcluster

# Sample data (Replace with actual dataset)
data = pd.DataFrame({
    'age': np.random.randint(18, 60, 100),
    'lifestyle': np.random.choice([0, 1], 100),  # 0 = sedentary, 1 = active
    'medical_history': np.random.choice([0, 1], 100),  # 0 = no issue, 1 = has condition
    'symptoms': np.random.choice([0, 1], 100)  # 0 = no symptoms, 1 = symptoms present
})

# Standardizing the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Hierarchical Clustering
linkage_matrix = linkage(scaled_data, method='ward')
clusters = fcluster(linkage_matrix, t=3, criterion='maxclust')

# Gaussian Mixture Model (GMM)
gmm = GaussianMixture(n_components=3, random_state=42)
gmm.fit(scaled_data)

def process_input(user_input):
    """
    Processes user input and predicts a health cluster.
    """
    try:
        # Handling different cases for lifestyle, medical history, and symptoms
        lifestyle_map = {'active': 1, 'moderate': 1, 'sedentary': 0}
        medical_map = {'none': 0, 'yes': 1, 'no': 0}
        symptoms_map = {'none': 0, 'yes': 1, 'no': 0}

        input_data = np.array([
            user_input['age'],
            lifestyle_map.get(user_input['lifestyle'].lower(), 0),
            medical_map.get(user_input['medical_history'].lower(), 0),
            symptoms_map.get(user_input['symptoms'].lower(), 0)
        ]).reshape(1, -1)

        # Standardizing input data
        input_scaled = scaler.transform(input_data)
        cluster = gmm.predict(input_scaled)[0]

        health_suggestions = {
            0: "Maintain a balanced diet and regular checkups.",
            1: "Increase physical activity and monitor blood sugar levels.",
            2: "Regular screenings and mental wellness exercises are recommended."
        }

        return health_suggestions[cluster], f"Cluster {cluster} Analysis: {health_suggestions[cluster]}"

    except Exception as e:
        return "Error processing input", f"An error occurred: {str(e)}"
