# Индиктовый калькулятор | Indiction Calculator
**`Russian`**_"Время идёт кругами. Но ты можешь знать, где находишься"._
**`English`**_"Time goes in circles. But you can know where you are."_
## Описание проекта | Description
**`Russian`**
**Indiction Calculator** - это утилита для перевода года в индиктовую дату и обратно, используя круги Солнцу (КС), круги Луне (КЛ) и индикты.
**Индиктовая дата** — это дата, которая задаётся не одним большим числом, а тремя маленькими числами, имеющими собственные названия: `индикт`, `круг Солнцу`, `круг Луне`.

_Правила использования:_
Каждое из чисел ежегодно увеличивалось на единицу, но как только достигало положенного ему предела, снова сбрасывалось до единицы. Затем число начинало возрастать на единицу снова и так далее.

_Значения чисел:_
`Индикт` — менялся от `1 до 15` и снова сбрасывался на `1`.
`Круг Солнцу` — менялся от `1 до 28` и снова сбрасывался на `1`.
`Круг Луне` — менялся от `1 до 19` и снова сбрасывался на `1`.

**`Пример записи: «данное событие произошло в индикт 14, круг Солнцу 16, круг Луне 19».`**

Поскольку числа-ограничители **15**, **28** и **19** являются взаимно-простыми, то любое их сочетание повторяется только через число лет, равное их произведению: **7980 (15 × 28 × 19)**.

Индиктовый способ летосчисления тесно связан с **юлианским календарем, пасхалией и христианской Пасхой**.

**`English`**
**Indicator Calculator** is a utility for converting a year to an indication date and back using circles to the Sun (CS), circles to the Moon (CL) and indicta.
An indication date is a date that is set not by one large number, but by three small numbers with their own names: `indication`, `circle to the Sun`, `circle to the Moon`.

_Usage rules:_
Each of the numbers increased by one each year, but as soon as it reached its limit, it was reset to one again. Then the number started increasing by one again and so on.

_Values of numbers:_
`The indicator` changed from `1 to 15` and reset to `1` again.
`The circle for the Sun` changed from `1 to 28` and reset to `1` again.
`The circle for the Moon` changed from `1 to 19` and reset to `1` again.

**`An example of an entry: "this event occurred at indication 14, circle to the Sun 16, circle to the Moon 19."`**

Since the limiter numbers **15**, **28**, and **19** are mutually prime, any combination of them repeats only after a number of years equal to their product.: **7980 (15 × 28 × 19).**

The indicative method of chronology is closely related to the **Julian calendar, Paschal calendar, and Christian Easter.**

## Технологии | Technologies

- `Python 3.x` - разрабатывалось на Python 3.13.0 | Developed on Python 3.13.0
- `tkinter` - встроенная библиотека (GUI) | built-in library (GUI)
- `PEP8`

## Установка | Installation

- Клонируйте репозиторий | Clone the repository
`git clone `
- Запустите Python файл `indiction_calculator.py` | Run Python file `indiction_calculator.py`
 
## Как использовать | How to use

**`Russian`**

1. На первой вкладке ("Из года н.э.") введите год нашей эры, и программа переведет его в индиктовую дату.
2. На второй вкладке ("Из индикта") введите значения КС (Круг Солнцу), КЛ (Круг Луне) и Индикта, чтобы получить соответствующий год нашей эры.
3. Калькулятор также отображает год в ЭСМ (эре от сотворения мира).

**`English`**

1. On the first tab ("From A.D.", see Russian translation), enter the year of our era, and the program will convert it to an indication date.
2. On the second tab ("From the indicator", see Russian translation), enter the values of CS (**C**ircle to the **S**un), CM (**C**ircle to the **M**oon) and **Indicator** to get the corresponding year of our era (A.D).
3. The calculator also displays the year in COTW (era from the **C**reation **O**f **T**he **W**orld).

### Пример | Example
- `Введите год | Enter Year A.D.:` **1954**:
- `ЭСМ | COTW:` 7462
- `КС | CS:` 14
- `КЛ | CM:` 14
- `Индикт| Indication:` 7

- `Введите КС| Enter CS:` 14, `КЛ | CM:` 14, `Индикт | Indication:` 7
- `ЭСМ | COTW:` 7462
- `Год нашей эры | The Year A.D.:` 1954
 
## Контрибьютинг | Contributing
**`Russian`**
Проект был разработан для моего отца. 
Если вы хотите помочь мне в улучшении проекта, создайте новый `issue` или отправьте `pull request`. 
Все улучшения приветствуются!

**`English`**
The project was designed for my father. 
If you want to help me improve the project, create a new `issue` or send a `pull request`. 
All improvements are welcome!
