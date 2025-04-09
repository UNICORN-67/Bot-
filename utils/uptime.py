# uptime

import time

start_time = time.time()

def get_uptime():
    uptime = int(time.time() - start_time)
    hours, remainder = divmod(uptime, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}ʜ {minutes}ᴍ {seconds}s"