# swearwords_shock
Шокирующий мат

Собрать образ: 
```shell
docker build -t shocker_word .
```  
Запустить контейнер:
```shell
docker run --network host -p 80:80 shocker_word
```