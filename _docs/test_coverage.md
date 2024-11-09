# Code Coverage

## Run Tests with Coverage Tracking

To run your tests with coverage tracking enabled, use the following command:

```bash
coverage run -m pytest
```

This command runs your tests (assuming you’re using `pytest`) and tracks coverage across your project’s code.

## Generate a Coverage Report

After running your tests, you can generate a report to view the coverage results. There are several options:

### Option A: Terminal Report

To see a simple summary in the terminal:

```bash
coverage report
```

### Option B: HTML Report

For a more detailed view, you can generate an HTML report:

```bash
coverage html
```

This creates an `htmlcov` directory containing HTML files that you can open in a browser. This report shows the percentage coverage for each file and highlights the lines that were not covered by your tests.

### Option C: XML Report

If you need an XML report (e.g., for CI integrations), you can generate one with:

```bash
coverage xml
```

### Step 4: Enforce Coverage Requirements (Optional)

To ensure that your code meets a minimum coverage threshold, you can use the `--fail-under` flag. For example, to enforce 80% minimum coverage:

```bash
coverage report --fail-under=80
```

This will exit with a non-zero status if coverage is below 80%.

### Step 5: Add Coverage to CI Pipeline (Optional)

In a CI/CD pipeline, you can automate coverage tracking and reporting by adding the `coverage` commands in your test script. If using GitHub Actions, you can add steps like these in your `.github/workflows/ci.yml` file:

```yaml
- name: Run tests with coverage
  run: coverage run -m pytest

- name: Generate coverage report
  run: coverage report --fail-under=80
```
