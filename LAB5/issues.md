# Lab 5: Static Code Analysis — Issues and Fixes

| Issue | Type | Original line | Description | Fix |
|---|---|---:|---|---|
| Mutable default argument | Bug | 15 | A list could be shared across function calls. | Used None as the default and initialized conditionally. |
| Bare exception | Code quality | 26 | Errors were silently suppressed. | Removed broad exception handling and validated inputs. |
| Unsafe eval | Security | 44 | Arbitrary Python expressions could execute. | Replaced eval with direct GPA calculation. |
| Weak MD5 hash | Security | 49 | MD5 is unsuitable for security-sensitive hashing. | Replaced MD5 with SHA-256. |
| Insecure PIN generation | Security | 53 | The standard random generator is not intended for security-sensitive values. | Used the secrets module. |
| Shell command execution | Security | 60 | Shell commands can introduce injection risks. | Removed shell execution. |
| Hard-coded token | Security | 64 | A token-like value was embedded in source. | Read configuration from an environment variable and stopped printing the token. |
| Unused code | Code quality | Various | Unused imports and variables generated warnings. | Removed unused code. |
| Style violations | Style | Various | Missing docstrings and formatting problems reduced readability. | Added docstrings and corrected formatting. |
