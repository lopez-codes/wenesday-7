# Arch Linux Setup for Wenesday

This folder contains resources to build a lightweight Arch Linux environment for AI development with the Wenesday project. The goal is to provide an OS setup that works well for machine learning tasks while remaining useful as a daily driver.

## Installation Overview
1. Install a minimal Arch Linux system. You can use the official [installation guide](https://wiki.archlinux.org/title/Installation_guide) or `archinstall`.
2. Clone the Wenesday repository:
   ```bash
   git clone https://github.com/blopen/free-wenesday-free
   ```
3. Use the helper script `install_ai_packages.sh` to install common AI packages and development tools.

## AI Package Installation
Run the following script inside this folder to install the recommended packages:
```bash
bash install_ai_packages.sh
```
This will install Python, common machine learning libraries like TensorFlow and PyTorch, and additional utilities useful for development.

Feel free to customize the script to match your hardware (e.g., enabling CUDA support) and personal workflow.

## Boot Manager and Desktop Environment

To use Arch Linux as a full operating system, you may want a boot manager and a graphical desktop. A common choice is **GRUB**, the same bootloader used by Ubuntu. Install it with:

```bash
pacman -S grub
# then follow the official instructions for `grub-install` and `grub-mkconfig`
```

For a free desktop experience, you can install **GNOME 4** and its display manager:

```bash
pacman -S gnome gnome-extra gdm
systemctl enable gdm
```

Other desktops or boot managers work as well; adjust the packages to your liking. The installation script can also be adapted for Debian or Ubuntu by replacing `pacman` with `apt` commands.
