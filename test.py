# 格式化 结构化 时间戳的转换
import datetime
import time


# date_stamp = datetime.datetime.fromtimestamp(a)
# print(date_stamp)
#
# date_str = datetime.datetime.strptime(date_stamp,'%Y-%m-%d')
# print(date_str)

# # 时间戳
# a = time.time()
# # 结构化
# time_array = time.localtime(a)
# print(f'结构化{time_array}')
# # 格式化
# checkpoint = time.strftime("%Y-%m-%d %H:%M:%S",time_array)
# print(f'格式化{checkpoint}')



#
# import re
# s = "http://book.chaoxing.com/search/keyword_/fenleiID_2109/field_01/sortName_/nPage_1/size_10.html"
# ret = re.search(r'nPage_(\d+)',s)
# current_page = ret.group(1)
# print(current_page)






