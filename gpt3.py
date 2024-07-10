import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'

def get_summary(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following text:\n\n{text}",
        max_tokens=150
    )
    
    try:
        summary = response['choices'][0]['text'].strip()
    except KeyError:
        raise ValueError("Unexpected response structure from GPT-3 API")
    
    return summary
