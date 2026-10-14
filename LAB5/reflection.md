# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis?
Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities, and style violations.

## 2. What did the three tools identify?
Pylint identified code-quality issues, including a mutable default argument, missing docstrings, unused variables, and unsafe expression evaluation. Bandit detected security concerns involving eval, MD5, random number generation, shell execution, and a hard-coded token. Flake8 identified formatting violations, an unused import, a bare exception, and unused variables.

## 3. How were the issues fixed?
The code was updated to remove unsafe expression evaluation and shell execution, use SHA-256 and a cryptographically secure PIN generator, validate inputs, remove unused code, and improve documentation and formatting.

## 4. What did you learn?
Different static analysis tools identify different types of problems. Using Pylint, Bandit, and Flake8 together helps improve code quality, security, and maintainability. Rerunning the tools verifies whether the reported problems have been resolved.
