# Илья Михайловский

Разрабатываю ML-системы и backend на Python. Живу в Москве, английский C1.

[Telegram](https://t.me/Iluuuaaa) · [Почта](mailto:ilyamihailovsy@gmail.com) · [GitHub](https://github.com/iluuua) · [LinkedIn](https://www.linkedin.com/in/ilua/)

## Резюме

| Направление | Резюме | Исходник |
| --- | --- | --- |
| ML Engineer · NLP и LLM | [Скачать PDF](https://github.com/iluuua/cv/raw/refs/heads/main/Ilya_Mikhailovsky_Resume.pdf) | [XeLaTeX](src/cv.tex) |
| ML Engineer · English | [Download PDF](https://github.com/iluuua/cv/raw/refs/heads/main/Ilya_Mikhailovsky_Resume_EN.pdf) | [XeLaTeX](src/cv-en.tex) |
| Python Backend Developer | [Скачать PDF](https://github.com/iluuua/cv/raw/refs/heads/main/Mikhailovsky_Ilya_Python_Backend_CV_RU.pdf) | [XeLaTeX](src/cv-backend.tex) |

## Опыт

**ReachFlow, основатель и разработчик.** С января 2026 года разрабатываю сервис для отделов продаж в Telegram. Построил поиск потенциальных клиентов по сообщениям и диалогового LLM-агента. Сократил число вызовов классификатора с пяти до двух, а объём входного текста в типовом тестовом диалоге уменьшился на 38%. Серверная часть работает на FastAPI и PostgreSQL. [ReachFlow](https://reachflow.tech)

**Delnovo, технический директор (июль 2023 — май 2026).** Подключил бота к базе знаний в PostgreSQL и Битрикс24. По оценке заказчика, бот автоматизировал около 80% типовых консультаций. Для другого клиента разработал API с OAuth для поиска по каталогу и настроил публикацию 89 страниц в Markdown для ИИ-агентов и в HTML для поисковых систем.

**NEAR AI, Solutions Engineer (июнь 2023 — июль 2024).** Решил 300 алгоритмических задач на C++ для обучения ИИ, в том числе 15 уровня IOI. Писал разборы и проверял решения других участников.

## Проекты

- **Лидеры цифровой трансформации 2026.** Вдвоём заняли 2-е место в задаче Московского метрополитена. По данным 3D-лидара детектор восстанавливает путь и находит препятствия. На конкурсных записях расчёт кадра занимал в среднем 13,9 мс на CPU. На 15,4 км свободного пути ложных тревог не было. [Код и демонстрация](https://github.com/iluuua/metro-lidar-obstacle-detection) · [Итоговый протокол](https://i.moscow/upload/lending/lct2026/edebdf.pdf#page=5)
- **AIDAO 2025.** Заняли 6-е место среди 248 команд. Реализовал Lift-Splat-Shoot на PyTorch. По кадрам четырёх камер модель строит карту статических препятствий вокруг автомобиля. На закрытом тесте получили IoU 0,5606, у победителя 0,564. [Код решения](https://github.com/iluuua/aidao-2025-bev-occupancy)
- **Молекулярная динамика.** Исследовал напряжения в алюминии вокруг включения Fe₄Al₁₃. [Код и материалы](https://github.com/iluuua/magnetostriction-plasticity-bounds)

## Образование

Учусь на программе «Прикладная математика и информатика» в Московском политехе, выпуск в 2029 году. Посещаю курсы ПМИ на ФКН НИУ ВШЭ как вольнослушатель.

## Сборка

Команда `make` собирает все версии резюме из исходников в `src/`. Нужен XeLaTeX со шрифтом STIX Two Text или PT Sans.
