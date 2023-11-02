import csv
from material_selector import ms


selected_indices = sorted([160,138,102,140,107,69,46,78,74,155,128,127,27,44,145,167,157,168,100,144])

with open("model_generated_mats.csv") as f:
    lines = f.readlines()

filtered_lines = lines[0:1]

for idx in selected_indices:
    filtered_lines.append(lines[idx + 1])

with open("model_generated_mats_subset.csv", "w") as f:
    f.writelines(filtered_lines)


# Define an empty dictionary to store the data
data_dict = []

# Open the CSV file and read it as a dictionary
with open("model_generated_mats_subset.csv", mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        row_with_floats = {k: float(v) for k, v in row.items()}
        data_dict.append(row_with_floats)

for dict_item in data_dict:
    neighbours = ms.get_existing_materials_with_min_distance(dict_item)
    ns = "$".join([it[1] for it in neighbours])
    dict_item["neighbours"] = ns

def write_dict_to_csv(list_of_dicts, filename):
    # Open the file in write mode ('w')
    with open(filename, 'w', newline='') as csvfile:
        # Extract the field names (keys of the dictionary)
        fieldnames = list_of_dicts[0].keys()
        
        # Initialize DictWriter object
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header (field names)
        csvwriter.writeheader()
        
        # Write the rows
        for row in list_of_dicts:
            csvwriter.writerow(row)

write_dict_to_csv(data_dict, "model_generated_mats_subset_with_neighbours.csv")

ms.write_existing_compositions_csv()