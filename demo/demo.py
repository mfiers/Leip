#!/usr/bin/env python

import fantail


@fantail.arg("name", help="Who do you want to say hello to??")
@fantail.command
def hello(app, args):
    """ Hello World """
    print("Hello {}!".format(args.name))


@fantail.cache()
@fantail.arg("output", cache='output')
@fantail.arg("val", help="value to take the sqrt of.", type=float)
@fantail.command
def sqrt(app, args):
    """Calculate sqrt"""
    import math
    import time
    x = math.sqrt(args.val)
    time.sleep(10)
    with open(args.output, 'w') as F:
        F.write(str(x))


if __name__ == '__main__':
    app = fantail.app()
    app.run()
