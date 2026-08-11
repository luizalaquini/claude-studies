import os
import anthropic
from dotenv import load_dotenv

load_dotenv(".env.local")

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

models = ["claude-haiku-4-5", "claude-sonnet-4-6", "claude-opus-4-7"]

prompt='What is prompt caching?'

for model in models:
    response = client.messages.create(
        model=model,
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}],
    )
    print(model, response.usage)