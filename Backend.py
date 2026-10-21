from openai import OpenAI

def AskAlternativeAi(prompt):
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key="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")
    
    resp = client.chat.completions.create(
        model="minimax/minimax-m3.1-flash:free",
        messages=prompt,
    )
    return resp.choices[0].message.content
