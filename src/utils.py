"""General purpose, reusable functions."""

import time


def get_timestamp():
    """Get a filename-friendly timestamp for the current time."""
    return time.strftime("%Y-%m-%d_%H-%M-%S")
