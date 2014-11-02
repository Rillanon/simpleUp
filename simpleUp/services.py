import entities


class ClipBoardService:
    def __init__(self):
        self.clip_board_text = None

    def get_clipboard_text(self):
        from Tkinter import Tk
        self.clip_board_text = Tk().clipboard_get()
        return self.clip_board_text


class ParseService:
    def __init__(self):
        self.credential = entities.AuthInfo()
        self.credential_found = None

    #parse returns true or false on if the text from clipboard contains the host details
    def parse(self, cb_string):
        import re
        try:
            #regex to get the host/user/pass for the ftp host
            m = re.search("((ftp://)(.+):(.+)@(.+))", cb_string)
            n = re.search('((FTP Server: )(.+)\n\n(Username: )(.+)\n\n(Password: )(.+)\n\n)', cb_string)
            if m:
                self.credential.username = m.group(3)
                self.credential.password = m.group(4)
                self.credential.host = m.group(5)
                self.credential_found = True
                return True
            elif n:
                self.credential.username = n.group(5)
                self.credential.password = n.group(7)
                self.credential.host = n.group(3)
                self.credential_found = True
                return True
            else:
                self.credential_found = False
                return False

        except AttributeError:
            self.credential_found = False
            return False

    def get_credential(self):
        if self.credential_found:
            print self.credential.username
        else:
            print "no credentials found"


class FTPService:

    def __init__(self):
        self.credential = entities.AuthInfo()
        self.session = None
        self.file = None
        self.file_path = None

    def set_host(self, auth_info):
        self.credential = auth_info

    def set_file_path(self, file_path):
        self.file_path = file_path

    def upload(self):
        import ftplib
        import datetime
        self.session = ftplib.FTP(self.credential.host,
                                  self.credential.username,
                                  self.credential.password)

        self.file = open(self.file_path, "rb")

        # saves to the ftp host using current date time as filename
        self.session.storbinary(datetime.datetime.now() + ".zip", self.file)

        self.session.quit()


class FileService:
    def __init__(self):
        import win32com.client
        cls_id = '{9BA05972-F6A8-11CF-A442-00A0C90A8F39}'
        shell_windows=win32com.client.Dispatch(cls_id)
        for i in range(shell_windows.Count):
            print shell_windows[i].LocationURL
            for j in range(shell_windows[i].Document.SelectedItems().Count):
                print '  ', shell_windows[i].Document.SelectedItems().Item(j).Path








