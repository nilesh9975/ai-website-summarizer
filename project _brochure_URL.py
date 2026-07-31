import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

MODEL = "gpt-5-nano"

system_prompt = """
You are a snarky assistant that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring navigation text.
Respond in Markdown.
"""

user_prompt_prefix = """
Here are the contents of a website.

Provide a short summary of this website.
If it includes news or announcements, summarize those too.

"""

def fetch_website_contents(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove scripts/styles
    for tag in soup(["script", "style", "noscript"]):
        tag.extract()

    text = soup.get_text(separator="\n", strip=True)

    return text[:15000]   # keep prompt manageable


def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website},
    ]


def summarize(url):
    website = fetch_website_contents(url)

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages_for(website)
    )

    return response.choices[0].message.content


def main():
    url = input("Enter website URL: ")
    print("\nSummarizing...\n")

    summary = summarize(url)
    print(summary)


if __name__ == "__main__":
    main()