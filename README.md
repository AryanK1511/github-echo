# GitHub Echo

<p align="left">
  <a href="https://python.org">
    <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white" alt="Python Version">
  </a>
  <a href="https://pypi.org/project/gh-echo/">
    <img src="https://img.shields.io/pypi/v/gh-echo?color=blue&label=pypi%20package" alt="PyPI Version">
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
  <a href="https://youtu.be/bTbETpn7C9I">
    <img src="https://img.shields.io/badge/Watch-Demo-red?logo=youtube" alt="Watch Demo">
  </a>
</p>

<p align="center">
  <img width="100%" src="https://github.com/AryanK1511/github-echo/blob/main/assets/logo.png?raw=true"><br /><br />
</p>

**A command-line tool built to obtain in-depth, actionable information about GitHub repositories that is often challenging to decipher manually.**

> [!NOTE]
>
> You should have **Python 3+** installed before using this tool. Download from [python.org](https://www.python.org/downloads/).

Check out the [examples](./_examples/README.md) to learn more about how to use this tool.

## Table of Contentss

- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Command Structure](#command-structure)
- [TOML File Configuration](#toml-file-configuration)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [License](#license)
- [Author](#author)

## Usage

You can use this tool by installing it from PyPI.

### Installing via PyPI

1. **Open Terminal/Command Prompt**.
2. **Install the Tool**:

   ```bash
   pip install gh-echo
   ```

3. **Set Environment Variables**:

   #### macOS/Linux

   Add the following to your shell config (e.g., `.bashrc`, `.zshrc`):

   ```bash
   export GOOGLE_GEMINI_API_KEY='Your Google Gemini API Key' # Optional
   export GROQ_API_KEY='Your Groq API Key' # Optional
   export GITHUB_API_TOKEN='Your GitHub API Token'
   export GITHUB_API_VERSION='2022-11-28' # Optional
   ```

   Run `source ~/.bashrc` or `source ~/.zshrc`.

   #### Windows

   Open PowerShell and run:

   ```powershell
   [System.Environment]::SetEnvironmentVariable('GOOGLE_GEMINI_API_KEY', 'Your Google Gemini API Key', 'User') # Optional
   [System.Environment]::SetEnvironmentVariable('GROQ_API_KEY', 'Your Groq API Key', 'User') # Optional
   [System.Environment]::SetEnvironmentVariable('GITHUB_API_TOKEN', 'Your GitHub API Token', 'User')
   [System.Environment]::SetEnvironmentVariable('GITHUB_API_VERSION', '2022-11-28', 'User') # Optional
   ```

4. **Run the Tool**:

   ```bash
   gh-echo <GITHUB_REPOSITORY_URL> [OPTIONS]
   ```

   Example:

   ```bash
   gh-echo https://github.com/user/repo --output results.md
   ```

## Troubleshooting

- **Invalid GitHub URL**: Ensure the format is `https://github.com/owner/repo`.
- **Connection Issues**: Check your internet and API tokens.
- **Permission Errors**: Ensure the script has execution permissions.

## Command Structure

```bash
_main.py [OPTIONS] GITHUB_REPOSITORY_URL COMMAND [ARGS]...
```

### Arguments

| Argument                | Type | Description                             | Required |
| ----------------------- | ---- | --------------------------------------- | -------- |
| `github_repository_url` | TEXT | URL of the GitHub repository to analyze | Yes      |

### Options

| Option          | Shortcut | Type   | Description                        | Default |
| --------------- | -------- | ------ | ---------------------------------- | ------- |
| `--version`     | `-v`     | Flag   | Get the version number             | N/A     |
| `--temperature` | `-t`     | Option | Set output randomness (0.0 to 2.0) | 0.5     |
| `--output`      | `-o`     | PATH   | Path to the output file            | None    |
| `--help`        |          | Flag   | Show usage information             | N/A     |
| `--token-usage` |          | Flag   | Display token usage via `stderr`   | N/A     |

## TOML File Configuration

Create a `.github-echo-config.toml` file in your home directory for default settings:

```toml
# Example .github-echo-config.toml
github_repository_url = "https://github.com/username/repository"
model = "gemini" # or "groq"
model_temperature = 0.5
output_file = "/path/to/output/results.md"
token_usage = true
```

- **Path**:
  - Linux/macOS: `~/`
  - Windows: `C:\Users\YourUsername\`

Populate with preferred values for defaults.

## Contributing

For contributions, please refer to the [CONTRIBUTING](./CONTRIBUTING.md) file.

## Code of Conduct

Please read and adhere to our [CODE_OF_CONDUCT](./CODE_OF_CONDUCT.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

[Aryan Khurana](https://www.github.com/AryanK1511)
