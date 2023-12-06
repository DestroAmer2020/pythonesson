import socket
import threading
# Створення сокету для сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5555))
server_socket.listen(5)
# Список для зберігання підключених клієнтів
clients = []
# Функція обробки повідомлень від клієнта
def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'exit':
                clients.remove(client)
                client.close()
                break
            else:
                broadcast(message, client)
        except:
            break
# Функція розсилання повідомлень усім клієнтам
def broadcast(message, sender_client):
    for client in clients:
        if client != sender_client:
            try:
                client.send(message.encode('utf-8'))
            except:
                continue
# Очікування та обробка підключення нових клієнтів
def accept_clients():
    while True:
        client, addr = server_socket.accept()
        print(f'Підключено {addr}')
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()
# Запуск функції прийому клієнтів
accept_thread = threading.Thread(target=accept_clients)
accept_thread.start()