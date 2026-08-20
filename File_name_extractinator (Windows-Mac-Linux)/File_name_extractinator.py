import os

# Parent folder
parent_folder = input("Enter the parent folder path: ").strip()

# Output text file
output_file = "item_names.txt"

# Get files and folders inside the parent folder
items = os.listdir(parent_folder)

# Append names to the text file
with open(output_file, "a", encoding="utf-8") as f:
    for item in items:
        f.write(item + "\n")

print(f"Done! {len(items)} item names appended to '{output_file}'.")