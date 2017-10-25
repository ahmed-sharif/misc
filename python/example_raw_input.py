import sys

while True:
    # inp = sys.stdin.readline()
    try:
      # inp = input()
      inp = sys.stdin.readline()
      if not inp:
          break
      print (inp.rstrip())
    except:
      break
