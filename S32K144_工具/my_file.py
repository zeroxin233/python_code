from io_setup_tool import cfg_data

headf = 0

def GetNodeValueText(node,node_name):
	pin_node = node.getElementsByTagName(node_name)
	text = pin_node[0].childNodes[0].data
	return text

def myWriteCode_init():
	global headf
	headf = open(cfg_data.header_path,'w')	
	headf.close()
	
def myWriteCode_deinit():
	global headf
	headf.close()
	
def wrtie_fun_head(node):
	global headf
	pin_name = GetNodeValueText(node,'Pin_Name')
	headf=open(cfg_data.header_path,'a')
	headf.write('const S_PIN_CFG s_gpio_%s_define = { \n'%pin_name.lower())
	headf.close()

def wrtie_fun_end():	
	global headf
	headf=open(cfg_data.header_path,'a')
	headf.write('};\n')
	headf.close()
	
def write_prot_base(headf,node):
	text = GetNodeValueText(node,'Port_Base')	
	headf.write('%s,\n'%text)
	
def write_prot_pin_num(headf,node):
	text = GetNodeValueText(node,'Port_Pin_Num')	
	headf.write('GPIO_Pin_num_%s,\n'%text)
	
def write_pull_config_num(headf,node):
	text = GetNodeValueText(node,'Pull_Config')	
	headf.write('#if FEATURE_PORT_HAS_PULL_SELECTION\n')
	headf.write('        ')
	if text=='Not_Enable':
		headf.write('PORT_INTERNAL_PULL_NOT_ENABLED,\n')
	if text=='Pull_Down_Enable':
		headf.write('PORT_INTERNAL_PULL_DOWN_ENABLED,\n')
	if text=='Pull_Up_Enable':
		headf.write('PORT_INTERNAL_PULL_UP_ENABLED,\n')
	headf.write('        ')
	headf.write('#endif\n')

def write_rate_select(headf,node):
	text = GetNodeValueText(node,'Rate_Select')	
	headf.write('#if FEATURE_PORT_HAS_SLEW_RATE\n')
	headf.write('        ')
	if text=='Fast':
		headf.write('PORT_FAST_SLEW_RATE,\n')
	if text=='Slow':
		headf.write('PORT_SLOW_SLEW_RATE,\n')
	headf.write('        ')
	headf.write('#endif\n')
	
def write_passive_filter(headf,node):
	text = GetNodeValueText(node,'Passive_Filter')	
	headf.write('#if FEATURE_PORT_HAS_PASSIVE_FILTER\n')
	headf.write('        ')
	headf.write('%s,\n'%text)
	headf.write('        ')
	headf.write('#endif\n')
	
def write_open_drain(headf,node):
	text = GetNodeValueText(node,'Open_Drain')
	headf.write('#if FEATURE_PORT_HAS_OPEN_DRAIN\n')
	headf.write('        ')
	headf.write('%s,\n'%text)
	headf.write('        ')
	headf.write('#endif\n')
	
def write_drive_select(headf,node):
	text = GetNodeValueText(node,'Drive_Select')
	headf.write('#if FEATURE_PORT_HAS_DRIVE_STRENGTH\n')
	headf.write('        ')	
	if text=='High':
		headf.write('PORT_HIGH_DRIVE_STRENGTH,\n')
	if text=='Low':
		headf.write('PORT_LOW_DRIVE_STRENGTH,\n')
	headf.write('        ')
	headf.write('#endif\n')
	
def write_mux(headf,node):
	text = GetNodeValueText(node,'Mux')	
	headf.write('%s,\n'%text)
	
def write_pin_lock(headf,node):
	text = GetNodeValueText(node,'Pin_Lock')
	headf.write('#if FEATURE_PORT_HAS_PIN_CONTROL_LOCK\n')
	headf.write('        ')		
	headf.write('%s,\n'%text)
	headf.write('        ')
	headf.write('#endif\n')
	
def write_Int_Config(headf,node):
	text = GetNodeValueText(node,'Int_Config')	
	headf.write('%s,\n'%text)
	
def write_Clear_Int_Flag(headf,node):
	text = GetNodeValueText(node,'Clear_Int_Flag')	
	headf.write('%s,\n'%text)
	
def write_GPIO_Base(headf,node):
	text = GetNodeValueText(node,'Port_Base')
	if text=='PORTE':
		headf.write('PTE,\n')
	if text=='PORTD':
		headf.write('PTE,\n')
	if text=='PORTC':
		headf.write('PTC,\n')
	if text=='PORTB':
		headf.write('PTB,\n')
	if text=='PORTA':
		headf.write('PTA,\n')
	
def write_Direction(headf,node):
	text = GetNodeValueText(node,'Direction')
	if text=='Output':
		headf.write('GPIO_OUTPUT_DIRECTION,\n')
	if text=='Input':
		headf.write('GPIO_INPUT_DIRECTION,\n')

		
def wrtie_fun_iocfg(node):
	global headf
	headf=open(cfg_data.header_path,'a')
	headf.write('    {\n')
	
	headf.write('        ')
	write_prot_base(headf,node)
	
	headf.write('        ')
	write_prot_pin_num(headf,node)
	
	headf.write('        ')
	write_pull_config_num(headf,node)
	
	headf.write('        ')
	write_rate_select(headf,node)
	
	headf.write('        ')
	write_passive_filter(headf,node)
	
	headf.write('        ')
	write_open_drain(headf,node)	
	
	headf.write('        ')
	write_drive_select(headf,node)
	
	headf.write('        ')
	write_mux(headf,node)
	
	headf.write('        ')
	write_pin_lock(headf,node)
	
	headf.write('        ')
	write_Int_Config(headf,node)
	
	headf.write('        ')
	write_Clear_Int_Flag(headf,node)
	
	headf.write('        ')
	write_GPIO_Base(headf,node)
	
	headf.write('        ')
	write_Direction(headf,node)
	
	headf.write('    },\n')
	headf.close()
	
	
def wrtie_other(node):
	global headf
	headf=open(cfg_data.header_path,'a')


	headf.write('    ')
	text = GetNodeValueText(node,'Normal_Mode')
	if text=='High':
		headf.write('PIN_SET_HIGH,\n')
	if text=='Low':
		headf.write('PIN_SET_LOW,\n')
	headf.write('    ')
	text = GetNodeValueText(node,'Sleep_Mode')
	if text=='High':
		headf.write('PIN_SET_HIGH,\n')
	if text=='Low':
		headf.write('PIN_SET_LOW,\n')


	
	headf.write('    ')
	text = GetNodeValueText(node,'Port_Pin_Num')	
	headf.write('GPIO_Pins_%s,\n'%text)

	headf.close()


def write_xml_file(doc):
	xmlf = open(cfg_data.xml_path,'w')
	xmlf.write(doc.toprettyxml(indent = ''))
	xmlf.close()

def write_header_file(doc,node):
	text = GetNodeValueText(node,'Pin_Attr')
	if (text == 'IO'):
		wrtie_fun_head(node)
		wrtie_fun_iocfg(node)
		wrtie_other(node)
		wrtie_fun_end()

def write_outfun_header_file(doc,node):
	pin_link_text = GetNodeValueText(node,'pin_link')
	if (pin_link_text != ''):
		global headf
		fun_name = GetNodeValueText(node,'Fun_Name')
		headf=open(cfg_data.fun_path,'a')
		text = '#define'
		headf.write('%-12s'%text)
		text = fun_name
		headf.write('%-24s'%text)
		text = 's_gpio_%s_define\n'%pin_link_text.lower()
		headf.write('%-18s'%text)
		
		
		fun_onoff = GetNodeValueText(node,'On:OFF')
		if (fun_onoff == 'low:high'):
			text = '  #define'
			headf.write('%-12s'%text)
			text = '%s_On'%fun_name
			headf.write('%-24s'%text)
			text = 'Low'
			headf.write('%-12s'%text)
			headf.write('\r')

			text = '  #define'
			headf.write('%-12s'%text)
			text = '%s_Off'%fun_name
			headf.write('%-24s'%text)
			text = 'High'
			headf.write('%-12s'%text)
			headf.write('\r')

		else:
			
			text = '  #define'
			headf.write('%-12s'%text)
			text = '%s_On'%fun_name
			headf.write('%-24s'%text)
			text = 'High'
			headf.write('%-12s'%text)
			headf.write('\r')

			text = '  #define'
			headf.write('%-12s'%text)
			text = '%s_Off'%fun_name
			headf.write('%-24s'%text)
			text = 'Low'
			headf.write('%-12s'%text)
			headf.write('\r')
			''''''
		headf.close()

def write_infun_header_file(doc,node):
	pin_link_text = GetNodeValueText(node,'pin_link')
	if (pin_link_text != ''):
		global headf
		fun_name = GetNodeValueText(node,'Fun_Name')
		headf=open(cfg_data.fun_path,'a')
		text = '#define'
		headf.write('%-12s'%text)
		text = fun_name
		headf.write('%-24s'%text)
		text = 's_gpio_%s_define\n'%pin_link_text.lower()
		headf.write('%-18s'%text)

		
		headf.close()

def write_header_init():
	headf=open(cfg_data.header_path,'w')
	headf.close()
	headf=open(cfg_data.fun_path,'w')
	headf.close()