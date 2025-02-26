
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
    print(f"Topics available: {topics}") 
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

    issue_title = "Approval Required"
    issue_body = f"""## Approval Request
    Content: {text}

    Please approve or reject:

    - ✅ Approve: Comment `/approve`
    - ❌ Not Approve: Comment `/reject`
    """
    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    data = {"title": issue_title, "body": issue_body}

    response = requests.post(url, json=data, headers=headers)
    print(response.json())






print("testing")
topic=get_topic()
print(topic)
prompt = f"""Generate a high-engagement LinkedIn post (100-150 words) on {topic} so far in a professional yet conversational tone for a junior developer in AI, IT, or software. Start with a bold statement, thought-provoking question, or personal insight to grab attention. Provide concise, valuable insights with actionable takeaways, avoiding generic statements. Ensure a smooth flow without unnecessary spaces. Use emojis naturally to highlight key points and improve readability without overuse. End with a compelling thought that sparks discussion and ask a question to invite comments. Add 4-7 relevant LinkedIn hashtags for maximum reach, ensuring they are popular yet specific"""
print(prompt)
text="sample testing"
# con=generate_script(prompt)
# print("*********")
# print(con)
create_issue(text)
print("completed")

