# Building and Publishing a Package with Poetry

## 1. **Prepare Your Project**

Ensure your `pyproject.toml` file is correctly configured. Here’s a basic example:

```toml
[tool.poetry]
name = "your-package-name"
version = "0.1.0"
description = "A short description of your package."
authors = ["Your Name <your-email@example.com>"]
license = "MIT"
readme = "README.md"
homepage = "https://github.com/yourusername/your-repo"
repository = "https://github.com/yourusername/your-repo"
keywords = ["keyword1", "keyword2"]

[tool.poetry.dependencies]
python = "^3.9"

[tool.poetry.dev-dependencies]
pytest = "^6.2.5"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

## 2. **Build the Package**

To build your package, use the following command. This will create distribution archives in the `dist/` directory:

```bash
poetry build
```

The `dist/` directory will contain `.tar.gz` and `.whl` files, which are the distribution archives of your package.

## 3. **Publish to PyPI**

To publish your package to the official PyPI repository, you need to have an account on [PyPI](https://pypi.org/). You should also have an API token for authentication.

1. **Add PyPI as a Repository** (if not already set):

   ```bash
   poetry config pypi-token.pypi your-pypi-token
   ```

   Replace `your-pypi-token` with your actual PyPI API token. You can generate a token from your PyPI account settings.

2. **Publish the Package**:

   ```bash
   poetry publish --build
   ```

   This command builds and publishes the package in one step.

### Publishing to TestPyPI

TestPyPI is a separate instance of the Python Package Index used for testing and experimentation. It allows you to test package uploads and installation before publishing to the main PyPI repository.

#### 1. **Create a TestPyPI Account**

Register for an account on [TestPyPI](https://test.pypi.org/). After registering, you’ll receive an API token for publishing.

#### 2. **Configure TestPyPI Repository**

Add TestPyPI as a repository in your Poetry configuration:

```bash
poetry config repositories.testpypi https://test.pypi.org/legacy/
```

Add your TestPyPI token:

```bash
poetry config pypi-token.testpypi your-testpypi-token
```

Replace `your-testpypi-token` with the API token from your TestPyPI account.

#### 3. **Build and Publish to TestPyPI**

To publish to TestPyPI, use the `--repository` option:

```bash
poetry publish --build --repository testpypi
```

This will build your package and publish it to TestPyPI.
