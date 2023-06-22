""" Python script to validate data

Run as:

    python3 scripts/validata_data.py data
"""

from pathlib import Path
import sys
import hashlib

def file_hash(filename):
    """ Get byte contents of file `filename`, return SHA1 hash

    Parameters
    ----------
    filename : str
        Name of file to read

    Returns
    -------
    hash : str
        SHA1 hexadecimal hash string for contents of `filename`.
    """
    hash = hashlib.sha1()
  
    with open(filename, 'rb') as f:
        contents = f.read()  
    return hashlib.sha1(contents).hexdigest()
    # Open the file, read contents as bytes.
    # Calculate, return SHA1 has on the bytes from the file.
    # This is a placeholder, replace it to write your solution.
    raise NotImplementedError(
        'This is just a template -- you are expected to code this.')


def validate_data(data_directory):
    """ Read ``data_hashes.txt`` file in `data_directory`, check hashes

    Parameters
    ----------
    data_directory : str
        Directory containing data and ``data_hashes.txt`` file.

    Returns
    -------
    None

    Raises
    ------
    ValueError:
        If hash value for any file is different from hash value recorded in
        ``data_hashes.txt`` file.
    """
    data_path = Path(data_directory) / "data_hashes.txt"
    with open(data_path) as f:
        lines = f.readlines()
        for line in lines:
            hash, file_path = line.split()
            if hash != file_hash(data_path.parent / file_path):
                raise ValueError(f"The file {file_path} is damaged")
        f.close()
            
    # Read lines from ``data_hashes.txt`` file.
    # Split into SHA1 hash and filename
    # Calculate actual hash for given filename.
    # If hash for filename is not the same as the one in the file, raise
    # ValueError
    # This is a placeholder, replace it to write your solution.
    # raise NotImplementedError('This is just a template -- you are expected to code this.')


def main():
    # This function (main) called when this file run as a script.
    #
    # Get the data directory from the command line arguments
    if len(sys.argv) < 2:
        raise RuntimeError("Please give data directory on "
                           "command line")
    data_directory = sys.argv[1]
    # Call function to validate data in data directory
    validate_data(data_directory)


if __name__ == '__main__':
    # Python is running this file as a script, not importing it.
    main()
