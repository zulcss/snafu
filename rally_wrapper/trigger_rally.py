import yaml
import subprocess
import logging

class RallyWrapperException(Exception):
    pass

class rally_trigger:
    """
        Will execute with the provided arguments and return normalized results
        for indexing
    """
    def __init__(self, logger):
        self.logger = logger

    def emit_actions(self):
        """
        Executes test and calls document parsers, if index_data is true will
        yield normalized data.
        """
        print("hello again")
