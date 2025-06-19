import yaml
import subprocess
import os
import shutil

ARCHISO_TEMPLATE = "/usr/share/archiso/configs/releng"
CUSTOM_DIR = "./archiso"
OUTPUT_DIR = "./output"
WORK_DIR = "./work"

def run(cmd):
    print(f"🏃 Ejecutando: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def prepare_dir():
    if os.path.exists(CUSTOM_DIR):
        print("🧹 Borrando configuración previa...")
        shutil.rmtree(CUSTOM_DIR)
    print(f"📁 Copiando plantilla de ArchISO desde {ARCHISO_TEMPLATE}...")
    shutil.copytree(ARCHISO_TEMPLATE, CUSTOM_DIR, symlinks=True)

def add_packages(config):
    pkglist_path = os.path.join(CUSTOM_DIR, "packages.x86_64")
    print("➕ Añadiendo paquetes al listado:")
    with open(pkglist_path, "a") as f:
        for pkg in config.get("packages", []):
            print(f"   - {pkg}")
            f.write(pkg + "\n")

def copy_files(config):
    print("📦 Copiando archivos personalizados:")
    for f in config.get("files", []):
        dest_path = os.path.join(CUSTOM_DIR, "airootfs", f["destination"].lstrip("/"))
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.copy(f["source"], dest_path)
        print(f"   - {f['source']} → {dest_path}")

def build_iso(iso_name):
    print("🛠️  Generando ISO personalizada...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    run(f"mkarchiso -v -w {WORK_DIR} -o {OUTPUT_DIR} {CUSTOM_DIR}")
    final_iso = os.path.join(OUTPUT_DIR, f"{iso_name}.iso")
    print(f"✅ ISO generada: {final_iso}")

def main():
    with open("config.yaml") as f:
        config = yaml.safe_load(f)

    prepare_dir()
    add_packages(config)
    copy_files(config)
    build_iso(config.get("iso_name", "arch-custom"))

if __name__ == "__main__":
    main()
