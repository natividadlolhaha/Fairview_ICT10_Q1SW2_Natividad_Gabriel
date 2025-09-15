from js import document
restaurant_name = "Gab's Ramen House"
owner_name = "Gabriel Natividad"
year_established = 2025
popular_item_price = 199.00
has_delivery = True
business_hours = "Open: 11:00 AM - 10:00 PM"
menu_prices = {
    "Shoyu Ramen": 199.00,
    "Miso Ramen": 220.00,
    "Pork Tonkotsu Ramen": 250.00,
    "Spicy Ramen": 230.00,
    "Tantanmen": 180.00
}
common_allergens = ["Egg", "Soy", "Wheat"]
tax_rate = 0.08

document.getElementById("restaurant_name").innerText = restaurant_name
document.getElementById("owner_name").innerText = f"Owner: {owner_name}"
document.getElementById("year_established").innerText = f"Since {year_established}"

document.getElementById("popular_item_price").innerText = f"Popular Item Price: ₱{popular_item_price:.2f}"
document.getElementById("has_delivery").innerText = f"Delivery Available: {has_delivery}"
document.getElementById("business_hours").innerText = business_hours
document.getElementById("tax_rate").innerText = f"Tax Rate: {tax_rate*100:.0f}%"
document.getElementById("allergens").innerText = "Common Allergens: " + ", ".join(common_allergens)

rows = ""
for item, price in menu_prices.items():
    rows += f"<tr><td>{item}</td><td>₱{price:.2f}</td></tr>"

document.getElementById("menu_table").innerHTML = rows
