from pathlib import Path
from PIL import Image

def detect_stego(file_path):
    """Detect basic LSB steganography patterns in an image."""
    
    file_path = Path(file_path)

    if not file_path.exists():
        return {"error": f"{file_path} does not exist"}

    try:
        img = Image.open(file_path)
        img_data = list(img.getdata())

        suspicious_pixels = 0

        for pixel in img_data:
            # Pixel may be single channel (grayscale) or tuple (RGB)
            values = pixel if isinstance(pixel, tuple) else (pixel,)

            # Check least significant bits
            for channel in values:
                if channel % 2 != 0:  # Odd values often used in steganography LSB
                    suspicious_pixels += 1
                    break

        total_pixels = len(img_data)
        percentage = (suspicious_pixels / total_pixels) * 100

        result = {
            "file": str(file_path),
            "format": img.format,
            "resolution": img.size,
            "mode": img.mode,
            "suspicious_pixel_ratio": f"{percentage:.2f}%"
        }

        # Result flag
        if percentage > 5:
            result["analysis_result"] = "⚠ Possible hidden data (LSB) detected"
        else:
            result["analysis_result"] = "✔ No significant signs of steganography"

        return result

    except Exception as e:
        return {"error": str(e)}


def lsb_score(file_path):
    """Lightweight risk score for watcher module."""
    
    result = detect_stego(file_path)

    if "suspicious_pixel_ratio" in result:
        # Convert "4.21%" → float
        return float(result["suspicious_pixel_ratio"].replace("%", ""))

    return 0.0


if __name__ == "__main__":
    test = input("Enter image path: ")
    print(detect_stego(test))
