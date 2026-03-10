# review-pr

Review a pull request in the GitHub remote repository.

## Instructions

When the user invokes this skill, review a GitHub pull request. Accept an optional PR number as an argument. If no PR number is provided, list open PRs and ask the user which one to review.

### Steps

1. If a PR number is provided, use it directly. Otherwise, run `gh pr list --repo sgujjar/abc` to show open PRs and ask the user to pick one.
2. Fetch PR details using `gh pr view <number> --repo sgujjar/abc`.
3. Fetch the PR diff using `gh pr diff <number> --repo sgujjar/abc`.
4. Analyze the changes and provide a review covering:
   - **Summary**: A brief description of what the PR does.
   - **File changes**: List of files modified, added, or deleted.
   - **Code quality**: Flag any bugs, security issues, style problems, or anti-patterns.
   - **Suggestions**: Actionable improvements, if any.
5. Present the review in a clear, structured format.
