# raspberry pi telegramm_bot

## Telegram бот на Raspberry Pi 
```
По запросу показывает температуру с
присоедиенного датчика DTH22
```

### Технологии
 - Docker, docker-compose
 - Python

### Установка и запуск
 - Регистрируем своего бота [здесь](https://core.telegram.org/bots#3-how-do-i-create-a-bot), запоминаем/копируем его токен.
 - Ставим docker и docker-compose (ищем в инете как)
 - Клонируем репозиторий в `/src/tbot` - все конфиги заточены под эту директорию
 - Собираем свой образ `sh docker_build.sh`, преварительно поменяв в `docker-compose.yml` [vsb2007](https://github.com/vsb2007/raspberry_telegramm_bot/blob/eb46c118f6f6fa0cabf7323a7100e22bac73e74f/docker-compose.yml#L5) 
и в `docker_build.sh` [vsb2007](https://github.com/vsb2007/raspberry_telegramm_bot/blob/497bf655755e04479f1314706a1186c5d64d22d5/docker_build.sh#L3) на что-то свое
 - Открываем фаил [myconfig.py.sample](config/myconfig.py.sample), убираем расширение `.sample` и подставляем свои данные
 - Настраиваем nginx для домена (у меня есть домен, потому рассматриваю именно этот вариант)
    * Обязательно ssl (бесплатно [тут](https://letsencrypt.org/))
    * Секция
```
location / {
	include uwsgi_params;
	uwsgi_pass unix:/srv/tbot/socket/tbot.sock;
}
```
должна соответствовать [этой строчке](https://github.com/vsb2007/raspberry_telegramm_bot/blob/f2904be2290ce14fd414bc5954cfbd771170c50a/app/tbot.ini#L7)

 - Далее
    * Если нет возможности создать домен 3 уровня специально для бота, то `location /bla-bla` синхронизируем с [этой строчкой](https://github.com/vsb2007/raspberry_telegramm_bot/blob/b89f186550285efe4b8b71708fcea555098a7387/bot.py#L66),
    и остальными аналогично (а может и нет, я не пробовал :))

 - В файле `bot.py` раскомментируем секцию [Set_webhook](https://github.com/vsb2007/raspberry_telegramm_bot/blob/497bf655755e04479f1314706a1186c5d64d22d5/bot.py#L114)
для настройки `webhook` для нашего бота. 
    * Заходим по ссылке `https://tbot.example.net/set_webhook` - если не видим `ok` - смотрим логи - ищем ошибку.
    * После настройки обратно комментируем.

