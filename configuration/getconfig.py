# log config
import logging.config
logging.config.fileConfig("../configuration/logging.ini")
log = logging.getLogger(__name__)

# app config
from configparser import ConfigParser
import os
configParser = ConfigParser()
configParser.read("../configuration/config.ini")
props = dict(configParser.items(os.environ.get("CONF", "DEFAULT")))
section = lambda sec, prop: configParser.items(sec, prop)
