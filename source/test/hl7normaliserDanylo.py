import hl7
import csv

def normalise_hl7(original_hl7_path):
    # Open the HL7 file for reading
    with open(original_hl7_path, 'r') as hl7_file:
        hl7_messages = hl7.parse(hl7_file.read())

    # Open a CSV file for writing
    with open('output.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        desired_order = ['Name', 'Date', 'Heartrate', 'BloodPressure', 'Sleep']
        # Write header row to the CSV file
        csv_writer.writerow(desired_order)  # Define column headers

        # Process each HL7 message
        for message in hl7_messages:
            # Extract data from the HL7 message and format it as needed
            field1 = message['Name']  # Replace with actual field extraction
            field2 = message['Date']  # Replace with actual field extraction
            field3 = message['Heartrate']
            field4 = message['Blood Pressure']
            field5 = message['Sleep'] # Replace with actual field extraction
            # ...

            # Write the extracted data to the CSV file
            csv_writer.writerow([field1, field2, field3, field4, field5])

    print("Conversion completed. CSV file saved as 'output.csv'")