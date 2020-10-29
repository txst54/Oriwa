Oriwafile = open("Oriwa_test.cp", "w")
def linebreak(li, fi):
  for i in li:
    fi.write(i + '\n')
Oriwa = ["1 -200.0 -200.0 -200.0 200.0", "1 -200.0 -200.0 200.0 -200.0", "1 200.0 200.0 -200.0 200.0", "1 200.0 200.0 200.0 -200.0"]
linebreak(Oriwa, Oriwafile)
