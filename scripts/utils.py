import requests

# 🔹 Fetch PR files from GitHub
def get_pr_files(repo_name, pr_number, headers):
    url = f"https://api.github.com/repos/{repo_name}/pulls/{pr_number}/files"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch PR files: {response.text}")

    return response.json()


# 🔹 Extract only relevant code changes
def extract_code_changes(files):
    code_changes = ""

    for file in files:
        if file["filename"].endswith((".py", ".js", ".java")) and "patch" in file:
            code_changes += f"\nFile: {file['filename']}\n{file['patch']}\n"

    if not code_changes:
        return "No relevant code changes found."

    # Limit size (Claude token safety)
    return code_changes[:8000]


# 🔹 Post comment to PR
def post_comment(repo_name, pr_number, headers, comment):
    url = f"https://api.github.com/repos/{repo_name}/issues/{pr_number}/comments"

    response = requests.post(
        url,
        headers=headers,
        json={"body": comment}
    )

    return response.status_code, response.text
