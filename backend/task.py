#!/usr/bin/env python
# -*- encoding:utf-8 -*-
"""
File Name: task
Author: shangxc
Created Time: 2019-07-09 22:51
"""
from .models import Flow, Port
import os
from traceback import print_exc


def check_flow():
    try:
        ports = Port.objects.all()
        for port in ports:
            result = os.popen(
                r"""iptables -vnxL|grep -E "p [sd]pt:%d$"|awk 'BEGIN{total=0}{total+=$2}END{print total}'""" % port.port).read()
            Flow.objects.create(port=port, flow=int(result))
    except Exception:
        print_exc()



if __name__ == '__main__':
    pass
