import requests
from bs4 import BeautifulSoup
from nltk.corpus import wordnet

# Discord webhook URL (replace with your own webhook URL)
discord_webhook_url = "https://discord.com/api/webhooks/1105622424369762378/SwKi8k2q0ErxktEO3-SGNteFXM8gfAVHy5hXNrqTOQx6LaUnX5LOu75CVNSNF1BCSdui"

# Function to check if a word is a valid English word
def is_word(word):
    return wordnet.synsets(word)

# Function to send message to Discord webhook
def send_discord_message(message):
    payload = {
        "content": message
    }
    requests.post(discord_webhook_url, data=payload)

# Function to check available Minecraft usernames
def check_usernames():
    available_usernames = []

    for length in range(3, 6):
        for word in wordnet.words():
            if len(word) == length and not requests.get(f"https://namemc.com/search?q={word}").text:
                available_usernames.append(word)

    if available_usernames:
        message = "Available Minecraft usernames:\n"
        message += "\n".join(available_usernames)
    else:
        message = "No available Minecraft usernames found."

    send_discord_message(message)

# Call the function to check usernames
check_usernames()
