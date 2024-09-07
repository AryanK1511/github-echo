# Commands for Distribution

To distribute your package on PyPi, follow these steps.

## Install Build Tools

First, ensure you have the necessary build and distribution tools installed:

```bash
python3 -m pip install build
python3 -m pip install wheel
python3 -m pip install twine
```

## Build the Package

Once the tools are installed, you can build your package. This will create source and wheel distributions under the `dist/` directory:

```bash
python3 -m build
```

This command generates two types of distributions:

- **Source Distribution (sdist)**: A `.tar.gz` file.
- **Wheel Distribution (bdist_wheel)**: A `.whl` file.

## Configure PyPi Credentials

Next, configure your PyPi credentials by adding a `.pypirc` file to your home directory if it doesn't already exist. Open the file using a text editor:

```bash
vi $HOME/.pypirc
```

Add the following content, replacing `pypi-XXX` with your actual PyPi token:

```ini
[pypi]
  username = __token__
  password = pypi-XXX
```

You can generate a PyPi token by visiting the [PyPi API tokens](https://pypi.org/manage/account/#api-tokens) page.

## Upload the Package

Once your package is built and `.pypirc` is configured, you can upload the distribution files to PyPi:

```bash
python3 -m twine upload dist/*
```

This command will prompt for your username and token if not already set in `.pypirc`.

## Verifying the Upload

After uploading, you can verify that your package is live on [PyPi](https://pypi.org/). Simply search for your package by name, or navigate to your project's URL:

```bash
https://pypi.org/project/your-package-name/
```

## Author

[Aryan Khurana](https://www.github.com/AryanK1511)
