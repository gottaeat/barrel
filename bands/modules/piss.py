from bands.util import unilen
from bands.util import drawbox
from bands.util import MIRCColors

# pylint: disable=invalid-name
c = MIRCColors()


# pylint: disable=too-few-public-methods
class Piss:
    def __init__(self, channel):
        self.channel = channel

    def print(self, pisser, pissee):
        if len(str(pissee)) == 0:
            msg = f"{c.ORANGE}{pisser}{c.LBLUE}, "
            msg += f"{c.WHITE}on {c.YELLOW}who{c.WHITE}?{c.RES}"
            self.channel.send_query(msg)
            return

        if unilen(str(pissee)) > self.channel.server.USER_NICKLIMIT:
            msg = f"{c.ORANGE}{pisser}{c.LBLUE}, {c.YELLOW}pissee "
            msg += f"{c.LRED}is wider than {self.channel.server.USER_NICKLIMIT} chars.{c.RES}"
            self.channel.send_query(msg)
            return

        msg = f"     {c.WHITE}ë{c.RES} \n"
        msg += f"   {c.WHITE}.-║- {c.LBLUE}<- {c.ORANGE}{pisser}{c.RES} \n"
        msg += f"   {c.ORANGE}╭{c.LRED}╰{c.WHITE}\\{c.RES} \n"
        msg += f"   {c.YELLOW}┊{c.WHITE}/ \\{c.RES} \n"
        msg += f"   {c.YELLOW}┊{c.RES} \n"
        msg += f" {c.YELLOW}{pissee}{c.RES} \n"

        msg = drawbox(msg, "single")
        msg += f"{c.WHITE} → {c.ORANGE}{pissee} "
        msg += f"{c.WHITE}just got {c.YELLOW}pissed on "
        msg += f"{c.WHITE}by {c.ORANGE}{pisser}"
        msg += f"{c.WHITE}.{c.RES}"

        self.channel.send_query(msg)
