import logging as lg
import leip

@leip.hook('prepare')
def test_pre_run(app):
    lg.warning("Running pre_run for app %s" % app)
    
