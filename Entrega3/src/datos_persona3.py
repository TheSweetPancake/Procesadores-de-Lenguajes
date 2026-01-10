from datosPersonales import DatosPersonales
from formacion import Formacion, FormacionItem
from idiomas import Idiomas, Idioma
from experiencia import Experiencia, ExperienciaItem
from habilidades import Habilidades, Habilidad
from portafolio import Portafolio, Proyecto, Merito


# Datos de la tercera persona - Laura Martínez Ortega
datos = DatosPersonales(
    nombre="Laura Martínez Ortega",
    foto=None,  # poner ruta de la imagen
    fecha_nacimiento="1993-03-22",
    bio="Diseñadora UX/UI y Desarrolladora Frontend con 7 años de experiencia creando experiencias digitales intuitivas y accesibles. Especializada en Design Systems y React.",
    email="laura.martinez@email.com",
    telefono="+34 612 345 678",
    linkedin="/in/lauramartinezux",
    github="/lauramartinez",
    web="https://lauramartinez.design"
)

form = Formacion(items=[
    FormacionItem(
        titulo="Grado en Diseño Digital y Multimedia",
        institucion="Universidad Complutense de Madrid",
        descripcion="Especialización en diseño de interfaces y experiencia de usuario",
        logros="Premio al mejor proyecto final: 'Sistema de diseño para apps de salud'",
        fecha="2016-06-20",
        en_curso=False,
        tipo="oficial"
    ),
    FormacionItem(
        titulo="Máster en Desarrollo Frontend Avanzado",
        institucion="Escuela de Organización Industrial (EOI)",
        descripcion="Programación avanzada en JavaScript, React y arquitectura frontend",
        logros=None,
        fecha="2019-11-15",
        en_curso=False,
        tipo="complementaria"
    ),
    FormacionItem(
        titulo="Certificación en Accesibilidad Web WCAG 2.1",
        institucion="Interaction Design Foundation",
        descripcion=None,
        logros="Puntuación: 98/100",
        fecha="2022-05-10",
        en_curso=False,
        tipo="complementaria"
    ),
    FormacionItem(
        titulo="Curso de Diseño de Producto Avanzado",
        institucion="Coursera - Google UX Design",
        descripcion="Metodologías de investigación de usuarios y testing",
        logros=None,
        fecha="2023-09-01",
        en_curso=True,
        tipo="complementaria"
    ),
])

langs = Idiomas(idiomas=[
    Idioma(nombre="Español", nivel="Nativo"),
    Idioma(nombre="Inglés", nivel="Avanzado", expedidor="C1 Cambridge - 2021"),
    Idioma(nombre="Alemán", nivel="Intermedio", expedidor="B1 Goethe - 2020")
])

xp = Experiencia(experiencias=[
    ExperienciaItem(
        tipo="laboral",
        organizacion="DigitalMind Agency",
        puesto="Lead UX/UI Designer",
        descripcion="Liderazgo del equipo de diseño. Creación y mantenimiento del Design System utilizado en 15+ proyectos. Aumento del 25% en la satisfacción del usuario en proyectos clave.",
        horas=40
    ),
    ExperienciaItem(
        tipo="laboral",
        organizacion="TechCreators Inc.",
        puesto="Senior Frontend Developer & UX Designer",
        descripcion="Desarrollo de componentes React reutilizables. Implementación de arquitectura basada en micro-frontends. Colaboración directa con equipo de producto.",
        horas=40
    ),
    ExperienciaItem(
        tipo="laboral",
        organizacion="StartupLabs",
        puesto="Diseñadora UX/UI",
        descripcion="Diseño de interfaces para aplicaciones móviles y web. Realización de tests de usabilidad y entrevistas con usuarios.",
        horas=40
    ),
    ExperienciaItem(
        tipo="voluntariado",
        organizacion="Design for Good NGO",
        puesto="Consultora de Accesibilidad",
        descripcion="Voluntariado para mejorar la accesibilidad de plataformas educativas para personas con discapacidad visual.",
        horas=10
    ),
])

skills = Habilidades(habilidades=[
    Habilidad(nombre="Figma", tipo="hard", categoria="Diseño", nivel="Avanzado"),
    Habilidad(nombre="Adobe Creative Suite", tipo="hard", categoria="Diseño", nivel="Avanzado"),
    Habilidad(nombre="React", tipo="hard", categoria="Frontend", nivel="Avanzado"),
    Habilidad(nombre="TypeScript", tipo="hard", categoria="Frontend", nivel="Avanzado"),
    Habilidad(nombre="Next.js", tipo="hard", categoria="Frontend", nivel="Intermedio"),
    Habilidad(nombre="Storybook", tipo="hard", categoria="Herramientas", nivel="Avanzado"),
    Habilidad(nombre="Design Systems", tipo="hard", categoria="Diseño", nivel="Avanzado"),
    Habilidad(nombre="User Research", tipo="hard", categoria="UX", nivel="Intermedio"),
    Habilidad(nombre="Prototyping", tipo="hard", categoria="UX", nivel="Avanzado"),
    Habilidad(nombre="Git", tipo="hard", categoria="Control de versiones", nivel="Intermedio"),
    Habilidad(nombre="Tailwind CSS", tipo="hard", categoria="Frontend", nivel="Avanzado"),
    Habilidad(nombre="Trabajo en equipo", tipo="soft", categoria="Habilidades", nivel="Avanzado"),
    Habilidad(nombre="Comunicación", tipo="soft", categoria="Habilidades", nivel="Avanzado"),
    Habilidad(nombre="Pensamiento crítico", tipo="soft", categoria="Habilidades", nivel="Avanzado"),
])

folio = Portafolio(
    proyectos=[
        Proyecto(
            nombre="Sistema de Diseño Aurora",
            descripcion="Design System completo para empresa fintech con 50+ componentes accesibles y documentados. Implementado en React y Figma.",
            categoria="Design System",
            tecnologias=["Figma", "React", "TypeScript", "Storybook", "Jest", "Cypress"],
            web="https://github.com/lauramartinez/aurora-design-system",
            grupo=["Laura Martínez", "Carlos Ruiz", "Ana López"]
        ),
        Proyecto(
            nombre="App de Salud Mental MindCare",
            descripcion="Aplicación móvil para seguimiento del bienestar emocional con interfaz empática y accesible. Ganadora del premio UX Awards 2022.",
            categoria="Salud Digital",
            tecnologias=["React Native", "Figma", "Node.js", "MongoDB", "AWS"],
            web="https://mindcare-app.com"
        ),
        Proyecto(
            nombre="Plataforma de E-learning Accesible",
            descripcion="Rediseño completo de plataforma educativa para cumplir con WCAG 2.1 AA. Mejora del 40% en accesibilidad.",
            categoria="Educación",
            tecnologias=["Vue.js", "Figma", "Django", "PostgreSQL", "Lighthouse"],
            web="https://github.com/lauramartinez/accessible-learning",
            grupo=["Laura Martínez", "Miguel Torres"]
        ),
    ],
    meritos=[
        Merito(nombre="Premio UX Awards 2022", descripcion="Mejor diseño de app de salud por MindCare"),
        Merito(nombre="Speaker en React Conf 2023", descripcion="Charla 'Design Systems en React: más allá de los componentes'"),
        Merito(nombre="Mentora en Women Who Code", descripcion="Mentoría a 20+ mujeres en diseño y desarrollo frontend"),
        Merito(nombre="Publicaciones en Smashing Magazine", descripcion="3 artículos sobre accesibilidad y sistemas de diseño"),
        Merito(nombre="Certificación Adobe Certified Expert", descripcion="Photoshop y Illustrator 2023"),
    ]
)
