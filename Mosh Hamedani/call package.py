import Ecommerce.shipping
Ecommerce.shipping.calc_shipping()

from Ecommerce.price import itemPrice
itemPrice()
itemPrice()

Ecommerce.shipping.calc_shipping()
# to make handy we can use another approach
from Ecommerce.shipping import calc_shipping
calc_shipping()

# another approach
from Ecommerce import price
price.itemPrice()

# calling delivery function from Ecommerce directory
from Ecommerce.delivery import ontimedelivery
ontimedelivery()
from Practice.dictionary_solutions import output
output
