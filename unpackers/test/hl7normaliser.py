import hl7
import csv


def normalise_hl7(input_hl7_path, output_hl7_path):
    # Read the original HL7 file
    with open(input_hl7_path, 'r') as hl7_file:
        hl7_content = hl7_file.read()

    # Parse the original HL7 content
    # parsed_message = hl7.parse(hl7_content)

    # Split the HL7 content into individual segments
    hl7_segments = hl7_content.split('\n')

    # Manually remove the MSH segment
    if hl7_segments[0].startswith('MSH'):
        hl7_segments = hl7_segments[1:]

    # Initialize an empty list to store parsed segments
    parsed_segments = []

    # Reconstruct the MSH segment and parse each segment
    for segment in hl7_segments:
        # Skip empty lines
        if segment:
            msh_segment = "MSH|" + segment[0:]  # Reconstruct the MSH segment
            parsed_segment = hl7.parse(msh_segment)
            parsed_segments.append(parsed_segment)

    # Flatten the structure to handle subcomponents and repetitions
    # flattened_segments = []
    # for segment in parsed_message:
    #     flattened_segment = []
    #     for field in segment:
    #         if isinstance(field, list):
    #             flattened_segment.extend(field)
    #         else:
    #             flattened_segment.append(field)
    #     flattened_segments.append(flattened_segment)

    # Reorder the segments
    # reordered_segments = [segment for segment in flattened_segments if segment[0] in desired_order]

    # Extract PID and OBX segments
    pid_segments = [segment for segment in parsed_segments if str(segment[0][2]) == 'PID']
    obx_segments = [segment for segment in parsed_segments if str(segment[0][2]) == 'OBX']

    # Combine the reordered segments into a new HL7 message
    # new_hl7_content = '\n'.join(['|'.join(str(field) for field in segment) for segment in reordered_segments])
    exported_segments = pid_segments + obx_segments

    csv_field_order = ['SegmentID', 'Name', 'Date', 'Heartrate', 'BloodPressure', 'Sleep']

    csv_data = []
    for segment in exported_segments:
        csv_row = {'SegmentID': segment[0]}
        for i, field_value in enumerate(segment[1:], start=1):
            csv_row[f'Field{i}'] = field_value
        csv_data.append(csv_row)

    # Save the new HL7 content to a new file
    # new_hl7_path = 'hl7Normal.csv'
    # new_hl7_path = 'unpackers/output/hl7Normal.csv'
    # with open(new_hl7_path, 'w') as new_hl7_file:
    #     new_hl7_file.write(new_hl7_content)
    #
    # print("New HL7 file created successfully.")
    with open(output_hl7_path, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=csv_field_order)
        csv_writer.writeheader()
        csv_writer.writerows(csv_data)

    print("New normalised CSV file form HL7 file created successfully.")



# normalise_hl7('input/input.hl7')