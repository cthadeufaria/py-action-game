## About

This repository will contain all code regarding the "software project" curricular unit of fall 2022.


| Directory        | Description                     |       Status       |
|------------------|---------------------------------|:------------------:|
| src              | Online RPG                      |     :warning:      |
| mini-quests/lab1 | Simple CLI-based adventure game | :heavy_check_mark: |
| mini-quests/lab2 | Improved version of Lab1        | :heavy_check_mark: |

---

## Installation

**Easiest option**: Download a compiled binary for your operating system, that can found under the "Releases" section. Then, click the downloaded file to run the game.

**Do it yourself**: You can also run the scripts directly if you have Python 3.8+ and pip installed on your system. 
 - Clone this repository (either via git clone or by downloading a zip file)
 - Run `pip install -r requirements.txt` on the base directory of the repository
 - Then run `python src/main.py` to run the game

**Compiling**: If you want to generate an executable, do the steps above and run `pyinstaller feupscape.spec`. The resulting binary can be found under the `dist/` folder.

---

## Roadmap

| Sprint |  Date  | Description                     |       Status       |
|:------:|:------:|---------------------------------|:------------------:|
|   1    | Oct 16 | Use Case Diagram                | :heavy_check_mark: |
|   1    | Oct 16 | Product Vision + P. V. Board    | :heavy_check_mark: |
|   1    | Oct 16 | Product Backlog (User Stories)  | :heavy_check_mark: |
|   1    | Oct 16 | Class Diagram                   | :heavy_check_mark: |
|   2    | Oct 30 | UI Mockups                      | :heavy_check_mark: |
|   2    | Oct 30 | Acceptance Tests                | :heavy_check_mark: |
|   2    | Oct 30 | Sprint #2 (review and planning) | :heavy_check_mark: |
|   3    | Oct 30 | Sprint #3 (review and planning) | :heavy_check_mark: |
|   4    | Nov 13 | Component/Package Diagram       |        :x:         |
|   4    | Nov 13 | Deployment Diagram              |        :x:         |
|   4    | Nov 13 | State Diagram                   |        :x:         |
|   4    | Nov 13 | Sequence Diagram                | :heavy_check_mark: |
|   4    | Nov 13 | Sprint #4 (review and planning) | :heavy_check_mark: |
|   5    | Nov 27 | Source Code / Gitlab mng.       |        :x:         |
|   5    | Nov 27 | Unit Tests                      | :heavy_check_mark: |
|   5    | Nov 27 | Sprint #5 (review and planning) |        :x:         |
| Final  | Dec 11 | Installation Instructions       |        :x:         |
| Final  | Dec 11 | User Manual                     |        :x:         |
| Final  | Dec 11 | Product Complexity / Features   |        :x:         |
| Final  | Dec 11 | Product Delivery (presentation) |        :x:         |

## Contribution guide
 - Object-Oriented Programming
 - Always use type annotations
 - Use docstrings for classes and methods
 - One branch for each contributor, PRs should be reviewed by another maintainer
 - PRs named after milestones

## Libraries
 - User interface: pygame
 - Multithreading: multiprocessing
 - Bundling: pyinstaller

## DevOps
 - Code formatting with [Black](https://github.com/python/black)
 - Linting with [Flake8](http://flake8.pycqa.org/en/latest/) + Docstrings [extension](https://pypi.org/project/flake8-docstrings/)
 - Type checking with [mypy](http://mypy-lang.org/)
 - Automatic documentation with [pdoc](https://pdoc.dev/)

## Tools
 - OS: Arch, Ubuntu, Windows 11
 - IDE: PyCharm, VSCode
 - Shell: Bash, Powershell
 - Scripting: Python
 - Diagrams: [Miro](https://miro.com/)
 - Project management: Gitlab wiki and issues
 - Wiki: Markdown
 - UI Mockups: Figma
 - Art: GIMP
