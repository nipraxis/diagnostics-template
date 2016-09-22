""" Tests for dvars calculation
"""

import os
import sys

import numpy as np

import nibabel as nib

MY_DIRECTORY = os.path.dirname(__file__)
SMALL_4D = os.path.join(MY_DIRECTORY, 'small_4d.nii')
SCRIPTS_DIRECTORY = os.path.join(MY_DIRECTORY, '..', 'scripts')
sys.path.append(SCRIPTS_DIRECTORY)

import calc_dvars


EXPECTED_RMS = [1.33811116,  1.53370821,  1.40858114]


def test_dvars():
    img = nib.load(SMALL_4D)
    rms_values = calc_dvars.calc_image_dvars(img)
    assert np.allclose(rms_values, EXPECTED_RMS)
