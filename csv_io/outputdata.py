import os
import pandas as pd
import time


class OutputData:
    output_dataframe = pd.DataFrame({'time': [], 'input_file': [], 'operation': [], 'result': []})