# Rong - A console coloring utility for Python console apps

#### Developed by [Md. Almas Ali][1]

***Version 0.0.2***

[![LICENSE](https://img.shields.io/github/license/dwisiswant0/WiFiID.svg "LICENSE")](LICENSE) <br>
![Image](https://raw.githubusercontent.com/Almas-Ali/rong/master/logo.png)

## Installation
It is very easy to install. Like as usual you can install it with `pip`.
```bash
pip install rong
```

## Documentation 

***Welcome to Rong documentation,*** <br>

Here you will learn about a CLI tool which can add color into your CLI bashed project. Highly recomended module in python by developers. Its easy to use and easily adaptable to every lavel developers. Anyone can learn this in 10 min. <br>
<a href="#examples">Give it a try ?</a>


### Project index's

1. <a href="#color-style-class">Color & Style codes</a><br>
2. <a href="#log-class">Log class</a><br>
3. <a href="#mark-class">Mark class</a><br>
4. <a href="#highlight-class">Highlight class</a><br>
5. <a href="#text-class">Text class</a><br>
6. <a href="#examples">Examples for practice</a><br>
7. <a href="#latestChanges">Latest changes history</a><br>


<div id="color-style-class"></div>

- Color & Styles

    - All Colors for forground and background:
        - `black`
        - `red`
        - `green`
        - `yellow`
        - `blue`
        - `purple`
        - `cyan`
        - `white`
		- `orange`
		- `tomato`
		- `pink`
		- `violet`
		- `gray`
		- `darkgreen`
		- `gold`
		- `yellowgreen`
		- `sandybrown`
		- `darkred`

		- `lightgray`
		- `lightblue`
		- `lightgreen`
		- `lightyellow`
		- `lightpurple`
		- `lightcyan`
		- `lightwhite`
		- `lightseagreen`
		- `lightred`
		- `lightpink`
		- `lightorange`
		- `lightviolet`

		- `transparent`

    - All Styles:
		- `blink` : for blinking text in console
        - `bold` : for bolding text in console
        - `clear` : for clearing all setted styles
		- `concealed` : for concealing text in console
		- `invisible` : for making text invisible in console
		- `italic` : for italicizing text in console
		- `overline` : for overlining text in console
		- `reverse` : for reversing text in console
		- `strike` : for strike text in console
		- `underline` : for underlining text in console
		- `underline-solid` : for solid underlining text in console
		- `underline-wavy` : for wavy underlining text in console
		- `underline-double` : for double underlining text in console
		- `underline-dotted` : for dotted underlining text in console
		- `underline-dashed` : for dashed underlining text in console

	- **NOTE :**
		1. You can use `clear` to clear all setted styles.
		2. When you use `underline` it will be `underline-solid` by default.
		3. `underline-wavy`, `underline-dotted` and `underline-dashed` underline is not supported in all terminals.


<br>
<div id="log-class"></div>

1. `Log` : A simple logging text class for coloring text
	
	- To display primary text `primary(text:str)`

	- To display blue text `blue(text:str)`

	- To display success text `success(text:str)`

	- To display green text `green(text:str)`

	- To display ok text `ok(text:str)`

	- To display warning text `warning(text:str)`

	- To display yellow text `yellow(text:str)`

	- To display help text `help(text:str)`

	- To display danger text `danger(text:str)`

	- To display error text `error(text:str)`

	- To display fail message `fail(text:str)`

	- To display underline `underline(text:str)`

	- To display bold text `bold(text:str)`

	- To display ok message `okmsg(text:str)`

	- To display wait message `waitmsg(text:str)`

	- To display error message `errormsg(text:str)`


<br>
<div id="mark-class"></div>

2. `Mark` : A simple class for coloring manually in line

    - To add color manually you need to use this class with some constant color which is binded into this class. You have to manually start the color as, this example bellow:

    ```python
    print(f"This is a {Mark.GREEN}sample Mark{Mark.END} test.")
    ```

<br>
<div id="highlight-class"></div>

3. `Highlight` : A class for highlighing text color

	- To get white color `white(text:str)`

	- To get bold white color `bwhite(text:str)`

	- To get green color `green(text:str)`

    - To get bold green color `bgreen(text:str)`

	- To get blue color `blue(text:str)`

	- To get bold blue color `bblue(text:str)`

	- To get yellow color `yellow(text:str)`

    - To get bold yellow color `byellow(text:str)`	

	- To get red color `red(text:str)`

	- To get bold red color `bred(text:str)`


<br>
<div id="text-class"></div>

4. Most powerfull, all in one class `Text`

	- To add forground / text color `foreground(color:str)`
	
	- To add backgroung color `background(color:str)`

	- To add styles as list `style(styles:list)`

	- To update object text `update(text:str):`

	- To show output text `print()`

    - All in one in a single line : 
    ```python
    Text(text="Single line test", styles=["bold", "underline-solid"])
    ```

<br>

<div id="examples"></div>

Some sample codes are for text.

```python
from rong import *

# In line Log display 
print(f"I am {Log.waitmsg('Almas')} Ali")
print(f"I am {Log.errormsg('Almas')} Ali")
print(f"I am {Log.warning('Almas')} Ali")
print(f"I am {Log.primary('Almas')} Ali")

# In line color with custom parameter 
print(f"{Mark.BLUE} Hi, {Mark.END}")
print(f"{Mark.RED} Hi, {Mark.END}")
print(f"{Mark.GREEN} Hi, {Mark.END}")
print(f"{Mark.CYAN} Hi, {Mark.END}")
print(f"This is a {Mark.GREEN}sample Mark{Mark.END} test.")

# In line text highlighting 
print(f"Enjoy {Highlight.red('Almas')}")
print(f"Enjoy {Highlight.bred('Almas')}")
print(f"Enjoy {Highlight.blue('Almas')}")
print(f"Enjoy {Highlight.bblue('Almas')}")
print(f"Enjoy {Highlight.yellow('Almas')}")
print(f"Enjoy {Highlight.byellow('Almas')}")

# Working with Text objects 
# Creating Text class object 
text = Text(text='Almas Ali')

# Adding forground color / text color 
text.foreground('blue')
text.foreground('purple')

# Adding background color 
text.background('white')

# Adding custom styles 
text.style(styles=['bold', 'underline'])

# Updating object text 
text.update(text=' New text ')

# Printing output in two ways 
# Advance methode bashed mode 
text.print()
# Normal pythonic mode 
print(text)

# Doing everything in one line
text1 = Text(text='Demo1', styles=['bold'], fg='blue', bg='white')
text1.print()

# Clearing all styles 
text2 = Text(text='Demo', styles=['clear'])
text2.print()
```


<div id="latestChanges"></div>

## Change History :
**0.0.2** - Fixed default background issue, added huge amonut of colors and styles varient. Added more examples and documentation. <br>
**0.0.1** - Initialized this project and written all this codes.

<br>

> Everything is open source. You can contribute in this project by submitting a issue or fixing a problem and make pull request.

<br>
Made with love by © *Md. Almas Ali*
<br>
LICENSE under MIT


[1]: <https://github.com/Almas-Ali> "Md. Almas Ali"
