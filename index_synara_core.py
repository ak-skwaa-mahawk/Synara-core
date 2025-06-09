
import os

def index_all_files(root_dir, output_file="synara_path_index.txt"):
    with open(output_file, "w", encoding="utf-8") as f:
        for foldername, subfolders, filenames in os.walk(root_dir):
            for filename in filenames:
                full_path = os.path.join(foldername, filename)
                f.write(full_path + "\n")
    print(f"✔️ File paths saved to {output_file}")

# Example usage — change this path to where your Synara folder lives
if __name__ == "__main__":
    index_all_files("C:/Users/YourUsername/Documents/Synara-core")