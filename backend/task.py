#!/usr/bin/env python
# -*- encoding:utf-8 -*-
"""
File Name: task
Author: shangxc
Created Time: 2019-07-09 22:51
"""
from .models import Flow, Port
import os
import traceback


def check_flow():
    try:
        ports = Port.objects.all()
        for port in ports:
            result = os.popen(
                r"""iptables -vnxL|grep -E "p [sd]pt:%d$"|awk 'BEGIN{total=0}{total+=$2}END{print total}'""" % port.port).read()
            Flow.objects.create(port=port, flow=int(result))
    except Exception:
        with open('/home/exp.log', 'w') as f:
            f.write(traceback.format_exc())
            f.write('\n')



if __name__ == '__main__':
    pass
