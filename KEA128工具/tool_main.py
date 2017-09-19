import tool_class

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

def get_header_str_format(dict):
    global header_str
    str_format = header_str.format(dict = dict,name = dict['Pin_Name'].lower())	
    return str_format

def write_file(str_file):
    headf = open('gpio.h','w')
    headf.write(str_file)
    headf.close()


iosetup_info = tool_class.class_excel_info('gpio_setup.xls','s_gpio_pin_define','KEA128_80 LQFP')
header_str_file = ""
for dict in iosetup_info.pin_map :
	if dict['Pin_Attr'] == 'IO':
   		header_str_file = header_str_file + str(get_header_str_format(dict))

write_file(header_str_file)

#iooutfun_info = class_excel_info('gpio_setup.xls','gpio_fun_define','Output_Fun')
#ioinfun_info = class_excel_info('gpio_setup.xls','gpio_fun_define','Input_Fun')  