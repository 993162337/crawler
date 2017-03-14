# -*- coding: utf-8 -*-
# @Author: woolson
# @Date:   2017-03-11 11:08:40
# @Last modified by:   woolson
# @Last modified time: 2017-03-11 22:03:90

import Tkinter, tkFileDialog, tkMessageBox
from Spider import Spider
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class Frame(Tkinter.Frame):
	"""docstring for Frame"""
	def __init__(self, master=None):
		Tkinter.Frame.__init__(self, master)
		self.grid(row=0, column=0, sticky="nsew")
		self.createFrame()

	# 创建Frame
	def createFrame(self):
		self.frame = Tkinter.Frame(self)
		self.frame.grid(row=1, column=0, padx=20, pady=10)

		# 选择小说网站Label
		self.websites = Tkinter.Label(self.frame, text="选择小说网站：")
		self.websites.grid(row=1, column=1)

		# 网站选择框
		website = Tkinter.StringVar()
		website.set("起点")
		self.siteSelect = Tkinter.OptionMenu(self.frame, website, "起点", "黑岩")
		self.siteSelect.grid(row=1, column=2, columnspan=2, sticky="W")

		# 输入小说名称Label
		self.fileName = Tkinter.Label(self.frame, text="输入小说名称：")
		self.fileName.grid(row=2, column=1)

		# 输入框
		name = Tkinter.StringVar()
		name.set("woolson")
		self.entryName = Tkinter.Entry(self.frame, textvariable=name)
		self.entryName.grid(row=2, column=2, columnspan=2, sticky="W")

		# 输入网址Label
		self.website = Tkinter.Label(self.frame, text="输入爬取网址：")
		self.website.grid(row=3, column=1)

		# 输入框
		url = Tkinter.StringVar()
		url.set("http://read.qidian.com/chapter/7g-Gf8G-eQxH9vdK3C5yvw2/ertDMJIXVrP4p8iEw--PPw2")
		self.entryUrl = Tkinter.Entry(self.frame, textvariable=url)
		self.entryUrl.grid(row=3, column=2, columnspan=2, sticky="W")

		# 选择保存位置Label
		self.saveLabel = Tkinter.Label(self.frame, text="选择保存位置：")
		self.saveLabel.grid(row=4, column=1)

		# 选择位置
		self.savePath = Tkinter.Button(self.frame, text="选择", command=self.selectPath)
		self.savePath.grid(row=4, column=2, sticky="W")

		# 显示选择的位置
		self.savePathText = Tkinter.Label(self.frame, text="")
		self.savePathText.grid(row=4, column=3)

		# 抓取进程
		# self.saving = Tkinter.Label(self.frame, text="123")
		# self.saving.grid(row=5, column=1, columnspan=3)

		# 确定按钮
		self.button = Tkinter.Button(self.frame, text="确定", command=self.startCB)
		self.button.grid(row=6, column=1, columnspan=3)

	# 选择文件范围
	def selectPath(self):
		filePath = tkFileDialog.askdirectory(initialdir="/Users/woolson/Downloads", title="选择保存位置", parent=self.frame)
		fileName = self.entryName.get()

		if filePath == "":
			tkMessageBox.showerror("woolson", "请输入小说名称！")
		else:
			self.filePath = filePath + "/" + fileName + ".txt"
			self.savePathText.config(text=self.filePath)

	# 确认开始回调声明
	def startCB(self):
		# 保存内容的文件
		file = open(self.filePath, "w")

		# 爬取得规则
		titleKlass = {"class": "j_chapterName"}
		contentKlass = {"class": "j_readContent"}
		nextKlass = {"id": "j_chapterNext"}

		page = self.entryUrl.get()
		# 开始爬取
		spider = Spider(titleKlass, contentKlass, nextKlass)

		if page == "" or self.filePath == "":
			tkMessageBox.showerror("woolson", "小说名称或链接未填写！")
		else:
			# 循环抓取下一章
			while page != "":
				result = spider.getContent(page)

				try:
					page = result["nextUrl"]
					file.write(result["title"] + "\n")
					file.write(result["content"] + "\n\n")

					print "正在写入->" + result["title"]
				except Exception as e:
					page = ""
					print "结束", result["error"]


def main():
	# tkinter 实例
	root = Tkinter.Tk()

	# 基本设置
	root.title("小说爬虫软件")
	root.minsize(100, 100)

	app = Frame(root)
	app.mainloop()

if __name__ == '__main__':
	main()
