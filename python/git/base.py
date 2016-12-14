import sys
from PySide import QtCore

git_cmds = None


def init(fw_root):
    global git_cmds
    if sys.platform == 'win32':
        from .git_win32 import GitCmds
    elif sys.platform == 'linux2':
        raise ImportError("Unsupported platform")
    elif sys.platform == 'darwin':
        raise ImportError("Unsupported platform")
    else:
        raise ImportError("Unsupported platform")

    git_cmds = GitCmds(fw_root)


def clone_subprocess(remote_url, local_url, branch):
    args = ["clone", "-b", branch, remote_url, local_url]
    process = QtCore.QProcess()
    process.setProcessChannelMode(process.MergedChannels)
    process.start(git_cmds.git, args)
    return process


def update_subprocess(local_url, remote='origin', branch=None):
    def call_git(args):
        process = QtCore.QProcess()
        process.setProcessChannelMode(process.MergedChannels)
        process.setWorkingDirectory(local_url)
        process.start(git_cmds.git, args)
        return process

    process_args = ['pull', remote]

    if branch is not None:
        p = call_git(['checkout', branch])  # Checkout [branch]
        if not p.waitForFinished(60000):  # Need to wait for process to finish
            return None

        p = call_git(['reset', "--hard", "origin/%s" % branch])  # Hard reset to origin/[branch]
        if not p.waitForFinished(60000):  # Ensure process is finished
            return None

        process_args.append(branch)

    return call_git(process_args)
