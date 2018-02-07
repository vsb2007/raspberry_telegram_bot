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
 - Собираем свой образ `sh docker_build.sh`, преварительно поменяв в `docker-compose.yml`
https://github.com/vsb2007/raspberry_telegramm_bot/blob/eb46c118f6f6fa0cabf7323a7100e22bac73e74f/docker-compose.yml#L5

