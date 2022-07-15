from scrapy import cmdline  # 这个本质也是在Terminal终端运行，这里可以右键文件，然后运行这个py文件，可以实现类似终端运行效果
cmdline.execute("scrapy crawl xina2".split())  # 如果想运行xina2项目，把这里的xina改成xina2即可
