__author__ = 'ima'
import npyscreen

class SimpleUp(npyscreen.NPSApp):
    def main(self):
        F = npyscreen.Form(name="simpleUP - simple utility")
        F.edit()
if __name__ == "__main__":
    App = SimpleUp()
    App.run()





