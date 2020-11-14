"""We assume that this file lives in the src dir, which lives in the root dir."""
import os

# TODO: tweak for running from exe vs. running from source
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
RESOURCES_DIR = os.path.join(PROJECT_ROOT, "resources")
DUMMY_DATA_DIR = os.path.join(RESOURCES_DIR, "dummy_data")
SRC_DIR = os.path.join(PROJECT_ROOT, "src")
LOGS_DIR = os.path.join(PROJECT_ROOT, "logs")
GRAPHS_DIR = os.path.join(PROJECT_ROOT, "graphs")
RESULTS_DIR = os.path.join(PROJECT_ROOT, "results")

OUTPUT_FOLDERS = [DUMMY_DATA_DIR,
                  LOGS_DIR,
                  GRAPHS_DIR,
                  RESOURCES_DIR]


def create_output_folders():
    """Create the output folders if they don't already exist."""
    for f in OUTPUT_FOLDERS:
        if not os.path.exists(f):
            os.mkdir(f)
