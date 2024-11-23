# Dockerfile
FROM debian:bullseye

# Variables de entorno para configurar el servidor VNC
ENV DISPLAY=:1 \
    VNC_PORT=5901 \
    VNC_RESOLUTION=1920x1080 \
    VNC_DEPTH=24 \
    DEBIAN_FRONTEND=noninteractive

# Actualizar e instalar paquetes necesarios
RUN apt-get update && apt-get install -y \
    gnome-session \
    gnome-terminal \
    x11vnc \
    xvfb \
    dbus-x11 \
    supervisor \
    && apt-get clean

# Crear un usuario no root
RUN useradd -m -s /bin/bash dockeruser

# Crear el directorio .vnc y configurar el archivo de contraseña
RUN mkdir -p /home/dockeruser/.vnc \
    && x11vnc -storepasswd vncpassword /home/dockeruser/.vnc/passwd \
    && chown -R dockeruser:dockeruser /home/dockeruser/.vnc

# Configurar Xvfb y x11vnc
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

VOLUME /home/dockeruser/.config
VOLUME /opt

# Exponer el puerto VNC
EXPOSE $VNC_PORT

# Comando por defecto
CMD ["supervisord", "-n"]
