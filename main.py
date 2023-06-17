import customtkinter

app = customtkinter.CTk()
app.title('คิดไปทำไมให้Aiคิดให้ดีกว่า')
app.geometry('500*500')

# ข้อความแสดงผลคำตอบ
lable = customtkinter.CTkLabel(app, text="เครื่องตรวจคนติกเก", font=('Aria', 40))
lable.pack(pady=(20, 0))


answer_text = customtkinter.StringVar()
answer_lable = customtkinter.CTkLabel(app, textvariable=answer_text, font=('Aria',40))
answer_lable.pack(pady=(20,0))

# กล่องรับค่า input
entry = customtkinter.CTkEntry(app, placeholder_text="ใส่เข้ามาเลยค่ะ")
entry.pack(pady=(15, 0))

# ปุ่มกด
def button_event():
    user_input = entry.get()
    if user_input == 'เซ้น':
        answer = str(user_input) + "มึงมันเก"
    answer_text.set(answer)
    print(user_input, answer)

button = customtkinter.CTkButton(app, text="มาๆอ้ายมา", command=button_event)
button.pack(pady=(20,0))

app.mainloop()