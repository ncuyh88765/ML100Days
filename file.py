#文字檔案的讀取與儲存

#儲存檔案

#檔案物件=open(檔案路徑,mode=開啟模式)
file=open("data.txt",mode="w",encoding="utf-8") #開啟 #要加encoding這串中文才不會是亂碼
file.write("5\n3\n4") #操作
file.close() #關閉

#讀取模式:r///寫入模式:w///讀寫模式:r+///

#讀取全部文字 檔案物件.read()
with open ("data.txt",mode="r",encoding="utf-8") as file:
    data=file.read()
print(data)

#一次讀取一行
#for 變數 in 檔案物件:
#從檔案依序讀取每行文字到變數中

sum=0
with open("data.txt",mode="r",encoding="utf-8") as file:
    for line in file: #一行一行的讀取，並計算總合
        sum+=int(line)
print(sum)

#讀取JSON格式
#import json
#讀取到的資料=json.load(檔案物件)

import json
with open("config.json",mode="r") as file:
    data=json.load(file)
print (data) #data是一個字典資料
print("name,",data["name"])
print("version",data["version"])

data["name"]="New Name" #修改變數中的資料
#把最新的資料複寫回檔案中
with open("config.json",mode="r") as file:
    json.dump(data,file)

#寫入文字
#檔案物件.write(字串)
#寫入換行符號
#檔案物件.write("這是範例文字\n")
#寫入json格式
#import json
#json.dump(要寫入的資料,檔案物件)

#關閉檔案
#檔案物件.close()

#最佳實務
#with open(檔案路徑,mode=開啟模式) as 檔案物件:

#with open ("data.txt",mode="w",encoding="utf-8") as file:
#file.write("測試中文 好棒棒\n天竺鼠車車")
#讀取或寫入程式的程式 #會自動安全的關閉檔案
 