This Python 3 script is used to split a source data file (excel or csv) into several output data files (excel or csv) based on predefined
settings in the config.json file. A sample config file is shown below:

{
  "column": 4,
  "data_file":"data/data.xlsx",
  "output_folder":"data/"
}

column - defines the column by which the output files will be created. Column numbering starts from zero
data_file: source data file that will be split
out_folder: destination output folder for generated files

See requirements.txt for script requirements.

To run script: invove python3 MainApp.py from the command line