# Release Process

This document describes how to create a new release of the RecipesGalore recipe collection.

## Overview

The release process is **automated** via GitHub Actions. When you push a version tag, the workflow:

1. ✅ Creates a ZIP file of the `recipes/` folder (excludes `TEMPLATE.md`)
2. ✅ Generates `manifest.json` with recipe metadata for all recipes
3. ✅ Counts the number of recipes
4. ✅ Creates a GitHub Release with both assets attached
5. ✅ Generates release notes with download URLs
6. ✅ Makes both assets publicly downloadable (no auth required)

## Security

**Who can create releases?**

Only GitHub users with **write access** to this repository can create releases. Random users cannot:
- Push tags to this repo
- Trigger the release workflow
- Create releases

You control access via GitHub's repository collaborator settings.

## Prerequisites

- Git installed and configured
- Write access to the repository
- On the `main` branch with latest changes pulled

## Quick Start (Automated Script)

The easiest way to create a release is with the helper script:

```bash
./create-release.sh
```

The script will:
- ✅ Check for a clean working tree (no uncommitted changes)
- ✅ Verify you're on the `main` branch
- ✅ Pull latest changes (fast-forward only, fails if branches have diverged)
- ✅ Verify local `main` matches `origin/main` (no unpushed commits)
- ✅ Count recipes
- ✅ Prompt for version number
- ✅ Validate version format
- ✅ Check tag doesn't already exist (locally and on origin)
- ✅ Create and push the tag
- ✅ Display the release URL

**Example:**
```bash
$ ./create-release.sh

═══════════════════════════════════════════════
  RecipesGalore Release Creator
═══════════════════════════════════════════════

Found 17 recipes in the collection

Enter version number (e.g., 0.0.1):
0.0.1

Ready to create release:
  Version:     v0.0.1
  Recipes:     17
  Description: Release v0.0.1 - Recipe collection with 17 recipes

Continue? (y/n) y

✓ Tag created and pushed successfully!

Release will be available at:
https://github.com/CrismonicWave-org/digital-recipes/releases/tag/v0.0.1
```

## Manual Process

If you prefer to create releases manually:

### Step 1: Ensure you're on main

```bash
git checkout main
git pull origin main
```

### Step 2: Create a version tag

Use [semantic versioning](https://semver.org/): `v{major}.{minor}.{patch}`

```bash
# For initial release
git tag -a v0.0.1 -m "Initial recipe collection - 17 recipes"

# For future releases
git tag -a v0.1.0 -m "Added 10 new dessert recipes"
```

### Step 3: Push the tag

```bash
git push origin v0.0.1
```

### Step 4: Watch the workflow

The GitHub Actions workflow will run automatically:

- **Monitor:** https://github.com/CrismonicWave-org/digital-recipes/actions
- **Duration:** ~1-2 minutes

### Step 5: Verify the release

Once complete, verify the release:

- **Release page:** https://github.com/CrismonicWave-org/digital-recipes/releases
- **Download URL:** `https://github.com/CrismonicWave-org/digital-recipes/releases/download/{tag}/recipes.zip`

## Version Numbering Guidelines

Use [semantic versioning](https://semver.org/):

- **Major** (`v1.0.0`): Breaking changes, major restructuring
- **Minor** (`v0.1.0`): New recipes added, new features
- **Patch** (`v0.0.1`): Bug fixes, typo corrections, small updates

**Examples:**
- `v0.0.1` - Initial release with 17 recipes
- `v0.1.0` - Added 10 new breakfast recipes
- `v0.1.1` - Fixed typos in 3 recipes
- `v1.0.0` - Complete recipe database restructure

## What Gets Released

Each release attaches two assets (no authentication required to download):

| Asset | Size | Purpose |
|-------|------|---------|
| `manifest.json` | ~16 KB | Structured metadata for all recipes — ideal for app search/filter UIs |
| `recipes.zip` | ~500 KB | Full recipe markdown files — for offline use or bulk processing |

✅ **Included in `recipes.zip`:**
- All `.md` files in `recipes/` folder
- Recipe markdown with YAML frontmatter
- Complete instructions, ingredients, notes

❌ **Excluded from `recipes.zip`:**
- `TEMPLATE.md` (template file)
- Documentation files (README, guides)
- Git history
- Workflow files

## manifest.json

`manifest.json` is generated automatically at release time by `scripts/generate-manifest.py` and attached to every GitHub Release.

### Structure

```json
{
  "version": "v0.0.1",
  "generated": "2026-05-05T12:00:00Z",
  "recipeCount": 17,
  "recipes": [
    {
      "id": "chicken-tikka-masala",
      "filename": "chicken-tikka-masala.md",
      "title": "Chicken Tikka Masala",
      "slug": "chicken-tikka-masala",
      "category": "dinner",
      "difficulty": "intermediate",
      "totalTime": 45,
      "servings": 4,
      "description": "...",
      "featured": false,
      "cuisine": "indian",
      "primaryProtein": "chicken"
    }
  ],
  "facets": {
    "categories": ["appetizer", "breakfast", "dessert", "dinner", "lunch"],
    "proteins": ["beef", "chicken", "seafood"],
    "cuisines": ["american", "indian", "italian"],
    "difficulties": ["beginner", "intermediate"],
    "dietaryTags": ["gluten-free"],
    "cookingMethods": ["oven", "stovetop"],
    "occasions": [],
    "seasons": []
  }
}
```

### Key fields

- **`recipes[].filename`** — use this to fetch the full recipe markdown (see integration examples below)
- **`recipes[].id`** — filename stem without `.md`, useful as a UI key
- **`facets`** — pre-aggregated unique values for building filter UIs without scanning all recipes

## Download URLs

Each release generates public download URLs (no authentication required):

**manifest.json:**
```
https://github.com/CrismonicWave-org/digital-recipes/releases/download/{tag}/manifest.json
```

**recipes.zip:**
```
https://github.com/CrismonicWave-org/digital-recipes/releases/download/{tag}/recipes.zip
```

**Example (v0.0.1):**
```
https://github.com/CrismonicWave-org/digital-recipes/releases/download/v0.0.1/manifest.json
https://github.com/CrismonicWave-org/digital-recipes/releases/download/v0.0.1/recipes.zip
```

## Mobile/Web App Integration

**Recommended approach** — fetch the small manifest for instant search/filter UI, then download individual recipe markdown only when the user opens a recipe:

```javascript
// Step 1: Fetch manifest (~16 KB — instant!)
const tag = 'v0.0.1';
const manifestUrl = `https://github.com/CrismonicWave-org/digital-recipes/releases/download/${tag}/manifest.json`;
const manifest = await fetch(manifestUrl).then(r => r.json());

// Step 2: Display recipe list immediately using manifest metadata
displayRecipes(manifest.recipes);
// Use manifest.facets for filter dropdowns (category, cuisine, difficulty, etc.)

// Step 3: When user taps a recipe, fetch its full markdown using recipe.filename
async function openRecipe(recipe) {
  const recipeUrl = `https://raw.githubusercontent.com/CrismonicWave-org/digital-recipes/${tag}/recipes/${recipe.filename}`;
  const recipeContent = await fetch(recipeUrl).then(r => r.text());
  renderMarkdown(recipeContent);
}
```

**Always use `recipe.filename` (not `recipe.id`) to build the raw content URL** — `filename` is the canonical file name (e.g. `chicken-tikka-masala.md`) and matches the path inside `recipes.zip`.

**Fetch latest release dynamically via GitHub API:**

```javascript
const { assets } = await fetch(
  'https://api.github.com/repos/CrismonicWave-org/digital-recipes/releases/latest'
).then(r => r.json());

const manifestUrl = assets.find(a => a.name === 'manifest.json').browser_download_url;
const zipUrl      = assets.find(a => a.name === 'recipes.zip').browser_download_url;
```

## Troubleshooting

### Tag already exists

```bash
# List existing tags
git tag -l

# Delete local tag (if needed)
git tag -d v0.0.1

# Delete remote tag (if needed - use with caution!)
git push origin --delete v0.0.1
```

### Workflow failed

1. Check the Actions tab: https://github.com/CrismonicWave-org/digital-recipes/actions
2. Click on the failed workflow run
3. Review error logs
4. Fix issues and push a new tag (increment version)

### Release is missing ZIP file

- Check that the workflow completed successfully
- Verify the `recipes/` folder exists and contains `.md` files
- Check workflow logs for ZIP creation step

### Can't push tags

Verify you have write access:
```bash
git remote -v
# Should show your authenticated GitHub URL
```

## Workflow File

The release workflow is defined in `.github/workflows/release.yml`

Key components:
- **Trigger:** `push: tags: v*.*.*`
- **Manifest:** `python3 scripts/generate-manifest.py` (generates `manifest.json`)
- **ZIP Creation:** `zip -r ../recipes.zip . -x "TEMPLATE.md"`
- **Release Action:** `softprops/action-gh-release@v2` (attaches both `manifest.json` and `recipes.zip`)

## Future Improvements

Potential enhancements:
- [ ] Validate YAML frontmatter against schema before release
- [ ] Include recipe count by category in release notes
- [ ] Automated changelog generation
- [ ] Recipe validation tests in CI

## Questions?

- **Workflow not triggering?** Ensure tag matches `v*.*.*` pattern
- **Need to delete a release?** Use GitHub web interface (Releases → Delete)
- **Want to update a release?** Create a new version with incremented number

---

*Last updated: 2026-05-05*
