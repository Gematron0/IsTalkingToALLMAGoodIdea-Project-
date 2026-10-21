from openai import OpenAI

def AskOpenAI(prompt):
    client = OpenAI(api_key="SECRET")
    resp = client.chat.completions.create(
        model="gpt-5.5",
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content

def AskAlternativeAi(prompt):
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key="SECRET")
    
    resp = client.chat.completions.create(
        model="openrouter/free",
        messages=prompt,
    )
    return resp.choices[0].message.content
