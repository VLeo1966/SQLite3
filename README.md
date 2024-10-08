# SQLite3
```markdown
# Теория на сегодня:

## 1. Командная разработка

Сегодняшний урок будут вести два преподавателя: Нина и Максим.

Вы также можете разделиться на группы по 2-3 человека, разработать проект вместе и улучшить его.

### План урока:
1. Научимся работать с `sqlite3` — новый для нас модуль, с которым мы будем знакомиться.
2. Разработаем командный проект: **Система управления заказами для малого бизнеса**.

### 🧠 Что такое SQLite:
**SQLite** — это лёгкая серверная система управления базами данных, которая не требует отдельного серверного процесса. Библиотека `sqlite3` позволяет взаимодействовать с базами данных SQLite прямо в Python через SQL-запросы.

Мы научимся использовать `sqlite3` в проекте, работая с базой данных в файле.

### Основные возможности и команды SQLite:

1. **Создание подключения к базе данных**: Нужно для начала работы с базой данных.
2. **Создание объекта курсора**: Используется для отправки SQL-запросов.
3. **Выполнение SQL-команд**: Создание таблиц, наполнение их информацией.
4. **Управление транзакциями**: Завершение операций с помощью команды `commit()`, которая сохраняет результаты.
5. **Закрытие подключения**: Команда `close()` завершает работу с базой данных.

В PyCharm Community отсутствует встроенный просмотр баз данных, но в PyCharm Professional он есть. Однако работать можно в обеих версиях.

### Пример работы с базами данных:

1. **Импортируем модуль**:

    ```python
    import sqlite3
    ```

2. **Создаём подключение к базе данных**:

    ```python
    conn = sqlite3.connect('example.db')
    ```

3. **Создаём объект курсора**:

    ```python
    cur = conn.cursor()
    ```

4. **Создаём таблицу**:

    ```python
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    """)
    ```

5. **Сохраняем изменения**:

    ```python
    conn.commit()
    ```

6. **Добавляем данные в таблицу**:

    ```python
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Алексей", 30))
    conn.commit()
    ```

7. **Просматриваем данные**:

    ```python
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    ```

8. **Закрываем подключение**:

    ```python
    conn.close()
    ```

## 2. Разработка проекта: Система управления заказами для малого бизнеса

Для работы в команде используем **Git**.

### Шаги по созданию репозитория:

1. Переходим на сайт [github.com](https://github.com) и создаём репозиторий с именем `order-system`.
2. Добавляем файл `.gitignore` для Python.
3. Выбираем лицензию **MIT License**.
4. Приглашаем коллегу через раздел **Collaborators**.

### Разработка проекта:

1. **Импортируем модули**:

    ```python
    import tkinter as tk
    from tkinter import ttk
    import sqlite3
    ```

2. **Создаём интерфейс приложения**:

    ```python
    app = tk.Tk()
    app.title("Система управления заказами")
    ```

3. **Добавляем поля для ввода**:

    ```python
    tk.Label(app, text="Имя клиента").pack()
    customer_name_entry = tk.Entry(app)
    customer_name_entry.pack()

    tk.Label(app, text="Детали заказа").pack()
    order_details_entry = tk.Entry(app)
    order_details_entry.pack()
    ```

4. **Создаём таблицу для заказов**:

    ```python
    columns = ("id", "customer_name", "order_details", "status")
    tree = ttk.Treeview(app, columns=columns, show="headings")
    for column in columns:
        tree.heading(column, text=column)
    tree.pack()
    ```

5. **Инициализируем базу данных**:

    ```python
    def init_db():
        conn = sqlite3.connect('business_orders.db')
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            customer_name TEXT NOT NULL,
            order_details TEXT NOT NULL,
            status TEXT NOT NULL
        )
        """)
        conn.commit()
        conn.close()
    
    init_db()
    ```

6. **Функция добавления заказа**:

    ```python
    def add_order():
        conn = sqlite3.connect('business_orders.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO orders (customer_name, order_details, status) VALUES (?, ?, 'Новый')",
                    (customer_name_entry.get(), order_details_entry.get()))
        conn.commit()
        conn.close()
        customer_name_entry.delete(0, tk.END)
        order_details_entry.delete(0, tk.END)
        view_orders()
    ```

7. **Функция отображения заказов**:

    ```python
    def view_orders():
        for i in tree.get_children():
            tree.delete(i)
        conn = sqlite3.connect('business_orders.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM orders")
        rows = cur.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
        conn.close()
    ```

### Завершение проекта

1. **Создаём кнопку для добавления заказа**:

    ```python
    add_button = tk.Button(app, text="Добавить заказ", command=add_order)
    add_button.pack()
    ```

2. **Создаём функционал завершения заказа**:

    ```python
    from tkinter import messagebox

    def complete_order():
        selected_item = tree.selection()
        if selected_item:
            order_id = tree.item(selected_item, 'values')[0]
            conn = sqlite3.connect('business_orders.db')
            cur = conn.cursor()
            cur.execute("UPDATE orders SET status='Завершён' WHERE id=?", (order_id,))
            conn.commit()
            conn.close()
            view_orders()
        else:
            messagebox.showwarning("Предупреждение", "Выберите заказ для завершения")

    complete_button = tk.Button(app, text="Завершить заказ", command=complete_order)
    complete_button.pack()
    ```

3. **Запускаем приложение**:

    ```python
    app.mainloop()
    ```

### Работа с Git:

1. **Создаём ветку для разработки**.
2. **Вносим изменения и публикуем через GitHub Desktop**.
3. **Коммитим и вливаем изменения в основную ветку**.

## 3. Результаты урока

Сегодня мы:

1. Научились работать с `sqlite3` на практике.
2. Разработали командный проект “Система управления заказами для малого бизнеса”.
```