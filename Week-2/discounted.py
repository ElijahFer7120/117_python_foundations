""" 
WEEK 2 DEMO 2: "discounted cars"

purpose: Show a small decision-based program that changes output based on conditions.

"""
#scenario: imagine you're in walmart and they're doing a special discount on the new diecast thomas and friends line and you bought 4 of them.
#each of them cost 10 bucks each

#i picked the thomas diecast line is because i bought some thomas and friends diecast stuff last saturday

Thomas_diecast_purchased = 40.00
Discount_threshold = 30.00
Discount_rate = 0.10

if Thomas_diecast_purchased >= Discount_threshold:
    discount = Thomas_diecast_purchased * Discount_rate
    final_total = Thomas_diecast_purchased - discount
    print("Discount accepted:", discount)
    print("FINAL_TOTAL:", final_total)
else:
    print("Discount Denied")
    print("FINAL_TOTAL", Thomas_diecast_purchased)