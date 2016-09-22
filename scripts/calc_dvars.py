""" Script to calculate dvars values

For testing run::

    python3 scripts/calc_dvars.py tests/small_4d.nii

You should see:

    [1.33811116,  1.53370821,  1.40858114]

If you make that work, try running this script over one of your own images.

Next, in IPython, import this module, and use the ``calc_image_dvars`` function
to calculate the DVARS values for one of your images.

Plot the results.

Don't forget the "%matplotlib" in IPython

If you make that work, check that the tests pass by:

* Installing the ``pytest`` module from the terminal with::

    pip install pytest

  Then run the tests with::

   py.test
"""

import sys

import numpy as np

import nibabel as nib


def calc_image_dvars(img):
    """ Root mean squared difference between volumes in `img`.

    Parameters
    ----------
    img : image object
        nibabel image object containing 4D file, with last dimension length
        ``t``.

    Returns
    -------
    dvars : shape (t-1,) array
        1D array with root mean square difference values between each volume
        and the following volume
    """
    # For each voxel, calculate the differences between each volume and the one
    # following;
    #
    # Square the differences;
    # Sum over voxels for each volume, and divide by the number of voxels;
    # Return the square root of these values.
    raise RuntimeError('No code yet')


def main():
    # Get the first command line argument
    filename = sys.argv[1]
    img = nib.load(filename)
    print(calc_image_dvars(img))


if __name__ == '__main__':
    main()
