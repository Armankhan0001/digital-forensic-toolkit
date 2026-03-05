import hashlib
from pathlib import Path

def calc_hashes(file_path):
    """Calculate MD5 and SHA256 hashes of a file."""
    
    file_path = Path(file_path)

    if not file_path.exists():
        return {"error": f"{file_path} does not exist"}

    hash_md5 = hashlib.md5()
    hash_sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
            hash_sha256.update(chunk)

    return {
        "file": str(file_path),
        "md5": hash_md5.hexdigest(),
        "sha256": hash_sha256.hexdigest()
    }

if __name__ == "__main__":
    test = input("Enter file path: ")
    print(calc_hashes(test))
