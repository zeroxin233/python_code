import xlrd
class node:
    def __init__(self,name,value):
        self.name = name     
        self.value = value   

class class_excel_info:
	def __init__(self,file_path,sheet_name,base_name):
		self.sheet_gpio_pin = 0
		self.pin_base_x = 0
		self.pin_base_y = 0
		self.list_size = 0
		self.date_size = 0
		self.pin_map = []

		workbook = xlrd.open_workbook(file_path)
		self.sheet_gpio_pin = workbook.sheet_by_name(sheet_name)
		for x in range(self.sheet_gpio_pin.nrows):
			for y in range(self.sheet_gpio_pin.ncols):
				if self.sheet_gpio_pin.cell(x,y).value == base_name:
					self.pin_base_x = x
					self.pin_base_y = y
					if ((x == self.sheet_gpio_pin.nrows) and (y == self.sheet_gpio_pin.ncols)):
						print ('no found base_name')

		self.get_list_size()
		self.get_date_size()
		self.creat_pin_map()
		self.print_info()


	def get_list_size(self):
		for offset in range (0,self.sheet_gpio_pin.ncols-self.pin_base_y+1):
			x = (self.pin_base_x)
			y = (offset+self.pin_base_y)
			if self.sheet_gpio_pin.cell(x,y).value != '' :
				self.list_size = offset+1
			else:	
				break

	def get_date_size(self):
		for offset in range (0,self.sheet_gpio_pin.nrows-self.pin_base_x+1):
			x = (offset+self.pin_base_x)
			y = (self.pin_base_y)
			if self.sheet_gpio_pin.cell(x,y).value != '' :
				self.date_size = offset+1
			else:	
				break

	def creat_pin_map(self):
		
		for x in range(self.date_size-1):
			attr_dict = {}
			pin_node_name = 'list_id'
			pin_node_value = x
			attr_dict[pin_node_name] = pin_node_value
			for y in range(self.list_size):
				pin_node_name = self.sheet_gpio_pin.cell(self.pin_base_x,y+self.pin_base_y).value
				pin_node_value = self.sheet_gpio_pin.cell(self.pin_base_x+x+1,y+self.pin_base_y).value
				attr_dict[pin_node_name] = pin_node_value
				#print (pin_list[y].name)
				#print (pin_list[y].value)
			self.pin_map.append(attr_dict)


	def print_info(self):
		print ('date_size %d'%self.date_size)
		print ('list_size %d'%self.list_size)



def write_header_file(attr_dict):
	##print (attr_dict)
    if attr_dict['Pin_Attr'] == 'IO':
        header_str = \
"""
const S_PIN_CFG s_gpio_{name}_define = {{
    {{
        GPIO_{dict[Pin_Name]},
        PORT_INTERNAL_{dict[Pull_Config]},
        {dict[Open_Drain]},
        PORT_{dict[Drive_Select]}_DRIVE_STRENGTH,
        GPIO_{dict[Direction]}_DIRECTION,
    }},
    PIN_SET_{dict[Normal_Mode]},
    PIN_SET_{dict[Sleep_Mode]},
    {dict[Port_Pin_Num]},
}};
"""

        header_str_format = header_str.format(dict = attr_dict,name = attr_dict['Pin_Name'].lower())	
        print(header_str_format)


iosetup_info = class_excel_info('gpio_setup.xls','s_gpio_pin_define','KEA128_80 LQFP')
for i in iosetup_info.pin_map :
	write_header_file(i)

#iooutfun_info = class_excel_info('gpio_setup.xls','gpio_fun_define','Output_Fun')
#ioinfun_info = class_excel_info('gpio_setup.xls','gpio_fun_define','Input_Fun')  


