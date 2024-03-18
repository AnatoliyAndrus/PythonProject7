from app.io.input import console_input, file_input_built_in, file_input_pandas
from app.io.output import console_output, file_output

def main():
    i_file_path = "D:/Projects/Python/PythonProject7/app/test_folder/input_file.txt"
    o_file_path = "D:/Projects/Python/PythonProject7/app/test_folder/output_file.txt"

    c_i = console_input()
    f_b = file_input_built_in(i_file_path)
    f_p =file_input_pandas(i_file_path)

    console_output(c_i)
    console_output(f_b)
    console_output(f_p)

    file_output(o_file_path, c_i)
    file_output(o_file_path, f_b)
    file_output(o_file_path, f_p)

if __name__ == "__main__":
    main()