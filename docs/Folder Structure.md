# Overall Architecture

```
Frontend (Next.js)

        ↓

API Layer (Axios)

        ↓

FastAPI Backend

        ↓

AI Engine

        ↓

MongoDB
+
Pinecone
```

The biggest change I'd make is separating **shared functionality** from **chatbot-specific functionality**.

---

# Backend Folder Structure

```text
backend/
│
├── app/
│
│   ├── main.py
│   ├── dependencies.py
│
│
├── api/
│   │
│   ├── router.py                 # Includes every router
│   │
│   ├── auth.py
│   ├── profile.py
│   ├── chatbot.py
│   ├── chat.py
│   ├── memory.py
│   │
│   └── bots/
│       │
│       ├── coding.py
│       ├── study.py
│       ├── finance.py
│       ├── healthcare.py
│       ├── legal.py
│       ├── resume.py
│       ├── mental_health.py
│       ├── entertainment.py
│
│
├── core/
│   │
│   ├── security.py
│   ├── jwt.py
│   ├── config.py
│   ├── constants.py
│   ├── logger.py
│
│
├── database/
│   │
│   ├── mongodb.py
│   ├── pinecone.py
│
│
├── models/
│   │
│   ├── user.py
│   ├── chatbot.py
│   ├── chat.py
│   ├── message.py
│   ├── memory.py
│   ├── settings.py
│
│
├── schemas/
│   │
│   ├── auth.py
│   ├── user.py
│   ├── chatbot.py
│   ├── chat.py
│   ├── message.py
│   ├── memory.py
│
│
├── repositories/
│   │
│   ├── auth_repository.py
│   ├── chatbot_repository.py
│   ├── chat_repository.py
│   ├── memory_repository.py
│
│
├── services/
│   │
│   ├── auth_service.py
│   ├── chat_service.py
│   ├── chatbot_service.py
│   ├── memory_service.py
│   │
│   └── bots/
│       │
│       ├── coding_service.py
│       ├── study_service.py
│       ├── finance_service.py
│       ├── healthcare_service.py
│       ├── legal_service.py
│       ├── resume_service.py
│       ├── mental_health_service.py
│       ├── entertainment_service.py
│
│
├── ai/
│   │
│   ├── llm.py
│   ├── embeddings.py
│   ├── prompt_builder.py
│   ├── memory_extractor.py
│   ├── memory_retriever.py
│   ├── response_generator.py
│   ├── chatbot_factory.py
│
│
├── prompts/
│   │
│   ├── coding.txt
│   ├── study.txt
│   ├── finance.txt
│   ├── healthcare.txt
│   ├── legal.txt
│   ├── resume.txt
│   ├── entertainment.txt
│   ├── mental_health.txt
│
│
├── middleware/
│   │
│   ├── auth.py
│   ├── rate_limit.py
│   ├── exception.py
│
│
├── utils/
│   │
│   ├── helpers.py
│   ├── validators.py
│   ├── formatter.py
│
│
└── requirements.txt
```

---

# API Folder

This is exactly how I'd organize it.

```text
api/

    auth.py

    chat.py

    chatbot.py

    profile.py

    memory.py

    router.py

    bots/

        coding.py

        study.py

        finance.py

        healthcare.py

        legal.py

        resume.py

        entertainment.py

        mental_health.py
```

Example

```
POST /api/bots/coding/chat

POST /api/bots/study/chat

POST /api/bots/legal/chat

POST /api/bots/finance/chat
```

Every chatbot gets its own API.

---

# Services Folder

Each chatbot has different business logic.

```
services/

    bots/

        coding_service.py

        finance_service.py

        legal_service.py

        study_service.py

        healthcare_service.py

        resume_service.py

        entertainment_service.py

        mental_health_service.py
```

Inside

```
Coding Service

↓

Retrieve Coding Prompt

↓

Retrieve Coding Memory

↓

Call LLM

↓

Return Response
```

---

# Prompts Folder

```
prompts/

coding.txt

study.txt

finance.txt

legal.txt

resume.txt

healthcare.txt

mental_health.txt

entertainment.txt
```

Each chatbot loads only its prompt.

No huge prompt file.

---

# AI Folder

This should contain **generic AI code**, not chatbot code.

```
ai/

llm.py

embeddings.py

prompt_builder.py

response_generator.py

memory_extractor.py

memory_retriever.py

chatbot_factory.py
```

This folder should never know whether it's Coding Assistant or Finance Assistant.

---

# Frontend Folder Structure

```text
frontend/

app/

components/

    ui/

    common/

    layout/

    markdown/

    chat/

features/

    auth/

    dashboard/

    profile/

    chat/

    bots/

        coding/

        study/

        finance/

        healthcare/

        legal/

        resume/

        entertainment/

        mental_health/

services/

    api.ts

    auth.service.ts

    chat.service.ts

    chatbot.service.ts

    memory.service.ts

    bots/

        coding.service.ts

        study.service.ts

        finance.service.ts

        healthcare.service.ts

        legal.service.ts

        resume.service.ts

        entertainment.service.ts

        mental_health.service.ts

hooks/

store/

types/

utils/

lib/

public/
```

---

# Chat Components

```
components/

chat/

ChatWindow.tsx

ChatInput.tsx

MessageBubble.tsx

TypingIndicator.tsx

ChatHeader.tsx

MarkdownRenderer.tsx

CodeBlock.tsx

CopyButton.tsx
```

These are reused by every chatbot.

---

# Feature Folder

```
features/

bots/

coding/

page.tsx

CodingSidebar.tsx

CodingSettings.tsx

CodingHooks.ts

------------------------

finance/

page.tsx

FinanceSidebar.tsx

FinanceSettings.tsx
```

Every chatbot can later have unique UI.

For example

Coding Assistant

* Code Editor

Finance Assistant

* Charts

Healthcare

* File Upload

Legal

* PDF Upload

without affecting other bots.

---

# API Service Folder

```
services/

bots/

coding.service.ts

study.service.ts

finance.service.ts

healthcare.service.ts

legal.service.ts

resume.service.ts

entertainment.service.ts

mental_health.service.ts
```

Example

```ts
class CodingService {

askQuestion()

getChats()

deleteChat()

renameChat()

}
```

---

# Store

```
store/

authStore.ts

chatStore.ts

chatbotStore.ts

memoryStore.ts

themeStore.ts
```

---

# Why this architecture is better

Instead of one massive `chat.py` or `chat_service.py` containing dozens of `if chatbot == "coding"` conditions, each chatbot owns its API, service, prompt, and frontend feature while sharing common infrastructure.

This gives you:

* **Open/Closed Principle**: Add a new chatbot without modifying existing ones.
* **Independent evolution**: A Healthcare bot can support medical document uploads while the Coding bot gains code execution, without cross-impact.
* **Cleaner testing**: Test each chatbot in isolation.
* **Scalability**: Growing from 8 to 100+ chatbots mainly means adding a new folder in `api/bots`, `services/bots`, `prompts`, and `features/bots`.

