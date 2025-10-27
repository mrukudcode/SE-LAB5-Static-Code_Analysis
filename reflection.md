
### Reflection

1. **Which issues were the easiest to fix, and which were the hardest? Why?**
   - The easiest issues to fix were formatting-related, such as adding blank lines between functions and replacing `%` string formatting with f-strings. These were straightforward and didn’t affect program logic.
   - The hardest issue was refactoring the use of the `global` statement in `load_data()`. It required restructuring how data was loaded and updated without breaking the rest of the program. Ensuring input validation without disrupting functionality also required careful attention.

2. **Did the static analysis tools report any false positives? If so, describe one example.**
   - No major false positives were encountered. All flagged issues were valid and contributed to improving the code. However, the warning about using the `global` statement felt contextually acceptable for a small script, even though it’s discouraged in larger applications.

3. **How would you integrate static analysis tools into your actual software development workflow?**
   - I would integrate Pylint, Bandit, and Flake8 into a continuous integration (CI) pipeline using GitHub Actions. Each push or pull request would trigger these tools to automatically check for code quality and security issues.
   - Locally, I would use pre-commit hooks to run Flake8 and Bandit before allowing commits, ensuring that basic issues are caught early during development.

4. **What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**
   - The code is now more readable due to consistent formatting, proper naming conventions, and added docstrings.
   - Robustness improved significantly with input validation and safer file handling using context managers.
   - Security risks like `eval()` and bare `except:` were eliminated, making the code safer and more maintainable.
   - Overall, the code feels cleaner, more professional, and easier to extend or debug in the future.