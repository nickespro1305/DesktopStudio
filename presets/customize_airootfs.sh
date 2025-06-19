#!/usr/bin/env bash
set -e

USER_NAME="{{user_name}}"
USER_PASS="{{user_password}}"
USER_GROUPS="{{user_groups}}"

# Crear usuario con home y grupos
useradd -m -G "$USER_GROUPS" -s /bin/bash "$USER_NAME"

# Asignar contraseña
echo "$USER_NAME:$USER_PASS" | chpasswd

# Instalar sudo
pacman -Sy --noconfirm sudo

# Configurar sudoers
echo "%wheel ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/wheel
chmod 440 /etc/sudoers.d/wheel

# Autologin root en tty1
mkdir -p /etc/systemd/system/getty@tty1.service.d
cat > /etc/systemd/system/getty@tty1.service.d/autologin.conf <<EOF
[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin root --noclear %I \$TERM
EOF

# .bash_profile para autostart i3 en root
echo '[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && exec startx' > /root/.bash_profile

# .bash_profile para usuario nuevo que autoejecute startx
echo '[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && exec startx' > /home/"$USER_NAME"/.bash_profile
chown "$USER_NAME":"$USER_NAME" /home/"$USER_NAME"/.bash_profile
