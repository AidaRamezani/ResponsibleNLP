
import argparse
import random

from robbie.datasets import Dataset
from robbie.metrics import Metric
from robbie.predictors import Predictor
from robbie.runner import Runner
import pandas as pd
import argparse


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(conflict_handler="resolve")
    parser.add_argument("--result-dir", required=True)
    parser.add_argument("--num-samples", required=False, type=int, default=None)
    parser.add_argument("--seed", required=False, type=int, default=0)

    Dataset.add_args(parser)
    Predictor.add_args(parser)
    Metric.add_args(parser)

    args = parser.parse_args()
    

    dataset = Dataset.build(args)
    

    
