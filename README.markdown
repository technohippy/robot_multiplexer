Sample
======

multiplexer.py
--------------

    from robot_multiplexer import RobotMultiplexer
    from foo_robot import FooRobot
    from bar_robot import BarRobot

    if __name__ == '__main__':
      multiplexer = RobotMultiplexer([
        ('foo', FooRobot()), # foo.ROBOTNAME@appspot.com invokes FooRobot
        ('bar', BarRobot())  # bar.ROBOTNAME@appspot.com invokes BarRobot
      ])
      multiplexer.run()

app.yaml
--------

    application: ROBOTNAME
    version: 1
    runtime: python
    api_version: 1

    handlers:
    - url: /_wave/.*
      script: multiplexer.py
    - url: .*
      script: main.py

foo_robot.py
------------

    from waveapi import robot_abstract
    from waveapi import events

    class FooRobot(robot_abstract.Robot):
      def __init__(self):
        robot_abstract.Robot.__init__(self, 'FooRobot', '1.0')
        self.RegisterHandler(events.WAVELET_SELF_ADDED, self.on_self_added)

      def on_self_added(self, properties, context):
        wavelet = context.GetRootWavelet()
        wavelet.CreateBlip().GetDocument().SetText("I'm Foo!")

bar_robot.py
------------

    from waveapi import robot_abstract
    from waveapi import events

    class BarRobot(robot_abstract.Robot):
      def __init__(self):
        robot_abstract.Robot.__init__(self, 'BarRobot', '1.0')
        self.RegisterHandler(events.WAVELET_SELF_ADDED, self.on_self_added)

      def on_self_added(self, properties, context):
        wavelet = context.GetRootWavelet()
        wavelet.CreateBlip().GetDocument().SetText("I'm Bar!")

Living example
--------------

[Public Sample Wave](https://wave.google.com/wave/#restored:wave:googlewave.com!w%252BeVbr7mRiA)
