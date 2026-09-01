# Резюме и поиск работы

Мастерская, где живут два моих резюме и вся разведка вокруг них. Здесь я держу исходники, из которых собираются PDF и docx, тексты под hh и LinkedIn, разбор рынка вакансий, планы подготовки к собеседованиям и заметки по программам и школам. Репозиторий рабочий, тексты в нём переписываются по мере того, как меняется рынок и мой собственный опыт.

Всё написано под себя и от первого лица. Часть документов обращается ко мне на «ты», потому что так их удобнее перечитывать.

## Резюме

Два профиля, потому что рынок в 2026 году разошёлся на две разные роли под похожими названиями.

| Файл | Что это |
|---|---|
| [Mikhailovsky_Ilya_ML_Engineer.pdf](Mikhailovsky_Ilya_ML_Engineer.pdf) | ML-инженер, NLP и LLM. Одна страница. Исходник в `.tex`, тот же текст в `.md` |
| [Mikhailovsky_Ilya_Python_Backend.pdf](Mikhailovsky_Ilya_Python_Backend.pdf) | Python Backend Developer. Одна страница. Рядом лежат `.tex`, `.md` и `.docx` |
| [resume-backend-extended.md](resume-backend-extended.md) | Бэкенд-резюме на две страницы, с conversation engine, Discovery, Outreach и пет-проектами |
| [resume-hh-profile.md](resume-hh-profile.md) | Тот же опыт, разложенный по полям hh.ru, плюс границы честности для секции |
| [resume-hh-export-2026-05.doc](resume-hh-export-2026-05.doc) | Старая выгрузка профиля с hh от мая 2026 года, лежит архивом |

### Как пересобрать

PDF собирается XeLaTeX, шрифты PT Sans и PT Mono.

```bash
xelatex Mikhailovsky_Ilya_ML_Engineer.tex
```

```bash
xelatex Mikhailovsky_Ilya_Python_Backend.tex
```

Docx для бэкенд-резюме собирается скриптом, ему нужен `python-docx`.

```bash
python3 resume-build-docx.py
```

## Рынок

| Файл | Что внутри |
|---|---|
| [market-vacancies-shortlist.md](market-vacancies-shortlist.md) | Шорт-лист вакансий, куда отклик имеет смысл, с вилками и ссылками |
| [market-companies-and-channels.md](market-companies-and-channels.md) | Ранжированный список из 23 целей, три волны откликов, каналы найма и список того, куда не ходить |
| [market-interviews-research.md](market-interviews-research.md) | Как устроены ML-собеседования в российских компаниях. Банк из 56 вопросов, карта глубины по темам, план подготовки на три недели |
| [market-interviews-firsthand.md](market-interviews-firsthand.md) | Сырые слова знакомых, которые эти собеседования проходили. Исходник для проверки |

## Учёба

| Файл | Что внутри |
|---|---|
| [study-plan.md](study-plan.md) | Итоговый учебный план по этапам с чекпоинтами |
| [study-course-choice.md](study-course-choice.md) | Сравнение восьми вариантов и решение, чем закрывать пробел по классическому ML |
| [study-sokolov-repo.md](study-sokolov-repo.md) | Что полезного лежит в старых потоках курса Соколова и чего нет в текущем |
| [study-senatorovai-audit.md](study-senatorovai-audit.md) | Разбор школы SenatorovAI и почему я туда не пошёл |

## Программы и школы

| Файл | Что внутри |
|---|---|
| [programs-airi.md](programs-airi.md) | Как устроена аффилиация AIRI, карта лабораторий, три сценария входа |
| [programs-sirius.md](programs-sirius.md) | Студенческие ML-программы «Сириуса», цензы и окна подачи |
| [programs-sirius-letter.md](programs-sirius-letter.md) | Готовое письмо в НТУ «Сириус» с вопросами по требованиям к участникам |

## Публикации

| Файл | Что внутри |
|---|---|
| [post-linkedin-aidao.md](post-linkedin-aidao.md) | Пост в LinkedIn про финал AIDAO 2025, три версии по длине |
| [post-linkedin-aidao-story.md](post-linkedin-aidao-story.md) | Та же история, но с ночью перед сдачей |

## Прочее

В папке `references` лежат чужие резюме, которые я смотрел как образец вёрстки. Они не мои и в работу не идут.

## Как это писалось

Тексты держатся одного правила. Без двоеточий, тире, противопоставлений вида «не X, а Y» и без длинных перечислений внутри предложения. Короткие фразы, живой русский. Если правишь что-то здесь, держи ту же планку.
