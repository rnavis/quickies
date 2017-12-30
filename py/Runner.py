import sys
from Trade import Trade

from Equity import Equity

print("Enter number of trades = ", end="\n")
incoming = sys.stdin.readline()
trade = None
trades = []

if int(incoming) <1:
    print('Enter atleast one trade')
else:
    for j in range(int(incoming)) :
        print(" Enter product =")
        product = sys.stdin.readline()
        print(" Enter Quantity =")
        qty = sys.stdin.readline()
        print(" Enter Quote Price =")
        price = sys.stdin.readline()
        print(" Enter Price Type =")
        priceType = sys.stdin.readline()
        print(" Enter Broker Name [enter none if no brokers] =")
        broker = sys.stdin.readline()
        print('Creating the trade....')
        if (broker.rstrip('\n').lower() != 'none'):
            trade = Equity(product.rstrip('\n'), qty.rstrip('\n'), price.rstrip('\n'), priceType.rstrip('\n'), broker.rstrip('\n'))
        else:
            trade = Trade(product.rstrip('\n'), qty.rstrip('\n'), price.rstrip('\n'), priceType.rstrip('\n'))

        trades.append(trade)

for trade in trades:
    print(trade.get_type())
    print(trade.toString())

