import requests

import os
import pathlib

import re
from string import Template as model



def init(env):
    setEnv(env)
    bootstrap(env)


def setEnv(env):
    baseURL = f"https://{env.allowed_domains[0]}"

    env.begURL = f"{baseURL}/{env.begURL}"
    env.endURL = f"{baseURL}/{env.endURL}"

    env.start_urls.append(env.begURL)

    env.extendedPattern = f"^{baseURL}/wp-content/uploads/(((pages-post-)?erikaa?|nv)[_-]?)?([0-9]{{1,3}}(-([137]{{2,3}}|suite|OUI))?)([_-]?(c?oo?k(ay|ii?|k)?){{1,3}})?(-[12])?([_-]?(bis|tris))?\.(jpe?g|png)$"
    env.S = "\033[1;31m" # set color to bold red
    env.R = "\033[0m"    # reset color to normal

    env.outDir = "./out"
    env.tDir = f"{env.outDir}/{env.tDir}"
    env.urlFile = f"{env.outDir}/{env.urlFile}"

    env.nbPages = 0
    env.totalCptImgs = 0 # total number of downloaded images


def bootstrap(env):
    pathlib.Path(env.outDir).mkdir(exist_ok=True)

    env.tDir = createNumbered(env, env.tDir, False)
    env.urlFile = createNumbered(env, env.urlFile, True)


def createNumbered(env, initialName, isFile = True):
    testExistence = os.path.isfile if isFile else os.path.isdir

    if testExistence(initialName):
        cpt = 1
        newInitialName = f"{initialName}_{cpt}"
        env.logger.warning(f"{os.path.basename(initialName)} already exists, trying to create {os.path.basename(newInitialName)}")

        while testExistence(newInitialName):
            env.logger.warning(f"{os.path.basename(newInitialName)} already exists too")
            cpt += 1
            newInitialName = f"{initialName}_{cpt}"

        initialName = newInitialName

    if isFile:
        env.logger.warning(f"File {os.path.basename(initialName)} does not exist yet")
    else:
        os.mkdir(initialName)
        env.logger.warning(f"Created directory {os.path.basename(initialName)}")

    return initialName
