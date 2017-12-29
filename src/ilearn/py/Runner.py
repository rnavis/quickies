from src.ilearn.py.Trade import Trade
from src.ilearn.py.Equity import Equity

jcp = Equity('JCP', 1000, 15.00, 'BuyLong','GS')
bond = Trade('GOLD', 10000, 500.44,'SellShort')
print(jcp.toString())
print(bond.toString())