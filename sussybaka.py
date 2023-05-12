import requests
import json

def check_tiktok_username(username):
    url = f"https://www.tiktok.com/@{username}"
    response = requests.get(url)
    return response.status_code == 404

def send_to_discord_webhook(webhook_url, username):
    data = {
        "content": f"Available TikTok username: {username}"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    if response.status_code != 204:
        print(f"Failed to send webhook for username: {username}")

def generate_usernames(webhook_url):
    with open("english_words.txt", "r") as file:
        english_words = [word.strip() for word in file.readlines() if 2 <= len(word.strip()) <= 6]

    for word in english_words:
        if check_tiktok_username(word):
            send_to_discord_webhook(webhook_url, word)

if __name__ == "__main__":
    webhook_url = "https://discord.com/api/webhooks/1105622424369762378/SwKi8k2q0ErxktEO3-SGNteFXM8gfAVHy5hXNrqTOQx6LaUnX5LOu75CVNSNF1BCSdui"
    generate_usernames(webhook_url)
