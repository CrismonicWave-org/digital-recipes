#!/usr/bin/env python3
"""
RecipesGalore Manifest Generator

Parses recipe markdown files with YAML frontmatter and generates
a manifest.json file for efficient mobile/web app consumption.
"""

import os
import sys
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

def extract_yaml_frontmatter(content: str) -> Dict[str, Any]:
    """Extract YAML frontmatter from markdown content."""
    # Match YAML frontmatter between --- delimiters
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}
    
    yaml_content = match.group(1)
    
    # Simple YAML parser (handles our specific format)
    data = {}
    current_list_key = None
    
    for line in yaml_content.split('\n'):
        line = line.strip()
        
        # Skip comments and empty lines
        if not line or line.startswith('#'):
            continue
        
        # Handle list items
        if line.startswith('- '):
            if current_list_key:
                value = line[2:].strip().strip('"\'')
                if current_list_key not in data:
                    data[current_list_key] = []
                data[current_list_key].append(value)
            continue
        
        # Handle key-value pairs
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"\'')
            
            # Check if this starts a list
            if not value:
                current_list_key = key
                data[key] = []
            else:
                current_list_key = None
                # Convert numeric values
                if value.isdigit():
                    data[key] = int(value)
                elif value.lower() in ('true', 'false'):
                    data[key] = value.lower() == 'true'
                else:
                    data[key] = value
    
    return data

def process_recipe_file(file_path: Path) -> Dict[str, Any]:
    """Process a single recipe markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract YAML frontmatter
        metadata = extract_yaml_frontmatter(content)
        
        # Create recipe entry for manifest
        recipe = {
            'id': file_path.stem,  # filename without extension
            'filename': file_path.name,
            'title': metadata.get('title', 'Untitled Recipe'),
            'slug': metadata.get('slug', file_path.stem),
            'category': metadata.get('category', 'uncategorized'),
            'difficulty': metadata.get('difficulty', 'beginner'),
            'totalTime': metadata.get('totalTime', 0),
            'servings': metadata.get('servings', 0),
            'description': metadata.get('description', ''),
            'featured': metadata.get('featured', False),
        }
        
        # Optional fields
        if 'primaryProtein' in metadata:
            recipe['primaryProtein'] = metadata['primaryProtein']
        if 'cuisine' in metadata:
            recipe['cuisine'] = metadata['cuisine']
        if 'prepTime' in metadata:
            recipe['prepTime'] = metadata['prepTime']
        if 'cookTime' in metadata:
            recipe['cookTime'] = metadata['cookTime']
        if 'author' in metadata:
            recipe['author'] = metadata['author']
        if 'dietaryTags' in metadata:
            recipe['dietaryTags'] = metadata['dietaryTags']
        if 'cookingMethods' in metadata:
            recipe['cookingMethods'] = metadata['cookingMethods']
        if 'occasions' in metadata:
            recipe['occasions'] = metadata['occasions']
        if 'seasons' in metadata:
            recipe['seasons'] = metadata['seasons']
        
        return recipe
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)
        return None

def collect_facets(recipes: List[Dict[str, Any]]) -> Dict[str, List[str]]:
    """Collect unique values for each facet across all recipes."""
    facets = {
        'categories': set(),
        'proteins': set(),
        'cuisines': set(),
        'difficulties': set(),
        'dietaryTags': set(),
        'cookingMethods': set(),
        'occasions': set(),
        'seasons': set()
    }
    
    for recipe in recipes:
        if 'category' in recipe:
            facets['categories'].add(recipe['category'])
        if 'primaryProtein' in recipe:
            facets['proteins'].add(recipe['primaryProtein'])
        if 'cuisine' in recipe:
            facets['cuisines'].add(recipe['cuisine'])
        if 'difficulty' in recipe:
            facets['difficulties'].add(recipe['difficulty'])
        if 'dietaryTags' in recipe:
            facets['dietaryTags'].update(recipe['dietaryTags'])
        if 'cookingMethods' in recipe:
            facets['cookingMethods'].update(recipe['cookingMethods'])
        if 'occasions' in recipe:
            facets['occasions'].update(recipe['occasions'])
        if 'seasons' in recipe:
            facets['seasons'].update(recipe['seasons'])
    
    # Convert sets to sorted lists
    return {key: sorted(list(values)) for key, values in facets.items()}

def generate_manifest(recipes_dir: str, output_file: str, version: str = None):
    """Generate manifest.json from recipe markdown files."""
    recipes_path = Path(recipes_dir)
    
    if not recipes_path.exists():
        print(f"Error: Recipes directory not found: {recipes_dir}", file=sys.stderr)
        sys.exit(1)
    
    # Find all markdown files (exclude TEMPLATE.md)
    recipe_files = [
        f for f in recipes_path.glob('*.md')
        if f.name != 'TEMPLATE.md'
    ]
    
    if not recipe_files:
        print(f"Warning: No recipe files found in {recipes_dir}", file=sys.stderr)
    
    # Process all recipes
    recipes = []
    for file_path in sorted(recipe_files):
        recipe = process_recipe_file(file_path)
        if recipe:
            recipes.append(recipe)
    
    # Collect facets
    facets = collect_facets(recipes)
    
    # Build manifest
    manifest = {
        'version': version or 'unknown',
        'generated': datetime.utcnow().isoformat() + 'Z',
        'recipeCount': len(recipes),
        'recipes': recipes,
        'facets': facets
    }
    
    # Write manifest
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    # Print summary
    print(f"✓ Generated manifest with {len(recipes)} recipes")
    print(f"✓ Output: {output_file}")
    print(f"\nFacet counts:")
    for facet, values in facets.items():
        print(f"  {facet}: {len(values)}")

if __name__ == '__main__':
    # Get version from command line or environment
    version = os.environ.get('RELEASE_VERSION', 'dev')
    if len(sys.argv) > 1:
        version = sys.argv[1]
    
    # Generate manifest
    recipes_dir = 'recipes'
    output_file = 'manifest.json'
    
    print(f"Generating manifest for version: {version}")
    generate_manifest(recipes_dir, output_file, version)
    print("\n✓ Manifest generation complete!")
