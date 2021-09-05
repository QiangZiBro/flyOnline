import argparse
import logging
import random
import time

import geckodriver_autoinstaller

from fly_online.login import Login
from fly_online.ping import ping

logging.disable(logging.WARNING)


def random_sleep(mean, std):
    time_gap = int(random.gauss(mean, std))
    print("sleep:{} min {:.2f} s".format(time_gap // 60, time_gap % 60))
    time.sleep(time_gap)


def schedule(configs):
    while True:
        if not ping(url='https://www.baidu.com'):
            print("网络异常，尝试登录NBU账号")
            Login(configs.file).try_all()
        random_sleep(300, 60)


def fly():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, default='~/.local/fly-online/password.txt', help="密码文件位置")
    parser.add_argument('-l', '--login', default=False, action='store_true', help="直接登录校园内网")
    args = parser.parse_args()

    geckodriver_autoinstaller.install()

    if args.login:
        print("尝试登录到校园内网...")
        Login(args.file).try_all()
    else:
        schedule(args)


if __name__ == '__main__':
    fly()
