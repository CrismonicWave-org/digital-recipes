# Release Process

This document describes how to create a new release of the RecipesGalore recipe collection.

## Overview

The release process is **automated** via GitHub Actions. When you push a version tag, the workflow:

1. ✅ Creates a ZIP file of the `recipes/` folder (excludes `TEMPLATE.md`)
2. ✅ Counts the number of recipes
3. ✅ Creates a GitHub Release with the ZIP attached
4. ✅ Generates release notes with download URL
5. ✅ Makes the ZIP publicly downloadable (no auth required)

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
- ✅ Verify you're on the `main` branch
- ✅ Pull latest changes
- ✅ Count recipes
- ✅ Prompt for version number
- ✅ Validate version format
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

The release includes:

✅ **Included:**
- All `.md` files in `recipes/` folder
- Recipe markdown with YAML frontmatter
- Complete instructions, ingredients, notes

❌ **Excluded:**
- `TEMPLATE.md` (template file)
- Documentation files (README, guides)
- Git history
- Workflow files

## Download URLs

Each release generates a public download URL (no authentication required):

**Pattern:**
```
https://github.com/CrismonicWave-org/digital-recipes/releases/download/{tag}/recipes.zip
```

**Example:**
```
https://github.com/CrismonicWave-org/digital-recipes/releases/download/v0.0.1/recipes.zip
```

## Mobile/Web App Integration

Apps can fetch releases without authentication:

```javascript
// Option 1: Fetch specific version
const url = 'https://github.com/CrismonicWave-org/digital-recipes/releases/download/v0.0.1/recipes.zip';

// Option 2: Fetch latest release via API
fetch('https://api.github.com/repos/CrismonicWave-org/digital-recipes/releases/latest')
  .then(res => res.json())
  .then(release => {
    const zipUrl = release.assets.find(a => a.name === 'recipes.zip').browser_download_url;
    // Download from zipUrl
  });
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
- **ZIP Creation:** `zip -r ../recipes.zip . -x "TEMPLATE.md"`
- **Release Action:** `softprops/action-gh-release@v2`

## Future Improvements

Potential enhancements:
- [ ] Validate YAML frontmatter before release
- [ ] Generate recipe index/manifest JSON
- [ ] Include recipe count by category in release notes
- [ ] Automated changelog generation
- [ ] Recipe validation tests in CI

## Questions?

- **Workflow not triggering?** Ensure tag matches `v*.*.*` pattern
- **Need to delete a release?** Use GitHub web interface (Releases → Delete)
- **Want to update a release?** Create a new version with incremented number

---

*Last updated: 2026-05-05*
