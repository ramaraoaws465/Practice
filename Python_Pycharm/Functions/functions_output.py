def format_name(f_name, l_name):
    # if f_name == "" or l_name == "":
    #     return "You dint provide any input"
    """Take the first and last name and format it to return the title case version of the name"""
    #print(f_name.title())
    #print(l_name.title())
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name?"), input("What is your last name?")))
#
#
# formated_string = format_name("angela", "Yu")
# print(formated_string)

# def funtion_1(text):
#     return text + text
#
# def function_2(text):
#     return text.title()
#
# output = function_2(funtion_1("hello"))
# print(output)