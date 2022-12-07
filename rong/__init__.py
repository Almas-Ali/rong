'''
Rong - A colorizing console utility for Python 3 (open source)
Developed by Almas Ali
Aim to make console coloring easy and fun for developers. Easy to use and easy to customizable.
'''

__version__ = '0.0.2'


class Error(Exception):
    '''Base class for other exceptions'''
    pass


class InvalidColorError(Error):
    '''Raised when invalid color is passed.'''
    pass


class InvalidStyleError(Error):
    '''Raised when invalid style is passed.'''
    pass


class InvalidForegroundError(Error):
    '''Raised when invalid forground color is passed.'''
    pass


class InvalidBackgroundError(Error):
    '''Raised when invalid background color is passed.'''
    pass


class Log:
    '''Log write color text'''

    @staticmethod
    def primary(text: str):
        return f"\033[94m{text}\033[0m"

    @staticmethod
    def blue(text: str):
        return f"\033[94m{text}\033[0m"

    @staticmethod
    def success(text: str):
        return f"\033[92m{text}\033[0m"

    @staticmethod
    def green(text: str):
        return f"\033[92m{text}\033[0m"

    @staticmethod
    def ok(text: str):
        return f"\033[92m{text}\033[0m"

    @staticmethod
    def warning(text: str):
        return f"\033[93m{text}\033[0m"

    @staticmethod
    def yellow(text: str):
        return f"\033[93m{text}\033[0m"

    @staticmethod
    def help(text: str):
        return f"\033[93m{text}\033[0m"

    @staticmethod
    def danger(text: str):
        return f"\033[31m{text}\033[0m"

    @staticmethod
    def error(text: str):
        return f"\033[31m{text}\033[0m"

    @staticmethod
    def fail(text: str):
        return f"\033[31m\033[1m{text}\033[0m"

    @staticmethod
    def underline(text: str):
        return f"\033[4m{text}\033[0m"

    @staticmethod
    def bold(text: str):
        return f"\033[1m{text}\033[0m"

    @staticmethod
    def okmsg(text: str):
        return f"\033[1m\033[92m\u2705 {text}\033[0m"

    @staticmethod
    def waitmsg(text: str):
        return f"\033[1m\033[93m\u231b {text}\033[0m"

    @staticmethod
    def errormsg(text: str):
        return f"\033[1m\033[31m\u274C {text}\033[0m"


class Mark:
    '''Mark color text'''

    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'

    ENDC = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    ITALIC = '\x1B[3m'

    HEADER = '\033[95m' + BOLD
    PASS = GREEN + BOLD
    FAIL = RED + BOLD

    OKMSG = BOLD + GREEN + u'\u2705' + "  "
    ERRMSG = BOLD + FAIL + u"\u274C" + "  "
    WAITMSG = BOLD + YELLOW + u'\u231b' + "  "

    HELP = YELLOW
    END = ENDC
    TRANSPARENT = '\033[0m'

    FG_COLORS = {
        'black': END,
        'red': RED,
        'green': GREEN,
        'yellow': YELLOW,
        'blue': BLUE,
        'purple': PURPLE,
        'cyan': CYAN,
        'white': WHITE,
		'orange': '\033[38;5;208m',
		'tomato': '\033[38;5;203m',
		'pink': '\033[38;5;205m',
		'violet': '\033[38;5;99m',
		'gray': '\033[38;5;244m',
		'darkgreen': '\033[38;5;22m',
		'gold': '\033[38;5;220m',
		'yellowgreen': '\033[38;5;154m',
		'sandybrown': '\033[38;5;215m',
		'darkred': '\033[38;5;124m',

		'lightgray': '\033[38;5;250m',
		'lightblue': '\033[38;5;117m',
		'lightgreen': '\033[38;5;118m',
		'lightyellow': '\033[38;5;226m',
		'lightpurple': '\033[38;5;141m',
		'lightcyan': '\033[38;5;123m',
		'lightwhite': '\033[38;5;255m',
		'lightseagreen': '\033[38;5;37m',
		'lightred': '\033[38;5;203m',
		'lightpink': '\033[38;5;217m',
		'lightorange': '\033[38;5;208m',
		'lightviolet': '\033[38;5;99m',
        
		'transparent': TRANSPARENT
    }

    BG_COLORS = {
        'black': '\033[2;40m',
        'red': '\033[2;41m',
        'green': '\033[2;42m',
        'yellow': '\033[2;43m',
        'blue': '\033[2;44m',
        'purple': '\033[2;45m',
        'cyan': '\033[2;46m',
        'white': '\033[2;47m',
		'orange': '\033[2;48;5;208m',
		'tomato': '\033[2;48;5;203m',
		'pink': '\033[2;48;5;205m',
		'violet': '\033[2;48;5;99m',
		'gray': '\033[2;48;5;240m',
		'darkgreen': '\033[2;48;5;22m',
		'gold': '\033[2;48;5;220m',
		'yellowgreen': '\033[2;48;5;154m',
		'lightyellow': '\033[2;48;5;226m',
		'sandybrown': '\033[2;48;5;215m',
		'darkred': '\033[2;48;5;124m',

		'lightgray': '\033[2;48;5;250m',
		'lightblue': '\033[2;48;5;153m',
		'lightgreen': '\033[2;48;5;154m',
		'lightyellow': '\033[2;48;5;227m',
		'lightpurple': '\033[2;48;5;200m',
		'lightcyan': '\033[2;48;5;159m',
		'lightwhite': '\033[2;48;5;255m',
		'lightseagreen': '\033[2;48;5;37m',
		'lightred': '\033[2;48;5;203m',
		'lightpink': '\033[2;48;5;217m',
		'lightorange': '\033[2;48;5;208m',
		'lightviolet': '\033[2;48;5;99m',

        'transparent': '\033[2;49m'
    }

    STYLES = {
        'blink': '\033[5m',
        'bold': BOLD,
        'clear': '\033[2;0m',
		'concealed': '\033[8m',
        'invisible': '\033[8m',
        'italic': ITALIC,
        'overline': '\033[53m',
		'reverse': '\033[7m',
        'strike': '\033[9m',
		'dim': '\033[2m',
		'underline': UNDERLINE,
        'underline-solid': UNDERLINE,
        'underline-wavy': '\033[4:3m' + '\033[58;2;104m',
		'underline-dotted': '\033[4;2m',
		'underline-double': '\033[21m',
		'underline-dashed': '\033[4;3m'
    }


class Highlight:
    '''Background highlighting'''

    @staticmethod
    def white(text: str):
        return f"\x1B[3m{text}\033[0m"

    @staticmethod
    def bwhite(text: str):
        return f"\x1B[3m\033[1m{text}\033[0m"

    @staticmethod
    def green(text: str):
        return f"\x1B[3m\033[92m{text}\033[0m"

    @staticmethod
    def bgreen(text: str):
        return f"\x1B[3m\033[1m\033[92m{text}\033[0m"

    @staticmethod
    def blue(text: str):
        return f"\x1B[3m\033[94m{text}\033[0m"

    @staticmethod
    def bblue(text: str):
        return f"\x1B[3m\033[1m\033[94m{text}\033[0m"

    @staticmethod
    def yellow(text: str):
        return f"\x1B[3m\033[93m{text}\033[0m"

    @staticmethod
    def byellow(text: str):
        return f"\x1B[3m\033[1m\033[93m{text}\033[0m"

    @staticmethod
    def red(text: str):
        return f"\x1B[3m\033[91m{text}\033[0m"

    @staticmethod
    def bred(text: str):
        return f"\x1B[3m\033[1m\033[91m{text}\033[0m"


class Text(Mark):
    '''Text a one line color manager'''

    def __init__(self, text: str, fg: str = 'white', bg: str = 'transparent', styles: list = []):
        self.text = text
        self.styles = self.style(styles)
        self.fg = Mark.FG_COLORS.get(fg)
        self.bg = Mark.BG_COLORS.get(bg)

    def foreground(self, color: str):
        try:
            self.fg = Mark.FG_COLORS[color]
        except:
            raise InvalidForegroundError(
                f"Invalid foreground color: \"{color}\"")

    def background(self, color: str):
        try:
            self.bg = Mark.BG_COLORS[color]
        except:
            raise InvalidBackgroundError(
                f"Invalid background color: \"{color}\"")

    def style(self, styles: list):
        try:
            self.st: str = ''.join([Mark.STYLES[i] for i in styles])
            return self.st
        except:
            raise InvalidStyleError(f"Invalid style: \"{styles}\"")

    def print(self):
        print(self.fg + self.bg + self.st + self.text + self.END)

    def update(self, text: str):
        self.text = text

    def __str__(self):
        try:
            return self.fg + self.bg + self.st + self.text + self.END
        except:
            raise "[!] Error"
