from openai import OpenAI

def AskAlternativeAi(prompt):
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key="SECRET")
    
    resp = client.chat.completions.create(
        model="minimax/minimax-m3.1-flash:free",
        messages=prompt,
    )
    return resp.choices[0].message.content
