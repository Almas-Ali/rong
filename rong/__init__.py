'''
Rong - A colorizing console tool for Python 3 (open source)
Developed by Almas Ali
Aim to make console coloring easy and fun for developers. Easy to use and easy to customizable.
'''

__version__ = '0.0.1'

class Log:
	'''Log write color text'''
	
	@staticmethod
	def primary(text:str):
		return f"\033[94m{text}\033[0m"
	
	@staticmethod
	def blue(text:str):
		return f"\033[94m{text}\033[0m"
	
	@staticmethod
	def success(text:str):
		return f"\033[92m{text}\033[0m"
		
	@staticmethod
	def green(text:str):
		return f"\033[92m{text}\033[0m"
	
	@staticmethod
	def ok(text:str):
		return f"\033[92m{text}\033[0m"

	@staticmethod
	def warning(text:str):
		return f"\033[93m{text}\033[0m"
	
	@staticmethod
	def yellow(text:str):
		return f"\033[93m{text}\033[0m"
	
	@staticmethod
	def help(text:str):
		return f"\033[93m{text}\033[0m"
	
	@staticmethod
	def danger(text:str):
		return f"\033[31m{text}\033[0m"
		
	@staticmethod
	def error(text:str):
		return f"\033[31m{text}\033[0m"
	
	@staticmethod
	def fail(text:str):
		return f"\033[31m\033[1m{text}\033[0m"
		
	@staticmethod
	def underline(text:str):
		return f"\033[4m{text}\033[0m"
	
	@staticmethod
	def bold(text:str):
		return f"\033[1m{text}\033[0m"
		
	@staticmethod
	def okmsg(text:str):
		return f"\033[1m\033[92m\u2705 {text}\033[0m"
		
	@staticmethod
	def waitmsg(text:str):
		return f"\033[1m\033[93m\u231b {text}\033[0m"
		
	@staticmethod
	def errormsg(text:str):
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
	
	FG_COLORS = {
		'black' : END,
		'red' : RED,
		'green' : GREEN,
		'yellow' : YELLOW,
		'blue' : BLUE,
		'purple' : PURPLE,
		'cyan' : CYAN,
		'white' : WHITE
	}
	
	BG_COLORS = {
		'black' : '\033[2;40m',
		'red' : '\033[2;41m',
		'green' : '\033[2;42m',
		'yellow' : '\033[2;43m',
		'blue' : '\033[2;44m',
		'purple' : '\033[2;45m',
		'cyan' : '\033[2;46m',
		'white' : '\033[2;47m',
	}
	
	STYLES = {
		'underline' : UNDERLINE,
		'bold' : BOLD,
		'clear' : '\033[2;0m'
	}
		
	
class Highlight:
	'''Background highlighting'''
	
	@staticmethod
	def white(text:str):
		return f"\x1B[3m{text}\033[0m"
		
	@staticmethod
	def bwhite(text:str):
		return f"\x1B[3m\033[1m{text}\033[0m"
	
	@staticmethod
	def green(text:str):
		return f"\x1B[3m\033[92m{text}\033[0m"
		
	@staticmethod
	def bgreen(text:str):
		return f"\x1B[3m\033[1m\033[92m{text}\033[0m"

	@staticmethod
	def blue(text:str):
		return f"\x1B[3m\033[94m{text}\033[0m"
	
	@staticmethod
	def bblue(text:str):
		return f"\x1B[3m\033[1m\033[94m{text}\033[0m"
		
	@staticmethod
	def yellow(text:str):
		return f"\x1B[3m\033[93m{text}\033[0m"
	
	@staticmethod
	def byellow(text:str):
		return f"\x1B[3m\033[1m\033[93m{text}\033[0m"
		
	@staticmethod
	def red(text:str):
		return f"\x1B[3m\033[91m{text}\033[0m"
	
	@staticmethod
	def bred(text:str):
		return f"\x1B[3m\033[1m\033[91m{text}\033[0m"
		

class Text(Mark):
	'''Text a one line color manager'''
	
	def __init__(self, text:str, fg:str = 'white', bg:str = 'black', styles:list = []):
		self.text = text
		self.styles = self.style(styles)
		self.fg = Mark.FG_COLORS.get(fg)
		self.bg = Mark.BG_COLORS.get(bg)
			
	def foreground(self, color:str):
		self.fg = Mark.FG_COLORS.get(color)
	
	def background(self, color:str):
		self.bg = Mark.BG_COLORS.get(color)
	
	def style(self, styles:list):
		self.st:str = ''.join([Mark.STYLES.get(i) for i in styles])
		return self.st
	
	def print(self):
		print(self.fg + self.bg + self.st + self.text + self.END)
		
	def update(self, text:str):
		self.text = text
		
	def __str__(self):
		try:
			return self.fg + self.bg + self.st + self.text + self.END
		except:
			raise "[!] Error"
