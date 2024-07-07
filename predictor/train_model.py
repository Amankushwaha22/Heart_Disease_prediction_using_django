import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Read the heart disease training data from a CSV file
df = pd.read_csv('static/Heart_train.csv')
data = df.values
X = data[:, :-1]  # Input features (all columns except the last one)
Y = data[:, -1]   # Target variable (last column)

# Create and train a Random Forest Classifier model
rf = RandomForestClassifier(
    n_estimators=16,
    criterion='entropy',
    max_depth=9
)

rf.fit(np.nan_to_num(X), Y)

# Save the model to disk
MODEL_FILE = 'static/heart_disease_rf_model.pkl'
joblib.dump(rf, MODEL_FILE)

print("Model trained and saved to", MODEL_FILE)
