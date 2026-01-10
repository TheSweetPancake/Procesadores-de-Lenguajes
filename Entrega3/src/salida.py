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

# Asegurar que el directorio de salida existe
if not os.path.exists(generado_dir):
    os.makedirs(generado_dir)

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

# Cambiamos el nombre del archivo de salida para identificarlo fácilmente
output_filename = f"cv_generado_persona{PERSONA}.html"
output_file = os.path.join(generado_dir, output_filename)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Guardado {output_filename} usando la plantilla: {plantilla}")