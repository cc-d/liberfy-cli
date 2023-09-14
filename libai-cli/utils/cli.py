import argparse
import asyncio
from typing import Dict, Optional

import httpx
from api import project, syncdir, user
from api.utils import authhttpx
from httpx import Response
from logfunc import logf

from . import jwttoken


async def printinfo() -> None:
    async def lr(word: str, n=5, useprint=True):
        pstr = "\n%s %s %s\n" % ("=" * n, word, "=" * n)
        if useprint:
            print(pstr)
        return pstr

    await lr('INFO')  # ==== INFO ====
    token = await jwttoken.read()
    if token:
        print(f"Currently saved token: {token}")
    else:
        print("No token found.")


@logf()
async def apicmd(parser: argparse.ArgumentParser):
    args = parser.parse_args()
    print(args)
    for k, v in args.__dict__.items():
        print(k, v)
    if not hasattr(args, 'cmd') or args.cmd is None:
        parser.print_help()
        return

    if args.cmd.startswith('u'):
        act = args.act if args.act is not None else ''
        if act.startswith('c'):
            return await user.create(args.email, args.password)
        elif act.startswith('l'):
            return await user.tokenlogin(args.email, args.password)
        elif act.startswith('m'):
            return await user.me()
    elif args.cmd.startswith('p'):
        act = args.act if args.act is not None else ''
        if act.startswith('c'):
            return await project.create(
                args.name if args.name is not None else 'New Project'
            )
        elif act.startswith('a'):
            return await project.all()
        elif act.startswith('g'):
            return await project.get(args.project_id)
    elif args.cmd.startswith('s'):
        act = args.act if args.act is not None else ''
        if act.startswith('c'):
            return await syncdir.create(args.project_id, args.path)
        elif act.startswith('a'):
            return await syncdir.all(args.project_id)
        elif act.startswith('g'):
            return await syncdir.get(args.project_id, args.syncdir_id)
    elif args.cmd.startswith('i'):
        return await printinfo()
    else:
        parser.print_help()
        return
    return
