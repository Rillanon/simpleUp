from cement.core import foundation

app = foundation.CementApp('simpleUp')
try:
    app.setup()
    app.run()
    print "simple so simple..."
except:
    app.close(1)
finally:
    app.close(0)




