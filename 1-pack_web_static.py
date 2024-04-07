#!/usr/bin/python3
"""create a .tgz archive from contents of the web_static"""
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """pack web_static folder"""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    cur_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            cur_time.year, cur_time.month, cur_time.day,
            cur_time.hour, cur_time.minute, cur_time.second)
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, size))
    except Exception:
        output = None
    return output
