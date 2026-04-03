import gradio as gr

# Menu Data
menu_items = [
    {
        "id": 1,
        "name": "Bruschetta",
        "category": "Appetizers",
        "price": 8.99,
        "description": "Toasted bread topped with fresh tomatoes, garlic, basil, and olive oil.",
        "image": "https://images.unsplash.com/photo-1572695157366-5e585ab2b69f?w=400",
    },
    {
        "id": 2,
        "name": "Caesar Salad",
        "category": "Appetizers",
        "price": 10.99,
        "description": "Crisp romaine lettuce with caesar dressing, parmesan, and croutons.",
        "image": "https://images.unsplash.com/photo-1550304943-4f24f54ddde9?w=400",
    },
    {
        "id": 3,
        "name": "Garlic Bread",
        "category": "Appetizers",
        "price": 6.99,
        "description": "Warm bread with garlic butter and herbs.",
        "image": "https://images.unsplash.com/photo-1619535860434-ba1d8fa12536?w=400",
    },
    {
        "id": 4,
        "name": "Grilled Salmon",
        "category": "Mains",
        "price": 24.99,
        "description": "Fresh Atlantic salmon with lemon herb butter and seasonal vegetables.",
        "image": "https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400",
    },
    {
        "id": 5,
        "name": "Chicken Parmesan",
        "category": "Mains",
        "price": 18.99,
        "description": "Breaded chicken breast with marinara sauce and melted mozzarella.",
        "image": "https://images.unsplash.com/photo-1632778149955-e80f8ceca2e8?w=400",
    },
    {
        "id": 6,
        "name": "Beef Steak",
        "category": "Mains",
        "price": 29.99,
        "description": "8oz ribeye steak with peppercorn sauce and mashed potatoes.",
        "image": "https://images.unsplash.com/photo-1600891964092-4316c288032e?w=400",
    },
    {
        "id": 7,
        "name": "Pasta Primavera",
        "category": "Mains",
        "price": 16.99,
        "description": "Penne pasta with fresh vegetables in garlic olive oil.",
        "image": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=400",
    },
    {
        "id": 8,
        "name": "Chocolate Lava Cake",
        "category": "Desserts",
        "price": 9.99,
        "description": "Warm chocolate cake with molten center and vanilla ice cream.",
        "image": "https://images.unsplash.com/photo-1624353365286-3f8d62daad51?w=400",
    },
    {
        "id": 9,
        "name": "Tiramisu",
        "category": "Desserts",
        "price": 8.99,
        "description": "Classic Italian dessert with espresso-soaked ladyfingers and mascarpone.",
        "image": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=400",
    },
    {
        "id": 10,
        "name": "Cheesecake",
        "category": "Desserts",
        "price": 7.99,
        "description": "Creamy New York style cheesecake with berry compote.",
        "image": "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?w=400",
    },
]

categories = ["All", "Appetizers", "Mains", "Desserts"]

# CSS Styles
css = """
.header {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    padding: 30px;
    text-align: center;
    color: white;
}
.header h1 { margin: 0; font-size: 2.8em; }
.header p { margin: 10px 0 0; font-size: 1.2em; opacity: 0.9; }
.controls {
    display: flex;
    gap: 15px;
    padding: 20px;
    background: rgba(255,255,255,0.05);
    margin: 10px;
    border-radius: 15px;
    flex-wrap: wrap;
}
.controls input, .controls select {
    flex: 1;
    min-width: 200px;
    padding: 12px;
    border: none;
    border-radius: 10px;
    font-size: 16px;
}
.menu-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 25px;
    padding: 25px;
}
.food-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
    border-radius: 20px;
    padding: 20px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
    transition: transform 0.3s, box-shadow 0.3s;
}
.food-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}
.food-card img {
    width: 100%;
    height: 180px;
    object-fit: cover;
    border-radius: 12px;
}
.food-card .badge {
    display: inline-block;
    background: linear-gradient(135deg, #ff6b35, #ff8c42);
    padding: 5px 12px;
    border-radius: 20px;
    font-size: 12px;
    margin: 10px 0;
}
.food-card h3 { color: #f7c59f; margin: 10px 0 5px; font-size: 1.3em; }
.food-card .desc { color: #ccc; font-size: 14px; line-height: 1.5; margin: 10px 0; }
.food-card .price {
    color: #ff6b35;
    font-size: 1.5em;
    font-weight: bold;
}
.empty-state {
    text-align: center;
    color: #888;
    padding: 40px;
    font-size: 18px;
}
"""


# Filter Function
def filter_menu(category, search):
    filtered = menu_items

    if category and category != "All":
        filtered = [item for item in filtered if item.get("category") == category]

    if search:
        search = search.lower()
        filtered = [
            item
            for item in filtered
            if search in item.get("name", "").lower()
            or search in item.get("description", "").lower()
        ]

    if not filtered:
        return '<div class="empty-state">No dishes found 🍽️</div>'

    html = '<div class="menu-grid">'
    for item in filtered:
        html += f'''
        <div class="food-card">
            <img src="{item["image"]}" alt="{item["name"]}">
            <span class="badge">{item["category"]}</span>
            <h3>{item["name"]}</h3>
            <p class="desc">{item["description"]}</p>
            <div class="price">${item["price"]:.2f}</div>
        </div>'''
    html += "</div>"
    return html


# Build Gradio App
with gr.Blocks(css=css, title="Restaurant Menu") as demo:
    # Header
    gr.HTML("""
        <div class="header">
            <h1>🍽️ Restaurant Menu</h1>
            <p>Delicious dishes for every taste</p>
        </div>
    """)

    # Controls
    with gr.Row():
        with gr.Column(scale=1):
            category_dd = gr.Dropdown(
                choices=categories, value="All", label="Category", interactive=True
            )
        with gr.Column(scale=2):
            search_input = gr.Textbox(
                placeholder="Search dishes...", label="Search", interactive=True
            )

    # Menu Output
    menu_output = gr.HTML()

    # Events
    category_dd.change(filter_menu, [category_dd, search_input], menu_output)
    search_input.change(filter_menu, [category_dd, search_input], menu_output)

    # Load initial menu
    demo.load(lambda: filter_menu("All", ""), None, menu_output)

# Launch
demo.launch()
