# 🔹 Claude Model Configuration
CLAUDE_MODEL = "claude-3-haiku-20240307"

# 🔹 Token Limits (control cost + performance)
MAX_TOKENS = 1000
MAX_CODE_CHARS = 8000

# 🔹 File Filtering (only review relevant files)
ALLOWED_EXTENSIONS = (".py", ".js", ".java")

# 🔹 Retry Configuration
MAX_RETRIES = 3

# 🔹 Prompt Template (centralized prompt engineering)
PROMPT_TEMPLATE = """
You are a senior software engineer and security reviewer.

Analyze this pull request and provide:

1. 🔴 Critical Bugs
2. 🟡 Performance Issues
3. 🔐 Security Risks
4. 🟢 Code Quality Improvements

Be concise, structured, and actionable.

Code Changes:
{code_changes}
"""

# 🔹 Output Formatting
REVIEW_HEADER = "### 🤖 AutoPR Intelligence Review\n"
