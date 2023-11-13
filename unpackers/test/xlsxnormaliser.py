import pandas as pd


def normalise_xls(input_excel_path, output_excel_path):
    # Read the original Excel file (change the file extension if it's a .xls file)
    df = pd.read_excel(input_excel_path)


    # Define the desired column order
    desired_order = ['Name', 'Date', 'Heartrate', 'BloodPressure', 'Sleep']

    # Reorder the columns
    df_reordered = df[desired_order]

    # Save the reordered DataFrame to a new Excel file
    # new_excel_path = 'xlsNormal.csv'
    # new_excel_path = 'unpackers/output/xlsNormal.csv'
    df_reordered.to_csv(output_excel_path, index=False)

    print("New normalised CSV file form XLSX file created successfully.")

