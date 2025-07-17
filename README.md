# spark_delta_demo

Local workspace to test Apache Spark with Delta Lake using Python 3.9 and PDM for packaging.

## Stack

- Spark 3.3.3 (with Hadoop 3)
- Delta Lake (manual JAR or delta-spark)
- Python 3.9 (via system install)
- PDM for dependency management
- Ruff + Prettier + Pre-commit
- git-cliff for changelog generation

## Setup

Clone the repo, make sure you have Java 8 or 11, Spark 3.3 or 3.4 for delta compatibility, and Python 3.9 installed.

Then:

```bash
pdm install
pdm run pre-commit install
```

Prettier and git-cliff are installed globally (`npm` or `scoop`).

## Usage

```bash
pdm run format        # Prettier
pdm run lint          # Ruff
pdm run changelog     # git-cliff -> CHANGELOG.md
```


## Notes

* `.venv/` is optional — PDM handles environments
* No Docker for now — testing everything locally first
* Not publishing as a package yet, just internal usage
