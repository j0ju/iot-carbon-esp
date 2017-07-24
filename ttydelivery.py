# LICENSE: GPLv2, see attached License
# Author: Joerg Jungermann

class TtyDelivery():
    def __init__(self, template=None):
        self.template = b'iot.by-id.{id}.{metric} {value}'
        #self.template = b'iot.by-id.{id}.{metric} {value} {epoch}'

        self.deliverNonNumericValues = True

        if template:
            self.template = template

    def send(self, metric, value, id=None):
        import iotesp

        if not self.deliverNonNumericValues:
            if value == float('nan'):
                return
            if value == None:
                return

        if not id:
            id = iotesp.get_mac()
        send_string = self.template.format(metric=metric, value=value, id=id)

        print(send_string)

    def close(self):
        return

# vim: sw=4 ts=4 ft=python et foldmethod=indent
