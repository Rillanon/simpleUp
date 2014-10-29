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


class ParseService:
    def __init__(self):
        self.credential = LogOnInfo()

    def parse(self, cb_string):
        import re
        try:
            m = re.search('ftp://(.+?)\+(.+?)@(.+?)', cb_string)
            if m:
                self.credential.username = m.group(1)
                self.credential.password = m.group(2)
                self.credential.host = m.group(3)
        except AttributeError:
            try:
                n = re.search('FTP Server: (.+?)\n Username: (.+?)\n Password: (.+?)\n', cb_string)
                if n:
                    self.credential.username = n.group(2)
                    self.credential.password = n.group(3)
                    self.credential.host = n.group(1)
            except AttributeError:
                print "No credentials found"

    def get_credential(self):
        if self.credential.empty() is False:
            print "credentials found"
            return self.credential
        else:
            print "empty credential"




