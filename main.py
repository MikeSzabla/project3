from pathlib import Path
from csv_io.inputdata import InputData

def main():
    # set up directory
    root_dir = Path(__file__).parent
    input_folder_dir = root_dir / 'input'
    output_folder_dir = root_dir / 'output'

    inputData = InputData(input_folder_dir)
    input_dataframe = inputData.get_input_dataframe()

    breakpoint()



if __name__ == "__main__":
    main()
