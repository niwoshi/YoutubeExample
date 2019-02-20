# -*- coding: utf-8 -*-
import requests
import json

KEY_FILENAME = "Key"


def main():
    with open(file=KEY_FILENAME, mode='r', encoding='utf-8') as f:
        API_KEY = f.readline()
    print(API_KEY)
    print("↑APIキー")


if __name__ == '__main__':
    main()
