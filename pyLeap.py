# Task
# You are given the year, and you have to write a function to check if the year is leap or not.
# Note that you have to complete the function and remaining code is given as template.
# Input Format
# Read y, the year that needs to be checked.
# Constraints
# Output Format
# Output is taken care of by the template. Your function must return a boolean value (True/False)

def leap(y):
  isLeap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
  return isLeap

def main():
  y = int(raw_input(''))
  print(leap(y))

if __name__ == '__main__':
  main()