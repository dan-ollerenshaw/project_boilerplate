"""Generate some dummy data. Lets pretend we're analysing student test scores."""
import logging
import os

import numpy as np
import pandas as pd

from src.config import DUMMY_DATA_DIR
from src.utils import get_timestamp

LOGGER = logging.getLogger(__name__)


def generate_dummy_data():
    """Create a csv file in the resources folder suitable for analysing."""
    df = _generate_frame((10, 5))
    filepath = os.path.join(DUMMY_DATA_DIR, _generate_filename())
    df.to_csv(filepath)
    LOGGER.debug("Created dummy data file: {}".format(filepath))
    return df, filepath


def _generate_frame(dimensions):
    """

    Args:
        dimensions (tuple): 2-length tuple of ints, e.g. (10, 5)

    Returns:
        Dummy dataset (pd.DataFrame)
    """
    x_dim = dimensions[0]
    y_dim = dimensions[1]
    row_labels = ["student_{}".format(i) for i in range(x_dim)]
    columns = ["test_{}".format(i) for i in range(y_dim)]

    return pd.DataFrame(data={col: _generate_datapoints(x_dim) for col in columns},
                        index=row_labels)


def _generate_datapoints(size):
    """Generate scores from 0-10.

    Args:
        size (int): length of array

    Returns:
        array of datapoints (np.array)
    """
    return np.random.randint(low=0, high=11, size=size)


def _generate_filename():
    return "{}_{}.csv".format("dummy_data", get_timestamp())


def _purge_dummy_data_folder():
    """Remove files in the resources folder matching the dummy data filename pattern."""
    LOGGER.debug("Scanning resources folder for dummy data files to delete.")
    dummy_files = [os.path.join(DUMMY_DATA_DIR, f) for f in os.listdir(DUMMY_DATA_DIR)]
    for f in dummy_files:
        LOGGER.debug("Deleting file: {}".format(f))
        os.remove(f)
