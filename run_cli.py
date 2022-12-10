import argparse

import run
from Xdnmb import Xdnmb


def main(args):
    if args.cookie:
        cookie = args.cookie
    else:
        cookie = run.cookies()
        run.cookie = cookie
        if not cookie:
            print("[ERR]:\t请先设置cookie")
    if args.id:
        nmb_downloader = Xdnmb(cookie)
        result = nmb_downloader.get_with_cache(args.id, nmb_downloader.po)
        if args.optimize:
            result = run.analysis(result)
            print(f'[TIPS]:当前标题为"{result["title"]}"'
                  f',是否需要修改,如需修改请直接键入修改后的标题,不需请按回车')
            content = input('>').strip()
            if content != '':
                result['title]'] = content
        run.out(result, nmb_downloader)
    else:
        print("[ERR]:虚空下载不可取")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--cookie')
    parser.add_argument('-d', '--download', dest='id', help='下载某个串')

    parser.add_argument('-r', '--read-cache', action='store_true', help='读取上次缓存文件')  # TODO
    parser.add_argument('-o', '--optimize', action='store_true', help='启用优化选项')

    main(parser.parse_args())
