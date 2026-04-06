import os, sys
from loggerFunctions import *
import atexit
from pathlib import Path
import json
import shutil




class InitProject:
	def __init__(self):
		self.config = None
		self.CONFIG_PATH = Path("prefs/config.json")



	def CheckArgsConditions(self):
		if len(sys.argv) == 1:
			inform_error("Необхідно вказати назву проекту!")
			exit()
		else:
			name = sys.argv[1]
			if "/" in name or "\\" in name:
				inform_error("Недопустима назва!")
				exit()
			else:
				path = Path("../", name).resolve()
				path_tools = Path("../", name + "_Tools").resolve()
				inform(f"Перевірка шляху {path_tools}")

				if path_tools.exists():
					inform_warning(f"Директорія {path_tools} буде повністю очищена!")
					try:
						shutil.rmtree(path_tools)
						path_tools.mkdir()
						inform_ok(f"Директорія {path_tools} очищена!")
					except Exception as e:
						inform_error(f"Поилка створення директорії {path_tools}")
						inform_error(e)
						exit()
				else:
					try: 
						path_tools.mkdir()
						inform_ok(f"Директорія {path_tools} створена!")
					except Exception as e:
						inform_error(f"Помилка створення директорії {path_tools}")
						inform_error(e)
						exit()

				#тут вже є директорія з проектом



	def LoadConfig(self):
		inform(f"Завантажую файл конфігурації {self.CONFIG_PATH}")
		try:
			with open(self.CONFIG_PATH, "r") as f:
				self.config = json.load(f)
			inform("Файл конфігурації завантажено!")
		except FileNotFoundError:
			inform_error(f"Файл конфігурації {self.CONFIG_PATH} не знайдено!")
			exit()
		except json.JSONDecodeError as e:
			inform_error("Синтаксична помилка JSON: ")
			inform_error(e)
			exit()
		except Exception as e:
			inform_error("Непередбачувана помилка")
			inform_error(e)
					

	def Begin(self):
		self.LoadConfig()
		self.CheckArgsConditions()



def GudBuy():
	print("")



if __name__ == '__main__':
	atexit.register(GudBuy)
	print("\n")
	initProject = InitProject()
	initProject.Begin()