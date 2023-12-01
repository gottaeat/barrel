import time

from bands.irc.util import wrap_bytes


# pylint: disable=too-few-public-methods
class Channel:
    def __init__(self, server):
        self.server = server
        self.sock_ops = server.sock_ops

        self.name = None

        self.char_limit = None

        self.tstamp = None

    def send_query(self, msg):
        if "\n" in msg:
            for line in msg.split("\n"):
                if line != "":
                    if len(line.encode("utf-8")) > self.char_limit:
                        for item in wrap_bytes(line, self.char_limit):
                            self.sock_ops.send_raw(f"PRIVMSG {self.name} :{item}")
                            time.sleep(self.server.scroll_speed)
                    else:
                        self.sock_ops.send_raw(f"PRIVMSG {self.name} :{line}")
        else:
            if len(msg.encode("utf-8")) > self.char_limit:
                for item in wrap_bytes(msg, self.char_limit):
                    self.sock_ops.send_raw(f"PRIVMSG {self.name} :{item}")
                    time.sleep(self.server.scroll_speed)
            else:
                self.sock_ops.send_raw(f"PRIVMSG {self.name} :{msg}")