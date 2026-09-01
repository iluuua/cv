#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Собирает Mikhailovsky_Ilya_Python_Backend.docx из того же текста, что лежит в .md и .tex.
Запуск командой python3 build_docx.py
"""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

FONT = "Arial"           # universal, full Cyrillic coverage, ATS-safe
TEXT_W_CM = 18.0         # A4 (21cm) - left/right margins (1.5cm each)

doc = Document()

# ---- page + base style ----
sec = doc.sections[0]
sec.top_margin = Cm(1.0); sec.bottom_margin = Cm(1.0)
sec.left_margin = Cm(1.5); sec.right_margin = Cm(1.5)

normal = doc.styles["Normal"]
normal.font.name = FONT
normal.font.size = Pt(10)
normal.element.rPr.rFonts.set(qn("w:cs"), FONT)  # apply to complex/Cyrillic too
pf = normal.paragraph_format
pf.space_before = Pt(0); pf.space_after = Pt(0); pf.line_spacing = 1.04


def _set_cs(run):
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts"); rpr.append(rfonts)
    for a in ("w:ascii", "w:hAnsi", "w:cs"):
        rfonts.set(qn(a), FONT)


def run(p, text, *, bold=False, italic=False, size=10, color=None):
    r = p.add_run(text)
    r.bold = bold; r.italic = italic; r.font.size = Pt(size)
    if color:
        r.font.color.rgb = RGBColor.from_string(color)
    _set_cs(r)
    return r


def para(*, before=0, after=2, line=1.04, align=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.line_spacing = line
    if align is not None:
        p.alignment = align
    return p


def bottom_border(p):
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    b = OxmlElement("w:bottom")
    b.set(qn("w:val"), "single"); b.set(qn("w:sz"), "6")
    b.set(qn("w:space"), "2"); b.set(qn("w:color"), "333333")
    pBdr.append(b); pPr.append(pBdr)


def heading(text):
    p = para(before=7, after=3)
    bottom_border(p)
    run(p, text.upper(), bold=True, size=11)


def bullet(prefix=None, text=""):
    p = doc.add_paragraph(style="List Bullet")
    pf = p.paragraph_format
    pf.space_before = Pt(0); pf.space_after = Pt(2); pf.line_spacing = 1.04
    pf.left_indent = Cm(0.5); pf.first_line_indent = Cm(-0.25)
    if prefix:
        run(p, prefix + " ", bold=True)
    run(p, text)
    return p


def role(title, date):
    p = para(before=2, after=1)
    p.paragraph_format.tab_stops.add_tab_stop(Cm(TEXT_W_CM), WD_TAB_ALIGNMENT.RIGHT)
    run(p, title, bold=True)
    run(p, "\t" + date)


# ================= HEADER =================
p = para(after=1, align=WD_ALIGN_PARAGRAPH.CENTER)
run(p, "Михайловский Илья Евгеньевич", bold=True, size=17)
p = para(after=2, align=WD_ALIGN_PARAGRAPH.CENTER)
run(p, "Python Backend Developer", size=12)
p = para(after=1, align=WD_ALIGN_PARAGRAPH.CENTER)
run(p, "Москва · удалённо или гибрид")
p = para(after=2, align=WD_ALIGN_PARAGRAPH.CENTER)
run(p, "Telegram: @Iluuuaaa · ilyamihailovsy@gmail.com · github.com/iluuua · +7 995 410-33-10")

# ================= SUMMARY =================
heading("О себе")
p = para(after=2)
run(p, "Пишу бэкенд на Python. Бэкенд B2B SaaS-продукта ReachFlow спроектировал с нуля "
       "и довёл до продакшена. Он собран на FastAPI поверх asyncpg и PostgreSQL, "
       "с фоновыми воркерами на Redis и Dramatiq и асинхронными интеграциями с Telegram "
       "по MTProto и с языковыми моделями. Алгоритмическая база олимпиадная, на C++.")

# ================= SKILLS =================
heading("Навыки")
skills = [
    ("Бэкенд.", "Python, FastAPI, Pydantic, asyncio, REST API, JWT, OAuth"),
    ("Данные.", "PostgreSQL, SQL, asyncpg, pgvector, Redis"),
    ("Очереди и воркеры.", "Dramatiq, фоновые задачи, отложенные и запланированные действия"),
    ("Инфраструктура.", "Docker, Docker Compose, nginx, Kubernetes, CI/CD, Linux"),
    ("Качество и наблюдаемость.", "pytest, unittest, ruff, health-чеки, структурные логи, request-id и trace-id, OpenTelemetry"),
    ("Интеграции.", "Telegram API, MTProto, Telethon, Google OAuth, LLM через OpenRouter"),
    ("Алгоритмы.", "C++, алгоритмы и структуры данных"),
]
for pref, txt in skills:
    bullet(pref, txt)

# ================= EXPERIENCE =================
heading("Опыт работы")

role("ReachFlow, Python backend и product engineer", "с января 2026")
p = para(after=1)
run(p, "B2B SaaS для автоматизации продаж в Telegram · reachflow.tech", italic=True)
for b in [
    "Спроектировал и написал многотенантный бэкенд на FastAPI и asyncpg. В нём 14 доменных роутеров, "
    "среди них Auth, Workspaces, CRM, Inbox, Discovery, Outreach, Sequences, AI Brain, Billing, "
    "Connections, Import и Stats. Вход идёт по JWT и через Google OAuth с проверкой подписи по JWKS, "
    "а данные разных воркспейсов изолированы и на уровне запросов, и RLS-политиками Postgres.",
    "Спроектировал схему PostgreSQL. Сейчас в ней 8 доменных схем, 69 таблиц, 168 индексов "
    "и 33 forward-миграции, плюс bootstrap базы, диагностические эндпоинты и smoke-проверки схемы.",
    "Сделал фоновую обработку на Redis и Dramatiq. Отдельные акторы отвечают за диалог и за планировщик, "
    "входящие сообщения батчатся, follow-up и запланированные действия откладываются во времени, "
    "а очереди восстанавливаются после сбоя.",
    "Подключил Telegram по MTProto через Telethon. Написал login-flow, хранение и восстановление "
    "session string, работу через MTProxy и SOCKS, синхронизацию входящих и исходящих, свои лимиты "
    "отправки и обработку flood-ограничений.",
    "Построил слой оркестрации LLM поверх OpenRouter. В него входят профили моделей и цепочки фолбэков, "
    "классификация состояния лида, извлечение фактов, выжимка диалога для менеджера и трейсы вызовов, "
    "а эмбеддинги живут в pgvector.",
    "Довёл сервис до продакшена. Docker и Docker Compose, nginx обратным прокси с тем же origin "
    "для /api, health-чеки трёх уровней вплоть до валидации схемы БД, структурные логи с request-id "
    "и trace-id по OpenTelemetry, CI на GitHub Actions с тестами и ruff, 86 тестовых модулей. "
    "Деплой идёт на Amvera с managed PostgreSQL, для воркеров написаны Kubernetes-манифесты.",
]:
    bullet(text=b)

role("Фриланс, Python-разработчик", "с июля 2024")
for b in [
    "Телеграм-бот для дистрибьютора пластиковых окон. Асинхронный бот на Aiogram, интеграция "
    "с Битрикс24 по REST API, PostgreSQL с векторным поиском для авто-консультаций, уведомления "
    "о смене статуса заказа. По оценке заказчика бот автоматизировал около 80% типовых консультаций.",
    "Телеграм-бот для школы (@shkolo_teacher_bot). Внутри три роли, ученик, учитель и админ, "
    "автоматизация расписания, новостей и отчётности, деплой в Docker.",
]:
    bullet(text=b)

role("Near AI, разработчик решений на C++", "с июня 2023 по июль 2024")
for b in [
    "Решал олимпиадные алгоритмические задачи на C++ для обучения децентрализованного ИИ. "
    "Оптимизировал по времени и памяти, оценивал асимптотику, рефакторил.",
    "Оформлял решения в LaTeX и ревьюил код других участников, команда была международная.",
]:
    bullet(text=b)

# ================= EDUCATION =================
heading("Образование")
bullet("Московский политехнический университет.", "Прикладная математика и информатика, выпуск 2029")
bullet("НИУ ВШЭ, ФКН.", "Вольнослушатель курсов направления «Прикладная математика и информатика»")
bullet(text="В 2025 году прошёл Т-Поколение «Алгоритмы» в параллели B, Deep Learning School "
            "и научную школу ОЦ «Сириус»")

# ================= ADDITIONAL =================
heading("Дополнительно")
p = para(after=0)
run(p, "GitHub github.com/iluuua · английский C1 · русский родной")

out = "Mikhailovsky_Ilya_Python_Backend.docx"
doc.save(out)
print("saved:", out)
