import sys
import argparse
import socketio
import logging
import signal
from datetime import datetime


log = logging.getLogger(__name__)
sio = socketio.Client()
start_entry = None


def ask_character():
    print(f"[{date_time()}] - What character would you like to search for?", end=' ')
    character = input()
    send_query = {"query": character}

    if sio.connected:
        sio.emit('search', send_query)

    global start_entry
    start_entry = 0


def date_time():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")


@sio.event
def connect():
    print(f"[{date_time()}] - Client connected")
    ask_character()


@sio.event
def connect_error():
    print(f"[{date_time()}] - Client connection failed!")


@sio.event
def disconnect():
    print(f"[{date_time()}] - Client disconnected!")


@sio.on('search')
def on_message(data):
    global start_entry
    start_entry += 1

    if data['resultCount'] != -1:
        print("({}/{}) {} - [{}]".format(start_entry, data['resultCount'], data['name'], data['films']))
    else:
        print("ERR: {}".format(data['error']))
        ask_character()

    if sio.connected and start_entry == int(data['resultCount']):
        ask_character()


def signal_handler(signum, stack_frame):
    message = f'Signal handler called with signal {signum}'
    log.warning(message)
    log.debug(stack_frame)

    if sio.connected:
        sio.disconnect()

    sys.exit(0)


signal.signal(signal.SIGQUIT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGTSTP, signal_handler)  # ctrl+z
signal.signal(signal.SIGINT, signal_handler)  # ctrl+c


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='0.0.0.0', required=False)
    parser.add_argument('--port', default='3000', required=False)
    args = parser.parse_args()

    sio.connect(f'http://{args.host}:{args.port}')
    sio.wait()
    sys.exit(0)





