#!/usr/bin/env python

import fantail

@fantail.arg("name", help="Who do you want to say hello to??")
@fantail.command
def hello(app, args):
    """ Hello World """
    print("Hello {}!".format(args.name))

@fantail.arg('test')
@fantail.command
@fantail.memoize
def test(app, args):
    """ Wow """
    print(args)

if __name__ == '__main__':
    app = fantail.app()
    app.run()
