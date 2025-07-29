import random
import tkinter as tk
import tkinter.messagebox as msg
from PIL import Image,ImageTk

#功能
def btClick():
 b = enter.get()
#偵錯輸入
 if int(b) > 9:
  msg.showerror("錯誤","請輸入0~9的數字")
 else :
  msg.showinfo("執行","您輸入的答案:"+b)
#顯示輸入的答案
  #show.insert(tk.END,r) 測試顯示答案
  if r == int(b) :
          show.insert(tk.END,b+"   恭喜答對了!"+"\n")
  else : 
          show.insert(tk.END,b+"   猜錯了..."+"\n")


r = random.randint(0,9)#產生答案           
#視窗建立
root = tk.Tk()
root.configure(bg="#FFC78E")
root.geometry("750x700")
root.title("猜數字小遊戲")
#插入圖片
img = Image.open('數字圖.jpg')
tk_img = ImageTk.PhotoImage(img)
label = tk.Label(root, image=tk_img, width=370, height=330)
label.place(x=10,y=312)
#標籤
mes = tk.Label(root,text="請輸入數字: ",font=("Helvetica",18),bg="#FFC78E")
mes.place(x = 70,y = 70)

mes2 = tk.Label(root,text="隨機產出一個0~9的數字,\n請猜出正確的數字",
font=("微軟正黑體 Light",18),bg="#FFC78E")
mes2.place(x= 70,y=150)

#輸入訊息框
enter = tk.Entry(root,font=("Helvetica",20))
enter.place(x = 210,y = 70,width=40,height=35)
#顯示訊息框
show = tk.Text(root,font=("Tahoma",18),bg="#FFAF60")
show.place(x=400,y=50,width=300,height=600)
#按鈕
bt = tk.Button(root,text="確認",font=("Helvetica",16),command=btClick)
bt.place(x=270,y=68,width=60,height=40)


root.mainloop()#執行視窗
'''
a = random.randint(0,9)
print(a)
b = int(input("請輸入數字: "))
print(b)

while a != b :
  print("錯誤...")
  b = int(input("請輸入數字: "))
if a == b :
    print('恭喜猜中了!')
else  :
    print("錯誤...")
'''

'''
a = random.randint(0,9)
b = random.randint(0,9)
c = random.randint(0,9)
d = random.randint(0,9)
box = [a,b,c,d]

print(box)
'''
''' 字型顯示
for f in tk.Tk().call("font","families"):
  print(f)      
'''



