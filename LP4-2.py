def main():
  wkilo = int(input("Enter package weight in kilograms: "))
  lcent = int(input("Enter package length in centimeters: "))
  wcent = int(input("Enter package width in centimeters: "))
  hcent = int(input("Enter package height in centimeters: "))
  size = lcent * wcent * hcent

  if wkilo > 27:
    print("Too heavy")
  elif size > 100000:
    print("Too big")
  elif wkilo > 27 and size > 100000:
    print("Too big and too heavy")

if __name__ == "__main__":
  main()