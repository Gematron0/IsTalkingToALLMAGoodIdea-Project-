from openai import OpenAI

def ask_openai(prompt):
    client = OpenAI(api_key="SECRET")
    resp = client.chat.completions.create(
        model="gpt-5.5",
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content