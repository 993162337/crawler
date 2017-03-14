# -*- coding: utf-8 -*-
# @Author: woolson
# @Date:   2017-03-10 23:48:50
# @Last modified by:   woolson
# @Last modified time: 2017-03-11 22:03:97

from bs4 import BeautifulSoup
import requests
import json
import sys

# 此类只做给我链接和配置返回内容给你
class Spider:
	"""docstring for ArticleSpider"""
	def __init__(self, title, content, next_tag):
		# 设定配置，链接和不同网站承载内容的标签
		self.title_tag = title
		self.content_tag = content
		self.next_tag = next_tag

	# 获取页面内容并返回
	def getContent(self, url):
		result = {}

		#获取页面内容
		try:
			html = requests.get(url)
		except Exception as e:
			result["error"] = "所给的链接无效"
			return result

		soup = BeautifulSoup(html.text, "html.parser", from_encoding="utf-8")

		# 获取文章的title
		# title = soup.find_all(attrs=self.title_tag)
		# 获取文章的content
		content = soup.find_all(attrs=self.content_tag)
		# 获取下一章的链接
		# link = soup.find_all(attrs=self.next_tag)

		try:
			result["content"] = content[0].get_text()
			return result
		except Exception as e:
			result["error"] = "抓取中出现错误"
			return result
