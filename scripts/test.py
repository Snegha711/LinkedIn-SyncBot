
import google.generativeai as genai
import json
from datetime import datetime
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


    
    genai.configure(api_key="AIzaSyCU34NtFrX324iZbliAafvoUqOS-ZPnjiY")  
    model = genai.GenerativeModel("gemini-1.5-flash-latest")  
    response = model.generate_content(topic)  

    # Ensure response is structured properly
    if hasattr(response, "text"):
        con = response.text
    elif hasattr(response, "parts") and response.parts:
        con = response.parts[0].text
    else:
        con = ""

    # Clean unwanted characters
    con = con.replace("*", "").replace("/", "").replace("\n", "").replace("\\", "").strip()  

    return con  

print("testing")
topic=get_topic()
print(topic)
prompt = """Generate a high-engagement LinkedIn post (100-150 words) on {topic} so far in a professional yet conversational tone for a junior developer in AI, IT, or software. Start with a bold statement, thought-provoking question, or personal insight to grab attention. Provide concise, valuable insights with actionable takeaways, avoiding generic statements. Ensure a smooth flow without unnecessary spaces. Use emojis naturally to highlight key points and improve readability without overuse. End with a compelling thought that sparks discussion and ask a question to invite comments. Add 4-7 relevant LinkedIn hashtags for maximum reach, ensuring they are popular yet specific"""
print(prompt)
con=generate_script(prompt)
print("*********")
print(con)

