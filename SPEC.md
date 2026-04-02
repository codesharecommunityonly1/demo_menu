# 3D Product Showcase Menu - Specification

## Project Overview
- **Project Name**: 3D Food Showcase
- **Type**: Interactive single-page web application
- **Core Functionality**: A visually stunning 3D food menu where users can rotate, zoom, and tap on 3D food models to see prices and ingredients
- **Target Users**: Food shops, restaurants, online food retailers

## Visual & Rendering Specification

### Scene Setup
- **Camera**: Perspective camera with orbit controls for rotation/zoom
- **Lighting**:
  - Soft ambient light (warm white, intensity 0.4)
  - Main directional light (soft white, intensity 0.8, casting shadows)
  - Rim light for product highlights (subtle, from behind)
- **Environment**: Dark, elegant background with subtle gradient (deep charcoal to black)
- **Fog**: None (clean product visibility)

### Materials & Effects
- **Food Materials**: PBR-based with subtle subsurface scattering simulation for realism
- **Hover Effect**: Gentle glow/bloom on hover
- **Selection Effect**: Dramatic spotlight + info panel slide-in
- **Post-processing**: Subtle bloom for highlights, vignette for focus

### Color Palette
- **Primary Background**: #0a0a0a (near black)
- **Accent**: #ff6b35 (warm orange - appetizing)
- **Secondary Accent**: #f7c548 (golden yellow)
- **Text**: #ffffff (white), #e0e0e0 (light gray)
- **Panel Background**: rgba(15, 15, 15, 0.95)

### Typography
- **Primary Font**: "Playfair Display" (elegant headings)
- **Secondary Font**: "DM Sans" (clean body text)

## 3D Assets (Procedural)
Since we can't load actual 3D models, we'll create stylized geometric representations:
- **Burger**: Layered cylinder stack (bun, patty, lettuce, tomato, cheese)
- **Pizza**: Flat cylinder with segmented toppings
- **Sushi Roll**: Cylinder with rice/seaweed/filling
- **Donut**: Torus with frosting and sprinkles
- **Coffee Cup**: Cylinder with handle
- **Ice Cream**: Cone with sphere scoops

## Interaction Specification

### Controls
- **Orbit**: Click and drag to rotate around food
- **Zoom**: Mouse wheel to zoom in/out
- **Select**: Click on food item to open details panel
- **Close Panel**: Click X or click outside panel

### UI Elements
1. **Header**: Restaurant name, subtle tagline
2. **Food Grid**: 3D models displayed in elegant cards
3. **Detail Panel**: Slides in from right showing:
   - Food name (large)
   - Price (prominent, orange accent)
   - Description
   - Ingredients list
   - "Add to Cart" button
4. **Cart Indicator**: Shows item count in corner

## Animation Specification
- **Page Load**: Staggered fade-in of food cards (0.1s delay each)
- **Food Idle**: Gentle floating animation (translate Y ±5px, 3s loop)
- **Hover**: Scale up 1.05x, increase glow
- **Select**: Camera smoothly focuses on selected item
- **Panel Slide**: 0.3s ease-out slide from right

## Technical Implementation
- **3D Engine**: Three.js (via CDN)
- **Post-processing**: Three.js EffectComposer with UnrealBloomPass
- **Controls**: OrbitControls from Three.js examples
- **No build step**: Single HTML file with inline CSS/JS

## Acceptance Criteria
1. ✓ 6 different food items displayed as 3D models
2. ✓ Orbit controls allow rotation around each food item
3. ✓ Zoom works via mouse wheel
4. ✓ Clicking food opens detail panel with price + ingredients
5. ✓ Panel can be closed
6. ✓ Responsive design (works on desktop and mobile)
7. ✓ Smooth animations throughout
8. ✓ Visual quality feels premium and appetizing