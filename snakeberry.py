## common.py
## This file is part of Snakeberry by Bruno Hautzenberger (http://the-engine.at)
## Dual-licensed under the MIT (http://www.opensource.org/licenses/mit-license.php)
## and the Beerware (http://en.wikipedia.org/wiki/Beerware) license.

import tornado.ioloop
import tornado.web
import common
from snakeberryJSON import *
from radio import *
from audioSystem import *
from services import *

#Main loop
#Generates all service endpoints
#Author: Bruno Hautzenberger



if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", ListServices),
        (r"/radios", ListRadios),
        (r"/radio/play/(.*)", PlayRadio),
        (r"/radio/stop", StopRadio),
        (r"/radio/nowplaying", RadioNowPlaying),
        (r"/getvolume", GetVolume),
        (r"/setvolume/(.*)", SetVolume),
        (r"/getmac", GetMac),
        (r"/start",start),
        (r"/admin",admin),
        (r"/addradio",EditRadios),
        (r"/removeradio",RemoveRadio),
        (r"/shutdown",shutdown)
    ],static_path=common.STATIC_PATH)
    application.listen(8888) #Todo load port from a config file or so
    tornado.ioloop.IOLoop.instance().start()



