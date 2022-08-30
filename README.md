# Rong - A console color utility for python console app

#### Developed by [Md. Almas Ali][1]

***Version 1.0.0***

## Installation
It is very easy to install. Like as usual you can install it with `pip`.
```bash
pip install rong
```

## Documentation 

There is 3 main usage of this module at this point.

### Project index's

1. <a href="color-style-text">Color & Style codes</a><br>
2. <a href="log-text">Log class</a><br>
3. <a href="Mark-text">Mark class</a><br>
4. <a href="highlight-text">Highlight class</a><br>
5. <a href="text-text">Text class</a><br>

<br>
<div id="color-style-class"></div>

- All Colors for forground and background:
    - `black`
    - `red`
    - `green`
    - `yellow`
    - `blue`
    - `purple`
    - `cyan`
    - `white`

- All Styles:
    - `underline` : for underlining text in console
    - `bold` : for bolding text in console
    - `clear` : for clearing all setted styles

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

    - To add color manually you need to use this class with some constant color binded into this class. You have to manually start the color as 

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
    Text(text="Single line test", styles=["bold", "underline"])
    ```

<br>

Some sample codes are for text.

```python
# In line Log display 
print(f"I am {Log.waitmsg('Almas')} Ali")

# In line color with custom parameter 
print(f"{Mark.BLUE} Hi, {Mark.END}")

# In line text highlighting 
print(f"Enjoy {Highlight.red('Almas')}")

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
text2 = Text(text='Demo', styles=['clear'])
text2.print()

```


[1]: <https://github.com/Almas-Ali> "Md. Almas Ali"
