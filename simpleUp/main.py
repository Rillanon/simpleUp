from cement.core import foundation
import services

app = foundation.CementApp('simpleUp')
ps = services.ParseService()
cs = services.ClipBoardService()

try:
    app.setup()
    app.run()
    services.FileService()
    ps.parse(cs.get_clipboard_text())
    ps.get_credential()

except MemoryError:
    app.close(1)
finally:
    app.close(0)




