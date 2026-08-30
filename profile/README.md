## Hi, I'm Ilya 👋

**Python backend developer and ML / NLP engineer.** I take backends from an empty repo to production — and build the LLM systems that run on top of them.

[![Telegram](https://img.shields.io/badge/Telegram-@Iluuuaaa-2AABEE?logo=telegram&logoColor=white)](https://t.me/Iluuuaaa)
[![Email](https://img.shields.io/badge/Email-ilyamihailovsy@gmail.com-EA4335?logo=gmail&logoColor=white)](mailto:ilyamihailovsy@gmail.com)
[![CV](https://img.shields.io/badge/CV-PDF-333333?logo=readthedocs&logoColor=white)](https://github.com/iluuua/cv)

- 🚀 I designed and shipped the backend **and** the LLM layer of **[ReachFlow](https://reachflow.tech)** — a B2B SaaS that automates sales conversations in Telegram
- 🏅 **AIDAO 2025 finalist** — top-30 of 248 teams from 14 countries (Yandex Education × HSE Faculty of Computer Science)
- 🐍 Writing **production Python since 2022** — FastAPI, asyncio, PostgreSQL, Redis, Docker, Kubernetes
- 🎓 Applied Math & CS @ Moscow Polytechnic University, class of 2029 · 📍 Moscow · English C1

---

### What I work on

**A multi-tenant backend, built from scratch.** FastAPI + asyncpg across 14 domain routers — auth,
workspaces, CRM, inbox, discovery, outreach, sequences, billing and the rest. JWT and Google OAuth with
JWKS signature verification; workspace isolation enforced twice over, in the queries and in Postgres RLS
policies. The schema under it: 8 domain schemas, 69 tables, 168 indexes, 33 forward migrations, with
bootstrap, diagnostics endpoints and schema smoke checks.

**Async work that survives a restart.** Redis + Dramatiq dialogue and scheduler actors: incoming-message
batching, deferred follow-ups, scheduled actions, queue recovery after failures. Telegram over
MTProto / Telethon — login flow, session storage and restore, MTProxy / SOCKS, inbound and outbound sync,
rate limiting and flood handling.

**LLM orchestration that holds up in production.** 8 model calls per incoming message: batch gate,
lead-state classifier (16 event types, each anchored to a message with a confidence), typed fact extraction,
strategist → humanizer → reviewer, send planner. A registry of 25 tasks and 22 pydantic schemas with
`extra="forbid"` — a schema violation is a retryable error, never a silent one. Model profiles expand a job's
*role* into a `primary → fallback` chain over OpenRouter, with model ids only in env and a per-attempt trace
of model, latency and cost. Merged five classifier calls into two: 14–43% less input at the classification stage.

**Shipping it and keeping it up.** Docker + Compose, nginx reverse proxy, health checks that go as far as
validating the live schema (`/api/v1/health/db`), structured logging with request-id / trace-id
(OpenTelemetry), GitHub Actions CI running pytest and ruff over 86 test modules, deploy on managed
PostgreSQL plus Kubernetes manifests for the workers.

**Models from scratch, not just API calls.** PyTorch: Lift-Splat-Shoot for bird's-eye-view occupancy from four
car cameras — **IoU 0.5606** on the hidden test, against 0.564 for the winning team.

---

### Experience

| | |
|---|---|
| **ReachFlow** — Python Backend / ML & NLP Engineer | 2026 → now · designed and shipped the backend and the LLM layer of a B2B sales-automation SaaS |
| **Freelance Python developer** | 2024 → now · Aiogram bots — a RAG consultant over PostgreSQL vector search wired into Bitrix24 CRM (~80% of routine customer consultations automated), and a school bot with student / teacher / admin roles |
| **Near AI** — C++ solutions engineer | 2023 – 2024 · algorithmic C++ as training data for a decentralized AI, time and memory optimization, code review in an international team |

### Selected projects

- **[aidao-2025-bev-occupancy](https://github.com/iluuua/aidao-2025-bev-occupancy)** — AIDAO 2025 final: BEV occupancy from 4 cameras, Lift-Splat-Shoot written from scratch in PyTorch
- **[T-bank-CV](https://github.com/iluuua/T-bank-CV)** — logo-detection pipeline for T-Bank
- **[CMI-contest-RNN](https://github.com/iluuua/CMI-contest-RNN)** — reproducible training + inference pipeline for the CMI sensor-data contest
- **[Shkolobot](https://github.com/iluuua/Shkolobot)** — Telegram bot for teachers: roles, schedule and reporting automation, deployed in Docker
- **[cv](https://github.com/iluuua/cv)** — my résumé: PDF plus the XeLaTeX source it's built from

### Stack

| | |
|---|---|
| **Backend** | Python · FastAPI · Pydantic · asyncio · REST · JWT / OAuth (OIDC) · PostgreSQL · asyncpg · pgvector · Redis · Dramatiq |
| **Infra & ops** | Docker / Compose · nginx · Kubernetes · GitHub Actions · Linux · pytest · ruff · health checks · structured logging · OpenTelemetry |
| **NLP / LLM** | production LLM pipelines · prompt engineering · strict JSON-schema output · RAG · embeddings + pgvector · agents and tool calling · MCP · model routing and fallback · cost / latency |
| **ML / DL** | PyTorch · NumPy · pandas · training from scratch and transfer learning · mixed precision · loss design for the target metric · ResNet / FPN · segmentation |
| **Integrations & foundations** | Telegram MTProto / Telethon · Aiogram · Bitrix24 · Google OAuth · OpenRouter · C++ and competitive-programming algorithms |

---

📬 **[Telegram](https://t.me/Iluuuaaa)** · **[ilyamihailovsy@gmail.com](mailto:ilyamihailovsy@gmail.com)** · open to Python backend and ML/NLP roles
