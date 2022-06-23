import re
from datetime import datetime
import json

class regex_calculator:
	def __init__(self, regex_dict = {}, input_dict = {}, nb_runs = 1000, file_log=f"{__file__}.log"):
		self.regex_dict = regex_dict
		self.input_dict = input_dict
		self.nb_runs = nb_runs
		self.file_log = file_log
		self.log_string = f"Début de l'expérimentation : {datetime.now()}\n\n"
		self.run()

	def run(self):
		for input_name, input_value in list(self.input_dict.items()):
			for regex_name, regex_value in list(self.regex_dict.items()):
				self.experiment(regex_value,input_value,f"[{regex_name}] -> [{input_name}]")
		self.write_file_log()

	def experiment(self,regex,input_string,comment):
		start_tm = datetime.now().timestamp()
		for i in range(0,self.nb_runs):
			re.search(regex,input_string)
		stop_tm = datetime.now().timestamp()
		self.log_string += f"Test '{comment}' réalisé en : {self.calc_time(start_tm,stop_tm)}\n"

	def calc_time(self,start_tm, stop_tm):
		time = stop_tm - start_tm
		if time < 1:
			return f"{int(str(time).split('.')[1][:3])} ms"
		else:
			return f"{round(time,3)} s"

	def write_file_log(self):
		self.log_string += f"\nFin de l'expérimentation : {datetime.now()}\n"
		with open(self.file_log,"w") as file:
			file.write(self.log_string)


if __name__ == "__main__":
	try:
		dico_file = open("regex_dico.json")
		dico = json.load(dico_file)
		dico_file.close()	
		regex_calculator(regex_dict=dico["regex"], input_dict=dico["input"], nb_runs=dico["nb_runs"], file_log=dico["file_log"])

	except Exception as e:
		exit(f"Error : {e}")
