from cement.core import foundation
from simpleUp import classes

app = foundation.CementApp('simpleUp')
ps = classes.ParseService()
cs = classes.ClipBoardService()

try:
    app.setup()
    app.run()
    ps.parse(cs.get_clipboard_text())
    ps.get_credential()

except MemoryError:
    app.close(1)
finally:
    app.close(0)




