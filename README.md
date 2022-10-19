# MLDS_HW1-AutoTrading

In this HW, we will implement a very aged prediction problem from the financial field. Given a series of stock prices, including daily open, high, low, and close prices, decide your daily action and make your best profit for the future trading. Can you beat the simple “buy-and-hold” strategy?

## Description

- [HW1](https://drive.google.com/drive/folders/11DLorGf626qSI7KzHfsz5t5l5otyCHu0?usp=sharing)

## Development

### Suggested **vscode** extension:

1. Python
2. autoDocstring - Python Docstring Generator

### Use `Poetry` to develop

Install **python3.10.0** (recommended use [asdf](https://asdf-vm.com/guide/getting-started.html)) -> 安裝完 asdf 後，可參考 [vivian's notbook](https://hackmd.io/dNnq9rb4SNuWUCbukcT0MQ?view#asdf)

1. init the project: (**vvn 已建立，可跳過**)

   ```bash
   poetry new auto_trading
   ```

2. add a package (ex: pandas)

   ```bash
   poetry add pandas
   ```

   - removes a package from the current list of installed packages

     ```bash
     poetry remove pandas
     ```

   - To list all the available packages

     ```bash
     poetry show
     ```

3. Install dependencies

   - 法一： (若用 poetry -> Install dependencies from lock file)

     ```bash=
     poetry install
     ```

   - 法二： (pip)

     ```bash
     pip install -r requirement.txt
     ```

4. Execute the entrypoint

   - 若有 activate virtual environment (ex: poetry shell)

     ```bash
     python trader.py --training "Training Data" --testing "Testing Data" --output output.csv
     ```

   - 若沒有 activate virtual environment

     ```bash
     poetry run python trader.py
     ```

### update [PyPI](https://pypi.org/) dependencies

- exports the lock file to other formats

  - 法一：

    ```bash=
    poetry export -f requirements.txt --output requirements.txt
    ```

  - 法二： (pip)
    ```bash
    pip freeze > requirement.txt
    ```

## Style

- formatter, [PEP 8](https://www.python.org/dev/peps/pep-0008/)

- linter, [Pylint](https://www.pylint.org/)

## Library

- [autopep8](https://pypi.org/project/autopep8/)
- [pylint](https://pypi.org/project/pylint/)
- [asdf](https://asdf-vm.com/guide/getting-started.html#_1-install-dependencies)
- [poetry](https://python-poetry.org/docs/basic-usage/)
