import payable 

def main():
  cash1 = payable.Cash(100)
  cash2 = payable.Cash(200)
  cash1.print()
  cash2.print()
  cash1.pay(cash2,20)
  cash1.print()
  cash2.print()

  coin = payable.Coin()
  coin.print()

  paper = payable.Paper()
  paper.print()

if __name__ == '__main__':
  main()
