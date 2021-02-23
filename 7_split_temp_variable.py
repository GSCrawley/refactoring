# by Kami Bigdely
# Split temporary variable

patty = 70 # [gr]
pickle = 20 # [gr]
tomatoes = 25 # [gr]
lettuce = 15 # [gr]
buns = 95 # [gr]
sandwich_weight = (2 * patty + 4 * pickle + 3 * tomatoes + 2 * lettuce
                + 2 * buns)
print("NY Burger Weight", sandwich_weight)

kimchi = 30
mayo = 5 
golden_fried_onion = 20  

extras = (kimchi + mayo + golden_fried_onion)

kimchi_burger = sandwich_weight + extras

print("Seoul Kimchi Burger Weight", kimchi_burger)