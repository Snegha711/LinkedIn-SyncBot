import sys
import os
import requests
import json
def post_to_linkedIn(text):
    AUTHOR_URN = os.getenv("LINKEDIN_AUTHOR_URN")
    ACCESS_TOKEN  = os.getenv("ACCESS_LINKEDIN")
    CONTENT=text
    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json"
    }
    payload = {
        "author": AUTHOR_URN,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": CONTENT
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print("Status Code:", response.status_code)
    print("Response:", response.json())


if __name__ == "__main__":
    if len(sys.argv) > 1:
        post_to_linkedIn(sys.argv[1])
    else:
        print("No text provided.")