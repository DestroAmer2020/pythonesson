import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, Entry, Button, END
# Створення вікна Tkinter для клієнта
client_window = tk.Tk()
client_window.title('Чат клієнт')
# Створення текстового поля для введення повідомлень
message_entry = Entry(client_window, width=50)
message_entry.pack(pady=20)
# Створення області прокрутки для відображення чату
chat_display = scrolledtext.ScrolledText(client_window, height=15, width=50)
chat_display.pack(padx=10, pady=10)
# Функція відправки повідомлень на сервер
def send_message():
    message = message_entry.get()
    client_socket.send(message.encode('utf-8'))
    if message == 'exit':
        client_socket.close()
        client_window.destroy()
    message_entry.delete(0, END)
# Створення сокету для клієнта
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5555))
# Функція отримання повідомлень від сервера
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            chat_display.insert(tk.END, message + '\n')
            chat_display.yview(tk.END)
        except:
            break
# Створення окремого потоку для функції отримання повідомлень
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()
# Прив'язка функції відправки повідомлень до кнопки
send_button = Button(client_window, text='Відправити', command=send_message)
send_button.pack()
# Запуск Tkinter main loop
client_window.mainloop()