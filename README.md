1. положить в alert_scripts  
2. сделать владельцем пользователя zabbix (chown zabbix:zabbix tt.py)  
3. сделать исполняемым (cmod u+x tt.py)  
4. в морде добавить способ оповещения 
![](media.png)
5. ????  
6. понять и простить  


Я так и не понял как можно получить user_id. Единственный способ, который я нашёл это сходить по ссылке https://botapi.tamtam.chat/chats?access_token=<TOKEN> и взять chat_id с типом dialog.


Для версии 5.x используй webhook из xml.
