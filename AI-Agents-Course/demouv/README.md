# demouv — `uv` quick reference

This file shows common `uv` CLI commands and concise PowerShell examples. The `uv` tool here is presented as a project helper wrapper (project init, venv management, dependency management, and running commands). If your `uv` is an alias for another tool, adapt the examples accordingly.

## Quick examples

- Initialize a new project named `demouv`:

```powershell
uv init demouv
```

- Create / manage a virtual environment for the project:

```powershell
uv venv              # show status or create if missing
uv venv --create     # force-create the venv
uv venv --remove     # remove the venv
```

- Activate the created venv (PowerShell):

```powershell
.venv\Scripts\Activate
```

```cmd
.venv\Scripts\activate.bat
```

- Add a dependency (and update lock/metadata):

```powershell
uv add pandas
uv add pandas==2.2.0
uv add pytest --dev   # add as a dev dependency
```

- Remove a dependency:

```powershell
uv remove pandas
```

- Install all dependencies from the lockfile (CI / fresh clone):

```powershell
uv install
uv sync    # some tools use `sync` synonym
```

- Create or refresh the lockfile (pin versions):

```powershell
uv lock
```

- Update dependencies (all or a single package):

```powershell
uv update           # update everything
uv update pandas    # update only pandas
```

- List or inspect installed packages:

```powershell
uv list
uv show pandas
```

- Run a one-off command inside the project's venv:

```powershell
uv exec python -c "import pandas as pd; print(pd.__version__)"
```

- Run a project entrypoint or module inside the venv:

```powershell
uv run main.py
# or run a module: uv run -m package.cli
```

- Open an interactive shell with the venv activated:

```powershell
uv shell
# then run `python`, `ipython`, or other commands interactively
```

- CLI help:

```powershell
uv help
uv <subcommand> --help
```

## Notes & tips

- Use `--dev` (or the tool-specific dev flag) for developer-only dependencies like test frameworks and linters.
- Prefer creating a lockfile (`uv lock`) after adding/removing packages to ensure reproducible installs.
- If `uv` is an alias for `uvicorn` (ASGI server), use it to run ASGI apps, e.g. `uv main:app --reload --host 127.0.0.1 --port 8000`.
- The examples above mimic common project-manager wrappers; consult `uv help` in your environment for exact flags and behavior.

