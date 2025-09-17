# client.py
import socket
import json

HOST = "127.0.0.1"
PORT = 65432

def client_program():
    filename = input("Enter filename: ")
    word = input("Enter word to search: ")

    request = {"filename": filename, "word": word}

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(json.dumps(request).encode())
        data = s.recv(4096).decode()

    response = json.loads(data)

    if "error" in response:
        print(f"Error: {response['error']}")
    else:
        print(f"\nSearch Results for word '{response['word']}':")
        if response["matches"]:
            for match in response["matches"]:
                print(f"Line {match['line']}: {match['text']}")
        else:
            print("No matches found.")

if __name__ == "__main__":
    client_program()
