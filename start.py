# -*- coding: utf-8 -*-
# @Author: woolson
# @Date:   2017-03-14 21:04:46
# @Last Modified by:   woolson
# @Last Modified time: 2017-03-14 23:39:35

import sys
from Qidian import Qidian
from Heiyan import Heiyan
from Spider import Spider

reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    # 根据所带参数，确定使用哪个网站的配置参数
    try:
        website = sys.argv[1]
        url     = sys.argv[2]
    except Exception as e:
        print "please choose one website"
        exit()

    # 实例化
    dic = {
      "qidian": Qidian,
      "heiyan": Heiyan,
    }
    config = dic[website]()

    # 获取关键信息
    handler = Spider(config.title, config.content, config.next)

    chapters = config.getList(url)

    book = open("text.txt", "w")

    for item in chapters:
      print "正在下载->", item["title"]
      content = handler.getContent(item["href"])

      book.writelines(item["title"] + "\n")
      book.writelines(content["content"] + "\n")

if __name__ == '__main__':
    main()