"""
urls data helper
"""
import json
import os

def current_url():
    env = os.environ["env"]
    with open("springdemo/data/urls.json", 'r') as f:
        return json.load(f)[env]
