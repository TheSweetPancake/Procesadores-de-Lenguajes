import argparse
from pathlib import Path
import sys

from jinja2 import Environment, FileSystemLoader

from parsers.antlr_engine import parse_with_antlr


def render_html(data: dict, template_path: str) -> str:
    """Renderiza CV con Jinja2 usando datos del parser.
    
    Args:
        data: Diccionario con datos CV (desde antlr_engine.parse_with_antlr)
        template_path: Ruta al template HTML
    """
    template_path = Path(template_path)
    env = Environment(loader=FileSystemLoader(str(template_path.parent)))
    template = env.get_template(template_path.name)

    html = template.render(
        datos=data["datos"].to_dict() if data["datos"] else {},
        formacion=data["formacion"].to_dict() if data["formacion"] else {"formacion": []},
        idiomas=data["idiomas"].to_dict() if data["idiomas"] else {"idiomas": []},
        experiencia=data["experiencia"].to_dict() if data["experiencia"] else {"experiencia": []},
        habilidades=data["habilidades"].to_dict() if data["habilidades"] else {"habilidades": []},
        portafolio=data["portafolio"].to_dict() if data["portafolio"] else {"proyectos": [], "meritos": []},
    )
    return html


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="Ruta al .cv (ej: entradas/entrada.cv)")
    ap.add_argument("--template", required=True, help="Ruta al .html (ej: templates/plantilla_cv.html)")
    ap.add_argument("--out", required=True, help="Ruta de salida (ej: index.html)")
    args = ap.parse_args()

    input_path = Path(args.input)
    template_path = Path(args.template)
    out_path = Path(args.out)

    if not input_path.exists():
        print(f"[ERROR] No existe input: {input_path}", file=sys.stderr)
        sys.exit(2)

    if not template_path.exists():
        print(f"[ERROR] No existe template: {template_path}", file=sys.stderr)
        sys.exit(2)

    data = parse_with_antlr(input_path)
    html = render_html(data, str(template_path))

    out_path.write_text(html, encoding="utf-8")

    if not out_path.exists() or out_path.stat().st_size == 0:
        print("[ERROR] index.html no se generó o está vacío", file=sys.stderr)
        sys.exit(3)

    print(f"OK -> {out_path} generado")


if __name__ == "__main__":
    main()
