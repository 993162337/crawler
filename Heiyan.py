# -*- coding: utf-8 -*-
# @Author: woolson
# @Date:   2017-03-14 22:21:19
# @Last Modified by:   woolson
# @Last Modified time: 2017-03-14 23:30:00

from bs4 import BeautifulSoup
import requests
import json
import sys

class Heiyan:
  def __init__(self):
    self.title = {"id": "chapter_title_1702915"}
    self.content = {"class": "page-content"}
    self.next = {"class": "next-page-class"}

  def getList(self, url):
    try:
      htmlText = requests.get(url)
    except Exception as e:
      print "url is invalid"
      exit()

    soup = BeautifulSoup(htmlText.text, "html.parser", from_encoding="utf-8")
    chapter = soup.find_all("a", {"class": "name"})

    result = []

    for i, v in enumerate(chapter):
      result.append({
        "title": v.get_text(),
        "href": v["href"]
      })

    return result
