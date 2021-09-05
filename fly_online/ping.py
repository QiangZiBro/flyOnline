# -*- coding: utf-8 -*-
import urllib.request


def ping(url="baidu.com"):
    status_code = urllib.request.urlopen(url, timeout=3).getcode()
    return status_code == 200


if __name__ == "__main__":
    if ping():
        print("Accessed!")
    else:
        print("Not accessed")
