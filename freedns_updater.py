#!/usr/bin/python3

from hashlib import sha1
import requests

USERNAME = ""
PASSWORD = ""
API_URL = "https://freedns.afraid.org/api/?action=getdyndns&sha={sha1hash}"


def get_sha1(username, password):
    return sha1(f"{username}|{password}".encode('utf-8')).hexdigest()


def read_url():
    shahash = get_sha1(USERNAME, PASSWORD)
    url = API_URL.format(sha1hash=shahash)
    return url


def update_all():
    resp = requests.get(read_url())
    results = resp.text

    for line in results.splitlines():
        service, ip, update_url = line.split("|")
        print(f"Updating {service}")
        result = requests.get(update_url.strip())
        print(result)


update_all()
