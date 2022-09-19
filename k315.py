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
    self.m()
    self.put2()
    self.m()
    self.put()

def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.tl()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.tr()
    kt.m()
    kt.put5()
    kt.m()
    kt.put2()
    kt.m()
    kt.tr()
    kt.put5()
    kt.m()
    kt.put2()
    kt.m()
    kt.tr()
    kt.put5()
    kt.m()
    kt.put2()
    kt.m()
    kt.tr()
    kt.put5()
    kt.m()
    kt.put2()
    pass


if __name__ == "__main__":
    run_karel_program()