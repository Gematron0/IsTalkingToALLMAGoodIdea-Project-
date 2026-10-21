from openai import OpenAI

def ask_openai(prompt):
    client = OpenAI(api_key="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")
    resp = client.chat.completions.create(
        model="gpt-5.5",
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content