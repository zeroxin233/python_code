class Cfg_Setting():
	excel_path = 0
	xml_path = 0
	header_path = 0
	def __init__(self):
		self.excel_path = EXCEL_PATH
		self.xml_path = XML_PATH
		self.header_path = HEADER_PATH
		self.fun_path = FUN_PATH


import configparser
config = configparser.ConfigParser()
config.read("setup.ini") 



#选定的文件
EXCEL_PATH = 	config.get('PATH','excel_path')
XML_PATH = 		"io_setup.xml"
HEADER_PATH = 	config.get('PATH','header_path')
FUN_PATH = 		config.get('PATH','fun_path')
cfg_data= Cfg_Setting()


import my_excel
import my_xml
import my_file

from my_xml import xml_info
if __name__ == "__main__": 

	#print (my_excel.excel_info.date_size)
	my_file.write_header_init()
	for x in range(my_excel.excel_info.date_size-1):
		my_xml.creat_xml_node(my_excel.excel_info.pin_map[x])
	#print (my_excel.excel_info.outfun_data_size-1)
	for x in range(my_excel.excel_info.outfun_data_size-1):
		my_xml.creat_xml_outfun_node(my_excel.excel_info.outfun_pin_map[x])
	print ('my_excel.excel_info.infun_data_size')	
	print (my_excel.excel_info.infun_data_size-1)
	for x in range(my_excel.excel_info.infun_data_size-1):
		my_xml.creat_xml_infun_node(my_excel.excel_info.infun_pin_map[x])
	
	my_file.write_xml_file(xml_info.doc)

	#for x in range(my_excel.excel_info.date_size-1):
	#	my_file.write_header_file(xml_info.doc,pin)

	#for x in range(my_excel.excel_info.outfun_data_size-1):
	#	my_file.write_outfun_header_file(xml_info.doc,pin)
	