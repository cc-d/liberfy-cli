import argparse
from logfunc import logf


@logf()
def setup_argparse() -> argparse.ArgumentParser:
    """
    Set up argparse for Liberfy CLI.

    Returns:
        argparse.ArgumentParser: Configured argparse object for CLI.
    """
    parser = argparse.ArgumentParser(
        description="CLI for user, project, sync directory, and directory file management."
    )
    subparsers = parser.add_subparsers(dest="cmd")

    # User Commands
    user = subparsers.add_parser(
        "user", aliases=["u"], help="Manage users ('/user')."
    )
    user_subparsers = user.add_subparsers(dest="act")

    create_user = user_subparsers.add_parser(
        "create", aliases=["c"], help="Create a new user ('/user/create')."
    )
    create_user.add_argument("email", help="Email")
    create_user.add_argument("password", help="Password")

    token_user = user_subparsers.add_parser(
        "login",
        aliases=["l"],
        help="Get use login token with email/password ('/user/tokenlogin').",
    )
    token_user.add_argument("email", help="Email")
    token_user.add_argument("password", help="Password")

    me_user = user_subparsers.add_parser(
        "me", aliases=["m"], help="Get user details ('/user/me')."
    )

    # Project Commands
    project = subparsers.add_parser(
        "project", aliases=["p"], help="Manage projects ('/project')."
    )
    project_subparsers = project.add_subparsers(dest="act")
    project_all = project_subparsers.add_parser(
        "all", aliases=["a"], help="Get all projects ('/project/all')."
    )

    create_project = project_subparsers.add_parser(
        "create",
        aliases=["c"],
        help="Create a new project ('/project/create').",
    )
    create_project.add_argument(
        "name", default="DefaultProjectName", help="Name"
    )
    get_project = project_subparsers.add_parser(
        "get", aliases=["g"], help="Get project ('/project/get')."
    )

    get_project.add_argument("project_id", help="Project ID")

    # SyncDir Commands
    syncdir = subparsers.add_parser(
        "syncdir", aliases=["s"], help="Manage sync directories ('/syncdir')."
    )
    syncdir_subparsers = syncdir.add_subparsers(dest="act")

    init_syncdir = syncdir_subparsers.add_parser(
        "init",
        aliases=["i"],
        help="Initialize a new sync directory ('/syncdir/init').",
    )
    init_syncdir.add_argument("--p", required=True, help="Path")
    init_syncdir.add_argument("--pid", required=True, help="Project ID")

    details_syncdir = syncdir_subparsers.add_parser(
        "details",
        aliases=["d"],
        help="Get sync directory details ('/syncdir/details').",
    )
    details_syncdir.add_argument("--p", required=True, help="Project ID")
    details_syncdir.add_argument("--s", required=True, help="SyncDir ID")

    # DirFile Commands
    dirfile = subparsers.add_parser(
        "dirfile", aliases=["d"], help="Manage directory files ('/dirfile')."
    )
    dirfile_subparsers = dirfile.add_subparsers(dest="act")

    create_dirfile = dirfile_subparsers.add_parser(
        "create",
        aliases=["c"],
        help="Create a directory file ('/dirfile/create').",
    )
    create_dirfile.add_argument("--r", required=True, help="Relative Path")
    create_dirfile.add_argument("--c", help="Content")
    create_dirfile.add_argument("--sid", required=True, help="SyncDir ID")
    create_dirfile.add_argument("--cs", required=True, help="Checksum")
    create_dirfile.add_argument("--cst", default="md5", help="Checksum Type")

    # Info Commands
    info = subparsers.add_parser(
        "info", aliases=["i"], help="Get info of current liberfy-cli install"
    )

    return parser
