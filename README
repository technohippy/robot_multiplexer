HOW TO USE

  from waveapi import events
  from waveapi import robot_abstract
  from robot_multiplexer import RobotMultiplexer

  class FooRobot(robot_abstract.Robot):
    def __init__(self, name, version, image_url='', profile_url=''):
      robot_abstract.Robot.__init__(self, name, version, image_url, profile_url) 
      self.RegisterHandler(events.WAVELET_SELF_ADDED, self.on_self_added)

    def on_self_added(self, properties, context):
      wavelet = context.GetRootWavelet()
      wavelet.CreateBlip().GetDocument().SetText("I'm Foo!")

  class BarRobot(robot_abstract.Robot):
    def __init__(self, name, version, image_url='', profile_url=''):
      robot_abstract.Robot.__init__(self, name, version, image_url, profile_url) 
      self.RegisterHandler(events.WAVELET_SELF_ADDED, self.on_self_added)

    def on_self_added(self, properties, context):
      wavelet = context.GetRootWavelet()
      wavelet.CreateBlip().GetDocument().SetText("I'm Bar!")

  if __name__ == '__main__':
    multiplexer = RobotMultiplexer([
      ('foo', FooRobot('FooRobot', '1.0')), # => foo.YOURAPPNAME@appspot.com
      ('bar', BarRobot('BarRobot', '1.0'))  # => bar.YOURAPPNAME@appspot.com
    ])
    multiplexer.run()

