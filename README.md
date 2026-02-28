# 🎯 QUOTES RECOMMENDATION CHATBOT USING NLP (RASA)

## 📌 Project Overview

The **Quotes Recommendation Chatbot using Rasa NLU** is an intelligent conversational AI system designed to provide personalized quotes based on user intent and preferences. The chatbot understands natural language input and responds with motivational, inspirational, love, success, or humorous quotes through an interactive conversation.

This project demonstrates the practical implementation of **Natural Language Processing (NLP)** and **Conversational AI** using the Rasa framework, along with web deployment using Flask and REST API integration.

---

## 🚀 Key Features

- ✅ Intent Recognition using Rasa NLU
- ✅ Dialogue Management using Rasa Core
- ✅ Multiple Quote Categories:
  - Motivation
  - Inspiration
  - Love
  - Success
  - Funny
- ✅ Interactive Feedback System
- ✅ Fallback Mechanism for Unrecognized Inputs
- ✅ Dynamic Category Selection for "Not Satisfied" Flow
- ✅ Custom Test Stories Configuration
- ✅ REST API Integration
- ✅ Web-based Chat Interface (Flask)
- ✅ Real-time User-Bot Communication
- ✅ Scalable Architecture

---

## 🏗️ System Architecture

User → Web Interface (Flask) → REST API → Rasa NLU → Rasa Core → Response → Web Interface → User

### Components:

- **Rasa NLU** – Intent classification
- **Rasa Core** – Dialogue management
- **Domain.yml** – Intents & responses configuration
- **Stories.yml** – Conversation flow training
- **Rules.yml** – Fixed conversation rules
- **Flask App** – Web interface & API communication
- **Models Directory** – Trained chatbot model storage

---

## 🛠️ Technologies Used

- Python 3.8
- Rasa 3.6.21
- Rasa SDK
- Flask
- REST API
- HTML / CSS / JavaScript
- YAML Configuration Files

---

## 📂 Project Structure

```
QUOTES RECOMMENDATION CHATBOT USING NLP
│
├── actions/
├── data/
│   ├── nlu.yml
│   ├── stories.yml
│   └── rules.yml
│
├── models/
├── templates/
│   └── index.html
│
├── app.py
├── domain.yml
├── config.yml
├── credentials.yml
├── endpoints.yml
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```bash
pip install rasa flask requests
```

### 3️⃣ Initialize Rasa Project (if needed)

```bash
rasa init
```

---

## 🧠 Model Training

Train the chatbot using:

```bash
rasa train
```

This command trains:

- NLU model
- Dialogue management model

Trained model is stored in the `models/` directory.

---

## 🧪 Testing the Chatbot (CLI)

```bash
rasa shell
```

Test different inputs:

- hi
- give me motivation
- inspirational quote
- love quote
- funny quote
- bye

---

## 🌐 Web Deployment

### Step 1: Enable REST API

Ensure `credentials.yml` contains:

```
rest:
```

### Step 2: Run Rasa Server

```bash
rasa run --enable-api --cors "*"
```

### Step 3: Run Flask App

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 📊 Workflow Summary

### Epic 1 – Problem Understanding

- Defined business problem
- Identified user needs
- Conducted literature survey
- Analyzed social and business impact

### Epic 2 – Environment Setup

- Installed Rasa and dependencies
- Initialized project structure

### Epic 3 – Data Collection & Model Building

- Created intents in `nlu.yml`
- Defined responses in `domain.yml`
- Designed conversation flows in `stories.yml`
- Added rules in `rules.yml`
- Trained model

### Epic 4 – Testing & Deployment

- Tested using Rasa Shell
- Validated using test stories
- Deployed via web interface
- Verified frontend-backend integration

---

## 🎯 Business Impact

- Promotes mental well-being
- Provides instant motivational support
- Enhances user engagement
- Demonstrates real-world application of Conversational AI
- Scalable to multiple industries (wellness, education, customer service)

---

## 🔮 Future Enhancements

- Emotion Detection using Sentiment Analysis
- Machine Learning-based Personalization
- Multilingual Support (Hindi, Telugu, etc.)
- Voice-based Interaction
- Social Media Integration (WhatsApp, Telegram)
- Dynamic Quote APIs
- Cloud Deployment & Dockerization
- Analytics Dashboard
- Transformer-based NLP Models (BERT integration)

---

## 🏁 Conclusion

The Quotes Recommendation Chatbot successfully demonstrates the practical implementation of Natural Language Processing and Conversational AI using the Rasa framework. The system provides intelligent, real-time, and context-aware quote recommendations through a web-based interface. The project satisfies all defined requirements, follows structured development milestones, and presents a scalable solution for personalized content delivery.

---

## 👨‍💻 Author

Developed as part of the Artificial Intelligence & Machine Learning module project.

---

## 📜 License

This project is developed for academic and educational purposes.
