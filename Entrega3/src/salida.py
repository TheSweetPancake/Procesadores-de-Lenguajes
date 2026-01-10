import os
from jinja2 import Environment, FileSystemLoader

PERSONA = 3

if PERSONA == 1:
    from datos_persona1 import datos, form, langs, xp, skills, folio
    plantilla = "plantilla_cv.html"
elif PERSONA == 2:
    from datos_persona2 import datos, form, langs, xp, skills, folio
    plantilla = "plantilla_cv_persona2.html"
elif PERSONA == 3:
    from datos_persona2 import datos, form, langs, xp, skills, folio 
    plantilla = "plantilla_cv_persona3.html"
else:
    raise ValueError("PERSONA debe ser 1, 2 o 3")

######################################## fin de la selección de datos ########################################

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


output_file = os.path.join(generado_dir, "index.html")
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html)


print("Guardado index.html")
