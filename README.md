## Requirements

- Python 3.4 +
- OpenSSL (latest version)
- Pip

## Linux

If you are running on a Linux flavor, you’ll need a few extra packages before you start. You can download these packages by running:

```
$ sudo apt-get install python-dev libssl-dev
```

Instead of `python-dev` you may need to specify your Python version

```
$ sudo apt-get install python3.6-dev libssl-dev
```

## Windows

With windows you will need to have the latest OpenSSL version. Install [OpenSSL 32-bit or 64-bit](https://slproweb.com/products/Win32OpenSSL.html).

## Mac

If you do not have the latest version of OpenSSL you will encounter some installation issues with creating new applications since we need to download a zip of the application via GitHub.

With Mac you can install OpenSSL through `brew`.

```
brew install openssl
```

## Installation

The best way to install Masonite is by starting in a virtual environment first. This will avoid any issues with filesystem permissions.

```
python3 -m venv venv
```

Then activate the virtual environment:
```
WINDOWS: $ ./venv/Scripts/activate
MAC: $ source venv/bin/activate
```

## Install

```
pip install masonite
# 当前项目不需要
# project start .
project install
python craft serve
# 加速源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# 如果无法启动 执行pip install -r .\requirements.txt
```

## 修改.env文件
```
cp .env-example .env

DB_DATABASE=数据库名称
DB_USERNAME=数据库用户名
DB_PASSWORD=数据库密码

# 填充默认用户名密码 admin@admin.com/123456
python craft seed:run 

```
## 访问
`localhost:8000`

## 登录接口
```
Post: /api/auth
data: {
    "username": "admin@admin.com",
    "password": "123456"
}
```

Happy Crafting!


## 其它
使用前端项目请进入fe目录
```
cd fe
yarn install
yarn dev
```