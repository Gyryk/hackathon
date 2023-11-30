import merger
from normaliser import Normaliser

# declare and initialise sources
input_excel_path = 'source/input/input.xlsx'
output_excel_path = 'source/intermediate/xlsxNormal.csv'

input_csv_path = 'source/input/input.csv'
output_csv_path = 'source/intermediate/csvNormal.csv'

input_json_path = 'source/input/input.json'
output_json_path = 'source/intermediate/jsonNormal.csv'

output_path = 'source/output/output.xlsx'

normaliser = Normaliser()


# operate
normaliser.normalise_csv(input_csv_path, output_csv_path)
normaliser.normalise_xls(input_excel_path, output_excel_path)
normaliser.normalise_json(input_json_path, output_json_path)


merger.merge_files(output_csv_path, output_excel_path, output_json_path, output_path)


