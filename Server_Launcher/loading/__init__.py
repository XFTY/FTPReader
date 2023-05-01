import socket

class listenr:
    def __init__(self, IP:str, PORT:int) -> None:
        self.socket_connetExcpiton = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_connetExcpiton.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket_connetExcpiton.bind((IP, PORT))
        self.socket_connetExcpiton.listen()
        self.conn, self.addr = self.socket_connetExcpiton.accept()
        self.getter()

    def getter(self):

        self.conn.close()
        self.socket_connetExcpiton.close()

if __name__ == "__main__":
    listenr(IP="localhost", PORT=8080)