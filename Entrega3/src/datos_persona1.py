from datosPersonales import DatosPersonales
from formacion import Formacion, FormacionItem
from idiomas import Idiomas, Idioma
from experiencia import Experiencia, ExperienciaItem
from habilidades import Habilidades, Habilidad
from portafolio import Portafolio, Proyecto, Merito


# Datos de la primera persona
datos = DatosPersonales(
    nombre="Diu me cagoen",
    foto=None,  # poner ruta de la imagen
    fecha_nacimiento="1995-11-01",
    bio="Desarrollador de IA y software",
    email="baltasar@example.com",
    telefono="+34 600 000 000",
    linkedin="/in/baltasarlopez",
    github="/baltasar-dev",
    web="https://baltasar.dev"
)

form = Formacion(items=[
    FormacionItem(
        titulo="Licenciatura en Informática",
        institucion="Universidad Nacional",
        descripcion="Desarrollo de software",
        logros="Tesis en PLN",
        fecha="2018-12-15",
        en_curso=False,
        tipo="oficial"
    ),
    FormacionItem(
        titulo="Curso de Python Avanzado",
        institucion="Coursera",
        descripcion=None,
        logros=None,
        fecha="2022-06-20",
        en_curso=False,
        tipo="complementaria"
    ),
])

langs = Idiomas(idiomas=[
    Idioma(nombre="Español", nivel="Nativo"),
    Idioma(nombre="Inglés", nivel="C1", expedidor="Cambridge")
])

xp = Experiencia(experiencias=[
    ExperienciaItem(
        tipo="laboral",
        organizacion="TechCorp",
        puesto="Backend Developer",
        descripcion="Microservicios en Python",
        horas=40
    ),
    ExperienciaItem(
        tipo="voluntariado",
        organizacion="CodeForGood",
        puesto="Mentor",
        descripcion="Talleres de programación para jóvenes",
        horas=8
    ),
])

skills = Habilidades(habilidades=[
    Habilidad(nombre="Liderazgo", tipo="soft"),
    Habilidad(nombre="Comunicación", tipo="soft"),
    Habilidad(nombre="Python", tipo="hard", categoria="Programación", nivel="Avanzado"),
    Habilidad(nombre="TensorFlow", tipo="hard", categoria="IA", nivel="Intermedio"),
])

folio = Portafolio(
    proyectos=[
        Proyecto(
            nombre="Sistema de Recomendación",
            descripcion="Filtrado colaborativo para e-commerce",
            categoria="Machine Learning",
            tecnologias=["Python", "Pandas", "TensorFlow"],
            web="https://recomsys.example.com",
            grupo=["Laura Pérez", "Carlos Díaz"]
        ),
        Proyecto(
            nombre="Web Personal",
            descripcion="Blog y portafolio",
            categoria="Desarrollo Web",
            tecnologias=["HTML", "CSS", "JavaScript"],
            web="https://baltasar.dev"
        ),
    ],
    meritos=[
        Merito(nombre="Premio Innovación", descripcion="Soluciones con IA"),
        Merito(nombre="Beca Excelencia", descripcion="Rendimiento académico"),
    ]
)
