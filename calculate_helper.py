
from tkinter import *

wd = Tk()
wd.title("calculate_helper")
#wd.geometry("640x400+100+100")

Label(wd, text="이전타임 계산").grid(row=0, column=0, pady=10)

label_List1 = [None] * 8
entry_list1 = [0] * 8
label2_List1 = [None] * 8
message_List1 = ["바깥 동전", "카드 영수증", "계좌이체", "만원권", "오천원권", "천원권", "오백원", "백원"]
btn_List1 = [None] * 3
eval_List1 = [None] * 8

def cal():
    print(eval(entry_list1[0].get()))
    #label2_List1[i]['text'] = eval(entry_list1[i].get())
    

for i in range(8):
    label_List1[i] = Label(wd, text=message_List1[i]).grid(row=1+i, column=0)
    entry_list1[i] = Entry(wd)
    if i == 0 or i == 1 or i == 2:
        btn_List1[i] = Button(wd, text="계산", command=cal).grid(row=1+i, column=2)
    label2_List1[i] = Label(wd, text="금액 : ").grid(row=1+i, column=3)

for i in range(8):
    entry_list1[i].grid(row=1+i, column=1)

b1 = Button(wd, text="현금 합산 계산").grid(row=9, column=1)
e1 = Label(wd, text="총 금액 : ").grid(row=9, column=3)


Label(wd, text="근무중 추가된 금액").grid(row=10, column=0, pady=10)
label_List2 = [None] * 7
entry_list2 = [None] * 7
label2_List2 = [None] * 7
message_List2 = ["카드 영수증", "계좌이체", "만원권", "오천원권", "천원권", "오백원", "백원"]
for i in range(7):
    label_List2[i] = Label(wd, text=message_List2[i]).grid(row=11+i, column=0)
    entry_list2[i] = Entry(wd).grid(row=11+i, column=1)
    label2_List2[i] = Label(wd, text="금액 : ").grid(row=11+i, column=3)

b2 = Button(wd, text="갱신").grid(row=18, column=1); b2 = Button(wd, text="내역보기").grid(row=18, column=2)
e2 = Label(wd, text="총 금액 : ").grid(row=18, column=3)


Label(wd, text="마감시 계산").grid(row=19, column=0, pady=10)

label_List3 = [None] * 8
entry_list3 = [None] * 8
label2_List3 = [None] * 8
message_List3 = ["바깥 동전", "카드 영수증", "계좌이체", "만원권", "오천원권", "천원권", "오백원", "백원"]
btn_List3 = [None] * 3

for i in range(8):
    label_List3[i] = Label(wd, text=message_List1[i]).grid(row=20+i, column=0)
    entry_list3[i] = Entry(wd).grid(row=20+i, column=1)
    if i == 0 or i == 1 or i == 2:
        btn_List3[i] = Button(wd, text="계산").grid(row=20+i, column=2)
    label2_List3[i] = Label(wd, text="금액 : ").grid(row=20+i, column=3)

b4 = Button(wd, text="현금 합산 계산").grid(row=28, column=1)
e3 = Label(wd, text="총 금액 : ").grid(row=28, column=3)

wd.mainloop()