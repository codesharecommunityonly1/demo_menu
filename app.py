import gradio as gr
import json

# Menu Data - Complete Restaurant Menu
menu_items = [
    {
        "id": "paneer65",
        "name": "Paneer 65",
        "category": "Starters",
        "price": 180,
        "description": "Crispy paneer pieces tossed in spicy masala",
        "image": "images/paneer65.jpg",
        "model": "box",
        "color": "#FFA500",
    },
    {
        "id": "honey_chilly_potato",
        "name": "Honey Chilly Potato",
        "category": "Starters",
        "price": 140,
        "description": "Crispy potatoes with honey and chili sauce",
        "image": "images/honey_chilly_potato.jpg",
        "model": "sphere",
        "color": "#FFD700",
    },
    {
        "id": "american_choupsy",
        "name": "American Choupsy",
        "category": "Starters",
        "price": 170,
        "description": "American style fried veggie rolls",
        "image": "images/american_choupsy.jpg",
        "model": "cylinder",
        "color": "#DEB887",
    },
    {
        "id": "french_fries",
        "name": "French Fries",
        "category": "Starters",
        "price": 80,
        "description": "Crispy golden french fries",
        "image": "images/french_fries.jpg",
        "model": "cylinder",
        "color": "#FFD700",
    },
    {
        "id": "veg_manchurian",
        "name": "Veg Manchurian",
        "category": "Starters",
        "price": 110,
        "description": "Vegetable balls in manchurian sauce",
        "image": "images/veg_manchurian.jpg",
        "model": "sphere",
        "color": "#8B4513",
    },
    {
        "id": "paneer_manchurian",
        "name": "Paneer Manchurian",
        "category": "Starters",
        "price": 160,
        "description": "Paneer balls in manchurian sauce",
        "image": "images/paneer_manchurian.jpg",
        "model": "sphere",
        "color": "#A0522D",
    },
    {
        "id": "veg_spring_roll",
        "name": "Veg Spring Roll",
        "category": "Starters",
        "price": 150,
        "description": "Crispy vegetable spring rolls",
        "image": "images/veg_spring_roll.jpg",
        "model": "cylinder",
        "color": "#F4A460",
    },
    {
        "id": "paneer_tikka",
        "name": "Paneer Tikka",
        "category": "Tandoor",
        "price": 220,
        "description": "Tandoor roasted paneer tikka",
        "image": "images/paneer_tikka.jpg",
        "model": "box",
        "color": "#FFA500",
    },
    {
        "id": "dal_makhani",
        "name": "Dal Makhani",
        "category": "Main Course",
        "price": 160,
        "description": "Creamy black dal makhani",
        "image": "images/dal_makhani.jpg",
        "model": "cylinder",
        "color": "#8B4513",
    },
    {
        "id": "paneer_butter_masala",
        "name": "Paneer Butter Masala",
        "category": "Main Course",
        "price": 220,
        "description": "Creamy paneer butter masala",
        "image": "images/paneer_butter_masala.jpg",
        "model": "sphere",
        "color": "#FF8C00",
    },
    {
        "id": "palak_paneer",
        "name": "Palak Paneer",
        "category": "Main Course",
        "price": 180,
        "description": "Paneer in spinach gravy",
        "image": "images/palak_paneer.jpg",
        "model": "sphere",
        "color": "#006400",
    },
    {
        "id": "veg_fried_rice",
        "name": "Veg Fried Rice",
        "category": "Rice",
        "price": 110,
        "description": "Vegetable fried rice",
        "image": "images/veg_fried_rice.jpg",
        "model": "cylinder",
        "color": "#FFDAB9",
    },
    {
        "id": "veg_hyderabadi_biryani",
        "name": "Veg Hyderabadi Biryani",
        "category": "Rice",
        "price": 180,
        "description": "Hyderabadi style veg biryani",
        "image": "images/veg_hyderabadi_biryani.jpg",
        "model": "cylinder",
        "color": "#DAA520",
    },
    {
        "id": "garlic_nan",
        "name": "Garlic Nan",
        "category": "Breads",
        "price": 50,
        "description": "Nan topped with garlic",
        "image": "images/garlic_nan.jpg",
        "model": "cylinder",
        "color": "#FFA07A",
    },
    {
        "id": "sweet_lassi",
        "name": "Sweet Lassi",
        "category": "Beverages",
        "price": 40,
        "description": "Sweet yogurt drink",
        "image": "images/sweet_lassi.jpg",
        "model": "cylinder",
        "color": "#FFFACD",
    },
    {
        "id": "hot_sour_soup",
        "name": "Hot & Sour Soup",
        "category": "Soups",
        "price": 60,
        "description": "Spicy and tangy soup",
        "image": "images/hot_sour_soup.jpg",
        "model": "cylinder",
        "color": "#FF6347",
    },
    {
        "id": "veg_noodles",
        "name": "Veg Noodles",
        "category": "Noodles",
        "price": 90,
        "description": "Stir fried veg noodles",
        "image": "images/veg_noodles.jpg",
        "model": "cylinder",
        "color": "#FFD700",
    },
    {
        "id": "kadhai_paneer",
        "name": "Kadhai Paneer",
        "category": "Main Course",
        "price": 200,
        "description": "Paneer in kadhai style",
        "image": "images/kadhai_paneer.jpg",
        "model": "box",
        "color": "#CD5C5C",
    },
    {
        "id": "paneer_biryani",
        "name": "Paneer Biryani",
        "category": "Rice",
        "price": 220,
        "description": "Biryani with paneer",
        "image": "images/paneer_biryani.jpg",
        "model": "cylinder",
        "color": "#CD853F",
    },
    {
        "id": "veg_platter",
        "name": "Veg Platter",
        "category": "Tandoor",
        "price": 280,
        "description": "Assorted veg kebabs",
        "image": "images/veg_platter.jpg",
        "model": "box",
        "color": "#DAA520",
    },
]

# Get unique categories
categories = sorted(list(set(item["category"] for item in menu_items)))
categories.insert(0, "All")

# Stylish CSS
css = """
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');
* { font-family: 'Poppins', sans-serif; }
body { background: #0a0a0a; min-height: 100vh; }
.header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    padding: 40px 20px;
    text-align: center;
    color: white;
    position: relative;
    overflow: hidden;
}
.header::before {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);
    animation: shimmer 3s infinite linear;
}
@keyframes shimmer { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
.header h1 { margin: 0; font-size: 3em; font-family: 'Playfair Display', serif; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); letter-spacing: 2px; }
.header p { margin: 15px 0 0; font-size: 1.2em; opacity: 0.95; }
.controls { display: flex; gap: 15px; padding: 25px 20px; background: linear-gradient(180deg, rgba(30,30,30,0.9) 0%, rgba(20,20,20,0.95) 100%); margin: 15px; border-radius: 20px; flex-wrap: wrap; box-shadow: 0 8px 32px rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.05); }
.controls input, .controls select { flex: 1; min-width: 180px; padding: 14px 20px; border: 2px solid rgba(255,255,255,0.1); border-radius: 12px; font-size: 15px; background: rgba(255,255,255,0.08); color: white; transition: all 0.3s; }
.controls input:focus, .controls select:focus { border-color: #667eea; background: rgba(255,255,255,0.12); outline: none; box-shadow: 0 0 20px rgba(102,126,234,0.3); }
.controls input::placeholder { color: rgba(255,255,255,0.5); }
.menu-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 25px; padding: 25px; }
.food-card { background: linear-gradient(145deg, #1e1e2e 0%, #252535 100%); border-radius: 20px; padding: 18px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.08); transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); position: relative; overflow: hidden; }
.food-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, #667eea, #f093fb); opacity: 0; transition: opacity 0.3s; }
.food-card:hover { transform: translateY(-12px) scale(1.02); box-shadow: 0 25px 50px rgba(102,126,234,0.25); border-color: rgba(102,126,234,0.3); }
.food-card:hover::before { opacity: 1; }
.food-card img { width: 100%; height: 160px; object-fit: cover; border-radius: 15px; transition: transform 0.4s; }
.food-card:hover img { transform: scale(1.05); }
.food-card .badge { display: inline-block; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 6px 14px; border-radius: 20px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin: 12px 0; }
.food-card h3 { color: #ffffff; margin: 10px 0 8px; font-size: 1.15em; font-weight: 600; }
.food-card .desc { color: #aaa; font-size: 13px; line-height: 1.5; margin: 8px 0; }
.food-card .price { color: #00d2ff; font-size: 1.5em; font-weight: 700; text-shadow: 0 0 10px rgba(0,210,255,0.3); display: inline-block; margin-top: 8px; }
.food-card .view-3d { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; padding: 12px 20px; border-radius: 12px; cursor: pointer; margin-top: 12px; width: 100%; font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; transition: all 0.3s; }
.food-card .view-3d:hover { transform: scale(1.02); box-shadow: 0 10px 25px rgba(102,126,234,0.4); }
.modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.9); z-index: 1000; justify-content: center; align-items: center; backdrop-filter: blur(10px); }
.modal.active { display: flex; }
.modal-content { background: linear-gradient(145deg, #1e1e2e 0%, #252535 100%); padding: 30px; border-radius: 25px; max-width: 550px; width: 90%; text-align: center; color: white; position: relative; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 25px 80px rgba(102,126,234,0.3); }
.modal-content canvas { width: 100%; height: 350px; border-radius: 15px; box-shadow: inset 0 0 30px rgba(0,0,0,0.3); }
.modal-close { position: absolute; top: 15px; right: 25px; font-size: 40px; color: rgba(255,255,255,0.6); cursor: pointer; transition: all 0.3s; z-index: 10; }
.modal-close:hover { color: #fff; transform: rotate(90deg); }
.no-results { text-align: center; color: #888; padding: 60px 20px; font-size: 18px; }
.no-results span { font-size: 50px; display: block; margin-bottom: 20px; }
.suggestion-box { background: linear-gradient(135deg, rgba(102,126,234,0.2), rgba(240,147,251,0.1)); border: 1px solid rgba(102,126,234,0.3); border-radius: 15px; padding: 20px; margin: 15px; text-align: center; }
.suggestion-box h3 { color: #667eea; margin: 0 0 10px; }
"""

# Three.js
three_js = (
    """
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
let scene, camera, renderer, model, isRotating = true;
function init3D(modelType, color) {
    const container = document.getElementById('3d-container');
    container.innerHTML = '';
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, container.clientWidth / 350, 0.1, 1000);
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(container.clientWidth, 350);
    container.appendChild(renderer.domElement);
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
    scene.add(ambientLight);
    const pointLight = new THREE.PointLight(0xffffff, 1);
    pointLight.position.set(5, 5, 5);
    scene.add(pointLight);
    let geometry;
    switch(modelType) {
        case 'sphere': geometry = new THREE.SphereGeometry(1.2, 32, 32); break;
        case 'cylinder': geometry = new THREE.CylinderGeometry(0.8, 0.8, 1.8, 32); break;
        case 'box': geometry = new THREE.BoxGeometry(1.5, 1.2, 1); break;
        case 'torus': geometry = new THREE.TorusGeometry(0.8, 0.3, 16, 100); break;
        default: geometry = new THREE.SphereGeometry(1.2, 32, 32);
    }
    const material = new THREE.MeshPhongMaterial({ color: color, shininess: 100, specular: 0x111111 });
    model = new THREE.Mesh(geometry, material);
    scene.add(model);
    camera.position.z = 4;
    animate();
}
function animate() {
    if (isRotating && model) { model.rotation.y += 0.01; model.rotation.x += 0.005; }
    renderer.render(scene, camera);
    requestAnimationFrame(animate);
}
function toggleRotation() { isRotating = !isRotating; }
function showModal(id) {
    const item = """
    + json.dumps(
        {
            i["id"]: {
                "name": i["name"],
                "model": i["model"],
                "color": i["color"],
                "price": i["price"],
                "description": i["description"],
            }
            for i in menu_items
        }
    )
    + """;
    const data = item[id];
    document.getElementById('modal-title').innerText = data.name;
    document.getElementById('modal-price').innerText = 'Rs. ' + data.price;
    document.getElementById('modal-desc').innerText = data.description;
    document.getElementById('3d-modal').classList.add('active');
    init3D(data.model, data.color);
}
function hideModal() { document.getElementById('3d-modal').classList.remove('active'); isRotating = true; }
</script>
"""
)


def get_suggestions(search, limit=6):
    if not search:
        return []
    search = search.lower()
    suggestions = []
    for item in menu_items:
        name = item.get("name", "").lower()
        if (
            search in name
            or any(s in name for s in search.split() if len(s) > 2)
            or any(name.startswith(s) for s in search.split() if len(s) > 2)
        ):
            suggestions.append(item)
            if len(suggestions) >= limit:
                break
    return suggestions


def filter_menu(category, price_filter, search):
    filtered = list(menu_items)
    if category and category != "All":
        filtered = [item for item in filtered if item.get("category") == category]
    if search:
        search_lower = search.lower()
        filtered = [
            item
            for item in filtered
            if search_lower in item.get("name", "").lower()
            or search_lower in item.get("description", "").lower()
        ]
    if price_filter == "Low to High":
        filtered = sorted(filtered, key=lambda x: x.get("price", 0))
    else:
        filtered = sorted(filtered, key=lambda x: x.get("price", 0), reverse=True)
    if not filtered and search:
        suggestions = get_suggestions(search, 6)
        if suggestions:
            html = '<div style="text-align:center;color:#667eea;padding:20px;font-size:16px;">No exact matches. Showing suggestions:</div><div class="menu-grid">'
            for item in suggestions:
                html += f'<div class="food-card"><img src="{item["image"]}"><span class="badge">{item["category"]}</span><h3>{item["name"]}</h3><p class="desc">{item["description"][:50]}...</p><div class="price">Rs. {item["price"]}</div><button class="view-3d" onclick="showModal(\'{item["id"]}\')">View 3D</button></div>'
            html += "</div>"
            return html
    if not filtered:
        return '<div class="no-results"><span>🍽️</span>No dishes found</div>'
    html = '<div class="menu-grid">'
    for item in filtered:
        html += f'<div class="food-card"><img src="{item["image"]}"><span class="badge">{item["category"]}</span><h3>{item["name"]}</h3><p class="desc">{item["description"][:50]}...</p><div class="price">Rs. {item["price"]}</div><button class="view-3d" onclick="showModal(\'{item["id"]}\')">View 3D</button></div>'
    html += "</div>"
    return html


with gr.Blocks(css=css, title="3D Restaurant Menu") as demo:
    gr.HTML(three_js)
    gr.HTML("""<div class="header"><h1>🍛 3D RESTAURANT MENU</h1><p>Click on any dish to view interactive 3D Model</p></div>
    <div id="3d-modal" class="modal"><span class="modal-close" onclick="hideModal()">&times;</span><div class="modal-content"><h2 id="modal-title"></h2><div id="3d-container"></div><p id="modal-desc" style="color:#aaa;margin:12px 0;font-size:14px;"></p><p id="modal-price" style="color:#00d2ff;font-size:1.5em;font-weight:bold;"></p><button class="view-3d" onclick="toggleRotation()" style="width:auto;padding:8px 25px;">Toggle Rotation</button></div></div>""")
    with gr.Row():
        with gr.Column(scale=1):
            category_dd = gr.Dropdown(
                choices=categories, value="All", label="Category", interactive=True
            )
        with gr.Column(scale=1):
            price_filter = gr.Dropdown(
                choices=["Low to High", "High to Low"],
                value="Low to High",
                label="Price",
                interactive=True,
            )
        with gr.Column(scale=2):
            search_input = gr.Textbox(
                placeholder="🔍 Search dishes...", label="Search", interactive=True
            )
    menu_output = gr.HTML()
    category_dd.change(
        filter_menu, [category_dd, price_filter, search_input], menu_output
    )
    price_filter.change(
        filter_menu, [category_dd, price_filter, search_input], menu_output
    )
    search_input.change(
        filter_menu, [category_dd, price_filter, search_input], menu_output
    )
    demo.load(lambda: filter_menu("All", "Low to High", ""), None, menu_output)

app = demo

if __name__ == "__main__":
    demo.launch()
