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
 - Ставим docker и docker-compose (ищем в инете как)
 - Клонируем репозиторий в `/src/tbot` - все конфиги заточены под эту директорию
 - Собираем свой образ `sh docker_build.sh`, преварительно поменяв в `docker-compose.yml` [vsb2007](https://github.com/vsb2007/raspberry_telegramm_bot/blob/eb46c118f6f6fa0cabf7323a7100e22bac73e74f/docker-compose.yml#L5) 
и в `docker_build.sh` [vsb2007](https://github.com/vsb2007/raspberry_telegramm_bot/blob/497bf655755e04479f1314706a1186c5d64d22d5/docker_build.sh#L3) на что-то свое
 - Открываем фаил [myconfig.py.sample](raspberry_telegramm_bot/config/myconfig.py.sample), убираем расширение `.sample` и подставляем свои данные
 - В файле `bot.py` раскомментируем секцию [Set_webhook](https://github.com/vsb2007/raspberry_telegramm_bot/blob/497bf655755e04479f1314706a1186c5d64d22d5/bot.py#L114)
для настройки `webhook` для нашего бота. После настройки обратно комментируем.

