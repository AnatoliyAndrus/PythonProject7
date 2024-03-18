import pandas as pd

def console_input():
    """function for reading from console"""
    input1 = input()
    return input1

def file_input_built_in(pass_to_file):
    """function for reading from file using built-in function"""
    f = open(pass_to_file, "r");
    res = f.read()
    f.close()
    return res

def file_input_pandas(pass_to_file):
    """function for reading from file using pandas library"""
    data = pd.read_csv(pass_to_file)
    return data.to_string(header=False, index=False)

