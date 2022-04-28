""" Module with routines for finding outliers
"""

import os.path as op
from glob import glob


def detect_outliers(fname):
    return [42]


def find_outliers(data_directory):
    """ Return filenames and outlier indices for images in `data_directory`.

    Parameters
    ----------
    data_directory : str
        Directory containing containing images.

    Returns
    -------
    outlier_dict : dict
        Dictionary with keys being filenames and values being lists of outliers
        for filename.
    """
    image_fnames = glob(op.join(data_directory, '**', 'sub-*.nii.gz'),
                        recursive=True)
    outlier_dict = {}
    for fname in image_fnames:
        outliers = detect_outliers(fname)
        outlier_dict[fname] = outliers
    return outlier_dict
