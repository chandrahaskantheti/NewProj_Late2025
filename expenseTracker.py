import os
import csv
from datetime import datetime

file = 'expenses.csv'


def setup_csv(file):
  if not os.path.exists(file):
    with open(file, mode="w", newline='') as f:
      writer = csv.writer(f)
      if os.path.getsize(file) == 0:
        writer.writerow(['Date', 'Category', 'Amount', 'Description'])
      else:
        writer = csv.writer(f)
    
def view_expenses(file):
  if os.path.exists(file):
    with open(file, mode="r") as f:
      reader = csv.reader(f)
      next(reader)
      for row in reader:
        print(f"Date: {row[0]}, Category: {row[1]}, Amount: ${row[2]}, Description: {row[3]}")
  else:
    print("No expenses recorded yet.")

def main():
  print("Expense Tracker")
  setup_csv(file)
  
  view_expenses(file)
  
if __name__ == "__main__":
  main()