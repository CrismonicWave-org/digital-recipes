# RecipesGalore.org - Multi-Platform Project Plan

## Project Overview
Build a complete open-source platform for foodies to share recipes and food experiences across web and mobile. Three separate public repositories for clear separation of concerns:
- **digital-recipes** - Recipe content library (markdown/data)
- **recipesgalore-web** - Angular landing page hosted on Firebase
- **recipesgalore-mobile** - Ionic + Capacitor app for iOS & Android

---

## Repository Structure

```
CrismonicWave-org/
├── digital-recipes/              (Recipe content - this repo)
│   ├── chicken/
│   ├── blackstone/
│   ├── smoker/
│   └── README.md
│
├── recipesgalore-web/            (Web application)
│   ├── src/
│   ├── firebase.json
│   └── angular.json
│
└── recipesgalore-mobile/         (Mobile application)
    ├── src/
    ├── capacitor.config.ts
    └── icon.png
```

**Microservices approach:**
- Each repo is independently deployable
- Different tech stacks optimized for each platform
- Separate CI/CD pipelines
- Clear contribution guidelines per repo
- Shared data source (digital-recipes)

---

## Web Application - Phase 1

### 1.1 Firebase Project Setup
- [ ] Create Firebase project in Firebase Console
- [ ] Enable Hosting service
- [ ] Configure custom domain (recipesgalore.org)
- [ ] Set up SSL/TLS certificates (auto-managed by Firebase)
- [ ] Create service account for CI/CD (optional, for later automation)

### 1.2 Angular Project Initialization
- [ ] Create new Angular project: `ng new recipes-galore`
- [ ] Install Firebase tools: `npm install -g firebase-tools`
- [ ] Initialize Firebase in project: `firebase init`
- [ ] Configure firebase.json for hosting
- [ ] Set up environment configuration files (development, production)

### 1.3 Project Structure
```
recipes-galore/
├── src/
│   ├── assets/
│   │   ├── images/           (Logo, hero images)
│   │   └── styles/
│   ├── app/
│   │   ├── app.component.ts
│   │   ├── app.component.html    (Landing page template)
│   │   └── app.component.scss
│   └── main.ts
├── firebase.json
├── .firebaserc
└── README.md
```

---

## Phase 2: Landing Page Development

### 2.1 Design & Layout
- [ ] Create hero section with striking imagery
- [ ] Add welcome headline: "Welcome to RecipesGalore"
- [ ] Write compelling tagline: "Where foodies of the world share their recipes and food experiences"
- [ ] Design responsive layout for desktop, tablet, mobile

### 2.2 Components
- [ ] **Header Component**: Logo, site title, tagline
- [ ] **Hero Section**: Eye-catching welcome message and call-to-action
- [ ] **Mission Statement**: Brief description of RecipesGalore's purpose
- [ ] **Footer**: Contact info, social links, copyright

### 2.3 Styling & UI
- [ ] Choose color scheme (food-themed)
- [ ] Select typography fonts
- [ ] Create responsive design with CSS/SCSS
- [ ] Optimize for all devices
- [ ] Add smooth animations/transitions (optional)

### 2.4 Content
- Add welcome message
- Add mission/vision statement
- Add call-to-action (newsletter signup, social follow, etc.)
- Add footer links and social media icons

---

## Phase 3: Testing & Deployment

### 3.1 Testing
- [ ] Test responsive design on mobile, tablet, desktop
- [ ] Cross-browser testing
- [ ] Test all links and interactive elements

### 3.2 Build & Deploy
- [ ] Production build: `ng build --configuration production`
- [ ] Login to Firebase: `firebase login`
- [ ] Deploy to Firebase Hosting: `firebase deploy --only hosting`
- [ ] Verify deployment at recipesgalore.org

### 3.3 SEO & Meta Tags
- [ ] Add meta description
- [ ] Set up Open Graph tags for social sharing
- [ ] Create robots.txt
- [ ] Optional: Submit sitemap to search engines

---

## Mobile Application - Phase 2

### Mobile Stack
- **Framework**: Ionic + Capacitor
- **Language**: TypeScript/Angular
- **Platforms**: iOS & Android (single codebase)
- **Build Tool**: Ionic CLI

### 2.1 Project Setup
- [ ] Create new Ionic project: `ionic start recipesgalore-mobile blank --type=angular`
- [ ] Install Capacitor: `npm install @capacitor/core`
- [ ] Configure Capacitor for iOS & Android
- [ ] Set up native app icons and splash screens
- [ ] Configure app signing for App Store and Google Play

### 2.2 Mobile Landing Page
- [ ] Create responsive mobile-first design
- [ ] Add welcome screen with native feel
- [ ] Implement navigation menu
- [ ] Add call-to-action buttons (coming soon: recipe browsing)

### 2.3 Platform Configuration
- [ ] iOS: Build and test on physical device/simulator
- [ ] Android: Build and test on physical device/emulator
- [ ] Configure app identifiers (Bundle ID for iOS, Package name for Android)

### 2.4 App Store Preparation
- [ ] Create Apple Developer account
- [ ] Create Google Play Developer account
- [ ] Prepare app store listings
- [ ] Configure signing certificates

---

## Technology Stack

| Component | Technology |
|-----------|-----------|
| **Web Framework** | Angular 18+ |
| **Mobile Framework** | Ionic + Capacitor |
| **Language** | TypeScript |
| **Styling** | SCSS/CSS (responsive) |
| **Web Hosting** | Firebase Hosting |
| **Mobile Deployment** | App Store & Google Play |
| **Domain** | recipesgalore.org |
| **Package Manager** | npm |

---

## Timeline Estimate

| Phase | Duration | Status |
|-------|----------|--------|
| Phase 1: Web Setup & Deploy | 5-8 days | Not Started |
| Phase 2: Mobile Setup & Config | 3-5 days | Not Started |
| **Total MVP** | **8-13 days** | **Not Started** |

**Future phases** (Post-launch):
- Recipe browsing functionality
- User authentication
- Advanced features (favorites, sharing, etc.)
- App store optimization & submissions

---

## Next Steps

1. [ ] Create `recipesgalore-web` repository on GitHub
2. [ ] Create `recipesgalore-mobile` repository on GitHub
3. [ ] Initialize Angular project for web
4. [ ] Initialize Ionic/Capacitor project for mobile
5. [ ] Build landing page (web & mobile)
6. [ ] Deploy web to recipesgalore.org
7. [ ] Prepare mobile apps for app store submissions
