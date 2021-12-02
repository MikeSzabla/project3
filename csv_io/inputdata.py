import os
import pandas as pd


class InputData:

    input_dir = ""
    list_of_input_paths = []
    input_dataframe = pd.DataFrame(data={'value_a': [], 'value_b': [], 'operation': [], 'input_file': [], 'record_number': []})

    def __init__(self, input_dir):
        InputData.input_dir = input_dir
        InputData.set_list_of_input_paths(InputData.generate_list_of_input_paths(input_dir))
        InputData.populate_dataframe(InputData.get_list_of_input_paths())
        InputData.get_input_dataframe()

    @staticmethod
    def generate_list_of_input_paths(folder_dir):
        path_list = []
        for dirpath, _, filenames in os.walk(folder_dir):
            for f in filenames:
                path_list.append(os.path.abspath(os.path.join(dirpath, f)))
        return path_list

    @staticmethod
    def get_list_of_input_paths():
        return InputData.list_of_input_paths

    @staticmethod
    def set_list_of_input_paths(path_list):
        InputData.list_of_input_paths = path_list

    @staticmethod
    def populate_dataframe(list_of_input_paths):
        for path in list_of_input_paths:
            dataframe_from_csv = pd.read_csv(path)
            path_col = [os.path.relpath(path, InputData.input_dir)] * len(dataframe_from_csv.index)  # add column of file paths
            record_num_col = list(range(1, len(dataframe_from_csv.index)+1))
            dataframe_from_csv['input_file'] = path_col
            dataframe_from_csv['record_number'] = record_num_col
            InputData.append_dataframe(dataframe_from_csv)

    @staticmethod
    def append_dataframe(df):
        InputData.input_dataframe = pd.concat([InputData.get_input_dataframe(), df], ignore_index=True)

    @staticmethod
    def get_input_dataframe():
        return InputData.input_dataframe
