# Handy cheatsheet for `pipenv`:

## Basic Commands

- **Install Pipenv**

  ```bash
    pip install pipenv
  ```

- **Initialize a New Project**

  ```bash
    pipenv install
  ```

- **Install a Package**

  ```bash
    pipenv install <package-name>
  ```

- **Install a Package as a Development Dependency**
  
  ```bash
    pipenv install <package-name> --dev
  ```

- **Uninstall a Package**
  
  ```bash
    pipenv uninstall <package-name>
  ```

- **Update All Packages**
  
  ```bash
    pipenv update
  ```

- **Generate or Update `Pipfile.lock`**

  ```bash
    pipenv lock
  ```

- **Run a Command Inside the Virtual Environment**

  ```bash
    pipenv run <command>
  ```

- **Activate the Virtual Environment**

  ```bash
    pipenv shell
  ```

- **Deactivate the Virtual Environment**

  ```bash
    exit
  ```

- **Check Installed Packages**

  ```bash
    pipenv graph
  ```

- **Check for Security Vulnerabilities**

  ```bash
    pipenv check
  ```

### Advanced Usage

- **Install from a `requirements.txt`**

  ```bash
    pipenv install -r requirements.txt
  ```

- **Uninstall All Packages**

  ```bash
    pipenv clean
  ```

- **Run Tests**

  ```bash
    pipenv run pytest
  ```
