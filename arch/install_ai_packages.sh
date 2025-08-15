#!/usr/bin/env bash
# Install useful packages for AI development on Arch Linux.
# Run as root or with sudo.

set -e

# Update system
pacman -Syu --noconfirm

# Base development tools
pacman -S --needed --noconfirm base-devel git

# Python and scientific stack
pacman -S --needed --noconfirm python python-pip python-numpy \
    python-scipy python-pandas

# Machine learning libraries
pacman -S --needed --noconfirm python-tensorflow python-pytorch

# Optional: CUDA support (uncomment if using NVIDIA GPU)
# pacman -S --needed --noconfirm cuda cudnn

# Optional: install GRUB bootloader (similar to Ubuntu)
# pacman -S --needed --noconfirm grub

# Optional: install GNOME desktop environment and display manager
# pacman -S --needed --noconfirm gnome gnome-extra gdm

echo "AI development packages installed."
