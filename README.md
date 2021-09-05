# Fly online in NBU
循环检测内网下是否有网，如果没网就登录NBU账号，保持在线



## 🚀使用方法
1. 使用pip安装
```bash
pip install fly-online
```
2. 安装火狐浏览器
3. 写入密码单`~/.local/fly-online/password.txt` 

```bash
# mkdir -p ~/.local/fly-online && vim ~/.local/fly-online/password.txt
id,password
```
4. 运行
```bash
# 循环检测网络状态
fly
# 直接注册
fly -l 
```