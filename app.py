import gradio as gr
import json

# Menu Data - Complete Restaurant Menu
menu_items = [
    # STARTERS (Appetizers)
    {
        "id": "paneer65",
        "name": "Paneer 65",
        "category": "Starters",
        "price": 180,
        "description": "Crispy paneer pieces tossed in spicy masala",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "box",
        "color": "#FFA500",
    },
    {
        "id": "honey_chilly_potato",
        "name": "Honey Chilly Potato",
        "category": "Starters",
        "price": 140,
        "description": "Crispy potatoes with honey and chili sauce",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#FFD700",
    },
    {
        "id": "american_choupsy",
        "name": "American Choupsy",
        "category": "Starters",
        "price": 170,
        "description": "American style fried veggie rolls",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#DEB887",
    },
    {
        "id": "crispy_chilly_baby_corn",
        "name": "Crispy Chilly Baby Corn",
        "category": "Starters",
        "price": 160,
        "description": "Crispy baby corn with chili sauce",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#DAA520",
    },
    {
        "id": "french_fries",
        "name": "French Fries",
        "category": "Starters",
        "price": 80,
        "description": "Crispy golden french fries",
        "image": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=400",
        "model": "cylinder",
        "color": "#FFD700",
    },
    {
        "id": "dragon_paneer",
        "name": "Dragon Paneer",
        "category": "Starters",
        "price": 180,
        "description": "Spicy dragon sauce with paneer",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "box",
        "color": "#DC143C",
    },
    {
        "id": "veg_manchurian",
        "name": "Veg Manchurian",
        "category": "Starters",
        "price": 110,
        "description": "Vegetable balls in manchurian sauce",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#8B4513",
    },
    {
        "id": "paneer_manchurian",
        "name": "Paneer Manchurian",
        "category": "Starters",
        "price": 160,
        "description": "Paneer balls in manchurian sauce",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#A0522D",
    },
    {
        "id": "paneer_chilli",
        "name": "Paneer Chilli",
        "category": "Starters",
        "price": 160,
        "description": "Paneer with chili and soy sauce",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "box",
        "color": "#FF4500",
    },
    {
        "id": "crispy_chilly_mushroom",
        "name": "Crispy Chilly Mushroom",
        "category": "Starters",
        "price": 140,
        "description": "Crispy mushroom with chili",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#D2B48C",
    },
    {
        "id": "veg_lolipop",
        "name": "Veg Lolipop",
        "category": "Starters",
        "price": 150,
        "description": "Vegetable lolipops with sauce",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#FF6347",
    },
    {
        "id": "gobi65",
        "name": "Gobi 65",
        "category": "Starters",
        "price": 100,
        "description": "Crispy cauliflower 65",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#FFA07A",
    },
    {
        "id": "veg_spring_roll",
        "name": "Veg Spring Roll",
        "category": "Starters",
        "price": 150,
        "description": "Crispy vegetable spring rolls",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#F4A460",
    },
    {
        "id": "paneer_spring_roll",
        "name": "Paneer Spring Roll",
        "category": "Starters",
        "price": 190,
        "description": "Crispy paneer spring rolls",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#D2691E",
    },
    {
        "id": "paneer_roll",
        "name": "Paneer Roll",
        "category": "Starters",
        "price": 90,
        "description": "Wrap with paneer filling",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#CD853F",
    },
    {
        "id": "veg_roll",
        "name": "Veg Roll",
        "category": "Starters",
        "price": 60,
        "description": "Wrap with vegetable filling",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#DEB887",
    },
    {
        "id": "mushroom_salt_pepper",
        "name": "Mushroom Salt & Pepper",
        "category": "Starters",
        "price": 120,
        "description": "Mushroom with salt and pepper",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#A9A9A9",
    },
    {
        "id": "mushroom65",
        "name": "Mushroom 65",
        "category": "Starters",
        "price": 140,
        "description": "Spicy crispy mushrooms",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#808080",
    },
    {
        "id": "corn_salt_pepper",
        "name": "Corn Salt & Pepper",
        "category": "Starters",
        "price": 150,
        "description": "Sweet corn with salt pepper",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#FFDAB9",
    },
    {
        "id": "onion_pakora",
        "name": "Onion Pakora",
        "category": "Starters",
        "price": 80,
        "description": "Crispy onion pakora",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#DAA520",
    },
    {
        "id": "paneer_pakora",
        "name": "Paneer Pakora",
        "category": "Starters",
        "price": 150,
        "description": "Crispy paneer pakora",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "box",
        "color": "#FFA07A",
    },
    # SOUPS
    {
        "id": "hot_sour_soup",
        "name": "Hot & Sour Soup",
        "category": "Soups",
        "price": 60,
        "description": "Spicy and tangy soup",
        "image": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400",
        "model": "cylinder",
        "color": "#FF6347",
    },
    {
        "id": "lemon_coriander_soup",
        "name": "Lemon Coriander Soup",
        "category": "Soups",
        "price": 50,
        "description": "Fresh lemon and coriander soup",
        "image": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400",
        "model": "cylinder",
        "color": "#90EE90",
    },
    {
        "id": "clear_soup",
        "name": "Clear Soup",
        "category": "Soups",
        "price": 40,
        "description": "Light and clear vegetable soup",
        "image": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400",
        "model": "cylinder",
        "color": "#FFFACD",
    },
    {
        "id": "sweet_corn_soup",
        "name": "Sweet Corn Soup",
        "category": "Soups",
        "price": 60,
        "description": "Sweet corn in clear soup",
        "image": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400",
        "model": "cylinder",
        "color": "#FFD700",
    },
    {
        "id": "veg_manchow_soup",
        "name": "Veg Manchow Soup",
        "category": "Soups",
        "price": 70,
        "description": "Spicy veg manchow soup",
        "image": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400",
        "model": "cylinder",
        "color": "#8B4513",
    },
    {
        "id": "tomato_soup",
        "name": "Tomato Soup",
        "category": "Soups",
        "price": 40,
        "description": "Creamy tomato soup",
        "image": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400",
        "model": "cylinder",
        "color": "#FF4500",
    },
    # CHINESE MAIN COURSE
    {
        "id": "veg_manchurian_gravy",
        "name": "Veg Manchurian Gravy",
        "category": "Chinese Main Course",
        "price": 140,
        "description": "Veg manchurian in gravy (Full)",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#8B4513",
    },
    {
        "id": "paneer_manchurian_gravy",
        "name": "Paneer Manchurian Gravy",
        "category": "Chinese Main Course",
        "price": 180,
        "description": "Paneer manchurian in gravy (Full)",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#A0522D",
    },
    {
        "id": "paneer_chilli_gravy",
        "name": "Paneer Chilli Gravy",
        "category": "Chinese Main Course",
        "price": 200,
        "description": "Paneer in spicy gravy (Full)",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "box",
        "color": "#FF4500",
    },
    {
        "id": "mushroom_chilli_gravy",
        "name": "Mushroom Chilli Gravy",
        "category": "Chinese Main Course",
        "price": 190,
        "description": "Mushroom in chili gravy (Full)",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#696969",
    },
    {
        "id": "baby_corn_chilly_gravy",
        "name": "Baby Corn Chilly Gravy",
        "category": "Chinese Main Course",
        "price": 220,
        "description": "Baby corn in chilly gravy (Full)",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#9ACD32",
    },
    # NOODLES
    {
        "id": "veg_noodles",
        "name": "Veg Noodles",
        "category": "Noodles",
        "price": 90,
        "description": "Stir fried veg noodles",
        "image": "https://images.unsplash.com/photo-1569718212165-3a8278d5f7dc?w=400",
        "model": "cylinder",
        "color": "#FFD700",
    },
    {
        "id": "veg_hakka_noodles",
        "name": "Veg Hakka Noodles",
        "category": "Noodles",
        "price": 100,
        "description": "Hakka style veg noodles",
        "image": "https://images.unsplash.com/photo-1569718212165-3a8278d5f7dc?w=400",
        "model": "cylinder",
        "color": "#FFA500",
    },
    {
        "id": "paneer_noodles",
        "name": "Paneer Noodles",
        "category": "Noodles",
        "price": 130,
        "description": "Noodles with paneer",
        "image": "https://images.unsplash.com/photo-1569718212165-3a8278d5f7dc?w=400",
        "model": "cylinder",
        "color": "#FF8C00",
    },
    {
        "id": "chilli_garlic_noodles",
        "name": "Chilli Garlic Noodles",
        "category": "Noodles",
        "price": 110,
        "description": "Noodles with chili and garlic",
        "image": "https://images.unsplash.com/photo-1569718212165-3a8278d5f7dc?w=400",
        "model": "cylinder",
        "color": "#DC143C",
    },
    {
        "id": "schezwan_noodles",
        "name": "Schezwan Noodles",
        "category": "Noodles",
        "price": 110,
        "description": "Schezwan style noodles",
        "image": "https://images.unsplash.com/photo-1569718212165-3a8278d5f7dc?w=400",
        "model": "cylinder",
        "color": "#B22222",
    },
    {
        "id": "manchurian_noodles",
        "name": "Manchurian Noodles",
        "category": "Noodles",
        "price": 130,
        "description": "Noodles with manchurian",
        "image": "https://images.unsplash.com/photo-1569718212165-3a8278d5f7dc?w=400",
        "model": "cylinder",
        "color": "#8B0000",
    },
    {
        "id": "rk_special_noodles",
        "name": "R K Adarsh Special Noodles",
        "category": "Noodles",
        "price": 160,
        "description": "Special noodles with extra toppings",
        "image": "https://images.unsplash.com/photo-1569718212165-3a8278d5f7dc?w=400",
        "model": "cylinder",
        "color": "#FF4500",
    },
    # RICE
    {
        "id": "steam_rice",
        "name": "Steam Rice",
        "category": "Rice",
        "price": 60,
        "description": "Steamed basmati rice",
        "image": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400",
        "model": "cylinder",
        "color": "#F5F5DC",
    },
    {
        "id": "jeera_rice",
        "name": "Jeera Rice",
        "category": "Rice",
        "price": 80,
        "description": "Rice with cumin seeds",
        "image": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400",
        "model": "cylinder",
        "color": "#FFE4B5",
    },
    {
        "id": "veg_fried_rice",
        "name": "Veg Fried Rice",
        "category": "Rice",
        "price": 110,
        "description": "Vegetable fried rice",
        "image": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400",
        "model": "cylinder",
        "color": "#FFDAB9",
    },
    {
        "id": "paneer_fried_rice",
        "name": "Paneer Fried Rice",
        "category": "Rice",
        "price": 150,
        "description": "Fried rice with paneer",
        "image": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400",
        "model": "cylinder",
        "color": "#FFA07A",
    },
    {
        "id": "mushroom_fried_rice",
        "name": "Mushroom Fried Rice",
        "category": "Rice",
        "price": 140,
        "description": "Fried rice with mushroom",
        "image": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400",
        "model": "cylinder",
        "color": "#D2B48C",
    },
    {
        "id": "schezwan_fried_rice",
        "name": "Schezwan Fried Rice",
        "category": "Rice",
        "price": 120,
        "description": "Spicy schezwan fried rice",
        "image": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400",
        "model": "cylinder",
        "color": "#CD5C5C",
    },
    {
        "id": "rk_special_fried_rice",
        "name": "RK Adarsh Sp. Fried Rice",
        "category": "Rice",
        "price": 190,
        "description": "Special fried rice",
        "image": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400",
        "model": "cylinder",
        "color": "#FF6347",
    },
    {
        "id": "veg_pulao",
        "name": "Veg Pulao",
        "category": "Rice",
        "price": 140,
        "description": "Fragrant veg pulao",
        "image": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400",
        "model": "cylinder",
        "color": "#F0E68C",
    },
    {
        "id": "kashmiri_pulao",
        "name": "Kashmiri Pulao",
        "category": "Rice",
        "price": 200,
        "description": "Kashmiri style pulao with dry fruits",
        "image": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400",
        "model": "cylinder",
        "color": "#FFB6C1",
    },
    {
        "id": "paneer_pulao",
        "name": "Paneer Pulao",
        "category": "Rice",
        "price": 180,
        "description": "Pulao with paneer",
        "image": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400",
        "model": "cylinder",
        "color": "#FFA07A",
    },
    {
        "id": "green_peas_pulao",
        "name": "Green Peas Pulao",
        "category": "Rice",
        "price": 120,
        "description": "Pulao with green peas",
        "image": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400",
        "model": "cylinder",
        "color": "#90EE90",
    },
    {
        "id": "veg_hyderabadi_biryani",
        "name": "Veg Hyderabadi Dum Biryani",
        "category": "Rice",
        "price": 180,
        "description": "Hyderabadi style veg biryani",
        "image": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=400",
        "model": "cylinder",
        "color": "#DAA520",
    },
    {
        "id": "paneer_biryani",
        "name": "Paneer Biryani",
        "category": "Rice",
        "price": 220,
        "description": "Biryani with paneer",
        "image": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=400",
        "model": "cylinder",
        "color": "#CD853F",
    },
    # MAIN COURSE
    {
        "id": "plain_dal",
        "name": "Plain Dal",
        "category": "Main Course",
        "price": 60,
        "description": "Simple boiled dal",
        "image": "https://images.unsplash.com/photo-1546833999-b9f581a2026c?w=400",
        "model": "cylinder",
        "color": "#DAA520",
    },
    {
        "id": "dal_fry",
        "name": "Dal Fry",
        "category": "Main Course",
        "price": 80,
        "description": "Dal with tempered spices",
        "image": "https://images.unsplash.com/photo-1546833999-b9f581a2026c?w=400",
        "model": "cylinder",
        "color": "#FFA500",
    },
    {
        "id": "dal_tadka",
        "name": "Dal Tadka",
        "category": "Main Course",
        "price": 100,
        "description": "Dal with tempering",
        "image": "https://images.unsplash.com/photo-1546833999-b9f581a2026c?w=400",
        "model": "cylinder",
        "color": "#FFD700",
    },
    {
        "id": "dal_makhani",
        "name": "Dal Makhani",
        "category": "Main Course",
        "price": 160,
        "description": "Creamy black dal makhani",
        "image": "https://images.unsplash.com/photo-1546833999-b9f581a2026c?w=400",
        "model": "cylinder",
        "color": "#8B4513",
    },
    {
        "id": "rajma_masala",
        "name": "Rajma Masala",
        "category": "Main Course",
        "price": 180,
        "description": "Kidney beans in masala (Full)",
        "image": "https://images.unsplash.com/photo-1546833999-b9f581a2026c?w=400",
        "model": "sphere",
        "color": "#A52A2A",
    },
    {
        "id": "paneer_masala",
        "name": "Paneer Masala",
        "category": "Main Course",
        "price": 200,
        "description": "Paneer in masala curry (Full)",
        "image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=400",
        "model": "sphere",
        "color": "#FFA500",
    },
    {
        "id": "paneer_butter_masala",
        "name": "Paneer Butter Masala",
        "category": "Main Course",
        "price": 220,
        "description": "Creamy paneer butter masala (Full)",
        "image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=400",
        "model": "sphere",
        "color": "#FF8C00",
    },
    {
        "id": "paneer_mushroom_masala",
        "name": "Paneer Mushroom Masala",
        "category": "Main Course",
        "price": 190,
        "description": "Paneer and mushroom in masala (Full)",
        "image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=400",
        "model": "sphere",
        "color": "#CD853F",
    },
    {
        "id": "mix_veg",
        "name": "Mix Veg",
        "category": "Main Course",
        "price": 160,
        "description": "Mixed vegetables curry (Full)",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#228B22",
    },
    {
        "id": "sahi_paneer",
        "name": "Sahi Paneer",
        "category": "Main Course",
        "price": 240,
        "description": "Royal paneer gravy (Full)",
        "image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=400",
        "model": "sphere",
        "color": "#FFD700",
    },
    {
        "id": "palak_paneer",
        "name": "Palak Paneer",
        "category": "Main Course",
        "price": 180,
        "description": "Paneer in spinach gravy (Full)",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#006400",
    },
    {
        "id": "mushroom_masala",
        "name": "Mushroom Masala",
        "category": "Main Course",
        "price": 180,
        "description": "Mushroom in masala (Full)",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#696969",
    },
    {
        "id": "corn_palak",
        "name": "Corn Palak",
        "category": "Main Course",
        "price": 190,
        "description": "Sweet corn in spinach (Full)",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#2E8B57",
    },
    {
        "id": "paneer_bhurji",
        "name": "Paneer Bhurji",
        "category": "Main Course",
        "price": 220,
        "description": "Scrambled paneer (Full)",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "box",
        "color": "#FFA07A",
    },
    {
        "id": "aloo_green_matar",
        "name": "Aloo Green Matar",
        "category": "Main Course",
        "price": 140,
        "description": "Potato and green peas (Full)",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#32CD32",
    },
    {
        "id": "veg_kolhapuri",
        "name": "Veg Kolhapuri",
        "category": "Main Course",
        "price": 180,
        "description": "Spicy Kolhapuri veg (Full)",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#DC143C",
    },
    {
        "id": "kashmiri_aloo_dum",
        "name": "Kashmiri Aloo Dum",
        "category": "Main Course",
        "price": 220,
        "description": "Kashmiri style potato dum (Full)",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#FF6347",
    },
    {
        "id": "aloo_dum_masala",
        "name": "Aloo Dum Masala",
        "category": "Main Course",
        "price": 140,
        "description": "Potato in masala (Full)",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#FFA500",
    },
    {
        "id": "aloo_gobi_masala",
        "name": "Aloo Gobi Masala",
        "category": "Main Course",
        "price": 150,
        "description": "Potato and cauliflower (Full)",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#DAA520",
    },
    {
        "id": "paneer_pasanda",
        "name": "Paneer Pasanda",
        "category": "Main Course",
        "price": 190,
        "description": "Rich paneer curry (Full)",
        "image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=400",
        "model": "sphere",
        "color": "#FFB347",
    },
    {
        "id": "paneer_tikka_masala",
        "name": "Paneer Tikka Masala",
        "category": "Main Course",
        "price": 220,
        "description": "Paneer tikka in masala (Full)",
        "image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=400",
        "model": "sphere",
        "color": "#FF8C00",
    },
    {
        "id": "kadhai_paneer",
        "name": "Kadhai Paneer",
        "category": "Main Course",
        "price": 200,
        "description": "Paneer in kadhai style (Full)",
        "image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=400",
        "model": "box",
        "color": "#CD5C5C",
    },
    {
        "id": "paneer_do_pyaza",
        "name": "Paneer Do Pyaza",
        "category": "Main Course",
        "price": 220,
        "description": "Paneer with double onions (Full)",
        "image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=400",
        "model": "sphere",
        "color": "#FF6347",
    },
    {
        "id": "paneer_lababdar",
        "name": "Paneer Lababdar",
        "category": "Main Course",
        "price": 220,
        "description": "Rich creamy paneer (Full)",
        "image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=400",
        "model": "sphere",
        "color": "#FFA07A",
    },
    {
        "id": "paneer_malai_kofta",
        "name": "Paneer Malai Kofta",
        "category": "Main Course",
        "price": 200,
        "description": "Paneer kofta in cream (Full)",
        "image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=400",
        "model": "sphere",
        "color": "#FFEFD5",
    },
    {
        "id": "kadhai_mushroom",
        "name": "Kadhai Mushroom",
        "category": "Main Course",
        "price": 190,
        "description": "Mushroom in kadhai (Full)",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "box",
        "color": "#8B7355",
    },
    {
        "id": "veg_jalfrezi",
        "name": "Veg Jalfrezi",
        "category": "Main Course",
        "price": 160,
        "description": "Spicy veg jalfrezi (Full)",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#FF4500",
    },
    {
        "id": "mushroom_do_pyaza",
        "name": "Mushroom Do Pyaza",
        "category": "Main Course",
        "price": 190,
        "description": "Mushroom with double onions (Full)",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#A9A9A9",
    },
    {
        "id": "mushroom_matar_masala",
        "name": "Mushroom Matar Masala",
        "category": "Main Course",
        "price": 200,
        "description": "Mushroom and peas masala (Full)",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#808080",
    },
    # TANDOOR
    {
        "id": "paneer_tikka",
        "name": "Paneer Tikka",
        "category": "Tandoor",
        "price": 220,
        "description": "Tandoor roasted paneer tikka",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "box",
        "color": "#FFA500",
    },
    {
        "id": "paneer_malai_tikka",
        "name": "Paneer Malai Tikka",
        "category": "Tandoor",
        "price": 240,
        "description": "Creamy malai paneer tikka",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "box",
        "color": "#FFEFD5",
    },
    {
        "id": "achari_paneer_tikka",
        "name": "Achari Paneer Tikka",
        "category": "Tandoor",
        "price": 230,
        "description": "Pickle flavored paneer tikka",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "box",
        "color": "#FF6347",
    },
    {
        "id": "mushroom_tikka",
        "name": "Mushroom Tikka",
        "category": "Tandoor",
        "price": 180,
        "description": "Tandoor roasted mushroom",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#D2B48C",
    },
    {
        "id": "paneer_hariyali_tikka",
        "name": "Paneer Hariyali Tikka",
        "category": "Tandoor",
        "price": 220,
        "description": "Green herb paneer tikka",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "box",
        "color": "#32CD32",
    },
    {
        "id": "paneer_seekh_kebab",
        "name": "Paneer Seekh Kebab",
        "category": "Tandoor",
        "price": 250,
        "description": "Minced paneer seekh kebab",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#CD853F",
    },
    {
        "id": "veg_seekh_kabab",
        "name": "Veg Seekh Kabab",
        "category": "Tandoor",
        "price": 200,
        "description": "Vegetable seekh kabab",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#A0522D",
    },
    {
        "id": "veg_harabhara_kebab",
        "name": "Veg Harabhara Kebab",
        "category": "Tandoor",
        "price": 240,
        "description": "Green vegetable kebab",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#228B22",
    },
    {
        "id": "veg_platter",
        "name": "Veg Platter",
        "category": "Tandoor",
        "price": 280,
        "description": "Assorted veg kebabs",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "box",
        "color": "#DAA520",
    },
    {
        "id": "kashmiri_aloo_kebab",
        "name": "Kashmiri Aloo Kebab",
        "category": "Tandoor",
        "price": 200,
        "description": "Kashmiri style potato kebab",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "sphere",
        "color": "#FFB6C1",
    },
    # BREADS
    {
        "id": "tawa_roti",
        "name": "Tawa Roti",
        "category": "Breads",
        "price": 6,
        "description": "Plain tawa roti",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#F5DEB3",
    },
    {
        "id": "tawa_butter_roti",
        "name": "Tawa Butter Roti",
        "category": "Breads",
        "price": 12,
        "description": "Tawa roti with butter",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#FFE4B5",
    },
    {
        "id": "tandoori_roti",
        "name": "Tandoori Roti",
        "category": "Breads",
        "price": 15,
        "description": "Tandoor baked roti",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#DEB887",
    },
    {
        "id": "tandoori_butter_roti",
        "name": "Tandoori Butter Roti",
        "category": "Breads",
        "price": 20,
        "description": "Tandoori roti with butter",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#D2B48C",
    },
    {
        "id": "nan",
        "name": "Nan",
        "category": "Breads",
        "price": 35,
        "description": "Soft tandoor baked nan",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#F0E68C",
    },
    {
        "id": "butter_nan",
        "name": "Butter Nan",
        "category": "Breads",
        "price": 45,
        "description": "Nan with butter",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#FFDAB9",
    },
    {
        "id": "garlic_nan",
        "name": "Garlic Nan",
        "category": "Breads",
        "price": 50,
        "description": "Nan topped with garlic",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#FFA07A",
    },
    {
        "id": "white_til_nan",
        "name": "White Til Nan",
        "category": "Breads",
        "price": 45,
        "description": "Nan with white sesame",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#FAF0E6",
    },
    {
        "id": "kashmiri_nan",
        "name": "Kashmiri Nan",
        "category": "Breads",
        "price": 60,
        "description": "Sweet Kashmiri nan",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#FFB6C1",
    },
    {
        "id": "onion_kulcha",
        "name": "Onion Kulcha",
        "category": "Breads",
        "price": 45,
        "description": "Kulcha with onions",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#F4A460",
    },
    {
        "id": "masala_kulcha",
        "name": "Masala Kulcha",
        "category": "Breads",
        "price": 60,
        "description": "Spiced kulcha",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#D2691E",
    },
    {
        "id": "paneer_kulcha",
        "name": "Paneer Kulcha",
        "category": "Breads",
        "price": 60,
        "description": "Kulcha with paneer stuffing",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#CD853F",
    },
    {
        "id": "laccha_paratha",
        "name": "Laccha Paratha",
        "category": "Breads",
        "price": 35,
        "description": "Layered laccha paratha",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#DEB887",
    },
    {
        "id": "aloo_paratha",
        "name": "Aloo Paratha",
        "category": "Breads",
        "price": 35,
        "description": "Potato stuffed paratha",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#DAA520",
    },
    {
        "id": "paneer_paratha",
        "name": "Paneer Paratha",
        "category": "Breads",
        "price": 60,
        "description": "Paneer stuffed paratha",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#FFA07A",
    },
    {
        "id": "gobi_paratha",
        "name": "Gobi Paratha",
        "category": "Breads",
        "price": 40,
        "description": "Cauliflower paratha",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#F0E68C",
    },
    {
        "id": "missi_roti",
        "name": "Missi Roti",
        "category": "Breads",
        "price": 40,
        "description": "Traditional missi roti",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#8B4513",
    },
    {
        "id": "stuffed_nan",
        "name": "Stuffed Nan",
        "category": "Breads",
        "price": 70,
        "description": "Nan with stuffing",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400",
        "model": "cylinder",
        "color": "#CD5C5C",
    },
    # BEVERAGES
    {
        "id": "tea",
        "name": "Tea",
        "category": "Beverages",
        "price": 20,
        "description": "Indian masala tea",
        "image": "https://images.unsplash.com/photo-1564890369478-c89ca6d9cbe9?w=400",
        "model": "cylinder",
        "color": "#D2691E",
    },
    {
        "id": "coffee",
        "name": "Coffee",
        "category": "Beverages",
        "price": 30,
        "description": "Hot Indian coffee",
        "image": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=400",
        "model": "cylinder",
        "color": "#8B4513",
    },
    {
        "id": "cold_coffee",
        "name": "Cold Coffee",
        "category": "Beverages",
        "price": 80,
        "description": "Chilled coffee",
        "image": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=400",
        "model": "cylinder",
        "color": "#A0522D",
    },
    {
        "id": "cold_coffee_icecream",
        "name": "Cold Coffee with Ice-Cream",
        "category": "Beverages",
        "price": 110,
        "description": "Cold coffee with vanilla ice cream",
        "image": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=400",
        "model": "cylinder",
        "color": "#CD853F",
    },
    {
        "id": "mineral_water",
        "name": "Mineral Water",
        "category": "Beverages",
        "price": 20,
        "description": "1L mineral water bottle",
        "image": "https://images.unsplash.com/photo-1559839914-17aae19cec71?w=400",
        "model": "cylinder",
        "color": "#87CEEB",
    },
    {
        "id": "sweet_lassi",
        "name": "Sweet Lassi",
        "category": "Beverages",
        "price": 40,
        "description": "Sweet yogurt drink",
        "image": "https://images.unsplash.com/photo-1626200419199-391ae4be7a41?w=400",
        "model": "cylinder",
        "color": "#FFFACD",
    },
]

# Extract unique categories
categories = sorted(list(set(item["category"] for item in menu_items)))
categories.insert(0, "All")

# CSS
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
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
    padding: 20px;
}
.food-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
    border-radius: 15px;
    padding: 15px;
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
    height: 150px;
    object-fit: cover;
    border-radius: 10px;
}
.food-card .badge {
    display: inline-block;
    background: linear-gradient(135deg, #ff6b35, #ff8c42);
    padding: 4px 10px;
    border-radius: 15px;
    font-size: 11px;
    margin: 8px 0;
}
.food-card h3 { color: #f7c59f; margin: 8px 0 5px; font-size: 1.1em; }
.food-card .desc { color: #aaa; font-size: 13px; line-height: 1.4; margin: 8px 0; }
.food-card .price { color: #ff6b35; font-size: 1.4em; font-weight: bold; }
.food-card .view-3d {
    background: linear-gradient(135deg, #004e89, #0066b2);
    color: white;
    border: none;
    padding: 8px 15px;
    border-radius: 8px;
    cursor: pointer;
    margin-top: 8px;
    width: 100%;
    font-size: 14px;
}
.modal {
    display: none;
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.85);
    z-index: 1000;
    justify-content: center;
    align-items: center;
}
.modal.active { display: flex; }
.modal-content {
    background: linear-gradient(135deg, #1a1a2e, #16213e);
    padding: 25px;
    border-radius: 20px;
    max-width: 550px;
    width: 90%;
    text-align: center;
    color: white;
    position: relative;
}
.modal-content canvas { width: 100%; height: 350px; border-radius: 10px; }
.modal-close {
    position: absolute;
    top: 10px;
    right: 20px;
    font-size: 35px;
    color: white;
    cursor: pointer;
    z-index: 10;
}
"""

# Three.js
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
    
    const material = new THREE.MeshPhongMaterial({ 
        color: color,
        shininess: 100,
        specular: 0x111111
    });
    model = new THREE.Mesh(geometry, material);
    scene.add(model);
    camera.position.z = 4;
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

function hideModal() {
    document.getElementById('3d-modal').classList.remove('active');
    isRotating = true;
}
</script>
"""
)


def get_suggestions(search, limit=6):
    """Get similar item suggestions based on search query"""
    if not search:
        return []
    search = search.lower()
    suggestions = []

    for item in menu_items:
        name = item.get("name", "").lower()
        # Check for partial match, similar sounds, or related words
        if (
            search in name
            or any(s in name for s in search.split() if len(s) > 2)
            or any(name.startswith(s) for s in search.split() if len(s) > 2)
        ):
            suggestions.append(item)
            if len(suggestions) >= limit:
                break

    return suggestions


def filter_menu(category, search):
    filtered = menu_items

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

    # If no exact matches, show suggestions
    if not filtered and search:
        suggestions = get_suggestions(search, 6)
        if suggestions:
            html = f"""
            <div style="text-align:center;color:#ff6b35;padding:20px;font-size:16px;">
                No exact matches found. Showing suggestions:
            </div>
            <div class="menu-grid">"""
            for item in suggestions:
                html += f'''
                <div class="food-card">
                    <img src="{item["image"]}" alt="{item["name"]}">
                    <span class="badge">{item["category"]}</span>
                    <h3>{item["name"]}</h3>
                    <p class="desc">{item["description"][:50]}...</p>
                    <div class="price">Rs. {item["price"]}</div>
                    <button class="view-3d" onclick="showModal('{item["id"]}')">View 3D</button>
                </div>'''
            html += "</div>"
            return html

    if not filtered:
        return '<div style="text-align:center;color:#888;padding:40px;font-size:18px;">No dishes found</div>'

    html = '<div class="menu-grid">'
    for item in filtered:
        html += f'''
        <div class="food-card">
            <img src="{item["image"]}" alt="{item["name"]}">
            <span class="badge">{item["category"]}</span>
            <h3>{item["name"]}</h3>
            <p class="desc">{item["description"][:50]}...</p>
            <div class="price">Rs. {item["price"]}</div>
            <button class="view-3d" onclick="showModal('{item["id"]}')">View 3D</button>
        </div>'''
    html += "</div>"
    return html


with gr.Blocks(css=css, title="Restaurant Menu") as demo:
    gr.HTML(three_js)

    gr.HTML("""
        <div class="header">
            <h1>RESTAURANT MENU</h1>
            <p>Click on any dish to view 3D Model</p>
        </div>
        
        <div id="3d-modal" class="modal">
            <span class="modal-close" onclick="hideModal()">&times;</span>
            <div class="modal-content">
                <h2 id="modal-title"></h2>
                <div id="3d-container"></div>
                <p id="modal-desc" style="color:#aaa;margin:12px 0;font-size:14px;"></p>
                <p id="modal-price" style="color:#ff6b35;font-size:1.5em;font-weight:bold;"></p>
                <button class="view-3d" onclick="toggleRotation()" style="width:auto;padding:8px 25px;">Toggle Rotation</button>
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
