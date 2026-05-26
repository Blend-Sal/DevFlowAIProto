# DevFlowAI

**AI-assisted task prioritization for software developers**

DevFlowAI is a prototypical web application that demonstrates how AI can support developers in prioritizing software development tasks.  
It analyzes task metadata and natural language descriptions to generate an explainable priority ranking.

---

## Context
Developed for the university module **“Architectures and Applications of AI Systems”** with a focus on AI integration, system architecture, and explainability.

---

## Features
- Web-based task input
- AI-assisted prioritization
- NLP-based risk estimation
- Weighted scoring model
- Explainable AI output
- Demo tasks included

---

## Architecture
- **Frontend:** HTML / CSS  
- **Backend:** Python + FastAPI  
- **AI Module:** NLP + heuristic scoring  

---

## Technologies
Python, FastAPI, Jinja2, HTML/CSS, Uvicorn

---
## Running the application
uvicorn app:app --reload
## Installation
```bash
git clone https://git.mylab.th-luebeck.de/blend.salihu/DevFlowAI.git
cd DevFlowAI
pip install -r requirements.txt
