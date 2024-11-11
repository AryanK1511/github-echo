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
</p>

<p align="center">
  <img width="100%" src="https://github.com/AryanK1511/github-echo/blob/main/assets/logo.png?raw=true"><br /><br />
</p>

**A command-line tool built to obtain in-depth, actionable information about GitHub repositories that is often challenging to decipher manually.**

> [!NOTE]
>
> You should have **Python 3+** installed before using this tool. Download from [python.org](https://www.python.org/downloads/).

Check out the [examples](./_examples/README.md) and read the [usage instructions](#usage-instructions) to start using this tool.

![Help Demo](./assets/help-demo.gif)

## Table of Contents

- [Usage Instructions](#usage-instructions)
  - [Installing via PyPI](#installing-via-pypi)
- [Configuration](#configuration)
  - [Config File (`.github-echo.toml`)](#config-file-github-echotoml)
    - [Create the Config File](#create-the-config-file)
    - [Adding API Keys](#adding-api-keys)
    - [Removing the Config File](#removing-the-config-file)
- [Command Structure](#command-structure)
  - [Available Commands](#available-commands)
  - [`analyze` Command](#analyze-command)
    - [Usage](#usage)
    - [Arguments](#arguments)
    - [Options](#options)
    - [Example](#example)
- [Error Handling](#error-handling)
- [Example Run](#example-run)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [License](#license)
- [Author](#author)

## Usage Instructions

### Installing via PyPI

1. **Open Terminal/Command Prompt**.
2. **Install the Tool**:

   ```bash
   pip install gh-echo
   ```

3. **Verify Installation**:
   To check if the tool was installed correctly, run:

   ```bash
   gh-echo --version
   ```

   If successful, this will display the version of the tool.

4. **View Available Commands**:
   To view the commands and their descriptions:

   ```bash
   gh-echo --help
   ```

## Configuration

### Config File (`.github-echo.toml`)

This tool uses a configuration file named `.github-echo.toml` located in your home directory. The file allows you to set default values for various options, such as the LLM to use, token usage, and output file paths.

#### Create the Config File

To generate the `.github-echo.toml` configuration file, use the following command:

```bash
gh-echo init
```

This will create the configuration file at your home directory. The configuration file will look like this:

```toml
[settings]
model = "gemini"
token_usage = true

[api_keys]
# google_gemini_api_key=''
# github_api_token=''
# groq_api_key=''
```

- **model**: The default LLM to use (options: `gemini`, `groq`).
- **token_usage**: A boolean flag indicating whether to track token usage.

#### Adding API Keys

To use **Gemini** or **Groq**, you'll need API keys. You can obtain them from the following sources:

- **Gemini API Key**: [Google Gemini API](https://developers.google.com/ai/gemini)
- **Groq API Key**: [Groq API](https://groq.com/)

Make sure to replace `YOUR_GEMINI_API_KEY` and `YOUR_GROQ_API_KEY` in the configuration file with your actual API keys. If you want to use the GitHub API, you'll also need a GitHub API token. You can generate one [here](https://github.com/settings/tokens).

Add your keys to the `api_keys` section in the `.github-echo.toml` file. You can also choose to provide them as command-line options.

#### Removing the Config File

To remove the `.github-echo.toml` configuration file from your home directory, use the following command:

```bash
gh-echo remove-config
```

## Command Structure

The general command structure for the tool is as follows:

```bash
gh-echo [OPTIONS] COMMAND [ARGS]...
```

You can see a list of available commands by running:

```bash
gh-echo --help
```

### Available Commands

| Command         | Description                                                                       | Example Command                                                       |
| --------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `analyze`       | Analyze a GitHub repository and optionally output the results to a file.          | `gh-echo analyze https://github.com/username/repository -o result.md` |
| `init`          | Create the `.github-echo.toml` config file in the user's home directory.          | `gh-echo init`                                                        |
| `remove-config` | Remove the `.github-echo.toml` configuration file from the user's home directory. | `gh-echo remove-config`                                               |

### `analyze` Command

The `analyze` command analyzes a specified GitHub repository and generates insights. You can configure various options like model choice, temperature setting, and whether to track token usage.

#### Usage

```bash
gh-echo analyze [OPTIONS] GITHUB_REPOSITORY_URL
```

#### Arguments

| Argument                | Description                                  | Required |
| ----------------------- | -------------------------------------------- | -------- |
| `GITHUB_REPOSITORY_URL` | The URL of the GitHub repository to analyze. | Yes      |

#### Options

| Option                    | Description                                                                               | Default  |
| ------------------------- | ----------------------------------------------------------------------------------------- | -------- |
| `-m, --model`             | Choose the LLM to generate insights (`gemini` or `groq`).                                 | `gemini` |
| `-t, --model-temperature` | Set the temperature for the model (ranges from `0.0` to `1.0`).                           | `0.5`    |
| `--show-token-usage`      | Flag to print token usage during the process.                                             | `False`  |
| `-o, --output-file`       | Specify an output file path to save the results. Could be an absolute or a relative path. | `None`   |

#### Example

```bash
gh-echo analyze https://github.com/AryanK1511/github-echo -o result.md -t 0.5 -m gemini --show-token-usage
```

## Error Handling

If you encounter errors, the tool will print relevant messages to the console. For instance, missing configuration files will trigger a warning, and exceptions during the analysis process will be handled and displayed in the console.

## Example Run

Let's walk through an example of using the `analyze` command:

1. First, create the configuration file:

   ```bash
   gh-echo init
   ```

2. Next, use the `analyze` command with the desired options:

   ```bash
   gh-echo analyze https://github.com/AryanK1511/github-echo -o result.md -t 0.5 -m gemini --show-token-usage
   ```

3. This will analyze the specified GitHub repository, use the Gemini model with a temperature of 0.5, and save the results to `result.md`.

This tool is designed to help you easily analyze GitHub repositories and generate insights. By configuring the `.github-echo.toml` file and using the appropriate command-line options, you can customize the analysis process to suit your needs.

For more information:

- [Gemini API](https://developers.google.com/ai/gemini)
- [Groq API](https://groq.com/)
- [GitHub](https://github.com)

## Contributing

For contributions, please refer to the [CONTRIBUTING](./CONTRIBUTING.md) file.

## Code of Conduct

Please read and adhere to our [CODE_OF_CONDUCT](./CODE_OF_CONDUCT.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

[Aryan Khurana](https://www.github.com/AryanK1511)
