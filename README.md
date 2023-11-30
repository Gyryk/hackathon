# Health Tech Hackathon Project

## Introduction

This project was developed as a solution to the Health Tech Hackathon held on 11-12/11/2023, hosted by Carradale Futures, Microsoft, and the Queen Mary University London Computer Science Society. The challenge posed during the hackathon:
> Your challenge is to create an EPR lite solution with some key features and additional creative ideas to enhance patient care and healthcare management

## Challenges Faced

During the hackathon, we identified the following challenges:

- A variety of unstandardized data complicating operations
- Existing EPR models being either expensive or too complex for medical staff
- Lack of interoperability between different ERPs/devices

## Our Solution

Our solution addresses these challenges by providing a cheap and user-friendly EPR model that requires minimal technical knowledge to master

To use our EPR model:

1. Install the `EPR.zip` file 
2. Import the file into your PowerApps environment <br>
> Detailed instructions are provided on this link: https://www.youtube.com/watch?v=Ar6Gw-pQpGc

## Normaliser Functionality

In addition to the EPR model, our project includes a normaliser program that tackles the core issue of unstandardised data in various formats, such as .xlsx, .csv, .json, and, in the future, .hl7, .fit, and paper data.

To use the normaliser, follow these steps:

1. Download all the files.
2. Install Python, Pandas, hl7, openpyxl.
3. Place your files to be standardised and merged into the `../source/input` folder (sample files provided).
4. Navigate to the directory in the terminal and run `python3 scheduler.py` (or use an alternative method).
5. Find the output in the `../source/output/output.xlsx` folder after execution (a sample file is provided).

## Conclusion

In conclusion, we have developed an EPR model using Microsoft PowerApps and a lightweight, scalable Python program. This solution enables hospitals to work more efficiently and accurately.

This project was presented to the jury during the final part of the Hackathon and received high praise.

Feel free to reach out for any questions or feedback!
