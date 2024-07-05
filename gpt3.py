import requests

API_KEY = 'YOUR_OPENAI_API_KEY'
URL = 'https://api.openai.com/v1/engines/davinci-codex/completions'

def get_metadata(text):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    data = {
        'prompt': f"Extract metadata from this text: {text}",
        'max_tokens': 100
    }
    response = requests.post(URL, headers=headers, json=data)
    metadata = response.json()
    return metadata['choices'][0]['text']
