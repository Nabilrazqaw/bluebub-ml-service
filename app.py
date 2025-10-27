from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)

class RecommendationEngine:
    def __init__(self):
        self.user_profiles = {}
        self.product_features = {}
    
    def calculate_similarity(self, user_interests, product_categories):
        # Calculate similarity between user and products
        # Simple content-based filtering
        interest_vector = np.array([1 if cat in user_interests else 0 for cat in product_categories])
        return interest_vector.mean()
    
    def get_collaborator_recommendations(self, user_profile):
        # Recommend potential collaborators based on interests
        # Simulate ML recommendation
        recommendations = [
            {
                "name": "Dr. Siti Rahayu",
                "specialty": "Marine Biology",
                "match_score": 0.95,
                "common_interests": ["coral reef", "conservation"]
            },
            {
                "name": "PT. Maritim Tech",
                "specialty": "Ocean IoT",
                "match_score": 0.88,
                "common_interests": ["technology", "monitoring"]
            }
        ]
        return recommendations
    
    def predict_business_opportunity(self, location, category):
        # Predict business opportunity score
        # Simulate ML prediction
        base_score = np.random.uniform(0.6, 0.95)
        opportunity = {
            "score": round(base_score, 2),
            "confidence": "high" if base_score > 0.8 else "medium",
            "market_potential": "excellent" if base_score > 0.85 else "good",
            "recommended_actions": [
                "Expand to nearby regions",
                "Partner with local communities",
                "Invest in sustainable practices"
            ]
        }
        return opportunity

# Initialize recommendation engine
rec_engine = RecommendationEngine()

@app.route('/api/ml/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK", "message": "Bluebub ML Service is running"})

@app.route('/api/ml/recommend-collaborators', methods=['POST'])
def recommend_collaborators():
    try:
        data = request.json
        user_profile = data.get('user_profile', {})
        recommendations = rec_engine.get_collaborator_recommendations(user_profile)
        return jsonify({"success": True, "recommendations": recommendations})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/ml/predict-opportunity', methods=['POST'])
def predict_opportunity():
    try:
        data = request.json
        location = data.get('location', 'Indonesia')
        category = data.get('category', 'general')
        prediction = rec_engine.predict_business_opportunity(location, category)
        return jsonify({"success": True, "prediction": prediction})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/ml/analyze-market', methods=['POST'])
def analyze_market():
    try:
        data = request.json
        product_data = data.get('products', [])
        
        # Simulate market analysis
        analysis = {
            "trending_categories": ["Data Riset", "Teknologi"],
            "average_price": 5250000,
            "demand_forecast": "increasing",
            "competition_level": "moderate",
            "recommendations": [
                "Focus on sustainable fishing technology",
                "Collaborate with research institutions",
                "Expand data visualization services"
            ]
        }
        return jsonify({"success": True, "analysis": analysis})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
