from __future__ import annotations
from pathlib import Path
import json
from jinja2 import Environment, FileSystemLoader

def render_jinja(cv_json_path: Path, template_path: Path, output_html_path: Path) -> None:
    """
    Renderiza el JSON del CV usando Jinja2 template.
    
    Args:
        cv_json_path: Ruta al archivo JSON generado por el parser
        template_path: Ruta al template HTML de Jinja2
        output_html_path: Ruta de salida del HTML renderizado
    """
    # Cargar JSON
    with open(cv_json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Configurar Jinja2
    tp = Path(template_path)
    env = Environment(loader=FileSystemLoader(str(tp.parent)))
    template = env.get_template(tp.name)
    
    # Renderizar
    html = template.render(**data)
    
    # Guardar
    Path(output_html_path).write_text(html, encoding="utf-8")
