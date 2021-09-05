# Fly online in NBU
循环检测宁波大学内网下是否登录，如果没网就登录NBU账号，保持在线。**fly-online**非常容易使用，你只需要通过`pip`便可以安装使用：

```bash
pip install fly-online --index-url https://pypi.org/project/
```

## 🚀使用方法
1. 安装火狐浏览器

3. 写入密码单`~/.local/fly-online/password.txt` 

```bash
# mkdir -p ~/.local/fly-online && vim ~/.local/fly-online/password.txt
id,password
```
3. 运行

```bash
# 循环检测网络状态
fly
# 直接注册
fly -l 
```

