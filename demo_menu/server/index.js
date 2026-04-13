const express = require('express');
const cors = require('cors');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

const app = express();
const PORT = process.env.PORT || 5000;
const JWT_SECRET = 'digital-3d-menu-secret-2024';

app.use(cors());
app.use(express.json());

const foodsData = [
  { id: 'biryani', name: 'Chicken Biryani', price: 299, original_price: 399, description: 'Aromatic basmati rice with tender chicken, saffron, and traditional spices.', ingredients: ['Basmati Rice', 'Chicken', 'Saffron', 'Onions', 'Ginger', 'Garlic', 'Garam Masala', 'Mint', 'Coriander'], category: 'Indian Biryani', calories: 520, prep_time: '30 min', rating: 4.9, reviews: 234, badge: "Chef's Special", popular: true, image: 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=400', type: 'biryani' },
  { id: 'dal_makhani', name: 'Dal Makhani', price: 199, original_price: 249, description: 'Creamy black lentils slow-cooked with kidney beans, tomato, and aromatic spices.', ingredients: ['Black Lentils', 'Kidney Beans', 'Tomato', 'Cream', 'Butter', 'Garam Masala'], category: 'Indian Curries', calories: 320, prep_time: '25 min', rating: 4.8, reviews: 189, badge: 'Popular', popular: true, image: 'https://images.unsplash.com/photo-1546833999-b9f581a2026c?w=400', type: 'dal_makhani' },
  { id: 'paneer_tikka', name: 'Paneer Tikka', price: 279, original_price: 349, description: 'Cubes of cottage cheese marinated in yogurt and spices, grilled to perfection.', ingredients: ['Paneer', 'Yogurt', 'Ginger', 'Garlic', 'Garam Masala', 'Bell Peppers', 'Onions'], category: 'Indian Tandoor', calories: 380, prep_time: '20 min', rating: 4.7, reviews: 156, badge: 'Vegetarian', popular: true, image: 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=400', type: 'paneer_tikka' },
  { id: 'samosa', name: 'Crispy Samosa (3 pcs)', price: 99, original_price: 149, description: 'Golden fried pastries filled with spiced potatoes and peas.', ingredients: ['Flour', 'Potatoes', 'Peas', 'Cumin', 'Coriander', 'Ginger', 'Green Chili', 'Mint'], category: 'Indian Snacks', calories: 280, prep_time: '15 min', rating: 4.6, reviews: 312, badge: 'Bestseller', popular: true, image: 'https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400', type: 'samosa' },
  { id: 'naan', name: 'Garlic Naan', price: 59, original_price: 79, description: 'Soft and fluffy tandoor-baked bread topped with garlic and butter.', ingredients: ['All-Purpose Flour', 'Yeast', 'Yogurt', 'Garlic', 'Butter', 'Salt'], category: 'Indian Breads', calories: 180, prep_time: '10 min', rating: 4.9, reviews: 445, badge: 'Must Try', popular: true, image: 'https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400', type: 'naan' },
  { id: 'butter_chicken', name: 'Butter Chicken', price: 329, original_price: 399, description: 'Tender chicken in creamy tomato-based gravy with butter and fenugreek.', ingredients: ['Chicken', 'Tomato', 'Cream', 'Butter', 'Fenugreek', 'Garam Masala', 'Kashmiri Chili'], category: 'Indian Curries', calories: 480, prep_time: '25 min', rating: 4.9, reviews: 567, badge: 'Signature Dish', popular: true, image: 'https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=400', type: 'butter_chicken' },
  { id: 'masala_dosa', name: 'Masala Dosa', price: 199, original_price: 249, description: 'Crispy rice and lentil crepe filled with spiced potato filling.', ingredients: ['Rice', 'Urad Dal', 'Potatoes', 'Onions', 'Mustard Seeds', 'Curry Leaves', 'Coconut'], category: 'South Indian', calories: 290, prep_time: '20 min', rating: 4.7, reviews: 234, badge: 'Healthy', popular: true, image: 'https://images.unsplash.com/photo-1668236543090-82eba64ee968?w=400', type: 'dosa' },
  { id: 'idli_sambar', name: 'Idli Sambar (4 pcs)', price: 129, original_price: 169, description: 'Soft steamed rice cakes served with hot sambar and coconut chutney.', ingredients: ['Rice', 'Urad Dal', 'Toor Dal', 'Tamarind', 'Vegetables', 'Coconut', 'Mustard Seeds'], category: 'South Indian', calories: 220, prep_time: '15 min', rating: 4.6, reviews: 189, badge: 'Light & Healthy', popular: false, image: 'https://images.unsplash.com/photo-1668236543090-82eba64ee968?w=400', type: 'idli' },
  { id: 'palak_paneer', name: 'Palak Paneer', price: 249, original_price: 299, description: 'Cottage cheese in smooth and creamy spinach gravy.', ingredients: ['Paneer', 'Spinach', 'Onion', 'Tomato', 'Cream', 'Garlic', 'Ginger', 'Garam Masala'], category: 'Indian Curries', calories: 340, prep_time: '20 min', rating: 4.7, reviews: 167, badge: 'Healthy Choice', popular: false, image: 'https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400', type: 'palak_paneer' },
  { id: 'tandoori_chicken', name: 'Tandoori Chicken Full', price: 449, original_price: 549, description: 'Whole chicken marinated in yogurt and spices, roasted in tandoor.', ingredients: ['Chicken', 'Yogurt', 'Ginger', 'Garlic', 'Kashmiri Chili', 'Garam Masala', 'Lemon', 'Mint'], category: 'Indian Tandoor', calories: 420, prep_time: '35 min', rating: 4.8, reviews: 289, badge: 'Party Favorite', popular: true, image: 'https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=400', type: 'tandoori_chicken' },
  { id: 'chaat', name: 'Papdi Chaat', price: 149, original_price: 199, description: 'Crispy flour chips topped with potatoes, chickpeas, yogurt, and tangy chutneys.', ingredients: ['Flour Chips', 'Potatoes', 'Chickpeas', 'Yogurt', 'Tamarind Chutney', 'Green Chutney', 'Sev', 'Pomegranate'], category: 'Indian Snacks', calories: 310, prep_time: '10 min', rating: 4.8, reviews: 345, badge: 'Street Food', popular: true, image: 'https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400', type: 'chaat' },
  { id: 'lassi', name: 'Sweet Lassi', price: 79, original_price: 99, description: 'Creamy yogurt drink blended with sugar and cardamom.', ingredients: ['Yogurt', 'Sugar', 'Cardamom', 'Water', 'Ice'], category: 'Indian Drinks', calories: 150, prep_time: '5 min', rating: 4.7, reviews: 234, badge: 'Refreshing', popular: true, image: 'https://images.unsplash.com/photo-1626200419199-391ae4be7a41?w=400', type: 'lassi' },
  { id: 'gulab_jamun', name: 'Gulab Jamun (4 pcs)', price: 99, original_price: 129, description: 'Deep-fried milk dumplings soaked in rose-flavored sugar syrup.', ingredients: ['Milk Powder', 'Flour', 'Sugar', 'Rose Water', 'Cardamom', 'Ghee'], category: 'Indian Desserts', calories: 280, prep_time: '15 min', rating: 4.9, reviews: 456, badge: 'Dessert Favorite', popular: true, image: 'https://images.unsplash.com/photo-1627308595229-7830a5c91f9f?w=400', type: 'gulab_jamun' },
  { id: 'rasgulla', name: 'Rasgulla (5 pcs)', price: 99, original_price: 129, description: 'Spongy cottage cheese balls soaked in light sugar syrup.', ingredients: ['Cottage Cheese', 'Sugar', 'Rose Water', 'Cardamom'], category: 'Indian Desserts', calories: 180, prep_time: '20 min', rating: 4.8, reviews: 289, badge: 'Light Dessert', popular: true, image: 'https://images.unsplash.com/photo-1627308595229-7830a5c91f9f?w=400', type: 'rasgulla' },
  { id: 'chicken_tikka', name: 'Chicken Tikka Kebab', price: 299, original_price: 379, description: 'Tender chicken pieces marinated in spiced yogurt, grilled in tandoor.', ingredients: ['Chicken', 'Yogurt', 'Ginger', 'Garlic', 'Kashmiri Chili', 'Garam Masala', 'Bell Peppers', 'Onions'], category: 'Indian Tandoor', calories: 320, prep_time: '25 min', rating: 4.8, reviews: 234, badge: 'Kebab Special', popular: true, image: 'https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=400', type: 'chicken_tikka' },
  { id: 'manchurian', name: 'Vegetable Manchurian', price: 229, original_price: 279, description: 'Crispy vegetable balls in spicy Indo-Chinese gravy.', ingredients: ['Cabbage', 'Carrots', 'Beans', 'Soy Sauce', 'Garlic', 'Ginger', 'Green Chili', 'Corn Flour'], category: 'Indo-Chinese', calories: 340, prep_time: '20 min', rating: 4.6, reviews: 178, badge: 'Fusion', popular: false, image: 'https://images.unsplash.com/photo-1529692236671-f1f6cf9683ba?w=400', type: 'manchurian' }
];

const promotions = [
  { id: 1, title: '25% OFF Biryani!', desc: 'Special discount on all biryani varieties', code: 'BIRYANI25', discount: 25, expires: '2026-04-15' },
  { id: 2, title: 'Free Delivery', desc: 'Free delivery on orders over ₹500', code: 'FREESHIP', discount: 100, min_order: 500, expires: '2026-04-20' },
  { id: 3, title: '15% OFF First Order', desc: 'New user special discount', code: 'WELCOME15', discount: 15, expires: '2026-05-01' }
];

const categories = [
  { id: 'all', name: 'All', icon: '🍽️' },
  { id: 'Indian Biryani', name: 'Biryani', icon: '🍚' },
  { id: 'Indian Curries', name: 'Curries', icon: '🍛' },
  { id: 'Indian Tandoor', name: 'Tandoor', icon: '🔥' },
  { id: 'Indian Snacks', name: 'Snacks', icon: '🥟' },
  { id: 'Indian Breads', name: 'Breads', icon: '🫓' },
  { id: 'South Indian', name: 'South Indian', icon: '🥞' },
  { id: 'Indian Drinks', name: 'Drinks', icon: '🥛' },
  { id: 'Indian Desserts', name: 'Desserts', icon: '🍰' },
  { id: 'Indo-Chinese', name: 'Indo-Chinese', icon: '🍜' }
];

const users = new Map();
const orders = [];
let orderIdCounter = 1;

const authenticate = (req, res, next) => {
  const authHeader = req.headers.authorization;
  if (!authHeader) return res.status(401).json({ error: 'No token provided' });
  
  const token = authHeader.split(' ')[1];
  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    req.userId = decoded.userId;
    next();
  } catch (err) {
    return res.status(401).json({ error: 'Invalid token' });
  }
};

app.get('/api/foods', (req, res) => {
  const { category, search } = req.query;
  let filtered = [...foodsData];
  
  if (category && category !== 'all') {
    filtered = filtered.filter(f => f.category === category);
  }
  if (search) {
    const s = search.toLowerCase();
    filtered = filtered.filter(f => f.name.toLowerCase().includes(s) || f.description.toLowerCase().includes(s));
  }
  
  res.json(filtered);
});

app.get('/api/foods/:id', (req, res) => {
  const food = foodsData.find(f => f.id === req.params.id);
  if (food) res.json(food);
  else res.status(404).json({ error: 'Food not found' });
});

app.get('/api/promotions', (req, res) => {
  res.json(promotions);
});

app.get('/api/categories', (req, res) => {
  res.json(categories);
});

app.post('/api/apply-promo', (req, res) => {
  const { code } = req.body;
  const promo = promotions.find(p => p.code === code.toUpperCase());
  if (promo) res.json({ success: true, promo });
  else res.json({ success: false, error: 'Invalid promo code' });
});

app.post('/api/register', (req, res) => {
  const { username, email, password } = req.body;
  
  if (Array.from(users.values()).some(u => u.email === email)) {
    return res.status(400).json({ success: false, error: 'Email already exists' });
  }
  
  const userId = Date.now();
  const hashedPassword = bcrypt.hashSync(password, 10);
  const user = { id: userId, username, email, password: hashedPassword };
  users.set(userId, user);
  
  const token = jwt.sign({ userId }, JWT_SECRET, { expiresIn: '7d' });
  res.json({ success: true, token, user: { id: userId, username, email } });
});

app.post('/api/login', (req, res) => {
  const { email, password } = req.body;
  
  const user = Array.from(users.values()).find(u => u.email === email);
  if (!user || !bcrypt.compareSync(password, user.password)) {
    return res.status(401).json({ success: false, error: 'Invalid credentials' });
  }
  
  const token = jwt.sign({ userId: user.id }, JWT_SECRET, { expiresIn: '7d' });
  res.json({ success: true, token, user: { id: user.id, username: user.username, email: user.email } });
});

app.get('/api/profile', authenticate, (req, res) => {
  const user = users.get(req.userId);
  if (user) res.json({ id: user.id, username: user.username, email: user.email });
  else res.status(404).json({ error: 'User not found' });
});

app.put('/api/profile', authenticate, (req, res) => {
  const { username } = req.body;
  const user = users.get(req.userId);
  if (user) {
    user.username = username;
    res.json({ success: true });
  } else {
    res.status(404).json({ error: 'User not found' });
  }
});

app.get('/api/orders', authenticate, (req, res) => {
  const userOrders = orders.filter(o => o.user_id === req.userId);
  res.json(userOrders);
});

app.post('/api/orders', authenticate, (req, res) => {
  const { items, total, address, notes } = req.body;
  const order = {
    id: orderIdCounter++,
    user_id: req.userId,
    items,
    total,
    address,
    notes,
    status: 'pending',
    created_at: new Date().toISOString()
  };
  orders.push(order);
  res.json({ success: true, orderId: order.id });
});

app.get('/api/favorites', authenticate, (req, res) => {
  const user = users.get(req.userId);
  res.json(user?.favorites || []);
});

app.post('/api/favorites', authenticate, (req, res) => {
  const { foodId } = req.body;
  const user = users.get(req.userId);
  if (user) {
    if (!user.favorites) user.favorites = [];
    if (!user.favorites.includes(foodId)) {
      user.favorites.push(foodId);
    }
    res.json({ success: true });
  } else {
    res.status(404).json({ error: 'User not found' });
  }
});

app.delete('/api/favorites', authenticate, (req, res) => {
  const { foodId } = req.query;
  const user = users.get(req.userId);
  if (user && user.favorites) {
    user.favorites = user.favorites.filter(f => f !== foodId);
  }
  res.json({ success: true });
});

async function startServer() {
  app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
  });
}

startServer();
