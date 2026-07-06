# Product Requirements Document (PRD)

# Multi Chatbot Platform with Persistent Memory

Version: 1.0

---

# 1. Project Overview

Develop a full-stack AI-powered Multi Chatbot Platform where authenticated users can interact with multiple specialized AI chatbots from a single application.

Each chatbot maintains independent conversations and long-term memory, allowing personalized and context-aware responses across multiple sessions.

The application should provide a modern UI similar to ChatGPT while supporting multiple AI assistants specialized for different domains.

The platform must be scalable, modular, and follow clean architecture principles.

---

# 2. Objectives

The application must allow users to:

* Register/Login securely
* View available chatbots
* Start unlimited conversations
* Continue previous conversations
* Delete or rename chats
* Store complete conversation history
* Maintain persistent chatbot memory
* Generate AI responses using LLMs
* Retrieve relevant memories before answering
* Support Markdown rendering
* Support code syntax highlighting
* Stream responses (optional)

---

# 3. Technology Stack

## Frontend

* Next.js 15 (App Router)
* TypeScript
* TailwindCSS
* Zustand
* Axios
* React Markdown
* Shadcn UI

---

## Backend

* FastAPI
* Python
* LangChain
* JWT Authentication
* bcrypt Password Hashing

---

## Database

MongoDB Atlas

ODM:

* Motor (Async MongoDB Driver)

---

## AI

* OpenAI / Groq
* LangChain
* HuggingFace Embeddings

---

## Vector Database

Pinecone

---

## Deployment

Frontend

* Vercel

Backend

* Render

Database

* MongoDB Atlas

---

# 4. User Roles

Only one role.

User

Every user can:

* Login
* Chat
* Manage chats
* Edit profile

No admin panel required.

---

# 5. Application Modules

## Module 1

Authentication

Features

* Register
* Login
* JWT Authentication
* Logout
* Password Hashing
* Protected Routes

---

## Module 2

Dashboard

Features

Display

* User Profile
* Search Chatbots
* Available Chatbots
* Recent Conversations

---

## Module 3

Chatbot Selection

Display 8 chatbots

* Coding Assistant
* Study Assistant
* Mental Health Chatbot
* Finance Assistant
* Healthcare Assistant
* Legal Assistant
* Resume Writer
* Entertainment Guide

Every chatbot has

* Name
* Description
* Icon
* System Prompt

---

## Module 4

Chat Interface

Features

* ChatGPT-like UI
* Send Message
* Receive AI Response
* Streaming Response
* Markdown Rendering
* Syntax Highlighting
* Auto Scroll
* Typing Indicator
* Copy Message
* Regenerate Response

---

## Module 5

Conversation Management

Features

* Create Chat
* Rename Chat
* Delete Chat
* Continue Chat
* Search Chats
* Chat History

---

## Module 6

Memory Manager

Every chatbot should remember

* User Preferences
* User Facts
* Frequently Asked Topics
* Long-term Context

Memory Retrieval Flow

User Message

↓

Generate Embedding

↓

Search Pinecone

↓

Retrieve Top Memories

↓

Attach Memory to Prompt

↓

Generate AI Response

↓

Extract Important Facts

↓

Save Memory

---

## Module 7

AI Response Generator

Pipeline

User Input

↓

Load Chat History

↓

Retrieve Memory

↓

Construct Prompt

↓

LLM

↓

Generate Response

↓

Save Conversation

↓

Update Memory

---

## Module 8

Profile

Features

* Update Name
* Update Avatar
* Change Password
* Delete Account

---

# 6. Functional Requirements

Authentication

* JWT Authentication
* Password Hashing
* Protected APIs

---

Chat

* Unlimited Chats
* Unlimited Messages
* Independent Chat Sessions

---

Memory

Each chatbot has independent memory.

Example

Coding Assistant remembers coding discussions only.

Travel Assistant remembers travel discussions only.

---

History

Every message must be stored permanently.

---

AI

Every response should include

* Chat History
* Relevant Memories
* System Prompt

---

# 7. Non Functional Requirements

* Responsive UI
* Modular Code
* Reusable Components
* Clean Folder Structure
* Error Handling
* Loading States
* Optimistic UI
* Secure APIs
* Fast Response Time
* Scalable Architecture

---

# 8. Database Models

## User

```ts
{
_id:ObjectId,

name:string,

email:string,

password:string,

avatar:string,

createdAt:Date,

updatedAt:Date
}
```

---

## Chatbot

```ts
{
_id:ObjectId,

name:string,

description:string,

icon:string,

systemPrompt:string,

category:string,

createdAt:Date
}
```

---

## Chat

```ts
{
_id:ObjectId,

userId:ObjectId,

chatbotId:ObjectId,

title:string,

lastMessage:string,

createdAt:Date,

updatedAt:Date
}
```

---

## Message

```ts
{
_id:ObjectId,

chatId:ObjectId,

role:"user" | "assistant",

content:string,

tokens:number,

createdAt:Date
}
```

---

## Memory

```ts
{
_id:ObjectId,

userId:ObjectId,

chatbotId:ObjectId,

content:string,

embeddingId:string,

importance:number,

sourceChatId:ObjectId,

createdAt:Date
}
```

---

## User Settings

```ts
{
_id:ObjectId,

userId:ObjectId,

theme:string,

defaultChatbot:ObjectId,

language:string
}
```

---

# 9. API Endpoints

Authentication

```
POST /auth/register

POST /auth/login

GET /auth/profile

PUT /auth/profile

PUT /auth/password
```

---

Chatbots

```
GET /chatbots

GET /chatbots/:id
```

---

Chats

```
GET /chats

POST /chats

GET /chats/:id

PUT /chats/:id

DELETE /chats/:id
```

---

Messages

```
GET /messages/:chatId

POST /messages
```

---

Memory

```
POST /memory/store

GET /memory/:chatbotId
```

---

# 10. Folder Structure

## Frontend

```
app/

components/

features/

hooks/

lib/

services/

store/

types/

utils/

public/
```

---

## Backend

```
app/

api/

auth/

chat/

chatbot/

memory/

models/

schemas/

services/

repositories/

core/

utils/

config/

middleware/

database/

prompts/

embeddings/

vectorstore/

main.py
```

---

# 11. AI Workflow

```
User

↓

Authentication

↓

Choose Chatbot

↓

Open Chat

↓

Load Chat History

↓

Generate Embedding

↓

Retrieve Relevant Memories

↓

Combine

System Prompt
+
Chat History
+
Memories
+
Current Message

↓

LLM

↓

Generate Response

↓

Store Message

↓

Extract Important Facts

↓

Store Memory

↓

Return Response
```

---

# 12. Memory Strategy

Memory is **chatbot-specific**, ensuring each chatbot maintains its own context. A user's interactions with the Coding Assistant are isolated from those with the Travel Planner.

The system should:

* Extract meaningful facts from user messages (e.g., preferences, recurring tasks, personal context relevant to the chatbot).
* Generate embeddings for extracted memories using Hugging Face Embeddings.
* Store vectors in Pinecone and metadata in MongoDB.
* Retrieve the top-k relevant memories (e.g., top 5) during each new prompt.
* Update or merge duplicate memories when appropriate.
* Ignore trivial or low-value information.

---

# 13. Security

* JWT Authentication
* Password Hashing using bcrypt
* Environment Variables
* CORS Protection
* Input Validation
* Rate Limiting
* Prompt Injection Protection
* Secure HTTP Headers
* API Authentication Middleware

---

# 14. UI Requirements

The UI should resemble ChatGPT with a clean, responsive design.

### Layout

* Left sidebar containing chatbot selection and conversation history.
* Main chat area with messages.
* Top navigation displaying chatbot name and user profile.
* Mobile-responsive sidebar.

### Chat Experience

* Markdown rendering.
* Code syntax highlighting.
* Copy message button.
* Loading indicator while generating responses.
* Smooth scrolling.
* Dark and light theme support.

---

# 15. Expected Project Structure

### Frontend

* Feature-based architecture.
* Reusable UI components.
* Centralized API service layer.
* Zustand for global state management.
* Route protection for authenticated pages.

### Backend

* Layered architecture:

  * Routers
  * Services
  * Repositories
  * Models
  * Schemas
* Async FastAPI endpoints.
* Dependency injection where appropriate.
* Clear separation of AI logic, database logic, and API routes.

---

# 16. Development Guidelines for AI Code Generation

When generating code, the AI should follow these principles:

* Produce production-ready, modular, and maintainable code.
* Use TypeScript on the frontend and Python type hints on the backend.
* Follow RESTful API conventions.
* Implement robust error handling and validation.
* Use environment variables for secrets and API keys.
* Write reusable components and services.
* Keep frontend and backend decoupled.
* Ensure MongoDB collections are indexed where beneficial (e.g., `userId`, `chatId`, `chatbotId`).
* Use asynchronous database operations throughout the backend.
* Make the codebase easy to extend with new chatbot types, LLM providers, or memory strategies in the future.

---

This PRD is intentionally concise but detailed enough for an AI coding assistant to generate a complete, scalable implementation while minimizing assumptions and ambiguity.
