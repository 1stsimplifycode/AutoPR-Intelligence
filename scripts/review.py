import os
import requests
import anthropic

# 🔹 ENV VARIABLES (from GitHub Actions)
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
REPO_NAME = os.environ["REPO_NAME"]
PR_NUMBER = os.environ["PR_NUMBER"]

# 🔹 HEADERS for GitHub API
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# 🔹 STEP 1: Fetch PR files (diffs)
files_url = f"https://api.github.com/repos/{REPO_NAME}/pulls/{PR_NUMBER}/files"
response = requests.get(files_url, headers=headers)

files = response.json()

code_changes = ""

for file in files:
    if "patch" in file:
        code_changes += f"\nFile: {file['filename']}\n{file['patch']}\n"

# ⚠️ Handle empty PR case
if not code_changes:
    code_changes = "No significant code changes found."

# 🔹 STEP 2: Send code to Claude
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

claude_response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": f"""
You are a senior software engineer and security reviewer.

Analyze this pull request and provide:

1. 🔴 Critical Bugs
2. 🟡 Performance Issues
3. 🔐 Security Risks
4. 🟢 Code Quality Improvements

Be concise and structured.

Code Changes:
{code_changes}
"""
        }
    ]
)

# Extract text safely
review_comment = claude_response.content[0].text

# 🔹 STEP 3: Post review comment to PR
comment_url = f"https://api.github.com/repos/{REPO_NAME}/issues/{PR_NUMBER}/comments"

comment_response = requests.post(
    comment_url,
    headers=headers,
    json={"body": review_comment}
)

# 🔹 Debug logs (important)
print("Status Code:", comment_response.status_code)
print("Response:", comment_response.text)
print("Review posted successfully!")
