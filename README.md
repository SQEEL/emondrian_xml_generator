# eMondrian XML Generator

`eMondrian XML Generator` — это инструмент для автоматического создания XML-схем для работы с [eMondrian](https://github.com/pentaho/mondrian), использующий данные из ClickHouse.

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
  ```
