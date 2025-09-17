# server.py
import socket
import threading
import json
from search import Search

HOST = "127.0.0.1"  # Localhost
PORT = 65432        # Arbitrary port

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    try:
        data = conn.recv(1024).decode()
        if not data:
            return
        request = json.loads(data)
        filename = request.get("filename")
        word = request.get("word")

        try:
            search_obj = Search(filename)
            search_obj.clean()
            result = search_obj.getLines(word)
            response = {
                "word": word,
                "matches": [{"line": ln, "text": txt} for ln, txt in result[1:]]
            }
        except Exception as e:
            response = {"error": str(e)}

        conn.sendall(json.dumps(response).encode())

    finally:
        conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[SERVER STARTED] Listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
