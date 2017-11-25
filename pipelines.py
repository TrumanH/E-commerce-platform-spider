# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
'''
class AutoPipeline(object):
        def __init__(self):
                self.file = codecs.open("C:/Users/Truman/Desktop/python/临时用/mydata.json"
                        ,"wb",encoding="utf-8")
        def process_item(self, item, spider):
                print("process_item被调用")
                i=json.dumps(dict(item), ensure_ascii=False)
                line = i + '\n'
                print(i)
                self.file.write(line)
                return item
        def close_spider(self,spider):
                self.file.close() '''
#每种商品单独打包字典并分行
class AutoPipeline(object):
        def __init__(self):
                self.file = codecs.open("C:/Users/Truman/Desktop/python/临时用/mydata1.json"
                        ,"wb",encoding="utf-8")
        def process_item(self, item, spider):
                #print("process_item被调用",len(item["name"]))
                for j in range(0, len(item["name"])):
                        name=item["name"][j]
                        price=item["price"][j]
                        link=item["link"][j]
                        comnum=item["comnum"][j]
                        goods={"name":name,"price":price,"comnum":comnum,"link":link}
                        a=json.dumps(dict(goods), ensure_ascii=False)
                        print("第"+str(j)+"个商品")
                        line = a + '\n'
                        self.file.write(line)                        
                return item
        def close_spider(self, spider):
                self.file.close()
                
