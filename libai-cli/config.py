import os
import sys
from os.path import join as opjoin, expanduser


BASE_URL = "http://localhost:8888"


# Default Paths
HOMEDIR_PATH = expanduser("~")
LIBAI_HDIR_PATH = opjoin(HOMEDIR_PATH, ".libai")
LIBAI_CONFIG_PATH = opjoin(LIBAI_HDIR_PATH, "config.json")
JWT_TOKEN_PATH = opjoin(LIBAI_HDIR_PATH, "jwt.token")
