#!/usr/bin/env python3

import argparse
import asyncio
from typing import Optional
from parseargs import setup_argparse
from api import user, token as apitoken, authhttpx, project, syncdir
from utils import printinfo, apicmd


async def async_main():
    parser = setup_argparse()
    args = parser.parse_args()

    args.cmd = args.cmd.lower() if args.cmd is not None else None
    result = await apicmd(args)
    print(result)


if __name__ == "__main__":
    asyncio.run(async_main())
