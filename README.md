# my dotfiles
![screenshot-20231118-232853](https://github.com/kernelpanic95/dotfiles/assets/89152958/61dde83f-25f9-4c99-b63a-e72d3ca0e97f)

## This is the configuration of my Arch linux based installation for Hyprland (Wayland) and Qtile (Xorg) based on [Stephane Raabe dotfiles](https://gitlab.com/stephan-raabe/dotfiles/).

## screenshots

![screenshot-20231119-182105](https://github.com/kernelpanic95/dotfiles/assets/89152958/4f7a6ce7-b1a6-4526-bc29-a893609719a1)
![screenshot-20231119-165958](https://github.com/kernelpanic95/dotfiles/assets/89152958/4cc1cc8e-ba51-4130-a36e-bfb9ddaa93b1)
![screenshot-20231119-165448](https://github.com/kernelpanic95/dotfiles/assets/89152958/816d07c2-2269-4815-bf4d-308ce92dfaa1)
![screenshot-20231119-165254](https://github.com/kernelpanic95/dotfiles/assets/89152958/c9d20db2-8aca-45c2-95cc-785d4dd2bc8d)
![screenshot-20231119-165129](https://github.com/kernelpanic95/dotfiles/assets/89152958/93a5c154-f7cf-4a4f-9677-69390f5e547d)
![screenshot-20231119-165006](https://github.com/kernelpanic95/dotfiles/assets/89152958/4536ef1d-6ff3-421c-92e2-a43270b4c199)
![screenshot-20231119-164930](https://github.com/kernelpanic95/dotfiles/assets/89152958/435ba1d6-9349-48dd-9fcd-0f7bc88f6e3c)
![screenshot-20231119-000036](https://github.com/kernelpanic95/dotfiles/assets/89152958/554c0a60-14bc-4e0a-bb24-fa9ea072b6a9)

## common packages
<details>
<summary></summary>

- Terminal: alacritty
- Editor: nvim
- Prompt: starship
- Icons: Font Awesome
- Menus: Rofi
- Colorscheme: pywal (dynamic)
- Browsers: firefox
- Filemanager: Nautilus, Thunar
- Cursor: Bibata Modern Classic
- Icons: Kora-Icon-Theme
- Theme: Breeze-dark
- Virtual Machine: qemu 
</details>

## Hyprland
<details>
<summary></summary>

- Status Bar: waybar
- Screenshots: grim & slurp
- Clipboard Manager: cliphist
- Logout: wlogout
- Screenlock: swaylock-effects
</details>

## qtile
<details>
<summary></summary>

- Compositor: picom
- Status Bar: polybar
- Screenshots: scrot
</details>

## templating

Included is a pywal configuration that changes the color scheme based on a randomly selected wallpaper. With the key binding SuperKey + Shift + w you can change the wallpaper. SuperKey + Ctrl + w opens rofi with a list of installed wallpapers for your individual selection. See also the .bashrc and the key bindings on Hyprland and Qtile for more alias definitions.


## installation

To make it easy for you to get started with my dotfiles, here's a list of recommended next steps.

PLEASE BACKUP YOUR EXISTING .config WITH YOUR DOTFILES BEFORE STARTING THE SCRIPTS.

```
# Make sure that you're in your home directory
cd

# Clone the repository from your home directory
git clone https://github.com/kernelpanic95/dotfiles.git

# Or download the lastest version and unzip into ~/dotfiles folder

# Change into the new dotfiles folder
cd dotfiles

# Install all required packages
./1-install.sh

# Install hyprland window manager
./2-install-hyprland.sh
# OR/AND Install qtile window manager
./2-install-qtile.sh

# Install dotfiles
./3-install-dotfiles.sh

```
Please note that every Arch Linux system is different and I cannot guarantee that everything works fine on your system.

