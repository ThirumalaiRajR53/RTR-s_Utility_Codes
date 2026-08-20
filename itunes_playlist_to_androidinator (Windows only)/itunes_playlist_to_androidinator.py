import os
#import re

# Set this to your folder containing all the .m3u files
source_folder = r"C:\Users\rajth\Desktop\BU"

# Common root to strip (adjust if your paths differ)
prefix_to_remove = "E:\\Mobile Backups\\iTunes\\iTunes Media\\Music\\"

for filename in os.listdir(source_folder):
    if filename.lower().endswith('.m3u'):
        input_path = os.path.join(source_folder, filename)
        output_path = os.path.join(source_folder, filename.replace('.m3u', '_android.m3u'))

        with open(input_path, 'r', encoding='utf-8') as infile, \
             open(output_path, 'w', encoding='utf-8') as outfile:

            for line in infile:
                if line.startswith('#EXT'):  # skip metadata lines
                    continue

                # Normalize Windows path to Android-friendly format
                cleaned_line = line.replace(prefix_to_remove, 'Music/')
                cleaned_line = cleaned_line.replace('\\', '/').strip()

                if cleaned_line:  # skip empty lines
                    outfile.write(cleaned_line + '\n')

print("✅ Conversion complete. Fixed files saved with '_android.m3u' suffix.")
