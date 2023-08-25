### Hexlet tests and linter status:
[![Actions Status](https://github.com/thiSSSnake/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/thiSSSnake/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/6c3b8084ea84f7da5cdf/maintainability)](https://codeclimate.com/github/thiSSSnake/python-project-49/maintainability)
# BRAIN GAMES
_(5 игр)_

## Установка Poetry
_Poetry - это инструмент для управления зависимостями и пакетирования на Python._
_Этот проект использует этот инструмент, для дальнейшей установки сначала необходимо поставить Poetry_
```bash
# Windows (WSL), Linux, MacOS:
>> curl -sSL https://install.python-poetry.org | python3 -
```
```bash
>> poetry --version
```
## Установка
_Требования для установки:_
- _python = ^3.10_
- _prompt = "^0.4.1"_
- _Чтобы работать с проектом, вам необходимо клонировать репозиторий на свой компьютер. Это делается с помощью команды `git clone`. Клонируйте проект в командной строке:_
```bash
#HTTPS
>> git clone https://github.com/thiSSSnake/python-project-49.git
#SSH
>> git clone git@github.com:thiSSSnake/python-project-49.git
```
_Осталось перейти в нужную директорию и установить пакет:_
```bash
>> cd python-project-49
>> poetry build
>> python3 -m pip install --user dist/*.whl
# Если вы ранее установили пакет и хотите его обновить, используйте следующую команду:
# >> python3 -m pip install --user --принудительная переустановка dist/*.whl
```
## Основные комманды:
-```brain-even``` - Игра-проверка, четное число или нет
-```brain-calc``` - Игра-калькулятор на вычисление выражения
-```brain-gcd``` - Нахождение НОД (Наибольший Общий Делитель)
-```brain-progression``` - Вычисление числа из арифметической прогрессии
-```brain-prime``` - Простое ли число ?

## Первый запуск
[![asciicast](https://asciinema.org/a/YVoWhZrcci15zqkmKcciApNa9.svg)](https://asciinema.org/a/YVoWhZrcci15zqkmKcciApNa9)


---
## Игра Brain Even (Игра-проверка, четное число или нет).

_Игроку выдается случайное число. В ответ принимается либо "yes" если число четное либо "no" если нечетное._

[![asciicast](https://asciinema.org/a/Wk1P9gX6AinhvbXFvBx4mHV7b.svg)](https://asciinema.org/a/Wk1P9gX6AinhvbXFvBx4mHV7b)


## Игра Brain Calc (Игра-калькулятор на вычисление выражения).

_Игроку показывается случайное выражение, кторое нужно вычислить и внести правильный ответ._

[![asciicast](https://asciinema.org/a/3yDamuvv9LDjEe14A8aRemdcP.svg)](https://asciinema.org/a/3yDamuvv9LDjEe14A8aRemdcP)


## Игра Brain GCD (Нахождение НОД (Наибольший Общий Делитель)).

_Игра случайным образом выбирает два любых числа. Игорку нужно вычислить их наибольший общий делитель и внести его в ответ._

[![asciicast](https://asciinema.org/a/vhSopSsF2EC4ppegaRMyWlrm2.svg)](https://asciinema.org/a/vhSopSsF2EC4ppegaRMyWlrm2)


## Игра Brain Progression (Вычисление числа из арифметической прогрессии).

_Игроку показывается арифметическая прогрессия с пропущенным числом. Игроку нужно найти и внести это число в ответ._

[![asciicast](https://asciinema.org/a/unHiQeqaHq9D7OTTVDlYM6EFq.svg)](https://asciinema.org/a/unHiQeqaHq9D7OTTVDlYM6EFq)


## Игра Brain Prime (Простое ли число ?).

_Игра выбирает случайное число. Игроку нужно внести в ответ "yes" если число является простым, и "no" если нет.

[![asciicast](https://asciinema.org/a/rL3mgxlPIvuWQ7E3oZ6EG5kc3.svg)](https://asciinema.org/a/rL3mgxlPIvuWQ7E3oZ6EG5kc3)
