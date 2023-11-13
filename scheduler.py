import merger
from normaliser import Normaliser

# declare and initialise sources
input_excel_path = 'unpackers/input/input.xlsx'
output_excel_path = 'unpackers/intermediate/xlsxNormal.csv'

input_csv_path = 'unpackers/input/input.csv'
output_csv_path = 'unpackers/intermediate/csvNormal.csv'

input_json_path = 'unpackers/input/input.json'
output_json_path = 'unpackers/intermediate/jsonNormal.csv'

output_path = 'unpackers/output/output.xlsx'

normaliser = Normaliser()


# operate
normaliser.normalise_csv(input_csv_path, output_csv_path)
normaliser.normalise_xls(input_excel_path, output_excel_path)
normaliser.normalise_json(input_json_path, output_json_path)


merger.merge_files(output_csv_path, output_excel_path, output_json_path, output_path)


