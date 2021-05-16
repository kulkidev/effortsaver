# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from csvdiff.utils import extract_reference_record_to_file, compare_csv_file_using_index_field, \
    read_csv_file_with_pandas
import logging
from datetime import datetime

log_file_name = datetime.now().strftime('python-script-%H-%M-%d-%m-%Y.log')

logging.basicConfig(filename=log_file_name,
                    filemode='w',
                    format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)


def generate_input_file():
    ref_file = input("Please enter the reference file path with file name which contains the key:")
    lookup_file = input("Please enter the lookup file path with file name:")
    output_file = input("Please enter the output file path with file name:")
    extract_reference_record_to_file(index_file=ref_file,
                                     lookup_file=lookup_file,
                                     output_file=output_file)


def compare_two_csv_file():
    ref_file = input("Please enter the reference file path with file name:")
    lookup_file = input("Please enter the lookup file path with file name:")
    index_field = input("Please enter the index field to be used for checking:")
    compare_csv_file_using_index_field(file1=ref_file,
                                       file2=lookup_file,
                                       index_field=index_field)


def read_file_efficiently():
    input_file = input("Please enter the file path with file name which needs to be read:")
    read_csv_file_with_pandas(input_file)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    print("Starting the script with effort saver options")
    option = int(input(""" Please enter 1 if you want to lookup a value in a file and generate a file
     or 2 if you want to compare 2 csv files 
     or 3 if you want to read file using pandas"""))

    if option == 1:
        generate_input_file()
    elif option == 2:
        compare_two_csv_file()
    elif option == 3:
        read_file_efficiently()
    else:
        print("Invalid option selected. Please re-run the script")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
