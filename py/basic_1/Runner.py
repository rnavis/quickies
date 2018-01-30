import sys
from Trade import Trade

from Equity import Equity

print("Enter number of trades = ", end="\n")
try:
    incoming = int(sys.stdin.readline())
    trade = None
    trades = []
except ValueError:
    print("enter an integer")
    sys.exit()

if int(incoming) <1:
    print('Enter atleast one trade')
else:
    for j in range(int(incoming)) :
        try:
            print(" Enter product =")
            product = sys.stdin.readline()
            print(" Enter Quantity =")
            qty = int(sys.stdin.readline())
            print(" Enter Quote Price =")
            price = float(sys.stdin.readline())
            print(" Enter Price Type =")
            priceType = sys.stdin.readline()
            print(" Enter Broker Name [enter none if no brokers] =")
            broker = sys.stdin.readline()
            print('Creating the trade....')
            if (broker.rstrip('\n').lower() != 'none'):
                trade = Equity(product.rstrip('\n'), qty, price, priceType.rstrip('\n'), broker.rstrip('\n'))
            else:
                trade = Trade(product.rstrip('\n'), qty, price, priceType.rstrip('\n'))
        except ValueError:
            print("Incorrect number type")
        else:
            trades.append(trade)

for trade in trades:
    print(trade.get_type() + ' --->' + trade.toString())

