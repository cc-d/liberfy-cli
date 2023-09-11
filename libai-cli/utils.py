import argparse
import asyncio
from typing import Dict, Optional
from logfunc import logf
import httpx
from api import authhttpx, project, syncdir, token as apitoken, user
from httpx import Response


async def printinfo() -> None:
    token = apitoken.load_token()
    if token:
        print(f"Currently saved token: {token}")
    else:
        print("No token found.")


@logf()
async def apicmd(parseargs):
    args = parseargs
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
            return await syncdir.create_syncdir(args.project_id, args.path)
        elif act.startswith('a'):
            return await syncdir.get_all_syncdirs(args.project_id)
        elif act.startswith('g'):
            return await syncdir.get_syncdir(args.project_id, args.syncdir_id)
    elif args.cmd == "info":
        return await printinfo()
