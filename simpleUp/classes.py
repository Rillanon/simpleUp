class LogOnInfo:

    def __init__(self):
        self.host = None
        self.username = None
        self.password = None

    @staticmethod
    def empty(self):
        if (self.host is None) | (self.username is None) | (self.password is None):
            return True
        else:
            return False

class ClipBoardService:
    def __init__(self):
        self.clip_board_text = None

    def get_clipboard_text(self):
        from Tkinter import Tk
        self.clip_board_text = Tk().clipboard_get()
        return self.clip_board_text

class ParseService:
    def __init__(self):
        self.credential = LogOnInfo()
        self.credential_found = None

    def parse(self, cb_string):
        import re
        try:
            m = re.search("((ftp://)(.+):(.+)@(.+))", cb_string)
            n = re.search('FTP Server: (.+?)\n Username: (.+?)\n Password: (.+?)\n', cb_string)
            if m:
                self.credential.username = m.group(3)
                self.credential.password = m.group(4)
                self.credential.host = m.group(5)
                self.credential_found = True
                return True
            elif n:
                self.credential.username = n.group(2)
                self.credential.password = n.group(3)
                self.credential.host = n.group(1)
                self.credential_found = True
                return True
            else:
                return False

        except AttributeError:
            self.credential_found = False
            return False

    def get_credential(self):
        if self.credential.empty() is False:
            print self.credential.username
        else:
            print "no credentials found"





