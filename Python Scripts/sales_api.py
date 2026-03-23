from fastapi import FastAPI
import random
from datetime import datetime

app = FastAPI()

# Expanded Product List
products = [
    # Electronics
    "Mobile Phone", "Laptop", "Smart TV", "Tablet", "Smart Watch",
    "Headphones", "Bluetooth Speaker", "Gaming Console",
    "Camera", "Power Bank", "Router", "Printer",
    "Desktop Computer", "External Hard Drive", "Monitor",
    
    # Home Appliances
    "Refrigerator", "Air Conditioner", "Washing Machine",
    "Microwave Oven", "Mixer Grinder", "Electric Kettle",
    "Water Purifier", "Ceiling Fan", "Air Fryer",
    "Dishwasher", "Geyser", "Vacuum Cleaner",

    # Fashion
    "T-Shirt", "Jeans", "Sneakers", "Formal Shoes",
    "Jacket", "Kurta", "Saree", "Handbag",
    "Watch", "Sunglasses", "Sports Shoes",

    # Furniture
    "Sofa Set", "Dining Table", "Office Chair",
    "Bed", "Wardrobe", "Study Table",
    "Bookshelf", "TV Unit",

    # Grocery / FMCG
    "Cooking Oil", "Rice Bag", "Atta (Wheat Flour)",
    "Milk Pack", "Tea Powder", "Coffee Powder",
    "Shampoo", "Soap", "Toothpaste"
]

# Expanded Indian Cities List
cities = [

    # Maharashtra
    "Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad", "Kolhapur",

    # Karnataka
    "Bengaluru", "Mysuru", "Mangalore", "Hubli",

    # Tamil Nadu
    "Chennai", "Coimbatore", "Madurai", "Salem", "Tiruchirappalli",

    # Telangana
    "Hyderabad", "Warangal",

    # Andhra Pradesh
    "Visakhapatnam", "Vijayawada", "Guntur",

    # Gujarat
    "Ahmedabad", "Surat", "Vadodara", "Rajkot",

    # Uttar Pradesh
    "Lucknow", "Kanpur", "Agra", "Varanasi", "Noida", "Ghaziabad",

    # Rajasthan
    "Jaipur", "Udaipur", "Jodhpur", "Kota",

    # Madhya Pradesh
    "Indore", "Bhopal", "Gwalior",

    # Bihar
    "Patna", "Gaya",

    # West Bengal
    "Kolkata", "Siliguri", "Durgapur",

    # Punjab
    "Ludhiana", "Amritsar", "Jalandhar",

    # Haryana
    "Gurgaon", "Faridabad", "Panipat",

    # Kerala
    "Kochi", "Thiruvananthapuram", "Kozhikode",

    # Odisha
    "Bhubaneswar", "Cuttack",

    # Assam
    "Guwahati", "Dibrugarh",

    # Jharkhand
    "Ranchi", "Jamshedpur",

    # Chhattisgarh
    "Raipur", "Bilaspur",

    # Uttarakhand
    "Dehradun", "Haridwar",

    # Himachal Pradesh
    "Shimla", "Manali",

    # Goa
    "Panaji", "Margao",

    # Jammu & Kashmir
    "Srinagar", "Jammu"
]

channels = [
    {"channel": "Online", "platform": "Mobile App"},
    {"channel": "Online", "platform": "Website"},
    {"channel": "Offline", "platform": "Retail Store"}
]

promotions = [
    "Diwali Sale", "New Year Sale", 
    "Independence Day Offer", 
    "Republic Day Sale",
    "Black Friday Sale",
    "No Promotion"
]

@app.get("/sale")
def get_sale():
    product = random.choice(products)
    city = random.choice(cities)
    channel = random.choice(channels)
    promotion = random.choice(promotions)

    cost = random.randint(5000, 30000)
    revenue = cost * random.uniform(1.1, 1.5)

    return {
        "sale_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "product_name": product,
        "city": city,
        "segment": random.choice(["Retail", "Corporate"]),
        "gender": random.choice(["Male", "Female"]),
        "age_group": random.choice(["18-25", "26-35", "36-45", "46-60"]),
        "channel": channel["channel"],
        "platform": channel["platform"],
        "promotion": promotion,
        "quantity": random.randint(1, 5),
        "revenue": round(revenue, 2),
        "cost": round(cost, 2)
    }



# to run this code use : uvicorn sales_api:app --reload

# to stopped API running use : ctrl + c