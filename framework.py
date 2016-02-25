import sgtk

class RepoUtilsFramework(sgtk.platform.Framework):

    ##########################################################################################
    # init and destroy

    def init_framework(self):
        self.log_debug("%s: Initializing..." % self)

    def destroy_framework(self):
        self.log_debug("%s: Destroying..." % self)
