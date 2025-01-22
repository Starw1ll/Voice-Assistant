import customtkinter as ctk

# Функция для добавления сообщения в чат
def add_message(message):
    chat_box.configure(state="normal")  # Разрешаем редактирование
    chat_box.insert("end", message + "\n")
    chat_box.configure(state="disabled")  # Запрещаем редактирование
    chat_box.see("end")  # Прокручиваем вниз

app = ctk.CTk()
app.title("Голосовой помощник Эмма")
app.geometry("500x400")

# Создаем текстовое поле для чата
chat_box = ctk.CTkTextbox(app, width=480, height=300, state="disabled")
chat_box.pack(pady=10)

start_button = ctk.CTkButton(app, text="Запустить", command=start_emma)
start_button.pack(pady=5)

# Запускаем главный цикл
app.mainloop()
