# FlaskClicker

Проект "FlaskClicker" — это сайт-кликер, где каждое число представлено изображением. Изображения беруться в случайном порядке из Интернета.

Интерфейс:

![graphical_interface.png](./graphical_interface.png)

## Запуск проекта

Запуск проекта через Docker:
```bash
sudo docker run -p 5000:5000 shashaevkirill/flaskclicke
```

Далее идёт инструкция по мануальному запуску.

### Что нужно для запуска?

- [Git](https://git-scm.com/downloads)
- [Python3.11+](https://www.python.org/downloads/)

### Запуск:
1. Клонирование репозитория и переход в директорию проекта:
   ```bash
   git clone https://github.com/Shashaev/FlaskClicker.git
   cd FlaskClicker
   ```
2. Создание и активация виртуального окружения:
  - **Windows**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
  - **Linux/macOS**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Устоновка записимостей:
    ```bash
    pip install -r requirements/prod.txt
    ```
4. Запуск проекта:
  - **Windows**
    ```bash
    python src/main.py
    ```
  - **Linux/macOS**
    ```bash
    python3 src/main.py
    ```

После запуска сайт будет доступен по этой [ссылке](http://127.0.0.1:5000).
