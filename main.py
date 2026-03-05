import argparse
import json

from modules.hashes import calc_hashes
from modules.metadata import extract_metadata
from modules.stego import detect_stego
from modules.timeline import build_timeline
from modules.watcher import watch_directory
from modules.imaging import create_disk_image

def main():
    parser = argparse.ArgumentParser(description="Digital Forensics Toolkit")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Hash command
    hash_parser = subparsers.add_parser("hash", help="Calculate MD5 and SHA256 hashes of a file")
    hash_parser.add_argument("file", help="File path")

    # Metadata command
    metadata_parser = subparsers.add_parser("metadata", help="Extract file metadata")
    metadata_parser.add_argument("file", help="File path")

    # Stego command
    stego_parser = subparsers.add_parser("stego", help="Detect hidden data in image (steganography)")
    stego_parser.add_argument("file", help="Image file path")

    # Timeline command
    timeline_parser = subparsers.add_parser("timeline", help="Create timeline from folder")
    timeline_parser.add_argument("folder", help="Folder path")

    # Disk Imaging command
    image_parser = subparsers.add_parser("image-disk", help="Create forensic disk image")
    image_parser.add_argument("source", help="Disk source (e.g., /dev/sdb)")
    image_parser.add_argument("output", help="Output forensic image (e.g., forensic.dd)")

    # Watch Command
    watch_parser = subparsers.add_parser("watch", help="Monitor folder in real time for file changes")
    watch_parser.add_argument("folder", help="Folder path")

    args = parser.parse_args()
    result = None

    # Command Handling
    if args.command == "hash":
        result = calc_hashes(args.file)

    elif args.command == "metadata":
        result = extract_metadata(args.file)

    elif args.command == "stego":
        result = detect_stego(args.file)

    elif args.command == "timeline":
        result = build_timeline(args.folder)

    elif args.command == "image-disk":
        result = create_disk_image(args.source, args.output)

    elif args.command == "watch":
        watch_directory(args.folder)
        return  # No output format needed

    # Print results formatted as JSON
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
