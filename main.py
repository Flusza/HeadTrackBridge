from keyboard import KeyboardManager
from network import Network


if __name__ == '__main__':
    net = Network('127.0.0.1', 4243)
    keyboard = KeyboardManager()

    while True:
        data = net.read()
        keyboard.update(data)
