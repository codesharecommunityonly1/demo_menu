import gradio as gr

foods = [
    {
        "id": "biryani",
        "name": "Chicken Biryani",
        "price": 299,
        "original_price": 399,
        "description": "Aromatic basmati rice with tender chicken, saffron, and traditional spices.",
        "category": "Indian Biryani",
        "rating": 4.9,
        "reviews": 234,
        "badge": "Chef's Special",
        "image": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=400",
    },
    {
        "id": "dal_makhani",
        "name": "Dal Makhani",
        "price": 199,
        "original_price": 249,
        "description": "Creamy black lentils slow-cooked with kidney beans, tomato, and aromatic spices.",
        "category": "Indian Curries",
        "rating": 4.8,
        "reviews": 189,
        "badge": "Popular",
        "image": "https://images.unsplash.com/photo-1546833999-b9f581a2026c?w=400",
    },
    {
        "id": "paneer_tikka",
        "name": "Paneer Tikka",
        "price": 279,
        "original_price": 349,
        "description": "Cubes of cottage cheese marinated in yogurt and spices, grilled to perfection.",
        "category": "Indian Tandoor",
        "rating": 4.7,
        "reviews": 156,
        "badge": "Vegetarian",
        "image": "https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=400",
    },
    {
        "id": "samosa",
        "name": "Crispy Samosa (3 pcs)",
        "price": 99,
        "original_price": 149,
        "description": "Golden fried pastries filled with spiced potatoes and peas.",
        "category": "Indian Snacks",
        "rating": 4.6,
        "reviews": 312,
        "badge": "Bestseller",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
    },
    {
        "id": "butter_chicken",
        "name": "Butter Chicken",
        "price": 329,
        "original_price": 399,
        "description": "Tender chicken in creamy tomato-based gravy with butter and fenugreek.",
        "category": "Indian Curries",
        "rating": 4.9,
        "reviews": 567,
        "badge": "Signature Dish",
        "image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=400",
    },
    {
        "id": "masala_dosa",
        "name": "Masala Dosa",
        "price": 199,
        "original_price": 249,
        "description": "Crispy rice and lentil crepe filled with spiced potato filling.",
        "category": "South Indian",
        "rating": 4.7,
        "reviews": 234,
        "badge": "Healthy",
        "image": "https://images.unsplash.com/photo-1668236543090-82eba64ee968?w=400",
    },
    {
        "id": "gulab_jamun",
        "name": "Gulab Jamun (4 pcs)",
        "price": 99,
        "original_price": 129,
        "description": "Deep-fried milk dumplings soaked in rose-flavored sugar syrup.",
        "category": "Indian Desserts",
        "rating": 4.9,
        "reviews": 456,
        "badge": "Dessert Favorite",
        "image": "https://images.unsplash.com/photo-1627308595229-7830a5c91f9f?w=400",
    },
    {
        "id": "lassi",
        "name": "Sweet Lassi",
        "price": 79,
        "original_price": 99,
        "description": "Creamy yogurt drink blended with sugar and cardamom.",
        "category": "Indian Drinks",
        "rating": 4.7,
        "reviews": 234,
        "badge": "Refreshing",
        "image": "https://images.unsplash.com/photo-1626200419199-391ae4be7a41?w=400",
    },
]

categories = [
    "All",
    "Indian Biryani",
    "Indian Curries",
    "Indian Tandoor",
    "Indian Snacks",
    "South Indian",
    "Indian Desserts",
    "Indian Drinks",
]

css = """
.header { background: linear-gradient(135deg, #ff6b35, #ff8c42); padding: 20px; text-align: center; color: white; }
.header h1 { margin: 0; font-size: 2.5em; }
.menu-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; padding: 20px; }
.food-card { background: rgba(255,255,255,0.1); border-radius: 15px; padding: 15px; backdrop-filter: blur(10px); }
.food-card img { width: 100%; height: 150px; object-fit: cover; border-radius: 10px; }
.food-card h3 { color: #f7c59f; margin: 10px 0 5px; }
.food-card .price { color: #ff6b35; font-size: 1.4em; font-weight: bold; }
.food-card .original { text-decoration: line-through; opacity: 0.6; margin-left: 10px; }
.rating { color: #ffd700; }
"""


def get_menu(category, search):
    filtered = foods
    if category and category != "All":
        filtered = [f for f in filtered if f["category"] == category]
    if search:
        search = search.lower()
        filtered = [f for f in filtered if search in f["name"].lower()]

    html = '<div class="menu-grid">'
    for f in filtered:
        html += f'''
        <div class="food-card">
            <img src="{f["image"]}" alt="{f["name"]}">
            <span style="background:#ff6b35;padding:5px 10px;border-radius:10px;font-size:12px">{f["badge"]}</span>
            <h3>{f["name"]}</h3>
            <p>{f["description"][:60]}...</p>
            <span class="price">₹{f["price"]}</span><span class="original">₹{f["original_price"]}</span>
            <div class="rating">★ {f["rating"]} ({f["reviews"]} reviews)</div>
        </div>'''
    html += "</div>"
    return html


with gr.Blocks(css=css, title="DIGITAL 3D MENU") as demo:
    gr.HTML(
        '<div class="header"><h1>🍛 DIGITAL 3D MENU</h1><p>Interactive Indian Food Experience</p></div>'
    )

    with gr.Row():
        cat_dd = gr.Dropdown(choices=categories, value="All", label="Category")
        search_in = gr.Textbox(placeholder="Search food...", label="Search")

    menu_out = gr.HTML()

    cat_dd.change(get_menu, [cat_dd, search_in], menu_out)
    search_in.change(get_menu, [cat_dd, search_in], menu_out)
    demo.load(lambda: get_menu("All", ""), None, menu_out)

demo.launch()
