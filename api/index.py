from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app import app, rec_engine

# Export for Vercel
application = app

if __name__ == '__main__':
    app.run()
