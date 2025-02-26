
import google.generativeai as genai
import json
from datetime import datetime
import requests
import os
def get_topic():
    with open('files/topics.json', 'r') as file:
        topics = json.load(file)
    today = datetime.today().day
    print(f"Today's date (day): {today}")
    topic = topics.get(str(today))
    if topic is None:
        print("No topic found for today!")
        exit(1)        
    print(f"Selected topic: {topic}")
    return  topic
def generate_script(topic):  
    token = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=token)  
    model = genai.GenerativeModel("gemini-1.5-flash-latest")  
    response = model.generate_content(topic)  
    if hasattr(response, "text"):
        con = response.text
    elif hasattr(response, "parts") and response.parts:
        con = response.parts[0].text
    else:
        con = ""
    con = con.replace("*", "").replace("/", "").replace("\n", "").replace("\\", "").strip()  
    return con  


def create_issue(text):
    repo = "Snegha711/LinkedIn-SyncBot"  
    token = os.getenv("ACCESS_GITHUB")

    issue_title = "Approve content for LinkedIn post"
    issue_body = f"""## Approval Request
    Content: [{text}]

    Please approve or reject:

    - ✅ Approve: Comment `/approve`
    - ❌ Not Approve: Comment `/reject`
    """
    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    data = {"title": issue_title, "body": issue_body}

    response = requests.post(url, json=data, headers=headers)
    print(response.json())






topic=get_topic()
prompt = f"""
Generate a high-engagement LinkedIn post (100-150 words) on {topic} with the following structure:

🔹 **Hook (1-2 lines):**

- Start with a bold statement, thought-provoking question, or personal insight.
- Ensure it's concise and attention-grabbing.

🔹 **Main Content (3-5 short paragraphs, spaced apart):**

- Provide insights with short, punchy sentences.
- Use line breaks between sentences for readability.
- Keep it valuable and actionable—avoid generic statements.
- Include bullet points or emojis to emphasize key takeaways.

🔹 **Call to Action (1-2 lines):**

- End with a compelling thought or question to invite engagement.
- Encourage readers to comment and share their opinions.

✅ **Format for LinkedIn readability:**

- Short paragraphs with spaces.
- Bullet points & emojis for visual appeal.
- Engaging CTA to boost interaction.

🔹 **Include 4-7 relevant LinkedIn hashtags for maximum reach.**
"""  
content=generate_script(prompt)
create_issue(content)

