"""Analysis functions."""

import logging
import os

import matplotlib.pyplot as plt
import pandas as pd

from src.config import GRAPHS_DIR, RESULTS_DIR

LOGGER = logging.getLogger(__name__)


def analyse(df):
    """Run analysis."""
    assert isinstance(df, pd.DataFrame), "Expected DataFrame, got {}.".format(df)

    # Student with highest mean score
    top_avg_score = df.mean(axis=1).max()
    top_avg_student = df.mean(axis=1).idxmax()

    # Test with greatest range in scores
    highest_range = df.apply(lambda x: x.max() - x.min()).idxmax()

    # overall mean test score
    overall_mean = df.values.mean()

    # return results
    labels = ["Top student", "Test with greatest score range", "Overall mean test score"]
    results = [(top_avg_student, top_avg_score), highest_range, overall_mean]
    return pd.DataFrame({"result": results}, index=labels)


def save_results(results, input_filepath):
    """Save analysis results to the results dir in csv format."""
    filename = "results_" + os.path.basename(input_filepath)
    output_filepath = os.path.join(RESULTS_DIR, filename)
    LOGGER.debug("Generating results file: {}".format(output_filepath))

    results.to_csv(output_filepath)


def make_boxplot(df, input_filepath):
    """Save a boxplot png of the data in the graphs dir."""
    filename = os.path.basename(input_filepath)
    output_filepath = os.path.join(GRAPHS_DIR, filename).split(".")[0] + ".png"
    LOGGER.debug("Generating graph: {}".format(output_filepath))

    plt.boxplot(df)
    plt.xticks(ticks=range(1, len(df.columns)+1), labels=df.columns)
    plt.ylabel("Scores")
    plt.title("Distribution of scores for each test.")
    plt.savefig(output_filepath)
