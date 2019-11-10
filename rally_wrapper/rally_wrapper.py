#!/usr/bin/env python

import os
import argparse
import logging

import trigger_rally

logger = logging.getLogger("snafu")

class rally_wrapper():
    def __init__(self, parser):
        parser.add_argument(
            "-c", "--config",
            help="Rally configuration file")
        parser.add_argument(
            '-s', '--sample',
            type=int,
            help='number of times to run benchmark, defaults to 1',
            default=1)
        self.args = parser.parse_args()

        self.browbeat_config = self.args.config
        self.sample_size = self.args.sample

    def run(self):
        print("hello")
        rally_generator = trigger_rally.rally_trigger(logger)
        yield rally_generator
