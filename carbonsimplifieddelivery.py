# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann, Tobias Paepke

import socket
import iotesp

class CarbonSimplifiedDelivery():
    def __init__(self, template=None, server=None, port=2003):
        self.template = b'iot.by-id.{id}.{metric} {value}'
        self.server = None
        self.sock = None
        self.port = port
        self.retries = 5
        self.error_wait = 1
        self.debug = False
        self.id = iotesp.get_mac()
        self.deliverNonNumericValues = False

        if template:
            self.template = template
        if server:
            self.server = server
        else:
            print('CarbonDelivery(): no server given')

    def send(self, metric, value, id=None):
        if not self.deliverNonNumericValues:
            if value == float('nan'):
                return
            if value == None:
                return

        if not id:
            send_string = self.template.format(metric=metric, value=value, id=self.id)
        else:
            send_string = self.template.format(metric=metric, value=value, id=id)

        if self.server is None or self.debug:
            print(send_string)

        for i in range(1, self.retries):
            try:
                if not self.sock:
                    self.connect()
                if self.server:
                    self.sock.send(send_string + '\n')
                break
            except Exception as e:
                print("CarbonDelivery.send(): Exception:")
                print(e)
                self.sock = None

    def connect(self, server=None, port=2003):
        if server:
            self.server = server
        if self.server is not None:
            if self.debug:
                print("CarbonDelivery.connect(): connecting to server {}".format(self.server))
            self.sock = socket.socket()
            self.sock.connect(socket.getaddrinfo(self.server, port)[0][-1])

    def close(self):
        if self.sock:
            self.sock.close()
        self.sock = None

# vim: sw=4 ts=4 ft=python et foldmethod=indent
