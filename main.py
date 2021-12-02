from pathlib import Path
from csv_io.inputdata import InputData
from csv_io.outputdata import OutputData


def main():
    # set up directory
    root_dir = Path(__file__).parent
    input_folder_dir = root_dir / 'input'
    output_folder_dir = root_dir / 'output'

    input_data = InputData(input_folder_dir)
    input_dataframe = input_data.get_input_dataframe()

    output_data = OutputData(input_dataframe)
    output_dataframe = output_data.generate_output_dataframe()


if __name__ == "__main__":
    main()
