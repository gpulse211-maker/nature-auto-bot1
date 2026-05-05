import requests
import os
import random

# GET SECRETS FROM GITHUB
PAGE_ID = os.getenv("1986918968603740")
ACCESS_TOKEN = os.getenv("EAAS5LP7cptUBRfhozuD8wtM0aZCN2WhcZCZBhvWXPLzGYX0hJ9RKjtab5ArleYaLFrj6DCYJZAlSgcSAAnZAHbbg7XjiGOQlZC6Fe3xzuA4YZCsPvjO43hVwbLXau0t3ptEIvcY2odKAlcPCSYFmsWuZCutjZCpJSUZCOZA0THkB9ZBuNy5YCq5pkNLbzRFanUMObwbXWm3r2TOwsZAbZCLg2Qxijbb2Cjzpf4Tw0M7iwqtHQcMOVQtT4NJxJ9kVMJAHEhKZBIAqdIwvGGWu61pNqcGIYPzfwc26kDK2gZDZD")
PEXELS_API = os.getenv("XfGAoRzMzcQirEDA8U7HMseboDQKHiCc9UfqJctLu9rxMD2KJLYWGPA1")

# GET IMAGE FROM PEXELS
def get_image():
    url = "https://api.pexels.com/v1/search?query=sri lanka nature&per_page=15"
    headers = {"Authorization": PEXELS_API}

    try:
        res = requests.get(url, headers=headers)
        data = res.json()

        photos = data.get("photos", [])
        if not photos:
            print("No photos found")
            return None

        image = random.choice(photos)["src"]["original"]
        return image

    except Exception as e:
        print("Error getting image:", e)
        return None

# GENERATE CAPTION
def generate_caption():
    captions = [
        "🌿 Discover the beauty of Sri Lanka 🇱🇰 #nature #srilanka",
        "🏝️ Paradise found in Sri Lanka 🌅 #travel #nature",
        "🌄 Feel the calm of Sri Lanka 🍃 #beautifuldestinations",
        "🌊 Nature vibes from Sri Lanka 🌴 #explore",
        "🌺 Pure natural beauty 🇱🇰 #wanderlust"
    ]
    return random.choice(captions)

# POST TO FACEBOOK
def post_to_facebook(image_url, caption):
    post_url = f"https://graph.facebook.com/{PAGE_ID}/photos"

    payload = {
        "url": image_url,
        "caption": caption,
        "access_token": ACCESS_TOKEN
    }

    try:
        res = requests.post(post_url, data=payload)
        print("Facebook response:", res.json())
    except Exception as e:
        print("Error posting:", e)

# MAIN
if __name__ == "__main__":
    print("Bot started...")

    if not PAGE_ID or not ACCESS_TOKEN or not PEXELS_API:
        print("Missing environment variables!")
        exit()

    image = get_image()

    if image:
        caption = generate_caption()
        print("Posting:", caption)
        post_to_facebook(image, caption)
    else:
        print("No image to post")
