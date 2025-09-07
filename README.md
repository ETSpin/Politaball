# Python Starter Template 🐍

This repository provides a clean, reusable scaffold for Python projects using [Ruff](https://docs.astral.sh/ruff/) for linting and [Visual Studio Code](https://code.visualstudio.com/) for development.

## 📁 Project Structure
python-starter-template/
├── .vscode/              # VS Code workspace settings
│   └── settings.json
├── pyproject.toml        # Ruff configuration
├── .gitignore            # Files to exclude from Git tracking
├── src/                  # Source code lives here
│   └── main.py
└── README.md             # Project overview


## 🧰 Features

- ✅ Preconfigured Ruff linting and formatting
- ✅ Auto-fix on save in VS Code
- ✅ Clean `.gitignore` for Python projects
- ✅ Logical folder structure for scaling up

## 🚀 Usage

To start a new project using this template:

1. Click **"Use this template"** on GitHub
2. Clone your new repo locally
3. Start coding in `src/main.py`
4. Run Ruff via VS Code or CLI:  
   ```bash
   ruff check src/ --fix
   ```
