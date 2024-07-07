import requests

API_KEY = 'YOUR_OPENAI_API_KEY'
URL = 'https://api.openai.com/v1/engines/davinci-codex/completions'

def get_metadata_and_summary(text):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    
    # Prompt for metadata extraction
    metadata_prompt = f"Extract metadata from this text: {text}"
    metadata_data = {
        'prompt': metadata_prompt,
        'max_tokens': 100
    }
    metadata_response = requests.post(URL, headers=headers, json=metadata_data)
    metadata = metadata_response.json()['choices'][0]['text']
    
    # Prompt for summarization
    summary_prompt = f"Summarize this text: {text}"
    summary_data = {
        'prompt': summary_prompt,
        'max_tokens': 100
    }
    summary_response = requests.post(URL, headers=headers, json=summary_data)
    summary = summary_response.json()['choices'][0]['text']
    
    return {
        'metadata': metadata,
        'summary': summary
    }
