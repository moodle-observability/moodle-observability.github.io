"""Gera os rasters (PNG 512, apple-touch-icon 180, favicon.ico 16/32/48) a partir dos SVGs.

Renderiza cada SVG com o Chrome/Edge headless em 512x512 e reduz com Pillow (LANCZOS).

Uso: python pages/scripts/gerar_rasters.py  (a partir da pasta do workspace, com os plugins clonados ao lado)
Requisitos: Pillow e Google Chrome ou Microsoft Edge instalados.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

RAIZ = Path(__file__).resolve().parents[2]  # pasta do workspace (contém pages/ e tool_*/)
NAVEGADORES = [
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
]
TAMANHOS_ICO = [(16, 16), (32, 32), (48, 48)]


def navegador() -> str:
    for nome in ("chrome", "google-chrome", "chromium", "msedge"):
        achado = shutil.which(nome)
        if achado:
            return achado
    for caminho in NAVEGADORES:
        if caminho.exists():
            return str(caminho)
    sys.exit("erro: Chrome/Edge não encontrado para renderizar os SVGs.")


def renderizar(svg: Path, destino: Path, exe: str) -> Image.Image:
    with tempfile.TemporaryDirectory() as tmp:
        html = Path(tmp) / "r.html"
        png = Path(tmp) / "r.png"
        # SVG embutido inline: evita falha de carregamento de <img> por caminho/permissão.
        html.write_text(
            "<!doctype html><html><head><style>html,body{margin:0;padding:0;overflow:hidden}"
            "svg{display:block;width:512px;height:512px}</style></head><body>"
            + svg.read_text(encoding="utf-8")
            + "</body></html>",
            encoding="utf-8",
        )
        subprocess.run(
            [
                exe,
                "--headless=new",
                "--disable-gpu",
                "--hide-scrollbars",
                "--force-device-scale-factor=1",
                "--window-size=512,512",
                f"--screenshot={png}",
                html.as_uri(),
            ],
            check=True,
            capture_output=True,
            timeout=60,
        )
        if not png.exists():
            sys.exit(f"erro: o navegador não gerou captura para {svg}.")
        img = Image.open(png).convert("RGB").crop((0, 0, 512, 512))
        img.load()
    img.save(destino, optimize=True)
    return img


def validar(img: Image.Image, svg: Path) -> None:
    # Os logos têm fundo branco: canto preto indica renderização quebrada.
    if img.getpixel((2, 2)) != (255, 255, 255):
        sys.exit(f"erro: renderização inválida de {svg} (canto não é branco).")


def main() -> None:
    exe = navegador()
    alvos: list[tuple[Path, Path, Path | None, Path]] = [
        (
            RAIZ / "pages/img/logo.svg",
            RAIZ / "pages/img/logo-512.png",
            RAIZ / "pages/img/apple-touch-icon.png",
            RAIZ / "pages/favicon.ico",
        )
    ]
    for logo in sorted([*RAIZ.glob("tool_*/docs/logo/logo.svg"), *RAIZ.glob("logstore_*/docs/logo/logo.svg")]):
        pasta = logo.parent
        alvos.append((logo, pasta / "logo-512.png", None, pasta / "favicon.ico"))

    for svg, png512, apple, ico in alvos:
        img = renderizar(svg, png512, exe)
        validar(img, svg)
        if apple is not None:
            img.resize((180, 180), Image.LANCZOS).save(apple, optimize=True)
        img.save(ico, format="ICO", sizes=TAMANHOS_ICO)
        print(f"ok: {svg.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
