<p align="center">
  <img width="100%" src="https://github.com/AryanK1511/github-echo/blob/main/assets/logo.png?raw=true"><br /><br />
  <strong>A command-line tool built to obtain in-depth, actionable information about GitHub repositories that is often challenging to decipher manually</strong><br /><br />
</p>

<p align="center">
  <a href="https://python.org">
    <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white" alt="Python Version">
  </a>
  <a href="https://github.com/AryanK1511/github-echo">
    <img src="https://img.shields.io/github/stars/AryanK1511/github-echo?style=social" alt="GitHub Stars">
  </a>
  <a href="https://github.com/AryanK1511/github-echo/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/AryanK1511/github-echo" alt="GitHub Contributors">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/github/license/AryanK1511/github-echo" alt="License">
  </a>
  <a href="https://github.com/AryanK1511/github-echo/issues">
    <img src="https://img.shields.io/github/issues/AryanK1511/github-echo" alt="GitHub Issues">
  </a>
</p>

## Table of Contents

- [Usage](#usage)
- [Installing via PyPi](#installing-via-pypi)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions](#setup-instructions)
    - [For macOS/Linux](#for-macoslinux)
    - [For Windows](#for-windows)
- [Running the Tool Locally](#running-the-tool-locally)
  - [Prerequisites](#prerequisites-1)
  - [Setup Instructions](#setup-instructions-1)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Set Up Environment Variables](#2-set-up-environment-variables)
    - [3. Install Required Dependencies](#3-install-required-dependencies)
    - [4. Activate the Virtual Environment](#4-activate-the-virtual-environment)
    - [5. Running the CLI Tool Locally](#5-running-the-cli-tool-locally)
      - [On Windows](#on-windows)
      - [On macOS and Linux](#on-macos-and-linux)
- [Running Using Docker](#running-using-docker)
  - [On Windows](#on-windows-1)
  - [On macOS and Linux](#on-macos-and-linux-1)
- [Troubleshooting](#troubleshooting)
- [Further Usage Instructions](#further-usage-instructions)
  - [Arguments](#arguments)
  - [Options](#options)
- [More about `github-echo`](#more-about-github-echo)
  - [Information drawn from the GitHub API](#information-drawn-from-the-github-api)
  - [Gemini GenAI Integration](#gemini-genai-integration)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Usage

You can use this tool in two ways:

1. **[Install via PyPi](#installing-via-pypi)**: Quickly set up the tool with a simple `pip install`.
2. **[Run Locally](#running-the-tool-locally)**: Clone the repository and run it directly on your machine for development or testing.

## Installing via `PyPi`

### Prerequisites

1. **Python3+**: Ensure `Python3` is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Setup Instructions

1. Open a terminal or command prompt.

2. Install the tool via PyPi:

   ```bash
   pip install gh-echo
   ```

3. Once installed, you need to set the required environment variables in your shell configuration. Here are the steps for different systems:

#### For macOS/Linux

- Open your terminal.
- Add the environment variables to your shell configuration file (e.g., `.bashrc`, `.zshrc`, etc.)

  ```bash
  export GOOGLE_GEMINI_API_KEY='Your Google Gemini API Key'
  export GITHUB_API_TOKEN='Your GitHub API Token'
  export GITHUB_API_VERSION='2022-11-28'
  ```

- Run `source ~/.bashrc` (or `source ~/.zshrc` for Zsh) to apply the changes.

#### For Windows

- Open PowerShell as Administrator.
- Set the environment variables:

  ```powershell
  [System.Environment]::SetEnvironmentVariable('GOOGLE_GEMINI_API_KEY', 'Your Google Gemini API Key', 'User')
  [System.Environment]::SetEnvironmentVariable('GITHUB_API_TOKEN', 'Your GitHub API Token', 'User')
  [System.Environment]::SetEnvironmentVariable('GITHUB_API_VERSION', '2022-11-28', 'User')
  ```

- Now you can run the CLI tool from anywhere in your terminal:

  ```bash
  gh-echo <GITHUB_REPOSITORY_URL> [OPTIONS]
  ```

  Example:

  ```bash
  gh-echo https://github.com/user/repo --output results.md
  ```

## Running the Tool Locally

### Prerequisites

1. **Python3+**: Ensure `Python3` is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. **Git**: Ensure Git is installed. You can download it from [git-scm.com](https://git-scm.com/).
3. **Poetry**: Install Poetry by following the instructions at [poetry.eustace.io](https://python-poetry.org/docs/#installation).

### Setup Instructions

#### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/AryanK1511/github-echo
cd github-echo
```

#### 2. Set Up Environment Variables

For running the tool locally, create a `.env` file in the root of the repository and add the following content:

```text
GOOGLE_GEMINI_API_KEY='Your API Key'
GITHUB_API_TOKEN='Your API Token'
GITHUB_API_VERSION='2022-11-28'
```

- Replace `'Your API Key'` with your [Google Gemini API Key](https://aistudio.google.com/app/apikey).
- Replace `'Your API Token'` with your [GitHub Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

#### 3. Install Required Dependencies

Install the necessary Python packages using Poetry:

```bash
poetry install
```

This will install all required dependencies and set up a virtual environment.

#### 4. Activate the Virtual Environment

Activate the Poetry virtual environment with:

```bash
poetry shell
```

#### 5. Running the CLI Tool Locally

Once the environment is set up and dependencies are installed, you can run the tool locally.

##### On Windows

1. Open Command Prompt or PowerShell.

2. Navigate to the project directory:

   ```cmd
   cd path\to\github-echo
   ```

3. Run the script:

   ```cmd
   python _main.py <GITHUB_REPOSITORY_URL> [OPTIONS]
   ```

   Example:

   ```cmd
   python _main.py https://github.com/user/repo --output results.md
   ```

##### On macOS and Linux

1. Open Terminal.

2. Navigate to the project directory:

   ```bash
   cd /path/to/github-echo
   ```

3. Make the script executable (if needed):

   ```bash
   chmod +x _main.py
   ```

4. Run the script:

   ```bash
   python _main.py <GITHUB_REPOSITORY_URL> [OPTIONS]
   ```

   Example:

   ```bash
   python _main.py https://github.com/user/repo --output results.md
   ```

## Additional Information

- **For Help**: Run `./_main.py --help` or `python _main.py --help` to see the available options and usage instructions.
- **For Version**: Use the `--version` or `-v` flag to get the version number.

## Running Using Docker

> **WARNING:** If you run using Docker, it will deprive you of a lot of features that the command line tool offers. Pretty print becomes unavailable and overall it doesn't look very pretty. It's always recommended to run this tool locally for development purposes.

### Cloning the repo and setting the environment variables

- First, clone the repository to your local machine:

  ```bash
  git clone https://github.com/AryanK1511/github-echo
  cd github-echo
  ```

- Next, navigate to the `Dockerfile` in the root of this repository and fill in the environment variables

```txt
ENV GOOGLE_GEMINI_API_KEY='Your API Key'
ENV GITHUB_API_TOKEN='Your API Key'
ENV GITHUB_API_VERSION='2022-11-28'
```

- Replace `'Your API Key'` with your [Google Gemini API Key](https://aistudio.google.com/app/apikey).
- Replace `'Your API Token'` with your [GitHub Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
- You can leave the `GITHUB_API_VERSION` as is unless you really want to change it.

#### On Windows

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

#### On macOS and Linux

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

## Troubleshooting

- **Invalid GitHub URL**: Ensure the URL is correct and follows the format `https://github.com/owner/repo`.
- **Connection Issues**: Check your internet connection and API tokens.
- **Permission Errors**: On Windows, ensure you have the necessary permissions to run scripts. On macOS/Linux, ensure the script has execution permissions.

## Further Usage Instructions

```bash
_main.py [OPTIONS] GITHUB_REPOSITORY_URL COMMAND [ARGS]..._
```

### Arguments

| Argument                | Tsype | Description                                 | Default | Required |
| ----------------------- | ----- | ------------------------------------------- | ------- | -------- |
| `github_repository_url` | TEXT  | The URL of the GitHub repository to analyze | None    | Yes      |

### Options

| Option      | Shortcut | Type | Description                | Default |
| ----------- | -------- | ---- | -------------------------- | ------- |
| `--version` | `-v`     | Flag | Get the version number     |         |
| `--output`  | `-o`     | PATH | Path to the output file    | None    |
| `--help`    |          | Flag | Show this message and exit |         |

## More about `github-echo`

### Information drawn from the GitHub API

The tool fetches the following key information about GitHub repositories:

- **Repository Metadata**: Name, description, owner, URL, and other basic information.
- **Contributors**: Details about contributors, including their usernames, IDs, and avatars.
- **Issues and Pull Requests**: Information about open and closed issues and pull requests, including titles, states, and comments.
- **Labels**: Labels associated with issues and pull requests.
- **Activity Data**: Data related to repository activity, such as commit history and contributions.

### Gemini GenAI Integration

**Repo Insights** uses Gemini GenAI to analyze the fetched repository data. Gemini GenAI provides advanced capabilities for:

- **Summary Generation**: Creating comprehensive summaries based on the repository data.
- **Insight Extraction**: Identifying key patterns and insights that are not immediately obvious from raw data.

**How It Works**:

1. **Data Fetching**: The tool queries GitHub's API to gather repository data.
2. **Data Processing**: The fetched data is processed and formatted.
3. **AI Analysis**: The processed data is sent to Gemini GenAI, which analyzes it and generates a detailed summary.
4. **Summary Output**: The summary is either displayed in the terminal or saved to a specified file.

## Contributing

We welcome contributions to improve **Repo Insights**. If you have suggestions, bug reports, or enhancements, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

[Aryan Khurana](https://www.github.com/AryanK1511)
