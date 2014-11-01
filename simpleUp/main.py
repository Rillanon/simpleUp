from cement.core import foundation
from simpleUp import classes

app = foundation.CementApp('simpleUp')
clipboard = classes.ClipBoardService()

try:
    app.setup()
    app.run()
    print clipboard.get_clipboard_text()

except MemoryError:
    app.close(1)
finally:
    app.close(0)




