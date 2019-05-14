"""
urls data helper
"""
import json
import os

def current_url():
    env = os.environ["env"]

    with open("touring/data/urls.json", 'r') as f:
        return json.load(f)[env]
