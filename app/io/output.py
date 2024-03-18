

def console_output(text):
    """function for console writing"""
    print(text)


def file_output(pass_to_file, text):
    """function for file writing"""
    f = open(pass_to_file, "w")
    f.write(text)
    f.close()
