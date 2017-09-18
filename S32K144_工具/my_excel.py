import xlrd

from io_setup_tool import cfg_data


class node:
    def __init__(self,name,value):
        self.name = name     # 名称
        self.value = value     # 尺寸

class class_excel_info:
	sheet_gpio_pin = 0
	pin_base_x = 0
	pin_base_y = 0
	list_size = 0
	date_size = 0
	pin_map = []
	sheet_gpio_fun = 0
	outfun_base_x = 0
	outfun_base_y = 0
	outfun_list_size = 0
	outfun_data_size = 0
	outfun_pin_map = []
	infun_base_x = 0
	infun_base_y = 0
	infun_list_size = 0
	infun_data_size = 0
	infun_pin_map = []
	
		
	def get_base_xy(self):
		for x in range(self.sheet_gpio_pin.nrows):
			for y in range(self.sheet_gpio_pin.ncols):
				if self.sheet_gpio_pin.cell(x,y).value == 'S32K144_100 LQFP':
					self.pin_base_x = x
					self.pin_base_y = y
					print ('pin_base_x %d'%self.pin_base_x)
					print ('pin_base_x %d'%self.pin_base_x)
					pass
		for x in range(self.sheet_gpio_fun.nrows):
			for y in range(self.sheet_gpio_fun.ncols):
				if self.sheet_gpio_fun.cell(x,y).value == 'Output_Fun':
					self.outfun_base_x = x
					self.outfun_base_y = y
					print ('outfun_base_x %d'%self.outfun_base_x)
					print ('outfun_base_y %d'%self.outfun_base_y)
					pass
		for x in range(self.sheet_gpio_fun.nrows):
			for y in range(self.sheet_gpio_fun.ncols):
				if self.sheet_gpio_fun.cell(x,y).value == 'Input_Fun':
					self.infun_base_x = x
					self.infun_base_y = y
					print ('infun_base_x %d'%self.infun_base_x)
					print ('infun_base_y %d'%self.infun_base_y)
					pass


	def get_sheet(self):
		workbook = xlrd.open_workbook(cfg_data.excel_path)
		self.sheet_gpio_pin = workbook.sheet_by_name(u's_gpio_pin_define')
		self.sheet_gpio_fun = workbook.sheet_by_name(u'gpio_fun_define')
		print (self.sheet_gpio_fun)
		#print (self.sheet_gpio_pin)

	def get_list_size(self):
		for offset in range (0,self.sheet_gpio_pin.ncols-self.pin_base_y+1):
			x = (self.pin_base_x)
			y = (offset+self.pin_base_y)
			if self.sheet_gpio_pin.cell(x,y).value != '' :
				self.list_size = offset+1
			else:	
				break

		print ('list_size %d'%self.list_size)
		for offset in range (0,self.sheet_gpio_fun.ncols-self.outfun_base_y+1):
			x = (self.outfun_base_x)
			y = (offset+self.outfun_base_y)
			if self.sheet_gpio_fun.cell(x,y).value != '' :
				self.outfun_list_size = offset+1
			else:	
				break
		print ('outfun_list_size %d'%self.outfun_list_size)
		for offset in range (0,self.sheet_gpio_fun.ncols-self.infun_base_y+1):
			x = (self.infun_base_x)
			y = (offset+self.infun_base_y)
			if self.sheet_gpio_fun.cell(x,y).value != '' :
				self.infun_list_size = offset+1
			else:	
				break
		print ('infun_list_size %d'%self.infun_list_size)


	def get_date_size(self):
		for offset in range (0,self.sheet_gpio_pin.nrows-self.pin_base_x+1):
			x = (offset+self.pin_base_x)
			y = (self.pin_base_y)
			if self.sheet_gpio_pin.cell(x,y).value != '' :
				self.date_size = offset+1
			else:	
				break
		print ('date_size %d'%self.date_size)
		for offset in range (0,self.sheet_gpio_fun.nrows-self.outfun_base_y+1):
			x = (offset+self.outfun_base_x)
			y = (self.outfun_base_y)
			if self.sheet_gpio_fun.cell(x,y).value != '' :
				self.outfun_data_size = offset+1
			else:	
				break
		print ('outfun_data_size %d'%self.outfun_data_size)
		for offset in range (0,self.sheet_gpio_fun.nrows-self.infun_base_y+1):
			x = (offset+self.infun_base_x)
			y = (self.infun_base_y)
			if self.sheet_gpio_fun.cell(x,y).value != '' :
				self.infun_data_size = offset+1
			else:	
				break
		print ('infun_date_size %d'%self.infun_data_size)



	def creat_pin_map(self):
		for x in range(self.date_size-1):
			pin_list = []
			for y in range(self.list_size):
				pin_node_name = self.sheet_gpio_pin.cell(self.pin_base_x,y+self.pin_base_y).value
				pin_node_value = self.sheet_gpio_pin.cell(self.pin_base_x+x+1,y+self.pin_base_y).value
				io_node = node(pin_node_name,pin_node_value)
				pin_list.append(io_node)
				#print (pin_list[y].name)
				#print (pin_list[y].value)
			self.pin_map.append(pin_list)
		"""	
		for x in range (self.sheet_gpio_fun.ncols-1):
			for y in range (self.sheet_gpio_fun.nrows-1):
				try :
					print (self.sheet_gpio_fun.cell(x,y).value)
					print (x)
					print (y)
				except :
				    pass
		
		"""	
		for x in range(self.outfun_data_size-1):
			outfun_pin_list = []

			for y in range(self.outfun_list_size):
				pin_node_name = self.sheet_gpio_fun.cell(self.outfun_base_x,y+self.outfun_base_y).value
				pin_node_value = self.sheet_gpio_fun.cell(self.outfun_base_x+x+1,y+self.outfun_base_y).value
				io_node = node(pin_node_name,pin_node_value)
				outfun_pin_list.append(io_node)
			self.outfun_pin_map.append(outfun_pin_list)
		


		for x in range(self.infun_data_size-1):
			infun_pin_list = []

			for y in range(self.infun_list_size):
				pin_node_name = self.sheet_gpio_fun.cell(self.infun_base_x,y+self.infun_base_y).value
				pin_node_value = self.sheet_gpio_fun.cell(self.infun_base_x+x+1,y+self.infun_base_y).value
				io_node = node(pin_node_name,pin_node_value)
				print ('in %s'%pin_node_name)
				print ('in %s'%pin_node_value)

				infun_pin_list.append(io_node)
			self.infun_pin_map.append(infun_pin_list)

	def __init__(self):
		self.get_sheet()
		self.get_base_xy()
		self.get_list_size()
		self.get_date_size()
		self.creat_pin_map()



def init():
	excel_info = class_excel_info()
	return excel_info



excel_info = init()