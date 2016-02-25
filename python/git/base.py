import sys
import subprocess

git_cmds = None

def init(fw_root):
    global git_cmds
    if sys.platform == 'win32':
        from .git_win32 import GitCmds
    elif sys.platofrm == 'linux2':
        raise ImportError("Unsupported platform")
    elif sys.platform == 'darwin':
        raise ImportError("Unsupported platform")
    else:
        raise ImportError("Unsupported platform")

    git_cmds = GitCmds(fw_root)

def clone_subprocess(remote_url, local_url, branch):
    process_args = [git_cmds.git, 'clone',
                    '-b', branch,
                    remote_url, local_url]

    return subprocess.Popen(process_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            universal_newlines=True, bufsize=0)

def update_subprocess(local_url, remote='origin', branch=None):
    process_args = [git_cmds.git, 'pull', remote]
    if branch is not None:
        process_args.append(branch)

    return subprocess.Popen(process_args,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            cwd=local_url,
                            universal_newlines=True, bufsize=0)
