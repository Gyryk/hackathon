import pandas as pd
def merge_files(file1_path, file2_path, file3_path, output_path):
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)
    df3 = pd.read_csv(file3_path)

    merged_df = pd.concat([df1, df2, df3], ignore_index=True)

    merged_df.to_excel(output_path, index=False)

    print(f"Merged data saved to '{output_path}'")