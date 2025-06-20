#!/usr/bin/env bash
set -e

# Montar tmpfs en pacman cache para evitar problema de espacio
mkdir -p /var/cache/pacman/pkg
mount -t tmpfs -o size=10G tmpfs /var/cache/pacman/pkg

# Inicializar keyring para pacman
pacman-key --init
pacman-key --populate archlinux

# Actualizar y sincronizar base de datos de paquetes
pacman -Sy --noconfirm

# Instalar paquetes sin sudo (root)
pacman -S --noconfirm i3-wm xorg xorg-xinit i3status dmenu alacritty

# Autologin root en tty1
mkdir -p /etc/systemd/system/getty@tty1.service.d
cat > /etc/systemd/system/getty@tty1.service.d/autologin.conf <<EOF
[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin root --noclear %I \$TERM
EOF

# Configurar startx automático para root
echo '[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && exec startx' > /root/.bash_profile

# Desmontar tmpfs cache para limpiar
umount /var/cache/pacman/pkg || true
