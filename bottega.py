import requests

# Function: fetch_commit_data
# Purpose: Fetch commit data from a specified GitHub repository.
# Arguments:
#   - repo_owner (str): The owner of the repository (e.g., 'octocat').
#   - repo_name (str): The name of the repository (e.g., 'Hello-World').
#   - access_token (str): A personal access token for GitHub API authentication.
# Returns:
#   - A list of commit data (dict) if successful.
#   - Example: [{"sha": "abc123", "author": "johndoe", "message": "Initial commit", "date": "2023-01-01T00:00:00Z"}]
#   - On failure, should log an error and return None.
def fetch_commit_data(repo_owner: str, repo_name: str, access_token: str) -> list[dict]:
    """
    1. Build the URL for the GitHub API endpoint for fetching commits.
       Example URL: 'https://api.github.com/repos/{repo_owner}/{repo_name}/commits'

    2. Add the necessary headers for authentication using the access_token.
       Headers format: {'Authorization': f'Bearer {access_token}'}

    3. Make a GET request to the API endpoint.

    4. Handle HTTP errors by checking the response status code.
       Example: If status_code != 200, log the error and return None.

    5. Parse the JSON response to extract relevant commit data fields:
       - SHA (commit identifier)
       - Author (author's username or name)
       - Message (commit message)
       - Date (commit timestamp)

    6. Return the parsed commit data as a list of dictionaries.
       Example output:
       [{"sha": "abc123", "author": "johndoe", "message": "Initial commit", "date": "2023-01-01T00:00:00Z"}]
    """
    pass

# Function: display_commits
# Purpose: Display fetched commit data in a human-readable format.
# Arguments:
#   - commits (list of dict): The list of commit data returned from fetch_commit_data.
#   - limit (int): The maximum number of commits to display (default is 10).
# Returns:
#   - None. Prints commit data to the console.
def display_commits(commits, limit=10):
    """
    1. Check if the commits list is empty or None. If so, print a message like "No commits to display."

    2. Iterate over the commits up to the specified limit.

    3. For each commit, print the following details:
       - SHA (first 7 characters)
       - Author
       - Commit message
       - Date
       Example output:
       Commit: abc1234 | Author: johndoe | Date: 2023-01-01 | Message: Initial commit

    4. Add a separator or footer if there are more commits than the limit to indicate truncation.
    """
    pass

# Main execution flow:
if __name__ == "__main__":
    """
    1. Prompt the user for:
       - GitHub repository owner (e.g., 'octocat')
       - GitHub repository name (e.g., 'Hello-World')
       - Personal access token (to authenticate with the GitHub API)

    2. Call fetch_commit_data with the provided inputs.

    3. If commits are successfully fetched, call display_commits to show them.

    4. Handle edge cases:
       - If the fetch_commit_data function returns None, print a user-friendly error message.
       - If no commits are found, inform the user.
    """
    pass
