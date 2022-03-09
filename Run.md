## 每次进入都使用本地环境
```
WINDOWS: $ 
./venv/Scripts/activate
MAC: $ 
source venv/bin/activate
# 如果无法启动执行以下语句
pip install -r .\requirements.txt
```
## 然后启动本地服务
```
# 每次最好都执行以下语句，确保数据库结构一致
python craft migrate

# 启动服务
python craft serve
```