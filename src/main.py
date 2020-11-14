"""Read some raw data, do some data manipulations and save a results file."""

import argparse
import logging

import pandas as pd

from src.analysis import analyse, make_boxplot, save_results
from src.config import create_output_folders
from src.logger import setup_logging
from src.generate_dummy_data import generate_dummy_data


LOGGER = logging.getLogger(__name__)


def main(input_filepath=None):
    """Read a data file, perform analysis X, and save a results file.


    Args:
        input_filepath (str): optional, if None, then a dummy file is generated.

    """
    LOGGER.info("Starting program.")

    # read data
    if input_filepath:
        df = pd.read_csv(input_filepath, index_col=0)
    else:
        df, input_filepath = generate_dummy_data()

    # analyse
    results = analyse(df)
    save_results(results, input_filepath)

    # make graphs
    make_boxplot(df, input_filepath)

    LOGGER.info("Ending program.")


def _parse_args():
    parser = argparse.ArgumentParser(description="Perform analysis X on a data file.")
    parser.add_argument(
        "--input_filepath", type=str, help="Path to input data file."
    )
    return parser.parse_args()


if __name__ == '__main__':
    # for now this only works with path hacking. so we need tox
    ARGS = _parse_args()
    create_output_folders()
    setup_logging()
    main(input_filepath=ARGS.input_filepath)
