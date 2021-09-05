# Fly Online in NBU
循环检测宁波大学内网下是否登录，如果没网就登录NBU账号，保持在线。**fly-online**非常容易使用，只需要通过`pip`便可以安装使用：

```bash
pip install fly-online
```

## 使用方法
1. **安装火狐浏览器**

2. **写入密码单** `mkdir -p ~/.local/fly-online && vim ~/.local/fly-online/password.txt`，每行以`账号,密码`格式写入

## 例子

```bash
# 循环检测网络状态
fly
# 直接注册
fly -l 
```

