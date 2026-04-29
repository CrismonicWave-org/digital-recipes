# Contributing to RecipesGalore 🍳

**Welcome!** We're so glad you're here. RecipesGalore is a community recipe collection, and your recipes make this project special.

**You don't need to be a programmer** to contribute. If you can write a recipe and copy/paste text, you can do this! We'll walk you through everything step-by-step.

---

## 🎯 What Makes a Good RecipesGalore Recipe?

Before we dive into the "how," let's talk about what we're looking for:

✅ **Tested recipes** - You've made this dish successfully  
✅ **Clear instructions** - Step-by-step, like you're teaching a friend  
✅ **Accurate measurements** - US standards (cups, tablespoons, Fahrenheit)  
✅ **Honest attribution** - Give credit where it's due (family recipe? cookbook? your creation?)  
✅ **Photos welcome** - A picture of your finished dish helps others (optional but awesome!)

**We love:**
- Family recipes passed down through generations
- Creative twists on classics
- Cultural and regional specialties
- Everyday weeknight dinners
- Special occasion showstoppers
- Dietary-specific adaptations (gluten-free, vegan, etc.)

---

## 🚀 Quick Start: Three Ways to Contribute

### Option 1: Submit via GitHub (Easiest - No Account Needed)

**Best for:** Anyone who just wants to share a recipe without learning GitHub.

1. **Write your recipe** in a text document (Word, Google Docs, Notes app, anything!)
2. **Email or message it** to us at [contact method - you'll add this]
3. **We'll format it** and add it to the database for you
4. **You get full credit** - your name will be on the recipe

That's it! Easy peasy. 🎉

---

### Option 2: Submit via GitHub Issue (Recommended for Beginners)

**Best for:** People comfortable with websites but new to GitHub.

**What's GitHub?** Think of it like Google Docs for recipe collections. It keeps track of changes and lets many people work together.

**Steps:**

1. **Go to the RecipesGalore GitHub page**  
   Link: https://github.com/CrismonicWave-org/digital-recipes

2. **Click the "Issues" tab** at the top  
   (Issues = suggestions, recipe submissions, questions)

3. **Click the green "New Issue" button**

4. **Choose "Recipe Submission"** template  
   (We made a form that guides you through what info we need!)

5. **Fill out the form:**
   - Recipe title
   - Your name (for credit)
   - Paste your recipe text
   - Add any special notes

6. **Click "Submit"**

**That's it!** We'll review it, format it properly, and add it to the recipe database. You'll get a notification when it's live.

**No GitHub account?** You can still submit! GitHub lets anyone create issues.

---

### Option 3: Submit via Pull Request (For the Adventurous)

**Best for:** People who want to learn GitHub or already know a bit about it.

**What's a Pull Request?** It's like saying "Hey, I made some changes to the cookbook. Would you like to add them?" The project maintainers review your changes and add them if they look good.

**Think of it like this:**
- You make a **copy** of the cookbook (fork)
- You **add your recipe** to your copy
- You **show us** your addition (pull request)
- We **review and approve** it
- Your recipe goes **live** in the official cookbook!

**Detailed steps below** in the "Step-by-Step GitHub Guide" section.

---

## 📝 Recipe Template & Guidelines

### Start with the Template

We provide a **template** that shows exactly how to format your recipe. It's like a recipe for writing recipes! 😄

**Find it here:** `recipes/TEMPLATE.md`

**It includes:**
- Metadata section at the top (category, difficulty, time, etc.)
- Ingredient list format
- Instruction format
- Chef's notes section
- References to cooking guides

### Required Information

Every recipe needs these basics:

#### 1. Title & Description
```
Title: Classic Chocolate Chip Cookies
Description: Soft, chewy cookies with gooey chocolate chips. Perfect for any occasion!
```

#### 2. Basic Details
- **Category:** What meal type? (breakfast, lunch, dinner, appetizer, dessert, snack, drink, side-dish)
- **Difficulty:** beginner, intermediate, or advanced
- **Total Time:** How long from start to finish? (in minutes)
- **Servings:** How many people does this feed?

#### 3. Ingredients
- List in order of use
- Use US measurements (cups, tablespoons, teaspoons)
- Be specific: "1 cup all-purpose flour" not "flour"
- Group by category (main ingredients, seasonings, garnishes)

#### 4. Instructions
- Number each step
- One action per step
- Be specific about temperatures and times
- Include visual cues ("until golden brown" or "when a toothpick comes out clean")

#### 5. Attribution
- **Your name** as contributor
- **Original source** if adapted (cookbook, website, family recipe)
- Be honest and give credit!

### Optional (But Helpful!) Information

These aren't required, but they make recipes more useful:

- **Main protein:** beef, chicken, vegetarian, etc.
- **Cuisine style:** Italian, Mexican, American, etc.
- **Cooking method:** oven, stovetop, grill, slow cooker, etc.
- **Dietary tags:** gluten-free, dairy-free, vegan, keto, etc.
- **Best seasons:** summer, winter, year-round
- **Occasion:** weeknight dinner, holiday, game day, etc.
- **Photos:** Before, during, or after cooking
- **Chef's tips:** Your secrets for success!
- **Substitutions:** "No buttermilk? Use milk + vinegar"
- **Storage tips:** How to save leftovers

---

## 🔧 Step-by-Step GitHub Guide (Option 3)

**New to GitHub?** No worries! Here's a friendly walkthrough.

### Step 1: Create a Free GitHub Account

1. Go to https://github.com
2. Click "Sign up" (top right)
3. Follow the steps (email, password, username)
4. Verify your email
5. Done! You have a GitHub account.

### Step 2: "Fork" the Recipe Repository

**What's forking?** Making your own copy of the recipe collection to work on.

1. Go to: https://github.com/CrismonicWave-org/digital-recipes
2. Click the **"Fork"** button (top right, looks like a Y-shape)
3. GitHub creates your personal copy
4. You'll see: `YourUsername/digital-recipes` at the top

**You're now working on YOUR copy.** Any changes you make won't affect the main cookbook (yet).

### Step 3: Add Your Recipe

#### Method A: Using GitHub's Website (Easier)

1. In your forked repository, click **"recipes"** folder
2. Click **"Add file"** button → **"Create new file"**
3. Name your file: `my-recipe-name.md`  
   (Use lowercase, hyphens instead of spaces, end with `.md`)
4. Open the **TEMPLATE.md** file in another tab
5. **Copy the entire template**
6. **Paste it** into your new file
7. **Fill in your recipe** (replace the example text)
8. Scroll down, add a commit message: "Add [Recipe Name]"
9. Click **"Commit new file"**

#### Method B: Using GitHub Desktop (If You Want to Work Offline)

1. Download **GitHub Desktop**: https://desktop.github.com
2. Sign in with your GitHub account
3. Click **"File"** → **"Clone Repository"**
4. Select your forked `digital-recipes`
5. Choose where to save it on your computer
6. Open the `recipes` folder on your computer
7. Copy `TEMPLATE.md`, rename it to `your-recipe-name.md`
8. Open in any text editor (Notepad, TextEdit, VS Code, etc.)
9. Fill in your recipe
10. Save the file
11. In GitHub Desktop:
    - You'll see your new file listed
    - Add a description: "Add [Recipe Name]"
    - Click **"Commit to main"**
    - Click **"Push origin"** (uploads to GitHub)

### Step 4: Submit a Pull Request

**What's happening:** You're asking the RecipesGalore team to review and add your recipe.

1. Go to your forked repository on GitHub  
   (`github.com/YourUsername/digital-recipes`)
2. You'll see a banner: **"This branch is 1 commit ahead of CrismonicWave-org:main"**
3. Click **"Contribute"** → **"Open pull request"**
4. Write a title: "Add [Your Recipe Name]"
5. Add a description (optional):
   ```
   Hey! I'm submitting my family's famous lasagna recipe.
   It's been in our family for three generations. Hope you enjoy it!
   ```
6. Click **"Create pull request"**

### Step 5: Wait for Review

**What happens next:**

- A maintainer (Ken or another reviewer) will look at your recipe
- They might ask questions or suggest small edits
- You'll get an email notification for any comments
- Once approved, your recipe goes **live** in the official database!
- You'll get credit as a contributor 🎉

**Typical review time:** 1-3 days (we're volunteers!)

---

## 📏 Writing Guidelines

### Use US Measurements

RecipesGalore uses **US standard measurements** for consistency:

✅ **Volume:** cups, tablespoons (tbsp), teaspoons (tsp), fluid ounces (fl oz)  
✅ **Weight:** pounds (lb), ounces (oz)  
✅ **Temperature:** Fahrenheit (°F)

**Need help converting?** Check out our [US Measurement Guide](./US-MEASUREMENTS.md)

**Examples:**
- ✅ Good: "2 cups all-purpose flour"
- ❌ Avoid: "250g flour" (metric)
- ✅ Good: "Bake at 350°F for 25 minutes"
- ❌ Avoid: "Bake at 175°C" (Celsius)

### Write Clear Instructions

**Think:** You're teaching someone over the phone. They can't see you, so be specific!

**Bad example:**
```
1. Mix ingredients
2. Cook
3. Serve
```

**Good example:**
```
1. In a large bowl, whisk together 2 cups flour, 1 tsp baking soda, and 1/2 tsp salt.
2. In a separate bowl, beat butter and sugar until light and fluffy (about 3 minutes).
3. Add eggs one at a time, beating well after each addition.
4. Gradually mix dry ingredients into wet ingredients until just combined. Do not overmix.
```

**Tips for great instructions:**
- ✅ Use action verbs: whisk, fold, sauté, simmer
- ✅ Include times: "Cook for 5 minutes" not "Cook until done"
- ✅ Include temperatures: "Heat to 350°F" not "Heat oven"
- ✅ Add visual cues: "until golden brown" or "when mixture is bubbly"
- ✅ One action per step (easier to follow)

### Be Specific with Ingredients

**Vague:**
```
- Chicken
- Onion
- Some spices
```

**Specific:**
```
- 1 lb boneless, skinless chicken breast
- 1 medium yellow onion, diced (about 1 cup)
- 1 tsp paprika
- 1/2 tsp garlic powder
- 1/4 tsp black pepper
```

**Why?** Helps people shop and cook with confidence!

---

## 🖼️ Adding Photos

Photos make recipes more appealing! Here's how:

### Option 1: Include in Pull Request

1. Take photos of your finished dish
2. **Name them clearly:** `chocolate-chip-cookies.jpg`
3. Add to the `assets/images/` folder in your fork
4. Reference in your recipe YAML:
   ```yaml
   featuredImage: "./assets/images/chocolate-chip-cookies.jpg"
   ```

### Option 2: Link to External Images

If you have photos hosted elsewhere (your blog, Instagram, etc.):
```yaml
featuredImage: "https://your-website.com/image.jpg"
```

**Photo tips:**
- Use good lighting (natural light is best!)
- Clean background
- Show the finished dish
- Optional: Include step-by-step photos

---

## ⚖️ Copyright & Attribution

**Important:** We want recipes we have the right to share!

### ✅ You CAN Submit:

- **Your own original recipes** (created by you)
- **Family recipes** (traditional, passed down)
- **Adapted recipes** (you changed a published recipe significantly)
- **Public domain recipes** (very old, no copyright)

### ❌ You CANNOT Submit:

- **Copy-pasted recipes** from cookbooks or websites without permission
- **Celebrity chef recipes** (they're copyrighted)
- **Recipe blog content** word-for-word (unless you have permission)

### How to Handle Adaptations

**If you adapted a recipe from a source:**

1. **Significantly change it** (different ingredients, methods, your spin)
2. **Give credit** in the recipe:
   ```
   Original inspiration: Classic Carbonara from "Italian Cooking 101"
   Adapted by: [Your Name] (Made gluten-free, added peas)
   ```

**General rule:** If you changed 3+ ingredients or the cooking method, it's an adaptation. If you only swapped butter for oil, it's still the original (get permission or don't submit).

---

## 🤝 Community Guidelines

RecipesGalore is a friendly, welcoming place. We expect:

✅ **Be respectful** - Kind words, constructive feedback  
✅ **Give credit** - Attribute sources honestly  
✅ **Be helpful** - Answer questions, share tips  
✅ **Stay on topic** - This is about recipes and cooking  
✅ **Be patient** - Reviews take time, maintainers are volunteers

❌ **Not welcome:**
- Spam or advertisements
- Offensive or inappropriate content
- Trolling or harassment
- Plagiarism or copyright violation

---

## 🎓 Learning Resources

### New to GitHub?

- **GitHub Guides:** https://guides.github.com/activities/hello-world/
- **Markdown Basics:** https://www.markdownguide.org/basic-syntax/
- **YouTube:** Search "GitHub for beginners" for video tutorials

### Recipe Writing Tips

- **US Measurement Guide:** [US-MEASUREMENTS.md](./US-MEASUREMENTS.md)
- **Temperature Guide:** [TEMPERATURE-GUIDE.md](./TEMPERATURE-GUIDE.md)
- **Substitutions:** [SUBSTITUTIONS.md](./SUBSTITUTIONS.md)

### Need Help?

- **Open an Issue:** Ask questions in the Issues tab
- **Email:** [Your contact email here]
- **Discord/Slack:** [If you set up a community channel]

---

## 🏆 Recognition

**Contributors are the heart of RecipesGalore!**

Your contributions will be recognized:

✅ **Author credit** on every recipe you submit  
✅ **Contributors list** in the README  
✅ **GitHub contribution graph** (shows your activity)  
✅ **Community appreciation** - We love our recipe contributors!

---

## 🎉 Thank You!

Every recipe you share makes RecipesGalore better. Whether you submit one recipe or one hundred, you're helping build an amazing, ad-free, community-driven recipe collection.

**Your recipe might be someone's new favorite dinner!** 🍽️

Ready to get started? Grab the [Recipe Template](./recipes/TEMPLATE.md) and share something delicious!

**Questions?** Don't hesitate to ask. We're here to help!

---

*RecipesGalore - By cooks, for cooks* ❤️
