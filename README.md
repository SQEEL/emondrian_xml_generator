# eMondrian XML Generator

`eMondrian XML Generator` — это инструмент для автоматического создания XML-схем для работы с [eMondrian](https://github.com/SergeiSemenkov/eMondrian.git), использующий данные из ClickHouse.

## 📖 Описание

Проект предназначен для генерации XML-схем на основе структуры таблиц ClickHouse. Схемы включают:
- **Cubes (Кубы данных)**: создаются на основе структуры таблиц.
- **Dimensions (Измерения)**: для полей, не начинающихся с `n_`.
- **Measures (Метрики)**: для полей, начинающихся с `n_`.

Инструмент упрощает процесс настройки eMondrian, генерируя готовый к использованию XML для загрузки в систему.

---

## 🚀 Возможности

- Подключение к базе данных ClickHouse.
- Автоматическое извлечение метаданных таблиц и колонок.
- Генерация XML-файла, совместимого с eMondrian.
- Настройка измерений, иерархий и метрик на основе структуры данных.

---

## 📦 Установка

1. Убедитесь, что у вас установлен Python версии 3.7 или выше.
2. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/your-username/emondrian_xml_generator.git
   cd emondrian_xml_generator

---

## ⚙️ Конфигурация
Параметры подключения можно передавать через переменные окружения или задавать в коде:

- host: Адрес ClickHouse (например, localhost).
- port: Порт ClickHouse (по умолчанию 8123).
- database: Имя базы данных.
- username: Имя пользователя.
- password: Пароль.
- source_table: Имя таблицы.

---

## 🛠 Использование
1. Настройте подключение к базе данных ClickHouse.
2. Укажите параметры подключения и таблицу, для которой нужно сгенерировать XML, в главном скрипте main.py.
3. Запустите генерацию:
   ```bash
   python main.py
После выполнения скрипт создаёт:

- ### 📂 XML-файл
   Файл будет сохранён в текущей рабочей директории с именем, соответствующим таблице.
   Пример: dm_apt_data.xml

- ### 🖥️ Вывод в консоль
   Сгенерированный XML также выводится в консоль для быстрой проверки результата.

---

## 📄 Формат XML-файла
Пример сгенерированного XML:

```xml
<Schema name="your_schema_name">
    <Cube name="your_cube_name">
        <Table name="your_table_name"/>
        <Dimension name="Column1">
            <Hierarchy hasAll="true" allMemberName="All Column1">
                <Level name="Column1" column="column1" uniqueMembers="true"/>
            </Hierarchy>
        </Dimension>
        <Measure name="N_Column" column="n_column" aggregator="sum" formatString="#,###.00"/>
    </Cube>
</Schema>
```
---

## 📜 Лицензия
Этот проект распространяется под лицензией [MIT](https://github.com/SQEEL/emondrian_xml_generator/blob/main/LICENSE.md).
