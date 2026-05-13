#!/bin/bash

# RecipesGalore Release Script
# Creates a new version tag and triggers the automated release workflow

set -e  # Exit on error

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}═══════════════════════════════════════════════${NC}"
echo -e "${BLUE}  RecipesGalore Release Creator${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════${NC}"
echo ""

# Check if we're in the right directory
if [ ! -f "RELEASE_PROCESS.md" ]; then
    echo -e "${RED}Error: Must be run from the repository root directory${NC}"
    exit 1
fi

# Check for a clean working tree before doing anything else
if ! git diff-index --quiet HEAD -- 2>/dev/null; then
    echo -e "${RED}Error: Working tree has uncommitted changes.${NC}"
    echo "Please commit or stash your changes before creating a release."
    git status --short
    exit 1
fi

# Check if we're on main branch
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
    echo -e "${YELLOW}Warning: You are on branch '${CURRENT_BRANCH}', not 'main'${NC}"
    read -p "Do you want to switch to main? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git checkout main
        if ! git pull --ff-only origin main; then
            echo -e "${RED}Error: Could not fast-forward local main to origin/main.${NC}"
            echo "Your local main has diverged from origin. Please resolve this before releasing."
            exit 1
        fi
        echo -e "${GREEN}Switched to main and pulled latest changes${NC}"
    else
        echo -e "${RED}Aborted. Please checkout main branch first.${NC}"
        exit 1
    fi
fi

# Pull latest changes
echo -e "${BLUE}Pulling latest changes from origin/main...${NC}"
if ! git pull --ff-only origin main; then
    echo -e "${RED}Error: Could not fast-forward local main to origin/main.${NC}"
    echo "Your local main has diverged from origin. Please resolve this before releasing."
    exit 1
fi

# Verify HEAD is in sync with origin/main (no unpushed commits)
AHEAD=$(git rev-list --count origin/main..HEAD)
if [ "$AHEAD" -gt 0 ]; then
    echo -e "${RED}Error: Local main is ${AHEAD} commit(s) ahead of origin/main.${NC}"
    echo "Push your commits before releasing:"
    echo "  git push origin main"
    exit 1
fi

# Count recipes (excluding TEMPLATE.md)
RECIPE_COUNT=$(find recipes -name "*.md" -not -name "TEMPLATE.md" | wc -l | tr -d ' ')
echo -e "${GREEN}Found ${RECIPE_COUNT} recipes in the collection${NC}"
echo ""

# Get version number from user
echo -e "${YELLOW}Enter version number (e.g., 0.0.1):${NC}"
read VERSION

# Validate version format
if ! [[ $VERSION =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo -e "${RED}Error: Invalid version format. Use semantic versioning (e.g., 0.0.1)${NC}"
    exit 1
fi

TAG_NAME="v${VERSION}"

# Check if tag already exists locally or on origin
if git rev-parse "$TAG_NAME" >/dev/null 2>&1; then
    echo -e "${RED}Error: Tag ${TAG_NAME} already exists locally!${NC}"
    echo "Existing local tags:"
    git tag -l
    exit 1
fi

if git ls-remote --tags --exit-code origin "refs/tags/${TAG_NAME}" >/dev/null 2>&1; then
    echo -e "${RED}Error: Tag ${TAG_NAME} already exists on origin!${NC}"
    echo "Matching remote tag:"
    echo "${TAG_NAME}"
    exit 1
fi

# Get release description
echo ""
echo -e "${YELLOW}Enter release description (or press Enter for default):${NC}"
read DESCRIPTION

if [ -z "$DESCRIPTION" ]; then
    DESCRIPTION="Release ${TAG_NAME} - Recipe collection with ${RECIPE_COUNT} recipes"
fi

# Confirmation
echo ""
echo -e "${BLUE}═══════════════════════════════════════════════${NC}"
echo -e "${BLUE}Ready to create release:${NC}"
echo -e "${GREEN}  Version:     ${TAG_NAME}${NC}"
echo -e "${GREEN}  Recipes:     ${RECIPE_COUNT}${NC}"
echo -e "${GREEN}  Description: ${DESCRIPTION}${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════${NC}"
echo ""
echo -e "${YELLOW}This will:${NC}"
echo "  1. Create git tag: ${TAG_NAME}"
echo "  2. Push tag to GitHub"
echo "  3. Trigger automated release workflow"
echo "  4. Generate recipes.zip"
echo "  5. Create public release on GitHub"
echo ""
read -p "Continue? (y/n) " -n 1 -r
echo

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${RED}Aborted.${NC}"
    exit 1
fi

# Create and push tag
echo ""
echo -e "${BLUE}Creating tag ${TAG_NAME}...${NC}"
git tag -a "$TAG_NAME" -m "$DESCRIPTION"

echo -e "${BLUE}Pushing tag to origin...${NC}"
git push origin "$TAG_NAME"

echo ""
echo -e "${GREEN}✓ Tag created and pushed successfully!${NC}"
echo ""
echo -e "${BLUE}═══════════════════════════════════════════════${NC}"
echo -e "${GREEN}Release process initiated!${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════${NC}"
echo ""
echo "The GitHub Actions workflow is now running..."
echo ""
echo "Monitor progress at:"
echo -e "${BLUE}https://github.com/CrismonicWave-org/digital-recipes/actions${NC}"
echo ""
echo "Release will be available at:"
echo -e "${BLUE}https://github.com/CrismonicWave-org/digital-recipes/releases/tag/${TAG_NAME}${NC}"
echo ""
echo "Download URL for mobile app:"
echo -e "${GREEN}https://github.com/CrismonicWave-org/digital-recipes/releases/download/${TAG_NAME}/recipes.zip${NC}"
echo ""
echo -e "${YELLOW}Note: It may take 1-2 minutes for the workflow to complete.${NC}"
echo ""
