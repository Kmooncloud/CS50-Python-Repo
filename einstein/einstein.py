# pset0 Einstein
# performes the e = (mc)^2 function

def main():
  x = int(input("m: "))
  print ("E: ", einstein(x))

def einstein(m):
  return m * pow(300000000, 2)

main()