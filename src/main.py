import sys
import os
import subprocess
import argparse

# Set the API key
if not os.getenv("MISTRALAI_API_KEY"):
    os.environ["MISTRALAI_API_KEY"] = getpass.getpass("Bt9sJgE1XLJzpfIvUWs02Hz3ccGxef3t")

def main():
    parser = argparse.ArgumentParser(description='Main script to compute embeddings and get character info.')
    parser.add_argument('command', choices=['compute-embeddings', 'get-character-info'], help='Command to run.')
    parser.add_argument('--input-dir', help='Directory containing story files.')
    parser.add_argument('--index-path', help='Path to save/load the FAISS index.')
    parser.add_argument('--metadata-path', help='Path to save/load the metadata.')
    parser.add_argument('--character-name', help='Name of the character.')
    args = parser.parse_args()

    if args.command == "compute-embeddings":
        if not all([args.input_dir, args.index_path, args.metadata_path]):
            parser.error('The following arguments are required for compute-embeddings: --input-dir, --index-path, --metadata-path')
        subprocess.run([sys.executable, 'src/compute_embeddings.py', '--input-dir', args.input_dir, '--index-path', args.index_path, '--metadata-path', args.metadata_path])
    elif args.command == "get-character-info":
        if not all([args.index_path, args.metadata_path, args.character_name]):
            parser.error('The following arguments are required for get-character-info: --index-path, --metadata-path, --character-name')
        subprocess.run([sys.executable, 'src/get_character_info.py', '--index-path', args.index_path, '--metadata-path', args.metadata_path, '--character-name', args.character_name])
    else:
        parser.error('Invalid command')

if __name__ == "__main__":
    main()
