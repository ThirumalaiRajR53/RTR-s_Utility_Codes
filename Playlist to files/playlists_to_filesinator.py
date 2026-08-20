import os
import shutil

def copy_songs_from_playlist(playlist_path, destination_root):
    playlist_name = os.path.splitext(os.path.basename(playlist_path))[0]
    destination_folder = os.path.join(destination_root, playlist_name)
    os.makedirs(destination_folder, exist_ok=True)

    with open(playlist_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    song_paths = [line.strip() for line in lines if line.strip() and not line.startswith('#')]

    for song_path in song_paths:
        if not os.path.isabs(song_path):
            song_path = os.path.join(os.path.dirname(playlist_path), song_path)

        if os.path.isfile(song_path):
            try:
                shutil.copy2(song_path, destination_folder)
                print(f"✅ Copied: {song_path}")
            except Exception as e:
                print(f"❌ Failed to copy {song_path}: {e}")
        else:
            print(f"⚠️ File not found: {song_path}")

def process_all_playlists(playlist_directory, output_directory):
    if not os.path.isdir(playlist_directory):
        print("❌ Playlist directory not found.")
        return

    os.makedirs(output_directory, exist_ok=True)

    for file_name in os.listdir(playlist_directory):
        if file_name.lower().endswith('.m3u'):
            playlist_path = os.path.join(playlist_directory, file_name)
            print(f"\n📁 Processing playlist: {file_name}")
            copy_songs_from_playlist(playlist_path, output_directory)

if __name__ == "__main__":
    # Change these paths as needed
    
    # Folder where all .m3u files are stored
    playlist_folder = r"C:\Users\rajth\Desktop\PL"
    
    # Folder where copied songs will be placed
    output_folder = r"E:\Mobile Backups\Playlist to android\CopiedPlaylists"

    process_all_playlists(playlist_folder, output_folder)
