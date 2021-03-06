# -*- coding: utf-8 -*-
import requests
from pprint import pprint
import json

KEY_FILENAME = "Key"
YOUTUBEAPI_ENDPOINT = "https://www.googleapis.com/youtube/v3/"


def main():
    with open(file=KEY_FILENAME, mode='r', encoding='utf-8') as f:
        API_KEY = f.readline()

    search_url = YOUTUBEAPI_ENDPOINT + "search?part=snippet&q={}&order=date&maxResults={}&key={}"

    response = requests.get(search_url.format(
        "DaiGo",
        50,
        API_KEY
    ))

    if response.status_code == requests.codes.ok:
        res_json = response.json()

        if "items" in res_json:
            for video_info in res_json["items"]:
                if ("snippet" in video_info) and ("title" in video_info["snippet"]):
                    print(video_info["snippet"]["title"])


if __name__ == '__main__':
    main()
