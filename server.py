import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 3000
ADDRR = (IP, PORT)

def main():

    server = socket.socket()
    server.bind(ADDRR)
    server.listen()
    print(f"[Listening] server on {IP} port: {PORT}")

    while True:
        conn, addr = server.accept()

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"thread active {threading.active_count}")

if __name__=="__main__":
    print("waiting...")
    main()