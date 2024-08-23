import sys
import argparse
import pyheif
from PIL import Image
from pathlib import Path


def convert_heic_to_png(heic_file_path: Path, output_png_path: Path) -> None:
    heif_file = pyheif.read(heic_file_path)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    image.save(output_png_path, "PNG")


def convert_all(dirpath: Path, delete_converted=False) -> None:
    counter = 0
    for heic_file in dirpath.rglob('*.HEIC'):
        if heic_file.is_file():
            output_png = heic_file.with_suffix(f'.PNG').with_name(heic_file.stem + '_conv' + f'.PNG')
            print(f"Converting {heic_file} >> {output_png}", end='... ')
            convert_heic_to_png(heic_file, output_png)
            print('done')
            if delete_converted:
                print(f"\tDeleting '{heic_file}'")
                heic_file.unlink()
            counter += 1

    if counter > 0:
        print(f"Operation completed, converted {counter} HEIC files to PNG.")
    else:
        print(f"No files converted")


def print_usage_info():
    usage_message = """
    This script scans provided directory tree and converts all HEIC files to PNG.
    /// Written by PoisonFlash, 2024-08-23.
     
    Usage: python your_script.py <dirpath> [-D | --delete]

    Arguments:
      <dirpath>            Path to the directory containing HEIC files.

    Optional Flags:
      -D, --delete         Delete the original HEIC files after conversion.

    Examples:
      Convert HEIC files without deleting originals:
        python your_script.py /path/to/your/directory

      Convert HEIC files and delete originals after conversion:
        python your_script.py /path/to/your/directory -D
    """
    print(usage_message)


# if __name__ == '__main__':
#     d = Path(r'/home/evgeny/Documents/Projects/heif_to_png/tests/test_imgs/')
#     convert_all(d, delete_converted=True)

if __name__ == "__main__":
    # Initialize the argument parser
    parser = argparse.ArgumentParser(add_help=False)  # Disable default help to customize behavior

    # Positional argument for the directory path
    parser.add_argument("dirpath", type=str, nargs='?', help="Path to the directory containing HEIC files")

    # Optional flag for deleting the original HEIC files
    parser.add_argument("-D", "--delete", action="store_true", help="Delete the original HEIC files after conversion")

    # Add custom help options
    parser.add_argument("-h", "--help", action="store_true", help="Show usage information and exit")

    # Parse the arguments
    args = parser.parse_args()

    # If -h/--help flag is provided or no arguments are given, show usage info
    if args.help or len(sys.argv) == 1:
        print_usage_info()
        sys.exit(0)

    # If the dirpath is not provided, show usage info
    if args.dirpath is None:
        print_usage_info()
        sys.exit(1)

    # Convert the directory path string to a Path object
    dirpath = Path(args.dirpath)

    # Call the conversion function with the provided arguments
    convert_all(dirpath, delete_converted=args.delete)
