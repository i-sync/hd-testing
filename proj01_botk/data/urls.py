"""
urls data helper
"""
import json
import os

def current_url():
    env = os.environ["env"] if "env" in os.environ else "dev"
    with open("proj01_botk/data/urls.json", 'r') as f:
        return json.load(f)[env]
