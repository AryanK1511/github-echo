# Contributing to GitHub Echo

First off, thanks for taking the time to contribute! ❤️

All contributions are encouraged and valued! Check the [Table of Contents](#table-of-contents) for ways to help and details on how to contribute. Please read the relevant section before contributing to ensure a smooth experience for everyone. We look forward to your contributions! 🎉

> If you like the project but don’t have time to contribute, here are a few ways you can still show your support:
>
> - Star the project
> - Tweet about it
> - Refer to this project in your README
> - Mention it at meetups and share with friends/colleagues

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [I Have a Question](#i-have-a-question)
- [Some How Tos](#some-how-tos)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
- [Code Contribution](#code-contribution)
  - [Prerequisites](#prerequisites)
  - [Development Environment](#development-environment)
  - [Setup Instructions](#setup-instructions)
  - [Running Tests](#running-tests)
  - [Running the Linting Scripts](#running-the-linting-scripts)
  - [Making Your Changes](#making-your-changes)
  - [Improving Documentation](#improving-documentation)
- [Styleguides](#styleguides)
  - [Commit Messages](#commit-messages)
- [Join The Project Team](#join-the-project-team)
- [Attribution](#attribution)

## Code of Conduct

This project and everyone participating in it is governed by the [GitHub Echo Code of Conduct](https://github.com/AryanK1511/github-echo/blob/main/CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to <aryankhurana1511@gmail.com>.

## I Have a Question

> If you want to ask a question, please ensure you’ve reviewed the [Documentation](https://github.com/AryanK1511/github-echo/blob/main/README.md).

Before opening an issue, it’s helpful to search the [Issues](https://github.com/AryanK1511/github-echo/issues) to see if someone has already asked a similar question. If you find one, feel free to add more details or ask for clarification there. Otherwise, follow these steps:

- Open an [Issue](https://github.com/AryanK1511/github-echo/issues/new).
- Provide as much context as possible regarding the issue.

We will address the issue as soon as possible.

## Some How Tos

### Reporting Bugs

#### Before Submitting a Bug Report

Before submitting a bug report, please:

- Ensure you’re using the latest version.
- Verify that the issue is indeed a bug by checking the [documentation](https://github.com/AryanK1511/github-echo/blob/main/README.md) and existing issues.
- Collect the following information:
  - Stack trace (if applicable)
  - OS, Platform, Version
  - Versions of Python, packages, etc.
  - Steps to reliably reproduce the issue

#### How to Submit a Good Bug Report

- Open an [Issue](https://github.com/AryanK1511/github-echo/issues/new) and describe the bug clearly.
- Include details about the environment and steps to reproduce the issue.
- If the issue relates to security, please email it directly to <aryankhurana1511@gmail.com>.

### Suggesting Enhancements

#### Before Submitting an Enhancement

Before submitting an enhancement, make sure:

- You are on the latest version.
- The feature isn't already covered by the [documentation](https://github.com/AryanK1511/github-echo/blob/main/README.md).
- The suggestion aligns with the project's goals.

#### How to Submit a Good Enhancement Suggestion

- Open an [Issue](https://github.com/AryanK1511/github-echo/issues/new) with a clear, descriptive title.
- Provide a detailed step-by-step description of the enhancement and why it's needed.
- Include any relevant screenshots or GIFs to clarify the suggestion.
- Explain how this enhancement would benefit the project.

## Code Contribution

### Prerequisites

Ensure you have the following:

1. **Python3+**: Install Python3 from [python.org](https://www.python.org/downloads/).
2. **Git**: Install Git from [git-scm.com](https://git-scm.com/).
3. **Poetry**: Install Poetry by following the instructions at [poetry.eustace.io](https://python-poetry.org/docs/#installation).

### Development Environment

This project is built using Visual Studio Code (VSCode) as the primary development environment. Using VSCode will provide automatic formatting and coding standards.

#### Setup Instructions

1. **Clone the Repository**

   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/AryanK1511/github-echo
   cd github-echo
   ```

2. **Set Up Environment Variables**

   Create a `.env` file in the root of the repository and add:

   ```bash
   GOOGLE_GEMINI_API_KEY='Your Google Gemini API Key'
   GROQ_API_KEY='Your Groq API Key'
   GITHUB_API_TOKEN='Your API Token'
   ```

3. **Activate the Virtual Environment**

   Activate the virtual environment:

   ```bash
   poetry shell
   ```

4. **Install Dependencies**

   Install dependencies using Poetry:

   ```bash
   poetry install
   ```

5. **Pre-Commit Hook Setup**

   Set up the pre-commit hook to ensure code quality:

   ```bash
   pre-commit install
   ```

6. **Run the project**
   Here `python _main.py` is equivalent to using the `gh-echo` command.

   ```bash
   python _main.py [OPTIONS] COMMAND [ARGS]...
   ```

### Running Tests

You can run tests in various ways depending on your requirements:

#### Run All Tests

To run all tests, use:

```bash
poetry run run-tests
```

or simply:

```bash
pytest
```

#### Run Tests on Specific Files

To run tests on specific files, provide the file paths as arguments:

```bash
poetry run run-tests-on-files tests/unit/test_file1.py tests/unit/test_file2.py
```

#### Run Tests on Specific Classes

To run tests on specific classes within your test suite:

```bash
poetry run run-tests-on-classes TestClass1 TestClass2
```

#### Run Tests with Coverage

To execute tests while collecting code coverage data:

```bash
poetry run run-coverage
```

After running the above command, you can generate different coverage reports:

- **Generate a Coverage Report in the Terminal**:

  ```bash
  poetry run run-coverage-report
  ```

- **Generate an HTML Coverage Report**:

  ```bash
  poetry run run-coverage-html
  ```

  This will generate an HTML report in a `htmlcov` directory. Open `htmlcov/index.html` in your browser to view a detailed, interactive coverage report.

#### Watch Tests

For automatically re-running tests upon file changes, use **pytest-watch**:

```bash
poetry run watch-tests
```

#### Watch Tests with Coverage

To continuously run tests with coverage every time files change:

```bash
poetry run watch-tests-coverage
```

### Running the Linting Scripts

To run the linting scripts:

1. **Activate the Virtual Environment** (if not already done):

   ```bash
   poetry shell
   ```

2. **Run Linting**:

   ```bash
   poetry run lint
   ```

3. **Run Formatting**:

   ```bash
   poetry run format
   ```

4. **Run Both Linting and Formatting**:

   ```bash
   poetry run lint-and-format
   ```

### Making Your Changes

- Fork the repository, create a feature branch, and make your changes.
- Follow the [Styleguide](#styleguides) to maintain consistent code.

### Improving Documentation

Documentation improvements are welcome! If you see areas that can be clarified, improved, or expanded, feel free to submit a pull request.

## Styleguides

### Commit Messages

When committing changes, follow these guidelines:

1. **Use Present Tense**: Describe what the commit does, not what it did.

   - **Good**: "Fix bug in authentication"
   - **Bad**: "Fixed bug in authentication"

2. **Be Concise but Descriptive**: Provide enough context in the message to understand the change.

   - **Good**: "Add new endpoint for fetching user profile"
   - **Bad**: "Change files"

3. **Separate Subject and Body**: If necessary, provide further explanation in the body.

   - **Good**:

     ```txt
     Add new endpoint for fetching user profile

     This new endpoint allows users to retrieve their profile information. It supports both GET and POST methods.
     ```

4. **Use Semantic Prefixes**: Use prefixes to indicate the type of change.
   - `feat`: A new feature
   - `fix`: A bug fix
   - `docs`: Documentation changes
   - `chore`: Routine tasks (e.g., code refactor, updating dependencies)
   - `test`: Tests

## Join The Project Team

Interested in becoming part of the team? We’re always open to new contributors! If you feel your skills align with our needs, let us know, and we’ll be happy to have you on board.

## Attribution

This project was created and maintained by [Aryan Khurana](https://github.com/AryanK1511).
