import os.path

class GitCmds(object):
    def __init__(self, fw_root):
        git_folder = os.path.join(fw_root,
                                  'resources', 'win32', 'git')

        self.git = os.path.join(git_folder, 'bin', 'git')
