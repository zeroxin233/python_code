import xml.dom.minidom as Dom
import my_excel
import my_file
class class_xml_info:
	doc = 0
	io_setup_node = 0
	outfun_node = 0
	infun_node = 0
	def __init__(self):
		self.doc = Dom.Document()
		self.io_setup_node = self.doc.createElement("IO_Map")  
		self.doc.appendChild(self.io_setup_node)
		self.outfun_node = self.doc.createElement("Output_Fun")  
		self.io_setup_node.appendChild(self.outfun_node)
		self.infun_node = self.doc.createElement("Input_Fun")  
		self.io_setup_node.appendChild(self.infun_node)
		
def createNode(father,node_name,node_value):
	#print (node_name)
	pin_name_text = xml_info.doc.createTextNode(node_value) 
	pin_name_node = xml_info.doc.createElement(node_name)
	pin_name_node.appendChild(pin_name_text)
	father.appendChild(pin_name_node)
	return pin_name_node
	
def creat_xml_node(pin_list):
	
	pin_num_text = 'Pin_%d' %(int(pin_list[0].value))
	pin_num_node = xml_info.doc.createElement(pin_num_text)
	#print (my_excel.excel_info.list_size)
	for i in range(1,my_excel.excel_info.list_size):
		#print (pin_list[i].name)
		if pin_list[i].value != '':
			if type(pin_list[i].value)==float or type(pin_list[i].value)==int:
				createNode(pin_num_node,pin_list[i].name,'%d' %(pin_list[i].value))
			else:
				createNode(pin_num_node,pin_list[i].name,pin_list[i].value)
		else:
			createNode(pin_num_node,pin_list[i].name,'Null')

	""""""	
	xml_info.io_setup_node.appendChild(pin_num_node)
	my_file.write_header_file(xml_info.doc,pin_num_node)

def creat_xml_outfun_node(pin_list):
	pin_num_text = pin_list[0].value
	pin_num_node = xml_info.doc.createElement(pin_num_text)
	for i in range(1,my_excel.excel_info.outfun_list_size):
		if pin_list[i].value != '':
			if type(pin_list[i].value)==float or type(pin_list[i].value)==int:
				createNode(pin_num_node,pin_list[i].name,'%d' %(pin_list[i].value))
			else:
				createNode(pin_num_node,pin_list[i].name,pin_list[i].value)
		else:
			createNode(pin_num_node,pin_list[i].name,'Null')
	xml_info.outfun_node.appendChild(pin_num_node)
	my_file.write_outfun_header_file(xml_info.doc,pin_num_node)		
	print ('my_excel.excel_info.outfun_list_size %d'%my_excel.excel_info.outfun_list_size)
	for i in range(1,my_excel.excel_info.outfun_list_size):
		print (pin_list[i].value)

def creat_xml_infun_node(pin_list):
	pin_num_text = pin_list[0].value
	pin_num_node = xml_info.doc.createElement(pin_num_text)

	for i in range(1,my_excel.excel_info.infun_list_size):
		print ('aaa')
		print (pin_list[i].name)
		print (pin_list[i].value)
		if pin_list[i].value != '':
			if type(pin_list[i].value)==float or type(pin_list[i].value)==int:
				createNode(pin_num_node,pin_list[i].name,'%d' %(pin_list[i].value))
			else:
				createNode(pin_num_node,pin_list[i].name,pin_list[i].value)
		else:
			createNode(pin_num_node,pin_list[i].name,'Null')
	xml_info.infun_node.appendChild(pin_num_node)
	my_file.write_infun_header_file(xml_info.doc,pin_num_node)		
	print ('my_excel.excel_info.infun_list_size %d'%my_excel.excel_info.infun_list_size)
	for i in range(1,my_excel.excel_info.infun_list_size):
		print (pin_list[i].value)

def init():
	xml_info = class_xml_info()
	return xml_info

xml_info = init()