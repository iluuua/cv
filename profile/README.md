## Hi, I'm Ilya 👋

**Python backend developer and ML / NLP engineer.** I take backends from an empty repo to production — and build the LLM systems that run on top of them.

[![Telegram](https://img.shields.io/badge/Telegram-@Iluuuaaa-2AABEE?logo=telegram&logoColor=white)](https://t.me/Iluuuaaa)
[![Email](https://img.shields.io/badge/Email-ilyamihailovsy@gmail.com-EA4335?logo=gmail&logoColor=white)](mailto:ilyamihailovsy@gmail.com)
[![CV](https://img.shields.io/badge/CV-PDF-333333?logo=readthedocs&logoColor=white)](https://github.com/iluuua/cv)

- 🚀 Backend **and** LLM layer of **[ReachFlow](https://reachflow.tech)** — a B2B SaaS that automates sales conversations in Telegram
- 🏅 **AIDAO 2025 finalist** — top-30 of 248 teams from 14 countries (Yandex Education × HSE Faculty of Computer Science)
- 🐍 Writing **production Python since 2022** — FastAPI, asyncio, PostgreSQL, Redis, Docker, Kubernetes
- 🎓 Applied Math & CS @ Moscow Polytechnic University, class of 2029 · 📍 Moscow · English C1

### What I work on

- **A multi-tenant backend from scratch** — FastAPI + asyncpg, 14 domain routers, JWT and Google OAuth with JWKS verification, workspace isolation in both queries and Postgres RLS; 69 tables, 168 indexes, 33 migrations
- **Async work that survives a restart** — Redis + Dramatiq actors: message batching, deferred follow-ups, queue recovery; Telegram over MTProto / Telethon with session restore and flood handling
- **LLM orchestration** — 8 model calls per message, 22 pydantic schemas with `extra="forbid"` so a schema violation is retryable instead of silent, `primary → fallback` routing over OpenRouter with per-attempt cost traces; merged five classifier calls into two for 14–43% less input
- **Shipping it and keeping it up** — Docker, nginx, health checks down to schema validation, request-id / trace-id logging (OpenTelemetry), GitHub Actions over 86 test modules, Kubernetes for the workers
- **Models from scratch** — PyTorch: Lift-Splat-Shoot for bird's-eye-view occupancy from four cameras, **IoU 0.5606** against 0.564 for the winning team

### Experience

| | |
|---|---|
| **ReachFlow** — Backend / ML & NLP Engineer | 2026 → now · backend and LLM layer of a B2B sales-automation SaaS |
| **Freelance Python developer** | 2024 → now · Aiogram bots — a RAG consultant on PostgreSQL vector search wired into Bitrix24 (~80% of routine consultations automated), a school bot with student / teacher / admin roles |
| **Near AI** — C++ solutions engineer | 2023 – 2024 · algorithmic C++ as training data for a decentralized AI, code review in an international team |

### Selected projects

- **[aidao-2025-bev-occupancy](https://github.com/iluuua/aidao-2025-bev-occupancy)** — AIDAO 2025 final: BEV occupancy from 4 cameras, Lift-Splat-Shoot written from scratch in PyTorch
- **[T-bank-CV](https://github.com/iluuua/T-bank-CV)** — logo-detection pipeline for T-Bank
- **[CMI-contest-RNN](https://github.com/iluuua/CMI-contest-RNN)** — reproducible training + inference pipeline for the CMI sensor-data contest
- **[cv](https://github.com/iluuua/cv)** — my résumé: PDF plus the XeLaTeX source it's built from

### Stack

| | |
|---|---|
| **Backend** | Python · FastAPI · Pydantic · asyncio · JWT / OAuth · PostgreSQL · asyncpg · pgvector · Redis · Dramatiq |
| **Infra & ops** | Docker · nginx · Kubernetes · GitHub Actions · Linux · pytest · ruff · OpenTelemetry |
| **NLP / LLM** | production LLM pipelines · strict JSON-schema output · RAG · embeddings · agents and tool calling · MCP · model routing and fallback · cost / latency |
| **ML / DL & foundations** | PyTorch · NumPy · pandas · training from scratch · ResNet / FPN · segmentation · C++ and competitive-programming algorithms |

📬 **[Telegram](https://t.me/Iluuuaaa)** · **[ilyamihailovsy@gmail.com](mailto:ilyamihailovsy@gmail.com)** · open to Python backend and ML/NLP roles
