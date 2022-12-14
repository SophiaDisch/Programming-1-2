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
     
  def pick2(self):
    """Pick 2 beepers"""
    pick_beeper()
    move()
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

  def fic(self) -> bool:
    """Front is clear"""
    return front_is_clear()

  def fib(self) -> bool:
    """Front is blocked"""
    return not self.fic()

  def ric(self) -> bool:
    """Right is clear"""
    self.tr()
    if self.fic():
      self.tl()
      return True  # Immediately leaves the function
    self.tl()
    return False
  
  def rib(self) -> bool:
    """Right is blocked"""
    return not self.ric()

  def mazemove(self):
    """Maze move"""
    if self.fib():
      self.tl()
    else: # Otherwise...
      self.m()
      if self.ric():
        self.tr()
        self.m()
        if self.ric():
          self.tr()
          self.m()
    pass

def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.tl()
    kt.m()
    kt.m()
    kt.tr()
    kt.m()
    kt.tr()
    kt.m()
    kt.m()
    kt.ta()
    kt.m()
    kt.tr()
    kt.m()
    kt.tr()
    kt.m()
    kt.tl()
    kt.m()
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
    kt.tl()
    kt.m()
    kt.tl()
    kt.m()
    kt.m()
    kt.tr()
    kt.m()
    kt.tr()
    kt.m()
    kt.m()
    kt.tl()
    kt.m()
    kt.tl()
    kt.m()
    kt.m()
    kt.tr()
    kt.m()
    kt.tr()
    kt.m()
    kt.m()
    kt.tl()
    pass


if __name__ == "__main__":
    run_karel_program()