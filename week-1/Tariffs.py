"""
    Week one, Demo 2
    
"""
#*this are the pixar cars diecasts i bought at walmart
pixar_cars_purchased = 2
Price_each = 7.99

#*i originally bought some single packs but decided to get the double pack. 4.99 to 7.99

subtotal = pixar_cars_purchased * Price_each
tax_rate = 5.30 / 100

#*tariffs tax rate went from 3.50 to 5.30. thx trump

tax_amount = subtotal * tax_rate
total = subtotal + tax_amount

print("item purchased: ", pixar_cars_purchased)
print("Price each:", Price_each)
print("tax rate: ", tax_rate)
print("tax_amount: ", tax_amount)
print("total: ", total)

#REFLECTION
#*the values i used in this program are just the print values but do they make them into output?

#*it gathers the information from above the line of text from above,
#*it computes the total amount from it and generates the final results then executes it
