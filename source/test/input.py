# THIS FILE IS ONLY FOR TESTING HL7 PARSING AND CSV EXPORT
# DO NOT INCLUDE THIS FILE IN ANY FINAL SUBMISSION

import hl7
import csv

# Your original HL7 content
# hl7_content = """MSH|^~\&|SNDAPP|SNDFAC|RCVAPP|RCVFAC|20220101120000||ORU^R01|MSG00001|P|2.4|
# PID|1|12345|12345|Lee^David||19800101|M|20220101|
# OBX|1|NM|HR^Heart Rate|1|75|bpm|||F|||20220101120000|
# OBX|2|NM|BP^Blood Pressure|1|120/80|mmHg|||F|||20220101120000|
# OBX|3|ST|SLP^Sleep|1|7|h|||F|||20220101120000"""
hl7_content = """MSH|^~\&|HIS||LIS||20201103143041||ORU^R01|2020110314304123|P|2.3|||
PID|1|12345|12345|John Doe^Patient1||19700101|M|||123 Main St^^New York^NY^10001||555-555-5555|||M|||12345^0^M|12345^1^M||12345|||||N
ORC|RE|20201103143041^LIS|2020110314304123
OBR|1|20201103143041^LIS|2020110314304123|Heart Rate|||20201101120000|20201101121500||12345^John Doe^Patient1|||Report Comment
OBX|1|NM|Heart Rate^Heart Rate||72|bpm|||F|||20201101120500||12345^John Doe^Patient1|Report Comment
OBX|2|ST|Blood Pressure^Blood Pressure||120/80|mmHg|||F|||20201101120500||12345^John Doe^Patient1|Report Comment
OBX|3|ST|Sleep^Sleep||7|hours|||F|||20201101120500||12345^John Doe^Patient1|Report Comment
PID|2|67890|67890|Jane Smith^Patient2||19800214|F|||456 Elm St^^Los Angeles^CA^90001||555-555-5555|||F|||67890^0^F|67890^1^F||67890|||||N
ORC|RE|20201103143041^LIS|2020110314304123
OBR|2|20201103143041^LIS|2020110314304123|Heart Rate|||20201101130000|20201101131500||67890^Jane Smith^Patient2|||Report Comment
OBX|4|NM|Heart Rate^Heart Rate||65|bpm|||F|||20201101130500||67890^Jane Smith^Patient2|Report Comment
OBX|5|ST|Blood Pressure^Blood Pressure||130/75|mmHg|||F|||20201101130500||67890^Jane Smith^Patient2|Report Comment
OBX|6|ST|Sleep^Sleep||6|hours|||F|||20201101130500||67890^Jane Smith^Patient2|Report Comment"""

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

# Extract PID and OBX segments directly
pid_segments = [segment for segment in parsed_segments if str(segment[0][2]) == 'PID']
obx_segments = [segment for segment in parsed_segments if str(segment[0][2]) == 'OBX']

for segment in pid_segments:
    print(segment)

# Combine the extracted segments into a list
exported_segments = pid_segments + obx_segments

# Define the desired order of fields for CSV export
csv_field_order = ['SegmentID', 'Name', 'Date', 'Heartrate', 'Blood Pressure', 'Sleep']

# Create a list of dictionaries for CSV export
csv_data = []
for segment in exported_segments:
    csv_row = {'SegmentID': segment[0][0]}
    for i, field_value in enumerate(segment[1:], start=1):
        csv_row[f'Field{i}'] = field_value
    csv_data.append(csv_row)

# Save the CSV data to a file
csv_path = 'export.csv'
with open(csv_path, 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=csv_field_order)
    csv_writer.writeheader()
    csv_writer.writerows(csv_data)

print(f"CSV file '{csv_path}' created successfully.")
