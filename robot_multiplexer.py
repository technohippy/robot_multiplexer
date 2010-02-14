from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from waveapi import robot_abstract
from waveapi.robot import RobotCapabilitiesHandler
from waveapi.robot import RobotProfileHandler
from waveapi.robot import RobotEventHandler

class RobotMultiplexingCapabilitiesHandler(RobotCapabilitiesHandler):
  def __init__(self, subdomain_dict):
    self._subdomain_dict = subdomain_dict
    self._robot = self._subdomain_dict[-1][1]

  def get(self):
    host = self.request.host
    for (subdomain, robot) in self._subdomain_dict:
      if host.startswith(subdomain + '.'):
        self._robot = robot
        break
    RobotCapabilitiesHandler.get(self)

class RobotMultiplexingProfileHandler(RobotProfileHandler):
  def __init__(self, subdomain_dict):
    self._subdomain_dict = subdomain_dict
    self._robot = self._subdomain_dict[-1][1]

  def get(self):
    host = self.request.host
    for (subdomain, robot) in self._subdomain_dict:
      if host.startswith(subdomain + '.'):
        self._robot = robot
        break
    RobotProfileHandler.get(self)

class RobotMultiplexingJsonrpcHandler(RobotEventHandler):
  def __init__(self, subdomain_dict):
    self._subdomain_dict = subdomain_dict
    self._robot = self._subdomain_dict[-1][1]

  def get(self):
    host = self.request.host
    for (subdomain, robot) in self._subdomain_dict:
      if host.startswith(subdomain + '.'):
        self._robot = robot
        break
    RobotEventHandler.get(self)

  def post(self):
    host = self.request.host
    for (subdomain, robot) in self._subdomain_dict:
      if host.startswith(subdomain + '.'):
        self._robot = robot
        break
    RobotEventHandler.post(self)

class RobotMultiplexer:
  def __init__(self, subdomain_dict):
    self._subdomain_dict = subdomain_dict

  def run(self, debug=False):
    app = webapp.WSGIApplication([
        ('/_wave/capabilities.xml', lambda: RobotMultiplexingCapabilitiesHandler(self._subdomain_dict)),
        ('/_wave/robot/profile', lambda: RobotMultiplexingProfileHandler(self._subdomain_dict)),
        ('/_wave/robot/jsonrpc', lambda: RobotMultiplexingJsonrpcHandler(self._subdomain_dict))
    ], debug=debug)
    run_wsgi_app(app)

