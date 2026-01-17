"""
Módulo para generar la salida HTML del CV.
"""

import os
from jinja2 import Environment, FileSystemLoader
from datos_persona1 import datos as datos1, form as form1, langs as langs1, xp as xp1, skills as skills1, folio as folio1
from datos_persona2 import datos as datos2, form as form2, langs as langs2, xp as xp2, skills as skills2, folio as folio2
from datos_persona3 import datos as datos3, form as form3, langs as langs3, xp as xp3, skills as skills3, folio as folio3


def generar_html_cv(persona: int = 3) -> None:
    """Genera el HTML del CV usando Jinja2 con los datos de la persona especificada."""
    if persona == 1:
        datos, form, langs, xp, skills, folio = datos1, form1, langs1, xp1, skills1, folio1
        plantilla = "plantilla_cv.html"
    elif persona == 2:
        datos, form, langs, xp, skills, folio = datos2, form2, langs2, xp2, skills2, folio2
        plantilla = "plantilla_cv_persona2.html"
    elif persona == 3:
        datos, form, langs, xp, skills, folio = datos3, form3, langs3, xp3, skills3, folio3
        plantilla = "plantilla_cv_persona3.html"
    else:
        raise ValueError("PERSONA debe ser 1, 2 o 3")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(os.path.dirname(script_dir), "templates")
    generado_dir = os.path.join(os.path.dirname(script_dir), "generado")
    
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template(plantilla)
    
    html = template.render(
        datos=datos.to_dict(),
        formacion=form.to_dict(),
        idiomas=langs.to_dict(),
        experiencia=xp.to_dict(),
        habilidades=skills.to_dict(),
        portafolio=folio.to_dict()
    )
    
    output_file = os.path.join(generado_dir, "cv_generado.html")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"✓ CV generado exitosamente: {output_file}")



