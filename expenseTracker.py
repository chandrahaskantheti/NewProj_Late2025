file = 'ProjectsMidLate2025/expenses.csv'

def read_csv(file):
  with open(file, 'r') as f:
      readLines = f.read()
      print(readLines)
    
def main():
  print("Expense Tracker")
  read_csv(file)
  
if __name__ == "__main__":
  main()