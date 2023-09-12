import os
import sys
from os.path import join as opjoin, dirname, abspath, exists, expanduser


BASE_URL = "http://localhost:8888"


HOMEDIR = expanduser("~")
LIBAI_HDIR = opjoin(HOMEDIR, ".libai")

LIBAI_CONFIG = opjoin(LIBAI_HDIR, "config.json")


# PATHS
class Paths:
    HOMEDIR = expanduser("~")
    LIBAI_HDIR = opjoin(HOMEDIR, ".libai")
    LIBAI_CONFIG = opjoin(LIBAI_HDIR, "config.json")
    TOKEN_PATH = opjoin(LIBAI_HDIR, 'jwt.token')

    PATH_ATTRS = (HOMEDIR, LIBAI_HDIR, LIBAI_CONFIG, TOKEN_PATH)

    async def yield_paths(self):
        for path in self.PATH_ATTRS:
            yield path

    async def __iter__(self):
        return await self.yield_paths()

    async def paths_dict(self):
        {
            'paths': {
                "HOMEDIR": self.HOMEDIR,
                "LIBAI_HDIR": self.LIBAI_HDIR,
                "LIBAI_CONFIG": self.LIBAI_CONFIG,
                "TOKEN_PATH": self.TOKEN_PATH,
            }
        }


class CliConf:
    def __init__(self):
        self.PATHS = tuple(Paths.yield_paths())
        self.json_dict = {
            'paths': {
                k: v
                for k, v in zip(
                    ('HOMEDIR', 'LIBAI_HDIR', 'LIBAI_CONFIG', 'TOKEN_PATH'),
                    self.PATHS,
                )
            }
        }

        def as_json(self, *args, **kwargs):
            jdict = self.json_dict
            for k, v in jdict.items():
                print(f"{k}: {v}")

        self.BASE_URL, se = BASE_URL
