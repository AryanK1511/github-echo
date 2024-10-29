# Contributing to GitHub Echo

First off, thanks for taking the time to contribute! ❤️

All contributions are encouraged and valued! Check the [Table of Contents](#table-of-contents) for ways to help and details on how to contribute. Please read the relevant section before contributing to ensure a smooth experience for everyone. We look forward to your contributions! 🎉

> And if you like the project but just don't have time to contribute, that's fine. There are other easy ways to support the project and show your appreciation:
>
> - Star the project
> - Tweet about it
> - Refer this project in your project's README
> - Mention the project at local meetups and tell your friends/colleagues

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [I Have a Question](#i-have-a-question)
- [Some How Tos](#some-how-tos)
  - [Reporting Bugs](#reporting-bugs)
    - [Before Submitting a Bug Report](#before-submitting-a-bug-report)
    - [How to Submit a Good Bug Report](#how-to-submit-a-good-bug-report)
  - [Suggesting Enhancements](#suggesting-enhancements)
    - [Before Submitting an Enhancement](#before-submitting-an-enhancement)
    - [How to Submit a Good Enhancement Suggestion](#how-to-submit-a-good-enhancement-suggestion)
- [Code Contribution](#code-contribution)
  - [Prerequisites](#prerequisites)
  - [Development Environment](#development-environment)
    - [VSCode Configuration](#vscode-configuration)
    - [Features of the VSCode Configuration](#features-of-the-vscode-configuration)
  - [Setup Instructions](#setup-instructions)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Set Up Environment Variables](#2-set-up-environment-variables)
    - [3. Install Dependencies](#3-install-dependencies)
    - [4. Activate the Virtual Environment](#4-activate-the-virtual-environment)
  - [Running Tests](#running-tests)
  - [Running the Linting Scripts](#running-the-linting-scripts)
  - [Running the project using Docker](#running-the-project-using-docker)
    - [Cloning the repo and setting the environment variables](#cloning-the-repo-and-setting-the-environment-variables)
      - [On Windows](#on-windows)
      - [On macOS and Linux](#on-macos-and-linux)
  - [Making Your Changes](#making-your-changes)
  - [Improving The Documentation](#improving-the-documentation)
- [Styleguides](#styleguides)
  - [Commit Messages](#commit-messages)
- [Join The Project Team](#join-the-project-team)
- [Attribution](#attribution)

## Code of Conduct

This project and everyone participating in it is governed by the [GitHub Echo Code of Conduct](https://github.com/AryanK1511/github-echo/blob/main/CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to <aryankhurana1511@gmail.com>.

## I Have a Question

> If you want to ask a question, we assume that you have read the available [Documentation](https://github.com/AryanK1511/github-echo/blob/main/README.md).

Before you ask a question, it is best to search for existing [Issues](https://github.com/AryanK1511/github-echo/issues) that might help you. If you find a suitable issue but still need clarification, you can write your question there. Additionally, it’s advisable to search the internet for answers first.

If you still need to ask a question, we recommend the following:

- Open an [Issue](https://github.com/AryanK1511/github-echo/issues/new).
- Provide as much context as you can about what you're running into.

We will take care of the issue as soon as possible.

## Some How Tos

### Reporting Bugs

#### Before Submitting a Bug Report

To submit an effective bug report, please follow these steps:

- Ensure you are using the latest version.
- Verify that the issue is a bug and not due to your environment by consulting the [documentation](https://github.com/AryanK1511/github-echo/blob/main/README.md) and the [support section](#i-have-a-question).
- Check the [bug tracker](https://github.com/AryanK1511/github-echo/issues?q=label%3Abug) for similar issues.
- Search online, including Stack Overflow, for discussions about the problem.
- Gather the following information:
  - Stack trace (Traceback)
  - OS, Platform, and Version
  - Interpreter/SDK/Package Manager versions
  - Your input and output
  - Steps to reliably reproduce the issue

#### How to Submit a Good Bug Report

> **Important:** Do not report security issues or sensitive bugs publicly. Email them to <aryankhurana1511@gmail.com> instead.

To report a bug:

- Open an [Issue](https://github.com/AryanK1511/github-echo/issues/new) without labeling it as a bug yet.
- Describe the expected vs. actual behavior.
- Provide detailed reproduction steps, ideally with a reduced test case.
- Include the information you gathered.

After submission:

- The project team will label the issue.
- A team member will try to reproduce it; if details are missing, they will ask you for clarification.
- If reproducible, the issue will be marked for implementation.

### Suggesting Enhancements

This section explains how to suggest enhancements for GitHub Echo, including new features and minor improvements.

#### Before Submitting an Enhancement

- Ensure you are on the latest version.
- Review the [documentation](https://github.com/AryanK1511/github-echo/blob/main/README.md) to confirm the functionality isn't already covered.
- Search the [issues](https://github.com/AryanK1511/github-echo/issues) to see if your suggestion already exists. Comment on the existing issue instead of opening a new one.
- Ensure your idea aligns with the project's goals.

#### How to Submit a Good Enhancement Suggestion

Enhancements are submitted as [GitHub issues](https://github.com/AryanK1511/github-echo/issues).

- Use a **clear, descriptive title** for the suggestion.
- Provide a **detailed step-by-step description** of the enhancement.
- **Describe current behavior** vs. **expected behavior** and the reasoning behind your suggestion.
- Include **screenshots or GIFs** to illustrate the enhancement. Tools like [LiceCap](https://www.cockos.com/licecap/) for macOS/Windows or [silentcast](https://github.com/colinkeenan/silentcast) and [Byzanz](https://github.com/GNOME/byzanz) for Linux can help.
- **Explain the benefit** of the enhancement for GitHub Echo users and reference other projects that address similar needs.

## Code Contribution

### Prerequisites

1. **Python3+**: Ensure `Python3` is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. **Git**: Ensure Git is installed. You can download it from [git-scm.com](https://git-scm.com/).
3. **Poetry**: Install Poetry by following the instructions at [poetry.eustace.io](https://python-poetry.org/docs/#installation).

### Development Environment

This project is built using Visual Studio Code (VSCode) as the primary development environment. We highly recommend using VSCode for building and contributing to this project, as it includes configurations that enhance your coding experience.

#### VSCode Configuration

In the `.vscode` folder, you'll find settings that automatically format your code and ensure consistency across the codebase. Specifically, we use the [Ruff](https://marketplace.visualstudio.com/items?itemName=charliemarsh.ruff) extension by Charlie Marsh, which is a fast linter and formatter for Python.

#### Features of the VSCode Configuration

- **Auto-Save:** Changes are automatically saved, reducing the need to manually save files.
- **Code Formatting:** The project is configured to format code according to our defined standards whenever you save your files, helping to maintain a clean and consistent code style.

To get started, make sure to install the recommended extensions in the `.vscode/extensions.json` file, including Ruff. This setup will help you quickly adapt to the project's style and ensure your contributions are well-formatted.

### Setup Instructions

#### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/AryanK1511/github-echo
cd github-echo
```

#### 2. Set Up Environment Variables

For running the tool locally, create a `.env` file in the root of the repository and add the following content:

```bash
GOOGLE_GEMINI_API_KEY='Your Google Gemini API Key' # If you are using Google Gemini
GROQ_API_KEY='Your Groq API Key' # If you are using Groq's API
GITHUB_API_TOKEN='Your API Token'
GITHUB_API_VERSION='2022-11-28'
```

- Replace `'Your Google Gemini API Key'` with your [Google Gemini API Key](https://aistudio.google.com/app/apikey) if you want to use Google

Gemini.

- Replace `'Your Groq API Key'` with your [Groq API Key](https://www.groq.com/) if you want to use Groq's API.

#### 3. Install Dependencies

After setting up your environment variables, install the required dependencies with Poetry:

```bash
poetry install
```

#### 4. Activate the Virtual Environment

Activate the virtual environment created by Poetry:

```bash
poetry shell
```

### Running Tests

To ensure your changes don't break the code, run the test suite before submitting your contributions:

```bash
pytest
```

### Running the Linting Scripts

To maintain code quality, it's important to run linting scripts before submitting contributions. The GitHub Echo project provides several scripts that you can run using Poetry. Even though we have commit hooks setup, this is a good practice to adopt. Here’s how to use them:

1. **Activate the Virtual Environment**: If you haven't done so already, activate the Poetry virtual environment:

   ```bash
   poetry shell
   ```

2. **Run Linting**: Use the following command to lint all files in the current directory and automatically fix any fixable errors:

   ```bash
   poetry run lint
   ```

3. **Run Formatting**: If you want to format all files in the current directory, use:

   ```bash
   poetry run format
   ```

4. **Lint and Format Together**: To run both linting and formatting in one command, execute:

   ```bash
   poetry run lint-and-format
   ```

By following these steps, you can ensure that your contributions adhere to the project's coding standards.

### Running the project using Docker

> **WARNING:** If you run using Docker, it will deprive you of a lot of features that the command line tool offers. Pretty print becomes unavailable and overall it doesn't look very pretty. It's always recommended to run this tool locally for development purposes.

#### Cloning the repo and setting the environment variables

- First, clone the repository to your local machine:

  ```bash
  git clone https://github.com/AryanK1511/github-echo
  cd github-echo
  ```

- Next, navigate to the `Dockerfile` in the root of this repository and fill in the environment variables

```txt
ENV GOOGLE_GEMINI_API_KEY='Your Google Gemini API Key' # If you are using Google Gemini
ENV GROQ_API_KEY='Your Groq API Key' # If you are using Groq's API
ENV GITHUB_API_TOKEN='Your API Key'
ENV GITHUB_API_VERSION='2022-11-28'
```

- Replace `'Your Google Gemini API Key'` with your [Google Gemini API Key](https://aistudio.google.com/app/apikey) if you want to use Google Gemini LLM to extract insights.
- Replace `'Your Groq API Key'` with your [Groq API Key](https://console.groq.com/keys) if you want to use Groq's API to extract insights.
- Replace `'Your API Token'` with your [GitHub Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
- You can leave the `GITHUB_API_VERSION` as is unless you really want to change it.

##### On Windows

- **Install Docker:** Download and install Docker Desktop from [Docker’s website](https://docs.docker.com/engine/install/).
- **Build the Docker Image:** Open Command Prompt or PowerShell, navigate to the project directory, and build the Docker image:

  ```cmd
  docker build -t gh-echo .
  ```

- **Run the Docker Container:** Once the image is built, you can run a container with the following command:

  ```cmd
  docker run --rm gh-echo <GITHUB_REPOSITORY_URL> [OPTIONS]
  ```

  Example:

  ```cmd
  docker run --rm gh-echo https://github.com/user/repo --output results.md
  ```

##### On macOS and Linux

- **Install Docker:** Follow instructions at [Docker’s website](https://docs.docker.com/engine/install/).
- **Build the Docker Image:** Open Terminal, navigate to the project directory, and build the Docker image:

  ```bash
  docker build -t gh-echo .
  ```

- **Run the Docker Container:** Once the image is built, you can run a container with the following command:

  ```bash
  docker run --rm gh-echo <GITHUB_REPOSITORY_URL> [OPTIONS]
  ```

  Example:

  ```bash
  docker run --rm gh-echo https://github.com/user/repo --output results.md
  ```

### Making Your Changes

Now you can make changes to the code. When you're done, remember to:

1. Commit your changes with a descriptive commit message.
2. Push your changes to your forked repository.
3. Submit a pull request (PR) to the main repository, referencing the issue number you addressed.

### Improving The Documentation

Documentation contributions are welcome! Here are some ways you can help:

- Fix typos, grammar mistakes, or formatting issues in the README or other documentation files.
- Add examples or explanations to help users understand features better.
- Improve the project’s installation instructions or usage guides.

To contribute to the documentation:

1. Follow the same setup instructions as above to clone the repository.
2. Make your changes in the documentation files.
3. Commit and push your changes.
4. Submit a PR.

## Styleguides

### Commit Messages

Use the following format for commit messages:

```bash
[type]: Brief description (imperative mood)

More detailed description if necessary. Explain why the change was made, what was changed, and if it is related to any issues.
```

**Types**:

- `fix`: A bug fix
- `feat`: A new feature
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, etc.)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools and libraries

## Join The Project Team

If you're interested in actively maintaining GitHub Echo, feel free to reach out. The project is open to enthusiastic contributors who want to help manage and improve it.

## Attribution

This guide is adapted from the [Contributing to Open Source](https://opensource.guide/how-to-contribute/) guide.
