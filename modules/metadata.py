from PIL import Image, ExifTags
import exifread
import os, datetime

def extract_exif(path):
    try:
        img = Image.open(path)
        raw = img._getexif()
        if not raw: return {}
        return {ExifTags.TAGS.get(k,k): v for k,v in raw.items()}
    except:
        return {}

def extract_filesystem(path):
    st = os.stat(path)
    return {
        'created': datetime.datetime.fromtimestamp(st.st_ctime).isoformat(),
        'modified': datetime.datetime.fromtimestamp(st.st_mtime).isoformat(),
        'accessed': datetime.datetime.fromtimestamp(st.st_atime).isoformat()
    }

def extract_exif_exifread(path):
    try:
        with open(path, "rb") as f:
            tags = exifread.process_file(f)
            return {str(k): str(v) for k,v in tags.items()}
    except:
        return {}

def extract_metadata(path):
    return {
        "filesystem": extract_filesystem(path),
        "exif_pillow": extract_exif(path),
        "exif_exifread": extract_exif_exifread(path)
    }
