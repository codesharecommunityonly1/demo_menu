import gradio as gr
import json

# Menu Data
menu_items = [
    {
        "id": "bruschetta",
        "name": "Bruschetta",
        "category": "Appetizers",
        "price": 8.99,
        "description": "Toasted bread topped with fresh tomatoes, garlic, basil, and olive oil.",
        "image": "https://images.unsplash.com/photo-1572695157366-5e585ab2b69f?w=400",
        "model": "cylinder",
        "color": "#D4A574",
    },
    {
        "id": "caesar_salad",
        "name": "Caesar Salad",
        "category": "Appetizers",
        "price": 10.99,
        "description": "Crisp romaine lettuce with caesar dressing, parmesan, and croutons.",
        "image": "https://images.unsplash.com/photo-1550304943-4f24f54ddde9?w=400",
        "model": "sphere",
        "color": "#90EE90",
    },
    {
        "id": "garlic_bread",
        "name": "Garlic Bread",
        "category": "Appetizers",
        "price": 6.99,
        "description": "Warm bread with garlic butter and herbs.",
        "image": "https://images.unsplash.com/photo-1619535860434-ba1d8fa12536?w=400",
        "model": "box",
        "color": "#DEB887",
    },
    {
        "id": "salmon",
        "name": "Grilled Salmon",
        "category": "Mains",
        "price": 24.99,
        "description": "Fresh Atlantic salmon with lemon herb butter and seasonal vegetables.",
        "image": "https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400",
        "model": "torus",
        "color": "#FA8072",
    },
    {
        "id": "chicken",
        "name": "Chicken Parmesan",
        "category": "Mains",
        "price": 18.99,
        "description": "Breaded chicken breast with marinara sauce and melted mozzarella.",
        "image": "https://images.unsplash.com/photo-1632778149955-e80f8ceca2e8?w=400",
        "model": "sphere",
        "color": "#FFD700",
    },
    {
        "id": "steak",
        "name": "Beef Steak",
        "category": "Mains",
        "price": 29.99,
        "description": "8oz ribeye steak with peppercorn sauce and mashed potatoes.",
        "image": "https://images.unsplash.com/photo-1600891964092-4316c288032e?w=400",
        "model": "box",
        "color": "#8B4513",
    },
    {
        "id": "pasta",
        "name": "Pasta Primavera",
        "category": "Mains",
        "price": 16.99,
        "description": "Penne pasta with fresh vegetables in garlic olive oil.",
        "image": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=400",
        "model": "cylinder",
        "color": "#FFE4B5",
    },
    {
        "id": "lava_cake",
        "name": "Chocolate Lava Cake",
        "category": "Desserts",
        "price": 9.99,
        "description": "Warm chocolate cake with molten center and vanilla ice cream.",
        "image": "https://images.unsplash.com/photo-1624353365286-3f8d62daad51?w=400",
        "model": "sphere",
        "color": "#4A0E0E",
    },
    {
        "id": "tiramisu",
        "name": "Tiramisu",
        "category": "Desserts",
        "price": 8.99,
        "description": "Classic Italian dessert with espresso-soaked ladyfingers and mascarpone.",
        "image": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=400",
        "model": "box",
        "color": "#F5DEB3",
    },
    {
        "id": "cheesecake",
        "name": "Cheesecake",
        "category": "Desserts",
        "price": 7.99,
        "description": "Creamy New York style cheesecake with berry compote.",
        "image": "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?w=400",
        "model": "cylinder",
        "color": "#FFFACD",
    },
]

categories = ["All", "Appetizers", "Mains", "Desserts"]

# CSS and JS for 3D
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
    cursor: pointer;
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
.food-card .price { color: #ff6b35; font-size: 1.5em; font-weight: bold; }
.food-card .view-3d {
    background: linear-gradient(135deg, #004e89, #0066b2);
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 10px;
    cursor: pointer;
    margin-top: 10px;
    width: 100%;
}
.modal {
    display: none;
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.8);
    z-index: 1000;
    justify-content: center;
    align-items: center;
}
.modal.active { display: flex; }
.modal-content {
    background: linear-gradient(135deg, #1a1a2e, #16213e);
    padding: 30px;
    border-radius: 20px;
    max-width: 600px;
    width: 90%;
    text-align: center;
    color: white;
}
.modal-content canvas { width: 100%; height: 400px; }
.modal-close {
    position: absolute;
    top: 20px;
    right: 30px;
    font-size: 40px;
    color: white;
    cursor: pointer;
}
"""

three_js = (
    """
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
let scene, camera, renderer, model;
let isRotating = true;

function init3D(modelType, color) {
    const container = document.getElementById('3d-container');
    container.innerHTML = '';
    
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, container.clientWidth / 400, 0.1, 1000);
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(container.clientWidth, 400);
    container.appendChild(renderer.domElement);
    
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
    scene.add(ambientLight);
    
    const pointLight = new THREE.PointLight(0xffffff, 1);
    pointLight.position.set(5, 5, 5);
    scene.add(pointLight);
    
    let geometry;
    switch(modelType) {
        case 'sphere':
            geometry = new THREE.SphereGeometry(1.5, 32, 32);
            break;
        case 'cylinder':
            geometry = new THREE.CylinderGeometry(1, 1, 2, 32);
            break;
        case 'box':
            geometry = new THREE.BoxGeometry(2, 1.5, 1);
            break;
        case 'torus':
            geometry = new THREE.TorusGeometry(1, 0.4, 16, 100);
            break;
        default:
            geometry = new THREE.SphereGeometry(1.5, 32, 32);
    }
    
    const material = new THREE.MeshPhongMaterial({ 
        color: color,
        shininess: 100,
        specular: 0x111111
    });
    model = new THREE.Mesh(geometry, material);
    scene.add(model);
    
    camera.position.z = 5;
    
    animate();
}

function animate() {
    if (isRotating && model) {
        model.rotation.y += 0.01;
        model.rotation.x += 0.005;
    }
    renderer.render(scene, camera);
    requestAnimationFrame(animate);
}

function toggleRotation() {
    isRotating = !isRotating;
}

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
    document.getElementById('modal-price').innerText = '$' + data.price.toFixed(2);
    document.getElementById('modal-desc').innerText = data.description;
    document.getElementById('3d-modal').classList.add('active');
    init3D(data.model, data.color);
}

function hideModal() {
    document.getElementById('3d-modal').classList.remove('active');
    isRotating = true;
}
</script>
"""
)


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
        return '<div style="text-align:center;color:#888;padding:40px;font-size:18px;">No dishes found 🍽️</div>'

    html = '<div class="menu-grid">'
    for item in filtered:
        html += f'''
        <div class="food-card">
            <img src="{item["image"]}" alt="{item["name"]}">
            <span class="badge">{item["category"]}</span>
            <h3>{item["name"]}</h3>
            <p class="desc">{item["description"][:60]}...</p>
            <div class="price">${item["price"]:.2f}</div>
            <button class="view-3d" onclick="showModal('{item["id"]}')">View 3D Model</button>
        </div>'''
    html += "</div>"
    return html


with gr.Blocks(css=css, title="Restaurant Menu") as demo:
    gr.HTML(three_js)

    gr.HTML("""
        <div class="header">
            <h1>🍽️ Restaurant Menu</h1>
            <p>Click on a dish to view 3D model</p>
        </div>
        
        <div id="3d-modal" class="modal">
            <span class="modal-close" onclick="hideModal()">&times;</span>
            <div class="modal-content">
                <h2 id="modal-title"></h2>
                <div id="3d-container"></div>
                <p id="modal-desc" style="color:#ccc;margin:15px 0;"></p>
                <p id="modal-price" style="color:#ff6b35;font-size:1.5em;font-weight:bold;"></p>
                <button class="view-3d" onclick="toggleRotation()" style="width:auto;padding:10px 30px;">Toggle Rotation</button>
            </div>
        </div>
    """)

    with gr.Row():
        with gr.Column(scale=1):
            category_dd = gr.Dropdown(
                choices=categories, value="All", label="Category", interactive=True
            )
        with gr.Column(scale=2):
            search_input = gr.Textbox(
                placeholder="Search dishes...", label="Search", interactive=True
            )

    menu_output = gr.HTML()

    category_dd.change(filter_menu, [category_dd, search_input], menu_output)
    search_input.change(filter_menu, [category_dd, search_input], menu_output)
    demo.load(lambda: filter_menu("All", ""), None, menu_output)

demo.launch()
