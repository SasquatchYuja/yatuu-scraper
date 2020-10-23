import requests

import os
import pathlib

import re
from string import Template as model



def init(env):
    setEnv(env)
    bootstrap(env)
