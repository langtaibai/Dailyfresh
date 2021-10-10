# Dailyfresh
初学django框架时按照传智播客python教程所学习的项目,该项目包含了实际开发中的电商项目中大部分的功能开发和知识点实践。

功能:用户注册，用户登录，购物车，用户中心，首页，订单系统，地址信息管理，商品列表，商品详情，支付功能等等，是一个完整的电商项目流程
注:此项目纯属个人学习项目

技术栈
python + django + mysql + redis + celery + FastDFS(分布式图片服务器) + nginx

项目启动：
注意: 项目启动前请先查看项目配置环境文件,配置你相应的设置,并安装好各个环境,mysql+redis+nginx+fastDFS+celery等
项目包安装
pip install -r requirements.txt

Django启动命令
python manage.py runserver 
uwsgi web服务器启动：

注意: uwsgi开启需要修改配置文件中的DEBUG和ALLOWED_HOSTS
启动: uwsgi --ini 配置文件路径 / uwsgi --ini uwsgi.ini
停止: uwsgi --stop uwsgi.pid路径 / uwsgi --stop uwsgi.pid
celery分布式任务队列启动
celery -A celery_tasks.tasks worker -l info

redis服务端启动
sudo redis-server /etc/redis/redis.conf

FastDFS服务启动 ```
Trackerd服务 sudo /usr/bin/fdfs_trackerd /etc/fdfs/tracker.conf start

  storge服务
  sudo /usr/bin/fdfs_storaged /etc/fdfs/storage.conf start
  ```
nginx

启动nginx
sudo /usr/local/nginx/sbin/nginx
重启nginx
sudo /usr/local/nginx/sbin/nginx -s reload
建立索引文件--搜索引擎
新环境需要配置jieba分词,生成whoose_cn_backend文件

python manage.py rebuild_index
mysql事务隔离级别设置

sudo vim /etc/mysql/mysql.conf.d/mysql.cnf
transaction-isolation = READ-COMMITTED (读已提交)
