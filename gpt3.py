import requests

API_KEY = 'YOUR_OPENAI_API_KEY'
URL = 'https://api.openai.com/v1/engines/davinci-codex/completions'

def get_summary(text):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    summary_prompt = f"Summarize this text: {text}"
    summary_data = {
        'prompt': summary_prompt,
        'max_tokens': 100
    }
    summary_response = requests.post(URL, headers=headers, json=summary_data)
    summary = summary_response.json()['choices'][0]['text']
    return summary
