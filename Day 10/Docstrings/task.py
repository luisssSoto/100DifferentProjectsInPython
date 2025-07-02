def format_name(f_name, l_name):
    """f_name and l_name are formating in order to get a full name"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)

print(format_name("aLeX", "soTO"))




