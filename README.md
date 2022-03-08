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

# 如果无法启动 执行pip install -r .\requirements.txt
```

## 修改.env文件
```
DB_DATABASE=数据库名称
DB_USERNAME=数据库用户名
DB_PASSWORD=数据库密码
```
## 访问登录页
`localhost:8000/home`

Happy Crafting!
