import gradio as gr
from collections import defaultdict

foods_data = [
    {
        "id": "biryani",
        "name": "Chicken Biryani",
        "price": 299,
        "original_price": 399,
        "description": "Aromatic basmati rice with tender chicken, saffron, and traditional spices.",
        "ingredients": [
            "Basmati Rice",
            "Chicken",
            "Saffron",
            "Onions",
            "Ginger",
            "Garlic",
            "Garam Masala",
            "Mint",
            "Coriander",
        ],
        "category": "Indian Biryani",
        "calories": 520,
        "prep_time": "30 min",
        "rating": 4.9,
        "reviews": 234,
        "badge": "Chef's Special",
        "popular": True,
        "image": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=400",
        "type": "biryani",
    },
    {
        "id": "dal_makhani",
        "name": "Dal Makhani",
        "price": 199,
        "original_price": 249,
        "description": "Creamy black lentils slow-cooked with kidney beans, tomato, and aromatic spices.",
        "ingredients": [
            "Black Lentils",
            "Kidney Beans",
            "Tomato",
            "Cream",
            "Butter",
            "Garam Masala",
        ],
        "category": "Indian Curries",
        "calories": 320,
        "prep_time": "25 min",
        "rating": 4.8,
        "reviews": 189,
        "badge": "Popular",
        "popular": True,
        "image": "https://images.unsplash.com/photo-1546833999-b9f581a2026c?w=400",
        "type": "dal_makhani",
    },
    {
        "id": "paneer_tikka",
        "name": "Paneer Tikka",
        "price": 279,
        "original_price": 349,
        "description": "Cubes of cottage cheese marinated in yogurt and spices, grilled to perfection.",
        "ingredients": [
            "Paneer",
            "Yogurt",
            "Ginger",
            "Garlic",
            "Garam Masala",
            "Bell Peppers",
            "Onions",
        ],
        "category": "Indian Tandoor",
        "calories": 380,
        "prep_time": "20 min",
        "rating": 4.7,
        "reviews": 156,
        "badge": "Vegetarian",
        "popular": True,
        "image": "https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=400",
        "type": "paneer_tikka",
    },
    {
        "id": "samosa",
        "name": "Crispy Samosa (3 pcs)",
        "price": 99,
        "original_price": 149,
        "description": "Golden fried pastries filled with spiced potatoes and peas.",
        "ingredients": [
            "Flour",
            "Potatoes",
            "Peas",
            "Cumin",
            "Coriander",
            "Ginger",
            "Green Chili",
            "Mint",
        ],
        "category": "Indian Snacks",
        "calories": 280,
        "prep_time": "15 min",
        "rating": 4.6,
        "reviews": 312,
        "badge": "Bestseller",
        "popular": True,
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "type": "samosa",
    },
    {
        "id": "naan",
        "name": "Garlic Naan",
        "price": 59,
        "original_price": 79,
        "description": "Soft and fluffy tandoor-baked bread topped with garlic and butter.",
        "ingredients": [
            "All-Purpose Flour",
            "Yeast",
            "Yogurt",
            "Garlic",
            "Butter",
            "Salt",
        ],
        "category": "Indian Breads",
        "calories": 180,
        "prep_time": "10 min",
        "rating": 4.9,
        "reviews": 445,
        "badge": "Must Try",
        "popular": True,
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "type": "naan",
    },
    {
        "id": "butter_chicken",
        "name": "Butter Chicken",
        "price": 329,
        "original_price": 399,
        "description": "Tender chicken in creamy tomato-based gravy with butter and fenugreek.",
        "ingredients": [
            "Chicken",
            "Tomato",
            "Cream",
            "Butter",
            "Fenugreek",
            "Garam Masala",
            "Kashmiri Chili",
        ],
        "category": "Indian Curries",
        "calories": 480,
        "prep_time": "25 min",
        "rating": 4.9,
        "reviews": 567,
        "badge": "Signature Dish",
        "popular": True,
        "image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=400",
        "type": "butter_chicken",
    },
    {
        "id": "masala_dosa",
        "name": "Masala Dosa",
        "price": 199,
        "original_price": 249,
        "description": "Crispy rice and lentil crepe filled with spiced potato filling.",
        "ingredients": [
            "Rice",
            "Urad Dal",
            "Potatoes",
            "Onions",
            "Mustard Seeds",
            "Curry Leaves",
            "Coconut",
        ],
        "category": "South Indian",
        "calories": 290,
        "prep_time": "20 min",
        "rating": 4.7,
        "reviews": 234,
        "badge": "Healthy",
        "popular": True,
        "image": "https://images.unsplash.com/photo-1668236543090-82eba64ee968?w=400",
        "type": "dosa",
    },
    {
        "id": "idli_sambar",
        "name": "Idli Sambar (4 pcs)",
        "price": 129,
        "original_price": 169,
        "description": "Soft steamed rice cakes served with hot sambar and coconut chutney.",
        "ingredients": [
            "Rice",
            "Urad Dal",
            "Toor Dal",
            "Tamarind",
            "Vegetables",
            "Coconut",
            "Mustard Seeds",
        ],
        "category": "South Indian",
        "calories": 220,
        "prep_time": "15 min",
        "rating": 4.6,
        "reviews": 189,
        "badge": "Light & Healthy",
        "popular": False,
        "image": "https://images.unsplash.com/photo-1668236543090-82eba64ee968?w=400",
        "type": "idli",
    },
    {
        "id": "palak_paneer",
        "name": "Palak Paneer",
        "price": 249,
        "original_price": 299,
        "description": "Cottage cheese in smooth and creamy spinach gravy.",
        "ingredients": [
            "Paneer",
            "Spinach",
            "Onion",
            "Tomato",
            "Cream",
            "Garlic",
            "Ginger",
            "Garam Masala",
        ],
        "category": "Indian Curries",
        "calories": 340,
        "prep_time": "20 min",
        "rating": 4.7,
        "reviews": 167,
        "badge": "Healthy Choice",
        "popular": False,
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "type": "palak_paneer",
    },
    {
        "id": "tandoori_chicken",
        "name": "Tandoori Chicken Full",
        "price": 449,
        "original_price": 549,
        "description": "Whole chicken marinated in yogurt and spices, roasted in tandoor.",
        "ingredients": [
            "Chicken",
            "Yogurt",
            "Ginger",
            "Garlic",
            "Kashmiri Chili",
            "Garam Masala",
            "Lemon",
            "Mint",
        ],
        "category": "Indian Tandoor",
        "calories": 420,
        "prep_time": "35 min",
        "rating": 4.8,
        "reviews": 289,
        "badge": "Party Favorite",
        "popular": True,
        "image": "https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=400",
        "type": "tandoori_chicken",
    },
    {
        "id": "chaat",
        "name": "Papdi Chaat",
        "price": 149,
        "original_price": 199,
        "description": "Crispy flour chips topped with potatoes, chickpeas, yogurt, and tangy chutneys.",
        "ingredients": [
            "Flour Chips",
            "Potatoes",
            "Chickpeas",
            "Yogurt",
            "Tamarind Chutney",
            "Green Chutney",
            "Sev",
            "Pomegranate",
        ],
        "category": "Indian Snacks",
        "calories": 310,
        "prep_time": "10 min",
        "rating": 4.8,
        "reviews": 345,
        "badge": "Street Food",
        "popular": True,
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "type": "chaat",
    },
    {
        "id": "lassi",
        "name": "Sweet Lassi",
        "price": 79,
        "original_price": 99,
        "description": "Creamy yogurt drink blended with sugar and cardamom.",
        "ingredients": ["Yogurt", "Sugar", "Cardamom", "Water", "Ice"],
        "category": "Indian Drinks",
        "calories": 150,
        "prep_time": "5 min",
        "rating": 4.7,
        "reviews": 234,
        "badge": "Refreshing",
        "popular": True,
        "image": "https://images.unsplash.com/photo-1626200419199-391ae4be7a41?w=400",
        "type": "lassi",
    },
    {
        "id": "gulab_jamun",
        "name": "Gulab Jamun (4 pcs)",
        "price": 99,
        "original_price": 129,
        "description": "Deep-fried milk dumplings soaked in rose-flavored sugar syrup.",
        "ingredients": [
            "Milk Powder",
            "Flour",
            "Sugar",
            "Rose Water",
            "Cardamom",
            "Ghee",
        ],
        "category": "Indian Desserts",
        "calories": 280,
        "prep_time": "15 min",
        "rating": 4.9,
        "reviews": 456,
        "badge": "Dessert Favorite",
        "popular": True,
        "image": "https://images.unsplash.com/photo-1627308595229-7830a5c91f9f?w=400",
        "type": "gulab_jamun",
    },
    {
        "id": "rasgulla",
        "name": "Rasgulla (5 pcs)",
        "price": 99,
        "original_price": 129,
        "description": "Spongy cottage cheese balls soaked in light sugar syrup.",
        "ingredients": ["Cottage Cheese", "Sugar", "Rose Water", "Cardamom"],
        "category": "Indian Desserts",
        "calories": 180,
        "prep_time": "20 min",
        "rating": 4.8,
        "reviews": 289,
        "badge": "Light Dessert",
        "popular": True,
        "image": "https://images.unsplash.com/photo-1627308595229-7830a5c91f9f?w=400",
        "type": "rasgulla",
    },
    {
        "id": "chicken_tikka",
        "name": "Chicken Tikka Kebab",
        "price": 299,
        "original_price": 379,
        "description": "Tender chicken pieces marinated in spiced yogurt, grilled in tandoor.",
        "ingredients": [
            "Chicken",
            "Yogurt",
            "Ginger",
            "Garlic",
            "Kashmiri Chili",
            "Garam Masala",
            "Bell Peppers",
            "Onions",
        ],
        "category": "Indian Tandoor",
        "calories": 320,
        "prep_time": "25 min",
        "rating": 4.8,
        "reviews": 234,
        "badge": "Kebab Special",
        "popular": True,
        "image": "https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=400",
        "type": "chicken_tikka",
    },
    {
        "id": "manchurian",
        "name": "Vegetable Manchurian",
        "price": 229,
        "original_price": 279,
        "description": "Crispy vegetable balls in spicy Indo-Chinese gravy.",
        "ingredients": [
            "Cabbage",
            "Carrots",
            "Beans",
            "Soy Sauce",
            "Garlic",
            "Ginger",
            "Green Chili",
            "Corn Flour",
        ],
        "category": "Indo-Chinese",
        "calories": 340,
        "prep_time": "20 min",
        "rating": 4.6,
        "reviews": 178,
        "badge": "Fusion",
        "popular": False,
        "image": "https://images.unsplash.com/photo-1529692236671-f1f6cf9683ba?w=400",
        "type": "manchurian",
    },
]

categories = [
    {"id": "all", "name": "All", "icon": "🍽️"},
    {"id": "Indian Biryani", "name": "Biryani", "icon": "🍚"},
    {"id": "Indian Curries", "name": "Curries", "icon": "🍛"},
    {"id": "Indian Tandoor", "name": "Tandoor", "icon": "🔥"},
    {"id": "Indian Snacks", "name": "Snacks", "icon": "🥟"},
    {"id": "Indian Breads", "name": "Breads", "icon": "🫓"},
    {"id": "South Indian", "name": "South Indian", "icon": "🥞"},
    {"id": "Indian Drinks", "name": "Drinks", "icon": "🥛"},
    {"id": "Indian Desserts", "name": "Desserts", "icon": "🍰"},
    {"id": "Indo-Chinese", "name": "Indo-Chinese", "icon": "🍜"},
]

cart = defaultdict(int)


def get_filtered_foods(category, search):
    filtered = foods_data
    if category and category != "all":
        filtered = [f for f in filtered if f["category"] == category]
    if search:
        search = search.lower()
        filtered = [
            f
            for f in filtered
            if search in f["name"].lower() or search in f["description"].lower()
        ]
    return filtered


def generate_food_card(food):
    return f'''
    <div class="food-card">
        <img src="{food["image"]}" alt="{food["name"]}">
        <div class="badge">{food["badge"]}</div>
        <h3>{food["name"]}</h3>
        <p class="desc">{food["description"][:60]}...</p>
        <div class="price-row">
            <span class="price">₹{food["price"]}</span>
            <span class="original">₹{food["original_price"]}</span>
        </div>
        <div class="rating">★ {food["rating"]} ({food["reviews"]})</div>
    </div>
    '''


def render_menu(category, search):
    foods = get_filtered_foods(category, search)
    cards = "".join([generate_food_card(f) for f in foods])
    return f"""
    <div class="menu-grid">
        {cards}
    </div>
    """


css = """
:root {
    --primary: #ff6b35;
    --secondary: #004e89;
    --accent: #f7c59f;
    --dark: #1a1a2e;
    --light: #fafafa;
}
body {
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    color: var(--light);
    margin: 0;
    padding: 0;
}
.header {
    background: linear-gradient(90deg, var(--primary), #ff8c42);
    padding: 20px;
    text-align: center;
}
.header h1 { margin: 0; font-size: 2.5em; }
.header p { margin: 5px 0 0; opacity: 0.9; }
.search-bar { padding: 15px; background: rgba(255,255,255,0.1); }
.search-bar input {
    width: 100%; padding: 12px 20px; border: none; border-radius: 25px; font-size: 16px;
}
.categories { display: flex; flex-wrap: wrap; gap: 10px; padding: 15px; justify-content: center; }
.cat-btn {
    padding: 10px 20px; border: none; border-radius: 20px; background: rgba(255,255,255,0.15);
    color: white; cursor: pointer; font-size: 14px;
}
.cat-btn:hover { background: var(--primary); }
.menu-grid {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; padding: 20px;
}
.food-card {
    background: rgba(255,255,255,0.1); border-radius: 15px; padding: 15px;
    transition: all 0.3s;
}
.food-card:hover { transform: translateY(-5px); }
.food-card img { width: 100%; height: 150px; object-fit: cover; border-radius: 10px; }
.food-card .badge {
    position: absolute; top: 25px; left: 25px; background: var(--primary);
    padding: 5px 12px; border-radius: 15px; font-size: 12px; font-weight: bold;
}
.food-card h3 { margin: 10px 0 5px; color: var(--accent); }
.food-card .desc { font-size: 13px; opacity: 0.8; }
.price-row { display: flex; align-items: center; gap: 10px; margin: 10px 0; }
.price { font-size: 1.4em; font-weight: bold; color: var(--primary); }
.original { text-decoration: line-through; opacity: 0.6; }
.rating { color: #ffd700; margin-bottom: 10px; }
"""

with gr.Blocks(css=css, theme=gr.themes.Soft()) as demo:
    gr.HTML("""
        <div class="header">
            <h1>🍛 DIGITAL 3D MENU</h1>
            <p>Interactive Indian Food Experience</p>
        </div>
    """)

    with gr.Row():
        category_dropdown = gr.Dropdown(
            choices=[c["name"] for c in categories], value="All", label="Category"
        )
        search_input = gr.Textbox(
            placeholder="Search delicious food...", label="Search"
        )

    menu_output = gr.HTML()

    def update_menu(cat, search):
        cat_id = next((c["id"] for c in categories if c["name"] == cat), "all")
        return render_menu(cat_id, search)

    category_dropdown.change(
        update_menu, [category_dropdown, search_input], menu_output
    )
    search_input.change(update_menu, [category_dropdown, search_input], menu_output)
    demo.load(lambda: update_menu("All", ""), inputs=None, outputs=menu_output)

demo.launch()
