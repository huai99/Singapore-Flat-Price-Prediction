import mlflow.sklearn

def load_model():
    return mlflow.sklearn.load_model('sk_models_2')