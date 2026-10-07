import os
from PIL import Image
from pillow_heif import register_heif_opener

# Register HEIC opener with Pillow
register_heif_opener()


def convert_heic_folder(source_folder, output_format="JPG", keep_original=True):
    """
    Converts all HEIC/HEIF files in a specified folder to JPG or PNG.

    :param source_folder: Path to the folder containing HEIC images.
    :param output_format: 'JPG' or 'PNG' (default is 'JPG').
    :param keep_original: If False, deletes the original .heic files after conversion.
    """
    target_ext = f".{output_format.lower()}"
    if output_format.upper() == "JPEG":
        target_ext = ".jpg"

    # Ensure folder path exists
    if not os.path.exists(source_folder):
        print(f"Error: Directory '{source_folder}' does not exist.")
        return

    # Process all files in the directory
    converted_count = 0
    for file_name in os.listdir(source_folder):
        if file_name.lower().endswith(('.heic', '.heif')):
            heic_path = os.path.join(source_folder, file_name)

            # Formulate output file name
            base_name = os.path.splitext(file_name)[0]
            output_path = os.path.join(source_folder, f"{base_name}{target_ext}")

            try:
                # Open HEIC image and convert
                with Image.open(heic_path) as img:
                    # Convert RGBA to RGB if saving to JPG
                    if output_format.upper() == "JPG" and img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")

                    img.save(output_path, format=output_format.upper(), quality=95)
                    print(f"Converted: {file_name} -> {os.path.basename(output_path)}")
                    converted_count += 1

                # Optional: Delete original after conversion
                if not keep_original:
                    os.remove(heic_path)

            except Exception as e:
                print(f"Failed to convert {file_name}: {e}")

    print(f"\nFinished! Converted {converted_count} file(s).")


# --- Example Usage ---
if __name__ == "__main__":
    # Replace with your actual folder path
    folder_path = input('Please enter folder path.\n')

    # Choose output format: 'JPG' or 'PNG'
    convert_heic_folder(folder_path, output_format="JPEG", keep_original=True)