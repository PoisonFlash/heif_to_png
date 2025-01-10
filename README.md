# This utility converts heif images in a given directory to png format.

This script scans provided directory tree and converts all HEIC files to PNG.
/// Written by PoisonFlash, 2024-08-23.
 
##Usage:
```cmd
python3 heif_to_png.py <dirpath> [-D | --delete]
```

### Arguments:
  <dirpath>            Path to the directory containing HEIC files.

### Optional Flags:
  -D, --delete         Delete the original HEIC files after conversion.

## Examples:
Convert HEIC files without deleting originals:
```cmd
python3 heif_to_png.py /path/to/your/directory
```

Convert HEIC files and delete originals after conversion:
```cmd
python3 heif_to_png.py /path/to/your/directory -D
```
