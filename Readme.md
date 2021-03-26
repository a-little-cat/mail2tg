# mail2tg
部署在服务器上,定时收取邮件并发送给tg,bot.

# systemd example
创建文件**/etc/systemd/system/mail2tg.service**
```sh
[Unit]
Description=this is mail2tg service

[Service]
Type=simple
WorkingDirectory=/home/cat/project/mail2tg
ExecStart=/usr/bin/python3 mail2tg.py > log.txt

[Install]
WantedBy=multi-user.target
```
依次执行
```sh
sudo systemctl daemon-reload
sudo systemctl enable mail2tg
sudo systemctl start mail2tg
```