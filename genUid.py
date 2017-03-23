#!/usr/bin/env python

# -------------------------------------------------------------------------------
#
#    Copyright (c) 2016 Slava Vladyshevsky. All rights reserved.
#    Licensed under the MIT License. See LICENSE file in the project root.
#
#    Author:  Slava Vladyshevsky <slava.vladyshevsky(a)gmail.com>
#    Project: DevOps Automation
#
#    Short monotonically increasing ID generator.
#    The algorithm converts current time in milliseconds to 7-char Base66 string.
#    No collisions expected with process concurrency level of <1000 calls/second.
#
#    WARNING: the algorithm exposes ID creation time, since it's easily reverted.
#
# -------------------------------------------------------------------------------

BASE_ALPH = tuple("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_.")
BASE_LEN = len(BASE_ALPH)

if __name__ == "__main__":
    import time
    num = int(round(time.time() * 1000))
    s = ""
    while num:
        num, rem = divmod(num, BASE_LEN)
        s = BASE_ALPH[rem] + s

    print s
