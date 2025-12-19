import streamlit as st 
import dotenv
import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
import os
os.environ["GOOGLE_API_KEY"]=os.getenv("gem")

# -------------------Modules selection -------------------------------
modules=["Python","SQL","Power BI","EDA","Machine Learning","Deep Learning","Generative AI","Agentic AI"]

# ------------------------session-state -----------------------------------
if "selected_module" not in st.session_state:
    st.session_state["selected_module"] = None

if "conv" not in st.session_state:
    st.session_state["conv"] = []

if "memory" not in st.session_state:
    st.session_state["memory"] = []

if "feedback" not in st.session_state:
    st.session_state["feedback"] = {}

# --------------------------Main page -----------------------------
if st.session_state["selected_module"] is None:
    st.set_page_config(page_title="AI_Mentor_Chatbot",page_icon="🤖",layout="centered")
    st.title("👋 Welcome to AI Chatbot Mentor")
    st.write("Your personalized AI learning assistant.")
    st.write("Please select a learning module to begin.")

    st.session_state["selected_module"] = st.selectbox( "📌 Select Module", ["-- Select --"] + modules)

    if st.session_state["selected_module"] == "-- Select --":
        st.session_state["selected_module"] = None

    st.stop()

# -------------------- Module Page ------------------------------------------
module = st.session_state["selected_module"]

st.title(f"🎯 {module} AI Mentor")
st.write(f"I am your dedicated mentor for **{module}**.")
st.write("How can I help you today?")

# ----------------- INIT MEMORY FOR MODULE -------------------------
if not st.session_state["memory"]:
    system_prompt = f"""
You are an AI Mentor specialized ONLY in {module}.

Rules:
1. Answer ONLY questions related to {module}.
2. If the question is outside {module}, respond exactly:
   "Sorry, I do not know about this question. Please ask something related to the selected module."
3. Be clear, structured, and educational.
"""
    st.session_state["memory"].append(("system", system_prompt))

# -------------------------- Chat history --------------------------------
for msg in st.session_state["conv"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------------------------- User Query -----------------------------------
prompt = st.chat_input("Type your question")

if prompt:
    st.session_state["conv"].append(
        {"role": "user", "content": prompt}
    )
    st.session_state["memory"].append(("user", prompt))

    with st.chat_message("user"):
        st.write(prompt)

    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

    response = model.invoke(st.session_state["memory"])

    with st.chat_message("ai"):
        st.write(response.content)

    st.session_state["conv"].append({"role": "ai", "content": response.content})
    st.session_state["memory"].append(("ai", response.content))

# ------------------ Download Chat ---------------------------------
if st.session_state["conv"]:
    chat_text = ""
    for msg in st.session_state["conv"]:
        role = "User" if msg["role"] == "user" else "AI Mentor"
        chat_text += f"{role}: {msg['content']}\n\n"

    st.download_button("📥 Download Conversation",chat_text,file_name=f"{module}_Chat.txt", mime="text/plain")
    st.feedback("stars")


