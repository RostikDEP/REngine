import os, sys
from loguru import logger
from pathlib import Path
from loggerFunctions import *

class Compiler:
	def __init__(self):
		self.src_dir = Path("src/")
		self.rbin_dir = Path("rbin/")

		self.CheckArgsConditions()
		self.WalkSrcDir()



	def CheckArgsConditions(self):
		if len(sys.argv) == 1:
			if "compileRScript.py" in sys.argv[0]:
				inform(f"Папка SRC не вказана. Використовую {self.src_dir}")
		else:
			path = Path(sys.argv[1])
			if path.exists():
				self.src_dir = path
				inform(f"Використовую SRC шлях: {path}")
			else:
				inform_error(f"Не знайдено шлях {path}")
				exit()

		if self.rbin_dir.exists():
			inform(f"Папка RBIN: {self.rbin_dir}")
		else:
			inform_error(f"Папка RBIN не знайдена! {self.rbin_dir}")


	def WalkSrcDir(self):
		allRS = list(self.src_dir.glob("*.rscript"))
		if len(allRS) == 0:
			inform_error(f"Не знайдено .rscript файлів у директорії {self.src_dir}")
		else:
			inform(f"Знайдено {len(allRS)} файлів:")
			for file in allRS:
				inform_file(f"{file}")
		self.GoCompile(allRS)


	def GoCompile(self, rs_files):
		for file in rs_files:
			print("\n")
			inform(f"Опрацьовую: {file}")
			





if __name__ == "__main__":
	print("\n")
	compiler = Compiler()
	print("\n")