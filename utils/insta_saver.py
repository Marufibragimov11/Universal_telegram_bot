import requests


def save_insta(url):
    link = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {
        "url": url}

    headers = {
        "X-RapidAPI-Key": "3ae42eee16mshaaaa6751e807d09p18dabcjsne8d35fd9e05b",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.get(link, headers=headers, params=querystring)

    return response.json()

# d = save_insta(" ")
# print(d['error'])