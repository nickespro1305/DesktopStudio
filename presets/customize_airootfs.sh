#!/usr/bin/env bash
set -e

rm -f /var/db/Makefile

mkdir -p /tmp/pacman-cache
echo "CacheDir = /tmp/pacman-cache" >> /etc/pacman.conf

mount -t proc none /proc || true
mount --rbind /sys /sys || true
mount --rbind /dev /dev || true

USER_NAME="{{user_name}}"
USER_PASS="{{user_password}}"
USER_GROUPS="{{user_groups}}"

# Crear usuario con home y grupos, si no existe
if ! id "$USER_NAME" &>/dev/null; then
  echo "[INFO] Creando usuario $USER_NAME..."
  useradd -m -G "$USER_GROUPS" -s /bin/bash "$USER_NAME"
  echo "$USER_NAME:$USER_PASS" | chpasswd
else
  echo "[INFO] Usuario $USER_NAME ya existe, omitiendo creación y contraseña."
fi

# Inicializar el keyring de pacman
echo "[INFO] Inicializando keyring..."
pacman-key --init
pacman-key --populate archlinux


# Instalar sudo
pacman -Sy --noconfirm sudo

# Configurar sudoers
echo "%wheel ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/wheel
chmod 440 /etc/sudoers.d/wheel

# Autologin de root en tty1 (opcional, puedes quitar si no lo necesitas)
mkdir -p /etc/systemd/system/getty@tty1.service.d
cat > /etc/systemd/system/getty@tty1.service.d/autologin.conf <<EOF
[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin root --noclear %I \$TERM
EOF

# .bash_profile para autostart i3 en root
echo '[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && exec startx' > /root/.bash_profile

# .bash_profile para el nuevo usuario
echo '[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && exec startx' > /home/"$USER_NAME"/.bash_profile
chown "$USER_NAME":"$USER_NAME" /home/"$USER_NAME"/.bash_profile
