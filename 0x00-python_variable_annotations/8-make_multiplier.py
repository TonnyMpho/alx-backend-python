#!/usr/bin/env python3
""" type-annotated function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda val: val * multiplier
