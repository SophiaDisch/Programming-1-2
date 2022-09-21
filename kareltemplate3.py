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
    self.ta()
    self.m()
    self.m()
    self.m()
    self.m()

  def s(self):
    """Print S using beepers"""
    self.put2()
    self.m()
    self.put()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.m()
    self.tl()
    self.m()

  def p(self):
    """Print P using beepers"""
    self.tl()
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.tr()
    self.put2()
    self.m()
    self.tr()
    self.put2()
    self.m()
    self.tr()
    self.put2()
    self.ta()
    self.m()
    self.m()
    self.m()
    self.tr()
    self.m()
    self.m()
    self.tl()

  def i(self):
    """Print I using beepers"""
    self.tl()
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()
    self.tr()
    self.m()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.m()
    self.tl()
    self.m()

  def a(self):
    """Print A using beepers"""
    self.tl()
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.tr()
    self.put2()
    self.m()
    self.tr()
    self.put2()
    self.m()
    self.tr()
    self.put2()
    self.ta()
    self.m()
    self.tr()
    self.m()
    self.put2()
    self.tl()
    self.m()

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

def main():
    """ Karel code goes here! """
    kt = ktools()
  
    pass


if __name__ == "__main__":
    run_karel_program()