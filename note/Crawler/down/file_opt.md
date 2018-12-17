*** 文件读写相关操作 ***
# 1 open函数:
- open('file_name','way',encoding='')
- filename 为文件名,若没有则自动创建
- way一般有四种方式
  - r 读模式
  - w 写模式
  - a 追加模式
  - b 二进制方式
-encoding 为编码方式,默认为utf-8
# 2 一般使用:
```
open('file_name','way',coding='') as aka :
```
- 使用with过程可以智能关闭文件
- 还可以使用file_name.close()关闭
- 推荐使用with
# 3 读文件:
```data = f.read()```
- 按行读取:
  ```for line in date.readline()```
# 4 追加同上:
# 5 seek()函数:
- 一般使用:
``` seek(offset,where)```
- offset是指从多少个字节开始读取,是字节,一般中文编码占三个字节
- where是指移动位置:1从当前位置移动. 2从动结束位置移动,遇到换行会被截断
- seek()的三种模式:
  1. f.seek(p,0) 移动当文件第p个字节处，绝对位置
  1. f.seek(p,1) 移动到相对于当前位置之后的p个字节
  1. f.seek(p,2) 移动到相对文章尾之后的p个字节
# 6 另外:
关于unix和windows的换行符(unix:\n,win:\r\n).默认情况下,python会统一处理换行符,全部换成\n.
