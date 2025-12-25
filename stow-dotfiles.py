#!/usr/bin/env python3
import subprocess
from pathlib import Path

# Path to your dotfiles repository
DOTFILES_DIR = Path.home() / "repos/dotfiles"  # Adjust if your repo path is different

def stow_package(package_path: Path):
    print(f"Stowing package: {package_path.name}")
    subprocess.run(["stow", "-t", str(Path.home()), package_path.name], cwd=DOTFILES_DIR)

def main():
    if not DOTFILES_DIR.exists():
        print(f"Error: dotfiles directory {DOTFILES_DIR} does not exist.")
        return

    # Iterate over all directories in dotfiles (each is a package)
    for package in DOTFILES_DIR.iterdir():
        if package.is_dir():
            stow_package(package)

if __name__ == "__main__":
    main()
