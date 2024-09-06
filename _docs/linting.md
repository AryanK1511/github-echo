# Using `ruff` to format all files in the project

Ruff is a Python linter and formatter that helps ensure your code adheres to style guidelines and best practices. It aims to be a fast, comprehensive, and user-friendly tool for code quality. Here’s how you can use Ruff in your Python code:

## 1. **Installation**

First, you need to install Ruff. You can do this via pipenv:

```bash
pipenv install ruff --dev
```

This would install `ruff` as a development dependency.

### 2. **Basic Usage**

To check your code for issues, run Ruff from the command line:

```bash
ruff check path/to/your/code
```

For example, to check a file named `main.py`:

```bash
ruff check main.py
```

### 3. **Fixing Issues**

Ruff can also automatically fix some issues. To apply fixes, use the `--fix` option:

```bash
ruff check --fix path/to/your/code
```
