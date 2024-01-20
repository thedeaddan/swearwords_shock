# Используем официальный образ Python как базовый образ
FROM python:3.8-slim

# Устанавливаем необходимые зависимости
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libffi-dev \
        libssl-dev \
        libcurl4-openssl-dev \
        libjpeg-dev \
        libpng-dev \
        libpq-dev \
        wireless-tools \
        python3-dev \ 
        dnsmasq \
        hostapd\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Создаем директорию приложения в контейнере
WORKDIR /app

# Копируем все файлы из текущей директории в контейнер
COPY . /app

# Устанавливаем переменные окружения
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Устанавливаем Flask и другие зависимости через pip
RUN pip install --upgrade pip \
    && pip install pymorphy2 flask pyaccesspoint packaging

# Открываем порт 5000
EXPOSE 80

# Команда для запуска файла main.py
CMD ["sh", "-c", "pyaccesspoint start && python main.py"]

