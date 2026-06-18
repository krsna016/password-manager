# c1-password-manager

[![Language: Python](https://img.shields.io/badge/language-Python-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI Pipeline](https://github.com/krsna016/c1-password-manager/actions/workflows/ci.yml/badge.svg)](https://github.com/krsna016/c1-password-manager/actions/workflows/ci.yml)
[![Security: CodeQL](https://github.com/krsna016/c1-password-manager/actions/workflows/codeql.yml/badge.svg)](https://github.com/krsna016/c1-password-manager/actions/workflows/codeql.yml)

Professional engineering repository configurations deployed inside your GitHub profile.

---

## 📝 Overview & Core Description

Safely manage and store your passwords with this Python-based Password Manager. The project offers a secure and user-friendly interface for storing, retrieving, and generating strong passwords. Tkinter is utilized for the graphical user interface (GUI).

## Overview

Password Manager aims to simplify password management by securely storing passwords using encryption. It provides features such as storing passwords for various accounts, generating strong passwords, and retrieving passwords when needed.

## Features

- **Encryption Algorithms**: Passwords are securely stored using encryption algorithms.
- **User Interface**: Tkinter-based GUI for easy input and retrieval of passwords.
- **Password Generation**: Generate strong and random passwords.
- **Database Storage**: Passwords are stored in a json file (`passwords.json`).

## Project Structure

- `main/Main.py`: Main Python script implementing the password manager with Tkinter.

## Usage

1. **Run the `Main.py` Script:**
   - Execute the `Main.py` script to launch the application.

2. **Set Master Password:**
   - Enter your master password when prompted. This will be used to secure and access your stored passwords.

3. **Save Passwords:**
   - Input service name, username, and password to securely save your passwords.

4. **Retrieve Passwords:**
   - Enter service name and username to retrieve stored passwords.

5. **Generate Passwords:**
   - Click on the "Generate Password" button to create strong and random passwords.

## Configuration

- **No Explicit Configuration Required:**
  - The basic functionality works without additional configuration.
  
- **Security Note:**
  - While the application uses encryption, ensure a strong and unique master password.

## Getting Started

To start using the Password Manager project:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/krsna016/upskill-campus-intern-project-3.git

---

## 🏛️ System Design & Folder Structure
```text
.github/                  # CI/CD pipelines, Dependabot, and Issue/PR schemas
.editorconfig             # Unified file formatting configuration
.gitattributes            # Normalization variables for LF line endings
.gitignore                # Local environment overrides and cache limits
.pre-commit-config.yaml   # Quality check execution triggers
LICENSE                   # Permissive open-source MIT License
Makefile                  # Development workspace orchestrator
CHANGELOG.md              # Historical version tracking
CONTRIBUTING.md           # Developer onboarding guidelines
CODE_OF_CONDUCT.md        # Communication guidelines
SECURITY.md               # Responsible vulnerability disclosures
```

---

## 🛠️ Tooling & Tech Stack
- **Primary Environment:** Python runtime.
- **Workflow Automation:** GitHub Actions CI, Dependabot, and CodeQL.
- **Standards Checkers:** Git `pre-commit` hook validations.

---

## ⚙️ Quickstart & Local Setup
1. Clone this repository locally:
   ```bash
   git clone https://github.com/krsna016/c1-password-manager.git
   cd c1-password-manager
   ```
2. Trigger the local setup runner:
   ```bash
   make help
   ```

---

## 📋 Security & Responsible Disclosure
For details on disclosing vulnerabilities or hardcoded secrets, refer directly to our [SECURITY.md](SECURITY.md) guidelines.

---

## 📜 License
This repository is licensed under the permissive **MIT License**. For details, see the [LICENSE](LICENSE) file.
