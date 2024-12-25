englishdic = {"bird": "鳥", "cat": "貓", "dog": "狗", "fish": "魚", "mouse": "老鼠",
              "rabbit": "兔子", "cow": "母牛", "horse": "馬", "pig": "豬", "sheep": "綿羊"}
chinesedic = {"鳥": "bird", "貓": "cat", "狗": "dog", "魚": "fish", "老鼠": "mouse",
              "兔子": "rabbit", "母牛": "cow", "馬": "horse", "豬": "pig", "綿羊": "sheep"}


while(True):
    print("請輸入指令: 1.英翻中 2.中翻英 3.離開 ")
    x = input()
    if(x not in ['1', '2', '3']):
        print("請輸入正確的指令!\n")
        continue
    elif(x == '1'):
        print("")
        print("請輸入英文單字: ")
        y = input()
        if(y in englishdic.keys()):
            print(y+" => "+englishdic[y]+"\n")
        else:
            print("查無此單字\n")
    elif(x == '2'):
        print("")
        print("請輸入中文單字: ")
        y = input()
        if(y in chinesedic.keys()):
            print(y+" => "+chinesedic[y]+"\n")
        else:
            print("查無此單字\n")
    elif(x == '3'):
        print("")
        break
