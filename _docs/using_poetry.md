# Guide to using `poetry` for Python Dependency Management

## **Poetry Installation**

### Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Or with Homebrew (macOS):

```bash
brew install poetry
```

---

## **Initializing a Project**

### Initialize a New Poetry Project

```bash
poetry init
```

It will prompt you for project details and dependencies. To skip the interactive process:

```bash
poetry init --no-interaction
```

### Create a New Project with Default Settings

```bash
poetry new project-name
```

Creates a directory with a standard project structure.

---

## **Virtual Environment Management**

### Start a Shell in the Virtual Environment

```bash
poetry shell
```

### Deactivate the Virtual Environment

```bash
exit
```

### Run Commands in the Virtual Environment without Activating

```bash
poetry run python your_script.py
```

### List Installed Dependencies in the Virtual Environment

```bash
poetry show
```

### Show Dependency Tree (Resolved Dependencies)

```bash
poetry show --tree
```

---

## **Adding Dependencies**

### Add a Dependency

```bash
poetry add <package-name>
```

### Add a Specific Version

```bash
poetry add <package-name>==1.2.3
```

### Add a Dependency with Version Constraint

```bash
poetry add <package-name>^1.2
```

### Add Multiple Dependencies

```bash
poetry add <package1> <package2> <package3>
```

### Add Development Dependency

```bash
poetry add --dev <package-name>
```

### Add Packages from Git, Path, or URL

- **From Git:**

  ```bash
  poetry add git+https://github.com/repository/package.git
  ```

- **From Local Path:**

  ```bash
  poetry add ../path/to/package
  ```

- **From URL:**
  ```bash
  poetry add https://example.com/package.tar.gz
  ```

---

## **Removing Dependencies**

### Remove a Dependency

```bash
poetry remove <package-name>
```

### Remove a Development Dependency

```bash
poetry remove --dev <package-name>
```

---

## **Dependency Locking**

### Update All Dependencies

```bash
poetry update
```

### Update a Specific Dependency

```bash
poetry update <package-name>
```

### Install Dependencies from `poetry.lock`

```bash
poetry install
```

### Install Without Dev Dependencies

```bash
poetry install --no-dev
```

### Remove Unused Dependencies

```bash
poetry install --no-root
```

---

## **Package Versioning**

### Show the Current Version

```bash
poetry version
```

### Set a New Version

```bash
poetry version <new-version>
```

### Automatically Bump Version

- **Patch:** `poetry version patch`
- **Minor:** `poetry version minor`
- **Major:** `poetry version major`

---

## **Testing & Running Code**

### Run Python Scripts Inside Poetry

```bash
poetry run python your_script.py
```

### Run Tests (with pytest or similar)

```bash
poetry run pytest
```

### Run Another Tool in Virtual Environment

```bash
poetry run <tool> [args]
```

---

## **Managing Build & Distribution**

### Build the Package

```bash
poetry build
```

Creates a `.tar.gz` and `.whl` file in the `dist/` directory.

### Publish the Package to PyPI

```bash
poetry publish
```

### Publish to a Test Repository (TestPyPI)

```bash
poetry publish --repository testpypi
```

---

## **Managing Configuration**

### Global Configurations

```bash
poetry config --list
```

### Set Global Configuration

```bash
poetry config <key> <value>
```

For example, to store PyPI tokens:

```bash
poetry config pypi-token.pypi <your-token>
```

---

## **Useful Commands**

### Check for Dependency Conflicts

```bash
poetry check
```

### Export Dependencies to `requirements.txt`

```bash
poetry export --format requirements.txt --output requirements.txt
```

### List All Commands

```bash
poetry help
```

---

## **Using `pyproject.toml`**

### Example `pyproject.toml`:

```toml
[tool.poetry]
name = "my_project"
version = "0.1.0"
description = "My Awesome Project"
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.25.1"

[tool.poetry.dev-dependencies]
pytest = "^6.2.4"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

---

## **Lockfile Management**

### Regenerate the `poetry.lock` File

If you ever delete or need to regenerate the lockfile:

```bash
poetry lock
```

---

### Migrating Existing Projects to Poetry

If you already have a `requirements.txt` file:

```bash
poetry add $(cat requirements.txt)
```
