
# Feedback Streamlit App with Agno Agent

## 📌 Project Overview

This project implements a **user feedback system** for an application. Users can submit feedback including their **username**, **email**, the **issue they faced**, and optional **suggestions**.

The feedback is analyzed using an **AI agent** powered by the **Agno framework** with the **Groq model (gemma2-9b-it)**, which generates potential **technical causes** for the issue. All inputs and analysis results are stored in a CSV file for future reference.

The application provides a **Streamlit-based UI** for user interaction and a modular backend with an AI agent wrapper. It helps support teams troubleshoot faster by automatically identifying possible root causes.

---

## 🏗️ System Architecture

```
User (Web UI) ──> Streamlit UI ──> Agent Wrapper ──> Groq API (gemma2-9b-it)
       │                                    │
       └──────────<── CSV Storage <─────────┘
```

* **Streamlit UI**: Collects feedback input from users
* **Agent Wrapper**: Communicates with Groq API, formats prompt and handles response
* **Groq Model API**: Uses `gemma2-9b-it` for analyzing issue descriptions
* **CSV Storage**: Stores user input and AI-generated analysis

---

## 🧰 Selected Tech Stack

| Component          | Technology                | Purpose                                    |
| ------------------ | ------------------------- | ------------------------------------------ |
| Frontend UI        | Streamlit                 | Web app interface to collect user feedback |
| Backend AI Agent   | Agno Framework + Groq API | Interface with Groq's language model       |
| Language Model     | gemma2-9b-it (Groq)       | Analyze and extract issue causes           |
| Environment Config | `python-dotenv`           | Load environment variables (API key)       |
| Data Storage       | CSV file                  | Lightweight storage of feedback + analysis |
| Programming Lang.  | Python                    | Core implementation language               |

---

## 🔁 Workflow Outline

1. **User Accesses Feedback Form**
   Streamlit UI collects `username`, `email`, `issue description`, and optional `suggestions`.

2. **Submit Feedback**
   On clicking submit, the frontend sends the issue to the agent wrapper.

3. **Agent Processing**
   The wrapper formats and sends the input to the Groq API (`gemma2-9b-it`) for analysis.

4. **Receive Response**
   The agent returns possible technical causes based on the issue description.

5. **Store Feedback**
   The user input and AI analysis are saved in a `CSV` file.

6. **Display Confirmation**
   Streamlit confirms successful submission and displays the generated causes.

---

## 📁 Project Structure

```
feedback_project/
├── app.py                 # Streamlit frontend application
├── agent_wrapper.py       # Agno agent integration with Groq model
├── feedback_data.csv      # Stored feedback and AI analysis
├── requirements.txt       # Required Python libraries
├── .env                   # Contains GROQ_API_KEY (not to be shared)
└── README.md              # Project documentation (you’re reading it!)
```

---

## 📈 Next Steps & Improvements

### 🔗 Backend Integration

* **Integrate FastAPI** as a RESTful backend to:

  * Decouple UI from AI logic
  * Support multi-client access
  * Create secure API endpoints

### 🗃️ Persistent Storage

* Replace CSV with **SQLite**, **PostgreSQL**, or **MongoDB** for:

  * Efficient queries and filtering
  * Backup and integrity support
  * Better concurrency handling

### 🧠 Enhanced Prompting

* Improve prompt design to:

  * Support diverse issue types
  * Handle multilingual inputs
  * Increase analysis accuracy

### 🎨 UI/UX Enhancements

* Add:

  * Input validation and email format checks
  * Feedback history view (dashboard)
  * Export options: Excel or PDF

### 🔐 Authentication & Security

* Add:

  * CAPTCHA or login for spam prevention
  * Secure access to API endpoints

### 📊 Logging & Monitoring

* Integrate logs for:

  * API call tracking
  * Agent errors and usage reports
