#
# Coded by DenisDd#6912
# Website : http://denis3d.ml
#

import sys
import os

from bot_root.bot import bot

if __name__ == "__main__":
    if len(sys.argv) == 1:
        TOKEN = os.environ['TOKEN']
    else:
        TOKEN = sys.argv[1]

    bot.run(TOKEN)
