---
title: DIGITAL 3D MENU
emoji: 🍛
colorFrom: red
colorTo: blue
sdk: gradio
sdk_version: "4.0.0"
app_file: app.py
pinned: false
tags:
- food
- menu
- indian-cuisine
- gradio
- web-app
license: mit
---

# DIGITAL 3D MENU 🍛

Interactive Indian Food Menu for restaurants.

## Projects

### 1. Gradio App (Hugging Face)
- `app.py` - Gradio web interface
- `requirements.txt` - Dependencies

### 2. React Client (Local)
- `client/` - React + Vite frontend
- `server/` - Node.js Express API

## Running

**Gradio (Hugging Face):**
```bash
pip install gradio
python app.py
```

**React + Node:**
```bash
# Server
cd server && npm install && npm start

# Client  
cd client && npm install && npm run dev
```

## Food Categories

| Category | Items |
|----------|-------|
| Indian Biryani | Chicken Biryani |
| Indian Curries | Dal Makhani, Butter Chicken, Palak Paneer |
| Indian Tandoor | Paneer Tikka, Tandoori Chicken, Chicken Tikka |
| Indian Snacks | Samosa, Papdi Chaat |
| South Indian | Masala Dosa, Idli Sambar |
| Indian Desserts | Gulab Jamun, Rasgulla |

## License

MIT
