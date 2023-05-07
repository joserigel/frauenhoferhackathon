import os
import pandas as pd
from PIL import Image
from main import analyze_grid
from matplotlib import pyplot as plt
import numpy as np
from tqdm import tqdm


def preprocess_data(tif_folder, csv_file):
    # Read the CSV file containing the labels
    labels_df = pd.read_csv(csv_file)

    data = []

    # Create a dictionary to store preprocessed data
    data_dict = {"filename": [], "path": [], "label": []}

    # Iterate through the rows in the CSV file
    for index, row in labels_df.iterrows():
        # Get the filename and label from the CSV row
        filename, label = row['Id'], row['Label']

        # Check if the .tif file exists in the specified folder
        tif_file_path = os.path.join(tif_folder, filename)
        if os.path.isfile(tif_file_path):
            # Add the filename, image, and label to the data dictionary
            data_dict = {"filename": filename, "path": tif_file_path, "label": label}
            data.append(data_dict)
        else:
            print(f"File not found: {tif_file_path}")

    # Return the preprocessed data as a Pandas DataFrame
    return data


# Example usage:


main_folder = r'C:\Users\david\Desktop\data'
tif_folder = main_folder+r'\train'
csv_file = r'C:\Users\david\Desktop\data\labels_train.csv'
counts_file = main_folder+r'\hist_counts.npy'

preprocessed_data = preprocess_data(tif_folder, csv_file)

g = []
bad = []

g_g = 0
g_b = 0

for i in tqdm(preprocessed_data):



    #if(i["label"]=="good"):
    #    g_g +=1
    #    g.append(analyze_grid(i["path"], main_folder) )
    if (i["label"] == "silver_defect"):
        g_b += 1
        bad.append(analyze_grid(i["path"], main_folder))

    if(g_g>300 and g_b>300):
        break


#np.save(counts_file,res)

counts = np.load(counts_file)

a = np.count_nonzero((counts < 580))/counts.size

print(a)

fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)
fig.suptitle('Vertically stacked subplots')
ax1.hist(g, density=True, bins=20)  # density=False would make counts
ax2.hist(bad, density=True, bins=20)  # density=False would make counts

plt.show()


