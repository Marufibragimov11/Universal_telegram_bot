import openai

KEY = "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"

openai.api_key = KEY


def generate_response(text):
    response = openai.Completion.create(
        prompt=text,
        engine='gpt-3.5-turbo',
        max_tokens=500,
        temperature=0.5,
        n=1,
        stop=None,
        timeout=15
    )

    if response:
        return response.choices[0].text.strip()
    else:
        return None


res = generate_response('Can you please write me a text in past continious')
print(res)
