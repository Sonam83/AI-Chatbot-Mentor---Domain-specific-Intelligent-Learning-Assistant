# AI-Chatbot-Mentor-Domain-specific-Intelligent-Learning-Assistant

# Project Overview 

AI Chatbot Mentor is an interactive, AI-powered learning assistant designed to provide focused, module-specific mentoring across multiple technical domains.
Unlike generic chatbots, this application strictly restricts responses to the selected learning module, ensuring accurate, relevant, and distraction-free guidance.

# Key Objectives

Deliver domain-restricted AI mentorship

Prevent hallucinated or irrelevant responses

Maintain conversational context throughout a session

Provide a clean, user-friendly learning experience

Enable learners to download chat history for revision and documentation

# Available Learning Modules

Users can select one learning module at a time:

🐍 Python

🗄 SQL

📊 Power BI

📈 Exploratory Data Analysis (EDA)

🤖 Machine Learning (ML)

🧠 Deep Learning (DL)

✨ Generative AI (Gen AI)

🧩 Agentic AI

Each module launches a dedicated AI mentor interface tailored specifically to that domain.

# Technical Architecture
## Backend Logic

Prompt templates per module

Strict domain restriction rules

Session-based conversation memory

Google Gemini LLM invocation via LangChain

## Frontend

Streamlit UI

Module selection interface

Chat-style conversation UI

Download button for conversation history

# Application Flow

1) Welcome Screen
2) Module Selection
3) Module Specific Mentor Interface
4) Question Handling Logic

# Conversation Management

Full chat history is maintained during the session

Each user question and AI response is stored

Enables coherent, continuous mentoring interactions

# Chat History Download 

The application provides a Download Conversation feature at any time.

Downloads entire conversation (User + AI responses)

File format: .txt

Useful for: Revision , Notes preparation , Portfolio documentation , Offline learning


