import React, { useState, useEffect, useRef, Suspense } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls, Environment } from '@react-three/drei';

const API_URL = 'http://localhost:5000/api';

// Food Colors for 3D models
const foodColors = {
  biryani: { rice: '#ffd700', chicken: '#cd853f', spices: '#ff5722', saffron: '#ffd700', onion: '#8b4513' },
  dal_makhani: { dal: '#2d2d2d', cream: '#fffacd', tomato: '#dc143c', butter: '#ff8c00' },
  paneer_tikka: { paneer: '#fffacd', masala: '#ff5722', pepper: '#228b22', onion: '#ffffff' },
  samosa: { dough: '#d4a056', potato: '#daa520', peas: '#228b22', green: '#4a9c2d' },
  naan: { dough: '#d4a056', garlic: '#ffffff', butter: '#ff8c00' },
  butter_chicken: { chicken: '#cd853f', gravy: '#ff5722', cream: '#fffacd', butter: '#ff8c00' },
  dosa: { crepe: '#d4a056', potato: '#daa520', sambar: '#8b4513' },
  idli: { idli: '#ffffff', sambar: '#8b4513', chutney: '#228b22' },
  palak_paneer: { paneer: '#fffacd', spinach: '#228b22', onion: '#ffffff' },
  tandoori_chicken: { chicken: '#cd853f', masala: '#ff5722', lemon: '#ffd700' },
  chaat: { chips: '#d4a056', potato: '#daa520', yogurt: '#ffffff', chutney: '#ff5722', sev: '#ffd700' },
  lassi: { lassi: '#fffacd', sugar: '#ffffff' },
  gulab_jamun: { jamun: '#8b4513', syrup: '#ff69b4' },
  rasgulla: { rasgulla: '#ffffff', syrup: '#fffacd' },
  chicken_tikka: { chicken: '#cd853f', masala: '#ff5722', pepper: '#228b22' },
  Manchurian: { balls: '#daa520', gravy: '#8b0000', garlic: '#ffffff', chili: '#ff0000' }
};

// Food3D Component
function FoodModel({ type }) {
  const groupRef = useRef();
  const colors = foodColors[type] || { main: '#ff5722' };
  
  useFrame((state) => {
    if (groupRef.current) {
      groupRef.current.position.y = Math.sin(state.clock.elapsedTime * 1.5) * 0.03;
      groupRef.current.rotation.y += 0.005;
    }
  });

  return (
    <group ref={groupRef} rotation={[0.1, 0, 0]}>
      {type === 'biryani' && (
        <>
          <mesh position={[0, 0.1, 0]}>
            <sphereGeometry args={[0.55, 32, 16, 0, Math.PI * 2, 0, Math.PI / 2]} />
            <meshStandardMaterial color="#2d2d2d" roughness={0.3} />
          </mesh>
          <mesh position={[0, 0.2, 0]}>
            <cylinderGeometry args={[0.45, 0.5, 0.25, 32]} />
            <meshStandardMaterial color={colors.rice} roughness={0.6} />
          </mesh>
        </>
      )}
      {type === 'dal_makhani' && (
        <>
          <mesh position={[0, 0.1, 0]}>
            <sphereGeometry args={[0.5, 32, 16, 0, Math.PI * 2, 0, Math.PI / 2]} />
            <meshStandardMaterial color="#2d2d2d" roughness={0.3} />
          </mesh>
          <mesh position={[0, 0.18, 0]}>
            <cylinderGeometry args={[0.4, 0.45, 0.2, 32]} />
            <meshStandardMaterial color={colors.dal} roughness={0.4} />
          </mesh>
        </>
      )}
      {type === 'butter_chicken' && (
        <>
          <mesh position={[0, 0.1, 0]}>
            <sphereGeometry args={[0.55, 32, 16, 0, Math.PI * 2, 0, Math.PI / 2]} />
            <meshStandardMaterial color="#2d2d2d" roughness={0.3} />
          </mesh>
          <mesh position={[0, 0.18, 0]}>
            <cylinderGeometry args={[0.45, 0.5, 0.25, 32]} />
            <meshStandardMaterial color={colors.gravy} roughness={0.4} />
          </mesh>
        </>
      )}
      {type === 'samosa' && (
        <>
          <mesh position={[-0.12, 0, 0]} rotation={[0, Math.PI / 4, 0]}>
            <coneGeometry args={[0.22, 0.45, 4]} />
            <meshStandardMaterial color={colors.dough} roughness={0.7} />
          </mesh>
          <mesh position={[0.12, 0, 0]} rotation={[0, -Math.PI / 4, 0]}>
            <coneGeometry args={[0.22, 0.45, 4]} />
            <meshStandardMaterial color={colors.dough} roughness={0.7} />
          </mesh>
        </>
      )}
      {type === 'naan' && (
        <mesh position={[0, 0.08, 0]} rotation={[Math.PI, 0.2, 0]}>
          <sphereGeometry args={[0.35, 32, 16, 0, Math.PI * 2, 0, Math.PI / 2]} />
          <meshStandardMaterial color={colors.dough} roughness={0.8} />
        </mesh>
      )}
      {type === 'dosa' && (
        <>
          <mesh position={[0, 0.04, 0]}>
            <cylinderGeometry args={[0.55, 0.55, 0.04, 32]} />
            <meshStandardMaterial color={colors.crepe} roughness={0.6} />
          </mesh>
          <mesh position={[0.18, 0.08, 0]}>
            <cylinderGeometry args={[0.22, 0.28, 0.06, 32]} />
            <meshStandardMaterial color={colors.potato} roughness={0.5} />
          </mesh>
        </>
      )}
      {type === 'gulab_jamun' && (
        <>
          {[0, 1, 2, 3].map((i) => (
            <mesh key={i} position={[
              Math.cos(i * Math.PI / 2) * 0.08,
              i < 2 ? 0.08 : -0.02,
              Math.sin(i * Math.PI / 2) * 0.08
            ]}>
              <sphereGeometry args={[0.1, 16, 16]} />
              <meshStandardMaterial color={colors.jamun} roughness={0.5} />
            </mesh>
          ))}
          <mesh position={[0, 0.015, 0]}>
            <cylinderGeometry args={[0.3, 0.3, 0.06, 32]} />
            <meshStandardMaterial color={colors.syrup} roughness={0.3} transparent opacity={0.5} />
          </mesh>
        </>
      )}
      {type === 'lassi' && (
        <>
          <mesh>
            <cylinderGeometry args={[0.18, 0.14, 0.45, 32]} />
            <meshStandardMaterial color="#ffffff" roughness={0.1} transparent opacity={0.5} />
          </mesh>
          <mesh position={[0, -0.04, 0]}>
            <cylinderGeometry args={[0.16, 0.12, 0.3, 32]} />
            <meshStandardMaterial color={colors.lassi} roughness={0.4} />
          </mesh>
        </>
      )}
      {/* Default */}
      <mesh>
        <sphereGeometry args={[0.45, 32, 32]} />
        <meshStandardMaterial color={colors.main || '#ff5722'} roughness={0.5} />
      </mesh>
    </group>
  );
}

// FoodCard Component
function FoodCard({ food, onView3D, onAddToCart }) {
  return (
    <div className="glass-card rounded-2xl p-3 cursor-pointer" onClick={() => onView3D(food)}>
      <div className="relative rounded-xl overflow-hidden mb-3 aspect-square">
        <img src={food.image} alt={food.name} className="w-full h-full object-cover food-img" />
        {food.badge && (
          <div className="absolute top-2 left-2 px-2 py-1 rounded-full text-xs font-semibold bg-gradient-to-r from-orange-500 to-orange-400 text-white">
            {food.badge}
          </div>
        )}
        <button 
          onClick={(e) => { e.stopPropagation(); onView3D(food); }}
          className="absolute bottom-2 right-2 w-10 h-10 rounded-full bg-orange-500 flex items-center justify-center text-white hover:scale-110 transition shadow-lg"
        >
          🎮
        </button>
      </div>
      <div className="space-y-2">
        <div className="flex items-start justify-between">
          <h3 className="text-base font-semibold">{food.name}</h3>
          <div className="flex items-center gap-1 text-sm">
            <span className="text-yellow-500">★</span>
            <span>{food.rating}</span>
          </div>
        </div>
        <p className="text-gray-400 text-xs line-clamp-2">{food.description}</p>
        <div className="flex items-center justify-between pt-1">
          <div className="flex items-center gap-2">
            <span className="text-xl font-bold text-orange-500">₹{food.price}</span>
            {food.original_price && (
              <span className="text-sm text-gray-500 line-through">₹{food.original_price}</span>
            )}
          </div>
          <button 
            onClick={(e) => { e.stopPropagation(); onAddToCart(food); }}
            className="px-3 py-1.5 rounded-full btn-primary text-sm font-semibold"
          >
            Add +
          </button>
        </div>
      </div>
    </div>
  );
}

// Modal3D Component
function Modal3D({ food, onClose, onAddToCart }) {
  return (
    <div className="fixed inset-0 z-50" style={{ display: food ? 'block' : 'none' }}>
      <div className="absolute inset-0 bg-black/90 backdrop-blur-sm" onClick={onClose}></div>
      <div className="absolute inset-4 sm:inset-8 lg:inset-16 bg-card rounded-3xl border border-orange-500/20 modal-3d overflow-hidden flex flex-col">
        <div className="flex items-center justify-between p-4 border-b border-white/10">
          <div>
            <h2 className="text-2xl font-bold font-display">{food?.name}</h2>
            <p className="text-gray-400 text-sm">{food?.description}</p>
          </div>
          <button onClick={onClose} className="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center text-2xl hover:rotate-90 transition">&times;</button>
        </div>
        <div className="flex-1 relative">
          <Canvas camera={{ position: [0, 1, 4], fov: 45 }}>
            <ambientLight intensity={0.6} />
            <directionalLight position={[2, 3, 2]} intensity={0.8} />
            <directionalLight position={[-2, 1, -2]} intensity={0.4} color="#ff5722" />
            <pointLight position={[0, 2, -3]} intensity={0.5} />
            <Suspense fallback={null}>
              <FoodModel type={food?.type || 'biryani'} />
            </Suspense>
            <OrbitControls autoRotate autoRotateSpeed={1.5} enableDamping dampingFactor={0.05} minDistance={2} maxDistance={7} />
          </Canvas>
        </div>
        <div className="p-4 border-t border-white/10 flex items-center justify-between">
          <div className="flex items-center gap-4 text-sm text-gray-400">
            <span>🖱️ Drag to rotate</span>
            <span>🔍 Scroll to zoom</span>
          </div>
          <button onClick={() => { onAddToCart(food); onClose(); }} className="px-6 py-3 rounded-full btn-primary font-semibold">
            Add to Cart - ₹{food?.price}
          </button>
        </div>
      </div>
    </div>
  );
}

// Main App Component
function App() {
  const [foods, setFoods] = useState([]);
  const [categories, setCategories] = useState([]);
  const [promotions, setPromotions] = useState([]);
  const [cart, setCart] = useState([]);
  const [selectedFood, setSelectedFood] = useState(null);
  const [category, setCategory] = useState('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [showSearch, setShowSearch] = useState(false);
  const [showCart, setShowCart] = useState(false);
  const [showToast, setShowToast] = useState(false);
  const [toastMessage, setToastMessage] = useState('');
  const [appliedPromo, setAppliedPromo] = useState(null);
  const [user, setUser] = useState(null);
  const [showAuthModal, setShowAuthModal] = useState(false);
  const [authMode, setAuthMode] = useState('login');
  const [authForm, setAuthForm] = useState({ username: '', email: '', password: '' });

  useEffect(() => {
    fetchData();
    const savedUser = localStorage.getItem('user');
    if (savedUser) setUser(JSON.parse(savedUser));
  }, []);

  const fetchData = async () => {
    try {
      const [foodsRes, catsRes, promosRes] = await Promise.all([
        fetch(`${API_URL}/foods`),
        fetch(`${API_URL}/categories`),
        fetch(`${API_URL}/promotions`)
      ]);
      setFoods(await foodsRes.json());
      setCategories(await catsRes.json());
      setPromotions(await promosRes.json());
    } catch (err) {
      console.error('Failed to fetch data:', err);
    }
  };

  const filteredFoods = foods.filter(f => {
    const matchesCategory = category === 'all' || f.category === category;
    const matchesSearch = !searchQuery || f.name.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesCategory && matchesSearch;
  });

  const showToastMessage = (msg) => {
    setToastMessage(msg);
    setShowToast(true);
    setTimeout(() => setShowToast(false), 2000);
  };

  const addToCart = (food) => {
    setCart([...cart, food]);
    showToastMessage(`Added ${food.name} to cart!`);
  };

  const removeFromCart = (index) => {
    const newCart = [...cart];
    newCart.splice(index, 1);
    setCart(newCart);
  };

  const getCartTotal = () => {
    const subtotal = cart.reduce((sum, item) => sum + item.price, 0);
    let discount = 0;
    if (appliedPromo) {
      discount = appliedPromo.discount === 100 ? subtotal : subtotal * (appliedPromo.discount / 100);
    }
    return { subtotal, discount, total: subtotal - discount };
  };

  const applyPromoCode = async () => {
    const code = document.getElementById('promoCode').value.toUpperCase();
    try {
      const res = await fetch(`${API_URL}/apply-promo`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code })
      });
      const data = await res.json();
      if (data.success) {
        setAppliedPromo(data.promo);
        showToastMessage(`Promo ${data.promo.code} applied!`);
      } else {
        showToastMessage('Invalid promo code');
      }
    } catch (err) {
      showToastMessage('Invalid promo code');
    }
  };

  const handleCheckout = async () => {
    if (!user) {
      setShowAuthModal(true);
      return;
    }
    const { total } = getCartTotal();
    try {
      const res = await fetch(`${API_URL}/orders`, {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        },
        body: JSON.stringify({ items: cart, total, address: '', notes: '' })
      });
      if (res.ok) {
        showToastMessage('Order placed successfully!');
        setCart([]);
        setAppliedPromo(null);
        setShowCart(false);
      }
    } catch (err) {
      showToastMessage('Checkout failed');
    }
  };

  const handleAuth = async () => {
    const endpoint = authMode === 'login' ? 'login' : 'register';
    try {
      const res = await fetch(`${API_URL}/${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(authForm)
      });
      const data = await res.json();
      if (data.success) {
        localStorage.setItem('token', data.token);
        localStorage.setItem('user', JSON.stringify(data.user));
        setUser(data.user);
        setShowAuthModal(false);
        showToastMessage(`Welcome ${data.user.username}!`);
      } else {
        showToastMessage(data.error);
      }
    } catch (err) {
      showToastMessage('Auth failed');
    }
  };

  return (
    <div className="min-h-screen bg-dark">
      {/* Navigation */}
      <nav className="fixed top-0 left-0 right-0 z-50 glass border-b border-orange-500/20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16 sm:h-20">
            <a href="/" className="flex items-center gap-3 group">
              <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-orange-500 to-orange-400 flex items-center justify-center text-2xl font-bold font-display group-hover:scale-110 transition">D</div>
              <span className="text-xl sm:text-2xl font-bold font-display">DIGITAL <span className="text-orange-500 glow-text">3D MENU</span></span>
            </a>
            <div className="hidden md:flex items-center gap-6">
              <a href="#menu" className="text-sm hover:text-orange-500 transition">Menu</a>
              <a href="#deals" className="text-sm hover:text-orange-500 transition">Deals</a>
            </div>
            <div className="flex items-center gap-3">
              <button onClick={() => setShowSearch(!showSearch)} className="p-2 rounded-full hover:bg-white/10 transition">
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
              </button>
              {user ? (
                <div className="flex items-center gap-3">
                  <span className="text-sm text-gray-400 hidden sm:block">{user.username}</span>
                  <button onClick={() => { localStorage.clear(); setUser(null); showToastMessage('Logged out!'); }} className="text-orange-500 text-sm hover:underline">Logout</button>
                </div>
              ) : (
                <>
                  <button onClick={() => setShowAuthModal(true)} className="px-4 py-2 rounded-full text-sm hover:bg-white/10 transition">Login</button>
                  <button onClick={() => { setAuthMode('register'); setShowAuthModal(true); }} className="px-5 py-2.5 rounded-full btn-primary text-sm font-semibold">Sign Up</button>
                </>
              )}
              <button onClick={() => setShowCart(true)} className="relative p-2.5 rounded-full bg-white/10 hover:bg-white/20 transition">
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"/></svg>
                <span className="absolute -top-1 -right-1 w-5 h-5 rounded-full bg-red-500 text-xs flex items-center justify-center font-bold">{cart.length}</span>
              </button>
            </div>
          </div>
        </div>
      </nav>

      {/* Search Modal */}
      {showSearch && (
        <div className="fixed inset-0 z-50" style={{ display: showSearch ? 'block' : 'none' }}>
          <div className="absolute inset-0 bg-black/80 backdrop-blur-sm" onClick={() => setShowSearch(false)}></div>
          <div className="absolute top-24 left-1/2 -translate-x-1/2 w-full max-w-2xl px-4">
            <div className="glass rounded-2xl p-4" style={{ boxShadow: '0 0 30px rgba(255,87,34,0.3)' }}>
              <input 
                type="text" 
                placeholder="Search for food..." 
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full bg-transparent text-xl outline-none placeholder-gray-500 text-white"
                autoFocus
              />
            </div>
          </div>
        </div>
      )}

      {/* Hero Section */}
      <section className="relative pt-24 sm:pt-32 pb-16 sm:pb-24 hero-gradient mesh-bg">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-orange-500/20 text-orange-500 text-sm mb-6">
            <span className="w-2 h-2 rounded-full bg-orange-500"></span> Free Delivery on orders over ₹500
          </div>
          <h1 className="text-4xl sm:text-6xl lg:text-7xl font-bold font-display mb-6">
            Taste the <span className="text-orange-500 glow-text">Future</span> of Food
          </h1>
          <p className="text-lg sm:text-xl text-gray-400 max-w-2xl mx-auto mb-8">
            Explore our interactive 3D menu. Click any dish to view it in stunning 3D and order instantly!
          </p>
          <a href="#menu" className="inline-block px-8 py-4 rounded-full btn-primary text-lg font-semibold">
            🍽️ Explore Menu
          </a>
        </div>
      </section>

      {/* Promotions */}
      <section id="deals" className="py-6 border-y border-orange-500/10">
        <div className="max-w-7xl mx-auto px-4 overflow-x-auto flex gap-4">
          {promotions.map(promo => (
            <div key={promo.id} className="flex-shrink-0 rounded-2xl p-4 cursor-pointer hover:scale-105 transition bg-gradient-to-r from-orange-500/20 to-orange-400/10 border border-orange-500/30" onClick={() => { setShowCart(true); document.getElementById('promoCode').value = promo.code; }}>
              <div className="flex items-center gap-3">
                <div className="w-12 h-12 rounded-xl bg-orange-500/30 flex items-center justify-center text-2xl">🎁</div>
                <div><h3 className="font-semibold text-orange-500">{promo.title}</h3><p className="text-sm text-gray-400">{promo.desc}</p></div>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Categories */}
      <section className="py-6">
        <div className="max-w-7xl mx-auto px-4">
          <div className="flex gap-3 overflow-x-auto">
            {categories.map(cat => (
              <button key={cat.id} onClick={() => setCategory(cat.id)} className={`category-btn flex-shrink-0 px-5 py-2.5 rounded-full text-sm font-medium whitespace-nowrap ${category === cat.id ? 'active' : ''}`}>
                <span>{cat.icon}</span> {cat.name}
              </button>
            ))}
          </div>
        </div>
      </section>

      {/* Food Grid */}
      <section id="menu" className="py-8">
        <div className="max-w-7xl mx-auto px-4">
          <h2 className="text-2xl sm:text-3xl font-bold font-display mb-6">Our <span className="text-orange-500">Menu</span></h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
            {filteredFoods.map(food => (
              <FoodCard key={food.id} food={food} onView3D={setSelectedFood} onAddToCart={addToCart} />
            ))}
          </div>
        </div>
      </section>

      {/* 3D Modal */}
      <Modal3D food={selectedFood} onClose={() => setSelectedFood(null)} onAddToCart={addToCart} />

      {/* Cart Sidebar */}
      <div className={`fixed right-0 top-0 h-full w-full max-w-md bg-dark border-l border-orange-500/20 transform transition-transform z-50 ${showCart ? '' : 'translate-x-full'}`}>
        <div className="h-full flex flex-col">
          <div className="p-5 border-b border-white/10 flex items-center justify-between">
            <h2 className="text-xl font-bold font-display">Your Cart</h2>
            <button onClick={() => setShowCart(false)} className="w-10 h-10 rounded-full hover:bg-white/10 flex items-center justify-center text-2xl">&times;</button>
          </div>
          <div className="flex-1 overflow-y-auto p-5 space-y-3">
            {cart.length === 0 ? (
              <p className="text-center text-gray-400 py-12">Your cart is empty</p>
            ) : (
              cart.map((item, i) => (
                <div key={i} className="flex items-center gap-3 p-3 rounded-xl bg-white/5">
                  <img src={item.image} alt={item.name} className="w-14 h-14 rounded-lg object-cover" />
                  <div className="flex-1"><h4 className="font-semibold text-sm">{item.name}</h4><p className="text-orange-500">₹{item.price}</p></div>
                  <button onClick={() => removeFromCart(i)} className="text-red-500 text-xl">&times;</button>
                </div>
              ))
            )}
          </div>
          <div className="p-5 border-t border-white/10 space-y-3">
            <div className="flex gap-2">
              <input type="text" id="promoCode" placeholder="Promo code" className="flex-1 px-4 py-2.5 rounded-xl bg-white/10 border border-white/10 focus:border-orange-500 outline-none text-sm" />
              <button onClick={applyPromoCode} className="px-4 py-2.5 rounded-xl bg-orange-500/20 text-orange-500 font-semibold text-sm hover:bg-orange-500/30 transition">Apply</button>
            </div>
            <div className="flex justify-between text-base"><span>Subtotal</span><span>₹{getCartTotal().subtotal}</span></div>
            {appliedPromo && <div className="flex justify-between text-base text-green-500"><span>Discount</span><span>-₹{getCartTotal().discount.toFixed(0)}</span></div>}
            <div className="flex justify-between text-xl font-bold"><span>Total</span><span className="text-orange-500">₹{getCartTotal().total.toFixed(0)}</span></div>
            <button onClick={handleCheckout} className="w-full py-3.5 rounded-xl btn-primary text-base font-semibold">Checkout</button>
          </div>
        </div>
      </div>

      {/* Auth Modal */}
      {showAuthModal && (
        <div className="fixed inset-0 z-50">
          <div className="absolute inset-0 bg-black/80 backdrop-blur-sm" onClick={() => setShowAuthModal(false)}></div>
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-md p-8 rounded-3xl glass border border-orange-500/20">
            <button onClick={() => setShowAuthModal(false)} className="absolute top-4 right-4 text-2xl">&times;</button>
            <h2 className="text-3xl font-bold font-display text-center mb-2">{authMode === 'login' ? 'Welcome Back' : 'Create Account'}</h2>
            <p className="text-gray-400 text-center mb-8">{authMode === 'login' ? 'Sign in to continue' : 'Join thousands of food lovers'}</p>
            {authMode === 'register' && (
              <input type="text" placeholder="Full name" value={authForm.username} onChange={(e) => setAuthForm({...authForm, username: e.target.value})} className="w-full p-4 rounded-xl bg-white/5 border border-white/10 focus:border-orange-500 outline-none mb-4" />
            )}
            <input type="email" placeholder="Email" value={authForm.email} onChange={(e) => setAuthForm({...authForm, email: e.target.value})} className="w-full p-4 rounded-xl bg-white/5 border border-white/10 focus:border-orange-500 outline-none mb-4" />
            <input type="password" placeholder="Password" value={authForm.password} onChange={(e) => setAuthForm({...authForm, password: e.target.value})} className="w-full p-4 rounded-xl bg-white/5 border border-white/10 focus:border-orange-500 outline-none mb-6" />
            <button onClick={handleAuth} className="w-full py-4 rounded-xl btn-primary font-semibold mb-4">
              {authMode === 'login' ? 'Sign In' : 'Create Account'}
            </button>
            <p className="text-center text-gray-400">
              {authMode === 'login' ? "Don't have an account? " : 'Already have an account? '}
              <button onClick={() => setAuthMode(authMode === 'login' ? 'register' : 'login')} className="text-orange-500 font-semibold">
                {authMode === 'login' ? 'Sign Up' : 'Sign In'}
              </button>
            </p>
          </div>
        </div>
      )}

      {/* Toast */}
      <div className={`fixed bottom-6 left-1/2 -translate-x-1/2 px-6 py-3 rounded-full bg-green-500 text-white font-semibold transform transition-all duration-300 z-50 ${showToast ? '' : '-translate-y-20 opacity-0'}`}>
        {toastMessage}
      </div>
    </div>
  );
}

export default App;
