# 🧠 AutoPR-Intelligence Architecture

## 📌 Overview
AutoPR-Intelligence is an AI-powered DevOps system that automates pull request reviews using Claude. It analyzes code diffs, detects issues, and posts structured feedback directly on GitHub PRs.

---

## ⚙️ System Flow

GitHub Pull Request Event  
        ↓  
GitHub Actions Trigger  
        ↓  
PR Diff Extraction (GitHub API)  
        ↓  
Code Preprocessing (Filtering + Truncation)  
        ↓  
Claude AI Analysis Engine  
        ↓  
Structured Review Generation  
        ↓  
GitHub PR Comment Injection  

---

## 🧩 Core Components

### 1. GitHub Actions (Trigger Layer)
- Listens to PR events (open, update, reopen)
- Executes the AI pipeline automatically
- Provides environment variables (repo, PR number, tokens)

---

### 2. Review Engine (`review.py`)
- Orchestrates the full pipeline
- Fetches PR changes
- Sends data to Claude
- Handles response and posting

---

### 3. Utility Layer (`utils.py`)
- Handles GitHub API interactions
- Extracts relevant code diffs
- Filters file types
- Posts comments back to PR

---

### 4. Configuration Layer (`settings.py`)
- Stores model configuration
- Controls token limits
- Defines prompt templates
- Enables scalable customization

---

### 5. AI Engine (Claude)
- Performs reasoning on code diffs
- Detects:
  - Bugs
  - Security vulnerabilities
  - Performance issues
  - Code quality improvements

---

## 🔄 Data Flow

1. Developer creates or updates a PR  
2. GitHub Actions triggers workflow  
3. System fetches changed files via GitHub API  
4. Relevant diffs are extracted and cleaned  
5. Claude analyzes the code changes  
6. Structured feedback is generated  
7. Feedback is posted as a PR comment  

---

## 🚀 Design Principles

- **Event-Driven Architecture** → Triggered by PR events  
- **Modular Design** → Separation of concerns (utils, config, engine)  
- **Scalable** → Easy to extend with more agents or features  
- **Cost-Efficient** → Uses lightweight model (Haiku)  
- **Secure** → API keys handled via GitHub Secrets  

---

## 🔥 Future Enhancements

- Multi-agent system (security, performance, quality agents)
- Severity scoring (Critical, Warning, Suggestion)
- Multimodal input (logs, screenshots, diagrams)
- Dashboard for review analytics
- Integration with CI/CD pipelines

---

## 🧠 Architecture Summary

AutoPR-Intelligence follows an event-driven AI pipeline where GitHub Actions acts as the trigger, Claude serves as the reasoning engine, and the system automates intelligent code review by injecting insights directly into pull requests.
