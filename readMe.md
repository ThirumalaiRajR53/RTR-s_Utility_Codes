# File_name_extractinator (Windows/Mac/Linux)

A simple Python script that scans a parent folder and appends the names of all files and folders directly inside it to a text file.

## Features

* Lists files and folders in a specified directory
* Appends their names to `item_names.txt`
* Preserves existing entries in the output file
* Supports files and folders with Unicode characters

## Requirements

* Python 3.x

## Usage

Run the script:

```bash
python File_name_extractinator.py
```

Enter the path to the parent folder when prompted:

```text
Enter the parent folder path: C:\Users\YourName\Documents\MyFolder
```

The names will be appended to:

```text
item_names.txt
```

## Example

Given:

```text
MyFolder/
├── Document.pdf
├── Photo.jpg
├── Projects/
├── Videos/
└── Notes.txt
```

The output will be:

```text
Document.pdf
Photo.jpg
Projects
Videos
Notes.txt
```

> **Note:** The script scans only the immediate contents of the specified folder. It does not recursively scan subfolders.

---

# Image_background_erasinator

A simple Python script that automatically removes the background from an image using `rembg` and saves the result as a timestamped PNG.

## Features

* Automatically removes image backgrounds
* Supports common image formats through Pillow
* Generates a unique timestamped output filename
* Works on **Windows, Linux, and macOS**

## Requirements

* Python 3.x
* `rembg`
* `Pillow`

Install dependencies:

```bash
pip install rembg pillow
```

## Usage

Place the input image in the same directory as the script and name it:

```text
test.png
```

Run:

```bash
python image_background_erasinator.py
```

The processed image will be saved as:

```text
op_YYYYMMDD_HHMMSS.png
```

Example:

```text
op_20260820_104530.png
```

## Notes

* The current script expects the input file to be named `test.png`.
* The output is saved in the same directory.
* The script can be run on Windows, Linux, or macOS.

---

# itunes_playlist_to_androidinator

A simple Python script that converts iTunes `.m3u` playlists containing Windows file paths into Android-friendly `.m3u` playlists.

## Features

* Processes all `.m3u` files in a specified folder
* Removes iTunes metadata lines
* Converts Windows paths to Android-friendly paths
* Replaces Windows `\` separators with `/`
* Creates new files with the `_android.m3u` suffix
* Preserves the original playlist files

## Requirements

* Python 3.x

No external Python packages are required.

## Usage

Update the source folder in the script:

```python
source_folder = r"C:\Users\YourName\Desktop\Playlists"
```

Run:

```bash
python win-iTunes_to_Android.py
```

For example:

```text
playlist.m3u
```

becomes:

```text
playlist_android.m3u
```

## Notes

* Designed primarily for **Windows iTunes playlists**.
* The script expects the original iTunes music path prefix to be configured in `prefix_to_remove`.
* The generated playlists use `Music/` as the Android music root.
* Original `.m3u` files are not modified.

---

# playlists_to_filesinator

A simple Python script that reads `.m3u` playlists and copies all referenced music files into separate folders for each playlist.

## Features

* Processes multiple `.m3u` playlists automatically
* Creates a separate folder for each playlist
* Copies referenced music files while preserving file metadata
* Supports absolute and relative file paths
* Keeps original playlist files unchanged
* Works on **Windows, Linux, and macOS**

## Requirements

* Python 3.x

No external Python packages are required.

## Usage

Update these paths in the script:

```python
playlist_folder = r"C:\Path\To\Playlists"
output_folder = r"C:\Path\To\Output"
```

Run:

```bash
python Playlist_to_files.py
```

### Example

Given:

```text
Playlists/
├── Workout.m3u
├── Favorites.m3u
└── Road Trip.m3u
```

The script creates:

```text
Output/
├── Workout/
├── Favorites/
└── Road Trip/
```

Each folder contains the music files referenced by its corresponding playlist.

## Notes

* Only `.m3u` files are processed.
* Playlist metadata lines beginning with `#` are ignored.
* Missing files are reported but do not stop the entire process.
* Existing destination folders are reused.
