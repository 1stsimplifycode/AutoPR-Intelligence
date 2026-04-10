🚀 AutoPR-Intelligence
AI-powered Pull Request Reviewer using Claude that automatically detects bugs, security vulnerabilities, and performance issues directly on GitHub PRs.
---
📌 Overview
AutoPR-Intelligence is an event-driven DevOps tool that integrates GitHub Actions with Claude AI to automate intelligent code reviews. It analyzes pull request diffs and generates structured feedback, improving code quality and reducing manual review effort.
---
⚙️ Features
🤖 Automated PR review using Claude AI
🔐 Detects security vulnerabilities
⚡ Identifies performance issues
🧹 Suggests clean code improvements
🔄 Fully integrated with GitHub Actions
📊 Structured and readable feedback
---
🧠 Architecture
```
GitHub PR Event
      ↓
GitHub Actions
      ↓
PR Diff Extraction
      ↓
Claude AI Analysis
      ↓
Structured Feedback
      ↓
PR Comment Injection
```
---
🛠️ Tech Stack
Python
Claude API (Anthropic)
GitHub Actions
REST APIs
---
🚀 Setup Instructions
1. Clone the repository
```bash
git clone https://github.com/your-username/AutoPR-Intelligence.git
cd AutoPR-Intelligence
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Add GitHub Secrets
Go to:
GitHub → Settings → Secrets → Actions
Add:
```
ANTHROPIC_API_KEY = your_api_key
```
---
⚡ How It Works
Developer creates or updates a Pull Request
GitHub Actions workflow is triggered
System fetches PR code changes
Claude analyzes the code
AI-generated review is posted as a PR comment
---
📸 Demo (Add Later)
Screenshot of PR review comment
Example output
---
🔥 Future Enhancements
Multi-agent review system (security, performance, quality)
Severity scoring (Critical, Warning, Suggestion)
Multimodal input (logs, screenshots)
Dashboard for analytics
---
🧠 Use Case
Designed as an AI-powered DevOps assistant to automate code review workflows and enhance software quality using large language models.
---
🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first.
---
📄 License
MIT License
