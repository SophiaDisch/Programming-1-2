from stanfordkarel import *


class ktools:
  def m(self):
    """Shorthand for move"""
    move()

  def tl(self):
    turn_left()

  def tr(self):
    """Turn Right"""
    self.tl()
    self.tl()
    self.tl()
    
  def ta(self):
    """Turn around"""
    self.tl()
    self.tl()

  def pick(self):
    """Pick beeper"""
    pick_beeper()

  def put(self):
    """Put beeper"""
    put_beeper()

  def put2(self):
    """Put two beepers in a line"""
    self.put()
    self.m()
    self.put()

  def put5(self):
    """Put five beepers in a line"""
    self.put2()
    self.move()
    self.put2()
    self.move()
    self.put()

  def h(self):
    """Print H using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.tr()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()

  def e(self):
    """Print E using beepers"""
    self.put2()
    self.m()
    self.put()
    self.ta()
    self.m()
    self.m()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.m()
    self.tr()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()

  def l(self):
    """Print L using beepers"""
    self.tl()
    self.put2()
    self.m()
    self.put()
    self.m()
    self.put2()
    self.ta()
    self.m()
    self.m()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.m()
    self.m()

  def o(self):
    """Print O using beepers"""
    self.tl()
    self.put2()
    self.m()
    self.put()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.tr()
    self.put2()
    self.m()
    self.put()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.put2()

def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.tl()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.put()
    kt.tl()
    kt.m()
    kt.m()
    kt.m()
    kt.tr()
    kt.m()
    kt.tr()
    kt.m()
    kt.m()
    kt.m()
    kt.put()
    kt.tl()
    kt.m()
    kt.m()
    kt.m()
    kt.tr()
    kt.m()
    kt.tr()
    kt.m()
    kt.m()
    kt.m()
    kt.put()
    kt.tl()
    kt.m()
    kt.m()
    kt.m()
    kt.tr()
    kt.m()
    kt.tr()
    kt.m()
    kt.m()
    kt.m()
    kt.put()
    kt.tl()
    kt.m()
    pass


if __name__ == "__main__":
    run_karel_program()