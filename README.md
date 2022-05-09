# Genshin代理助手

改进windows下的mitmproxy代理流程，让玩家更加方便地连接到你的世界

## 如何使用

1.下载释放版文件[Releases · liujiaqi7998/genshinclienthelper (github.com)](https://github.com/liujiaqi7998/genshinclienthelper/releases)，解压到文件夹，运行 "Genshin代理助手.exe"

2.在页面上配置服务器地址和端口（如果服务器走https，请勾选使用SSL）

3.点击“启动代理”



## 已完成的功能

- [x] 完成代理工作
- [x] 完成GUI设计
- [x] 实现用户自由配置服务器
- [x] 自动配置系统代理
- [x] 自动检测证书并安装

## 文件说明：

| 文件                  | 作用               |
| --------------------- | ------------------ |
| config.ini            | 保存服务器配置信息 |
| mitmproxy-ca-cert.cer | mitmproxy的证书    |
| Proxylist.txt         | 需要代理的地址     |



Grasscutter Tools 来着 jie65535 的 https://github.com/jie65535/GrasscutterCommandGenerator

本程序仅用于测试本地代理服务知否正常，禁止用于各种商业活动

联系邮箱:liujiaqi7998@qq.com
