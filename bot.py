import requests
import os
import random

print("Bot started...")

# 🔐 LOAD ENV VARIABLES (FROM GITHUB SECRETS)
PAGE_ID = os.getenv("1986918968603740")
ACCESS_TOKEN = os.getenv("EAAS5LP7cptUBRQZAUbPsIyrAzpy8ykI5Q9FH16kAbmfzxNBusHUTleIQKztOV46J9A2OptCmKfOjoMvjgQqdXvfGeX6yqd6ptQ7IQEz8o4zZCVPO17piDd7hYvCUuwe2YLtVVGT1TvMrcZBZB1Y6ZA7SDl2Ji4ZATZAqYv9kIG51NLfxMTe8sJdIl7gHQA0DZBcmggMsylzIKP8H1fHuva5nQD8mudoDZCYoG4jT5PWtqmBQwvPmA02aEsag09cowkLZC3kTPBOP9zaJKNXBeqrob0kCG5DVsHXwZDZD")
PEXELS_API = os.getenv("XfGAoRzMzcQirEDA8U7HMseboDQKHiCc9UfqJctLu9rxMD2KJLYWGPA1")

# 🔍 DEBUG (IMPORTANT)
print("PAGE_ID:", "OK" if PAGE_ID else "MISSING")
print("TOKEN:", "OK" if ACCESS_TOKEN else "MISSING")
print("PEXELS:", "OK" if PEXELS_API else "MISSING")

# ❌ STOP IF MISSING
if not PAGE_ID or not ACCESS_TOKEN or not PEXELS_API:
    print("Missing environment variables!")
    exit()

# 🌿 GET IMAGE FROM PEXELS
def get_image():
    url = "https://api.pexels.com/v1/search?query=sri lanka nature&per_page=10"
    headers = {"Authorization": PEXELS_API}

    res = requests.get(url, headers=headers)
    data = res.json()

    photos = data.get("photos", [])
    if not photos:
        return None

    return random.choice(photos)["src"]["original"]

# ✍️ CAPTION GENERATOR
def get_caption():
    captions = [
        "🌿 Beautiful Sri Lanka Nature 🇱🇰",
        "🏝️ Paradise on Earth 🌅",
        "🌄 Pure natural beauty of Sri Lanka 🍃",
        "🌊 Calm and peaceful nature vibes 🌴",
        "🌺 Explore Sri Lanka beauty 🇱🇰"
    ]
    return random.choice(captions)

# 📤 POST TO FACEBOOK
def post_to_facebook(image_url, caption):
    url = f"https://graph.facebook.com/{PAGE_ID}/photos"

    payload = {
        "url": image_url,
        "caption": caption,
        "access_token": ACCESS_TOKEN
    }

    res = requests.post(url, data=payload)
    print("Facebook response:", res.json())

# 🚀 RUN BOT
image = get_image()

if image:
    caption = get_caption()
    print("Posting:", caption)
    post_to_facebook(image, caption)
else:
    print("No image found")
