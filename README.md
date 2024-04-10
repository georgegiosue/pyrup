# Simple python script to evaluate the feasibility of a software project uses the RUP methodology

## Table of Contents 📚
- [Description](#description)
- [Structure](#structure)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Description 📝

Evaluates the viability of a software project that uses the RUP methodology, considering the following aspects:
- NPV: Net Present Value
- IRR: Internal Rate of Return
- B/C: Benefit/Cost
- TR: Capital Return Rate

Evalua la viabilidad de un proyecto de software que utiliza la metodologia RUP, considerando los siguientes aspectos:
- VAN: Valor Actual Neto
- TIR: Tasa Interna de Retorno
- B/C: Beneficio/Costo
- TR: Tasa de retorno de capital

## Structure 📂

The repository is structured as follows:

```
───eval_project
    ├───main.py
    ├───README.md
    ├───requirements.txt

```

## Getting Started 🚀

### Clone ⬇️

Clone the repository to your local machine

```bash
git clone https://github.com/16george/eval_project.git
```

### Requirements 📋

- Python
- pip
- tkinter

Install tkinter (Linux only)

```bash
# Debian and Ubuntu based distributions
sudo apt-get install python3-tk
```

```bash
# Red Hat and Fedora based distributions
sudo dnf install python3-tkinter
```

### Environment 🛠️

Create a virtual environment to install dependencies in an isolated environment.

```bash
python -m venv venv
```

Activate the virtual environment

```bash
# Windows PowerShell
.\venv\Scripts\activate.ps1
```
```bash
# Linux
source venv/bin/activate
```

Install the dependencies
```bash
pip install -r requirements.txt
```

### Run ▶️

```python
python main.py
```

## Contribution 🤝

Contributions are always welcome. To contribute:

1. Fork the project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## Troubleshooting 🔧

if python is not recognized as an internal or external command, operable program or batch file. Try installing python3 and python-is-python3

```bash
# Debian and Ubuntu based distributions
sudo apt-get install python-is-python3 -y
```

```bash
# Red Hat and Fedora based distributions
sudo dnf install python-is-python3 -y
```

If you encounter any problems while setting up or running the application, please check the [Issues](https://github.com/16george/eval_project/issues) section of this repository to see if your issue has already been addressed. If not, feel free to open a new issue with a description of the problem you're experiencing.

## License 📄
```
MIT License

Copyright (c) 2023 George Giosue

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```