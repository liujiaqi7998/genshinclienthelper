import atexit
import configparser
import os

from mitmproxy import http
from mitmproxy import proxy, options
from mitmproxy.tools.dump import DumpMaster

# 获取需要代理的地址信息
try:
    filename = os.path.join(os.path.dirname(__file__), 'Proxylist.txt').replace("\\", "/")
    f = open(filename)
    LIST_DOMAINS = []
    line = f.readline()  # 调用文件的 readline()方法
    while line:
        line = f.readline()
        if len(line) != 0:
            line = line.replace("\n", "")
            LIST_DOMAINS.append(line)
    f.close()
except:
    print("代理列表(Proxylist.txt)异常")
    exit(1)

try:
    filename = os.path.join(os.path.dirname(__file__), 'config.ini').replace("\\", "/")
    config = configparser.ConfigParser()
    config.read(filename)
    REMOTE_HOST = str(config.get('Proxy', 'REMOTE_HOST'))
    REMOTE_PORT = int(config.get('Proxy', 'REMOTE_PORT'))
    USE_SSL = int(config.get('Proxy', 'USE_SSL'))
except:
    print("配置文件(config.ini)不正确，已使用默认配置")
    REMOTE_HOST = "127.0.0.1"
    REMOTE_PORT = 443
    USE_SSL = 1


class MlgmXyysd_Genshin_Impact_Proxy:

    def request(self, flow: http.HTTPFlow) -> None:
        global LIST_DOMAINS
        global REMOTE_HOST
        global REMOTE_PORT
        global USE_SSL
        if flow.request.host in LIST_DOMAINS:
            if USE_SSL:
                flow.request.scheme = "https"
            else:
                flow.request.scheme = "http"
            flow.request.host = REMOTE_HOST
            flow.request.port = REMOTE_PORT


title = '''
            ──────▄▀▄─────▄▀▄
            ─────▄█░░▀▀▀▀▀░░█▄
            ─▄▄──█░░░░░░░░░░░█──▄▄
            █▄▄█─█░░▀░░┬░░▀░░█─█▄▄█
──────────────────────────────────────────────
─██████████████─██████████████─██████──██████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─
─██░░██████████─██░░██████████─██░░██──██░░██─
─██░░██─────────██░░██─────────██░░██──██░░██─
─██░░██─────────██░░██─────────██░░██████░░██─
─██░░██──██████─██░░██─────────██░░░░░░░░░░██─
─██░░██──██░░██─██░░██─────────██░░██████░░██─
─██░░██──██░░██─██░░██─────────██░░██──██░░██─
─██░░██████░░██─██░░██████████─██░░██──██░░██─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─
─██████████████─██████████████─██████──██████─
──────────────────────────────────────────────
        Qi代理控制器（基于官方脚本二次开发）
        代理启动成功 游戏过程中请不要关闭本程序
    本项目开源免费，如果你是花钱购买的，请直接举报
──────────────────────────────────────────────    
'''

opts = options.Options(listen_host='0.0.0.0', listen_port=12735, ssl_insecure=True)
m = DumpMaster(opts)


def start():
    global m
    global opts
    pconf = proxy.config.ProxyConfig(opts)
    m.server = proxy.server.ProxyServer(pconf)
    m.addons.add(MlgmXyysd_Genshin_Impact_Proxy())
    try:
        m.run()
    except KeyboardInterrupt:
        finish()


def finish():
    global m
    print('结束程序')
    m.shutdown()


atexit.register(finish)

if __name__ == '__main__':
    print(title)
    print("当前游戏服务器地址:" + REMOTE_HOST + "  端口:" + str(REMOTE_PORT))
    print("──────────────────────────────────────────────")
    start()
