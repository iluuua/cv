## Hi, I'm Ilya 👋

**ML / NLP engineer and Python backend developer.** I build production LLM systems — and the services that keep them running.

[![Telegram](https://img.shields.io/badge/Telegram-@Iluuuaaa-2AABEE?logo=telegram&logoColor=white)](https://t.me/Iluuuaaa)
[![Email](https://img.shields.io/badge/Email-ilyamihailovsy@gmail.com-EA4335?logo=gmail&logoColor=white)](mailto:ilyamihailovsy@gmail.com)
[![CV](https://img.shields.io/badge/CV-PDF-333333?logo=readthedocs&logoColor=white)](https://github.com/iluuua/cv)

- 🤖 I own the LLM layer of **[ReachFlow](https://reachflow.tech)** — a B2B SaaS where an AI assistant runs sales conversations in Telegram
- 🏅 **AIDAO 2025 finalist** — top-30 of 248 teams from 14 countries (Yandex Education × HSE Faculty of Computer Science)
- 🐍 Writing **production Python since 2022** — FastAPI, asyncio, PostgreSQL, Redis, Docker
- 🎓 Applied Math & CS @ Moscow Polytechnic University, class of 2029 · 📍 Moscow · English C1

---

### What I work on

**LLM pipelines that survive production.** 8 model calls per incoming message: batch gate, lead-state
classifier (16 event types, each anchored to a message with a confidence), typed fact extraction with a
versioned memory policy, strategist → humanizer → reviewer, send planner. Merged five classifier calls into
two — 14–43% less input at the classification stage, with every section keeping its own failure mode.

**Strict structured output.** A registry of 25 LLM tasks and 22 pydantic JSON schemas with `extra="forbid"`,
schema normalization for provider strict mode, and my own response validation — a schema violation is a
retryable error, never a silent one. Executor with retries, cross-vendor fallback cascade, and a per-attempt
trace of model, latency and cost.

**Routing and tool-using agents.** Domain code names the *role* of a job; the router expands it into
`primary → fallback`, and model ids live only in environment variables. One `ToolSpec` registry is the single
source of truth for the prompt's tool block, the risk-based privilege gate, the trust boundary and an
MCP endpoint.

**The backend underneath.** FastAPI + asyncpg, background workers on Redis + Dramatiq, PostgreSQL with
pgvector, Docker, GitHub Actions CI, deploy and monitoring in prod.

**Models from scratch.** PyTorch, not just API calls: Lift-Splat-Shoot for bird's-eye-view occupancy from
four car cameras — **IoU 0.5606** on the hidden test, against 0.564 for the winning team.

---

### Experience

| | |
|---|---|
| **ReachFlow** — ML/NLP & Backend Engineer | 2026 → now · everything above, plus the infrastructure under it |
| **Freelance Python developer** | 2024 → now · RAG Telegram consultant bot over PostgreSQL vector search with Bitrix24 CRM integration — ~80% of routine customer consultations closed |
| **Near AI** — C++ solutions engineer | 2023 – 2024 · algorithmic C++ as training data for an AI platform, code review in an international team |

### Selected projects

- **[aidao-2025-bev-occupancy](https://github.com/iluuua/aidao-2025-bev-occupancy)** — AIDAO 2025 final: BEV occupancy from 4 cameras, Lift-Splat-Shoot written from scratch in PyTorch
- **[T-bank-CV](https://github.com/iluuua/T-bank-CV)** — logo-detection pipeline for T-Bank
- **[CMI-contest-RNN](https://github.com/iluuua/CMI-contest-RNN)** — reproducible training + inference pipeline for the CMI sensor-data contest
- **[cv](https://github.com/iluuua/cv)** — my résumé: PDF plus the XeLaTeX source it's built from

### Stack

| | |
|---|---|
| **ML / DL** | PyTorch · NumPy · pandas · training from scratch and transfer learning · mixed precision · loss design for the target metric · ResNet / FPN · segmentation |
| **NLP / LLM** | production LLM pipelines · prompt engineering · strict JSON-schema output · RAG · embeddings + pgvector · agents and tool calling · MCP · model routing and fallback · cost / latency |
| **Backend** | Python · FastAPI · asyncio · PostgreSQL / SQL · Redis · Dramatiq · Docker · CI/CD · Linux · pytest |
| **Foundations** | C++ · algorithms, data structures, complexity · probability, statistics, linear algebra, optimization |

---

📬 **[Telegram](https://t.me/Iluuuaaa)** · **[ilyamihailovsy@gmail.com](mailto:ilyamihailovsy@gmail.com)** · open to ML/NLP and Python backend roles
