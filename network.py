import socket
import struct


class Network:
    def __init__(self, ip: str, port: int) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((ip, port))

    def read(self) -> dict:
        """
        Tries to read data from the socket and returns the data in the form of a dict.

        :return: dict: A dictionary of the values your face is in.
        """
        data = {}
        try:
            raw_data = self.socket.recvfrom(48)[0]
            for i, label in enumerate(["x", "y", "z", "yaw", "pitch", "roll"]):
                d = struct.unpack('d', raw_data[i * 8:(i + 1) * 8])[0]
                data[label] = d
        except Exception as e:
            print(e)

        return data
