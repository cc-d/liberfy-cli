#!/usr/bin/env python3

import argparse
import asyncio
from typing import Optional
from parseargs import setup_argparse
from logfunc import logf
import utils.cli as cliutils


@logf()
async def async_main():
    parser = setup_argparse()

    result = await cliutils.apicmd(parser)

    print(result)
    return result


if __name__ == "__main__":
    asyncio.run(async_main())
