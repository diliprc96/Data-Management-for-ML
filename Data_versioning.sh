#!/bin/bash

# Check if correct number of arguments is provided
if [ "$#" -lt 2 ]; then
    echo "Usage: $0 <version_tag> <dataset_path1> [dataset_path2 ...]"
    exit 1
fi

# Assign input variables
VERSION_TAG=$1
shift  # Remove first argument (version tag) to process dataset paths

# Initialize Git and DVC if not already done
git init 2>/dev/null
dvc init 2>/dev/null

echo "Tracking datasets with DVC..."
for dataset in "$@"; do
    if [ -f "$dataset" ] || [ -d "$dataset" ]; then
        dvc add "$dataset"
        git add "$dataset.dvc"
        echo "Added $dataset to DVC tracking"
    else
        echo "Warning: File $dataset not found! Skipping..."
    fi
done

# Commit changes to Git
git add .gitignore
git commit -m "Version $VERSION_TAG: Updated datasets"

echo "Creating Git tag: $VERSION_TAG"
git tag -a "$VERSION_TAG" -m "Dataset version $VERSION_TAG"

echo "Pushing changes to remote repository..."
git push origin --tags

echo "Versioning completed successfully!"
