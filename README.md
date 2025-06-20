DEPENDENCIAS:
    global: archiso git python python-yaml make sudo


git clone https://github.com/nickespro1305/DesktopStudio

pacman -Syu --noconfirm && pacman -S archiso git python python-yaml make sudo --noconfirm && git clone https://github.com/nickespro1305/DesktopStudio && cd DesktopStudio