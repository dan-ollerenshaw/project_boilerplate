"""We assume that this file lives in the src dir, which lives in the root dir."""
import os

# TODO: tweak for running from exe vs. running from source
#TODO: since git doesn't bother with empty folders, we might want to generate them first
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
RESOURCES_DIR = os.path.join(PROJECT_ROOT, "resources")
DUMMY_DATA_DIR = os.path.join(RESOURCES_DIR, "dummy_data")
SRC_DIR = os.path.join(PROJECT_ROOT, "src")
LOGS_DIR = os.path.join(PROJECT_ROOT, "logs")
GRAPHS_DIR = os.path.join(PROJECT_ROOT, "graphs")
RESULTS_DIR = os.path.join(PROJECT_ROOT, "results")
