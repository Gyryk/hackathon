import pandas as pd


def normalise_csv(input_csv_path, output_csv_path):
    # Read the original CSV file
    df = pd.read_csv(input_csv_path)

    # Define the desired column order
    desired_order = ['Name', 'Date', 'Heartrate', 'BloodPressure', 'Sleep']

    # Reorder the columns
    df_reordered = df[desired_order]

    # Save the reordered DataFrame to a new CSV file
    # new_csv_path = 'csvNormal.csv'
    # new_csv_path = 'unpackers/output/csvNormal.csv'
    df_reordered.to_csv(output_csv_path, index=False)

    print("New normalised CSV file form CSV file created successfully.")
