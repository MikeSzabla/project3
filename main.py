from pathlib import Path
from csv_io.inputdata import InputData
from csv_io.outputdata import OutputData
import os
import shutil
import datetime


def main():
    # gather necessary directory paths
    root_dir = Path(__file__).parent
    input_folder_dir = root_dir / 'input'
    output_folder_dir = root_dir / 'output'
    done_folder_dir = root_dir / 'done'
    now = datetime.datetime.now()

    # create a dataframe using the input data
    input_data = InputData(input_folder_dir)
    input_dataframe = input_data.get_input_dataframe()

    # create a dataframe with the info that will be output
    output_data = OutputData(input_dataframe)
    output_dataframe = output_data.generate_output_dataframe()
    exception_dataframe = output_data.generate_exception_dataframe()

    # generate result csv from output_dataframe and exception_dataframe
    if not output_dataframe.empty:
        filename = 'calculation_results_'+now.strftime("%m-%d-%Y_%H-%M-%S")
        output_dataframe.to_csv(os.path.join(output_folder_dir, filename))
    if not exception_dataframe.empty:
        filename = 'exceptions_'+now.strftime("%m-%d-%Y_%H-%M-%S")
        exception_dataframe.to_csv(os.path.join(output_folder_dir, filename))

    # move files to done directory
    for file in input_data.get_list_of_input_paths():
        shutil.move(file, done_folder_dir)


if __name__ == "__main__":
    main()
