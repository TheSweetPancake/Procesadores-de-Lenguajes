from datosPersonales import DatosPersonales
from formacion import Formacion, FormacionItem
from idiomas import Idiomas, Idioma
from experiencia import Experiencia, ExperienciaItem
from habilidades import Habilidades, Habilidad
from portafolio import Portafolio, Proyecto, Merito

# Datos Personales Ampliados
datos = DatosPersonales(
    nombre="Elena Rivas Castro",
    foto=None, 
    fecha_nacimiento="1992-03-22",
    bio="Diseñadora UX/UI Senior y Product Strategist con más de 8 años de experiencia transformando ideas complejas en interfaces intuitivas. Experta en liderar procesos de User Research, creación de Design Systems escalables y optimización de la tasa de conversión (CRO). Enfocada en la accesibilidad y el diseño centrado en el ser humano.",
    email="elena.rivas@uxdesign.com",
    telefono="+34 611 222 333",
    linkedin="linkedin.com/in/elenarivas",
    github="github.com/elenarivas-design",
    web="https://elenarivas.pro"
)

# Formación Ampliada
form = Formacion(items=[
    FormacionItem(
        titulo="Máster en Diseño de Interacción y Experiencia de Usuario (UX)",
        institucion="IED Madrid",
        descripcion="Especialización en prototipado de alta fidelidad, flujos de usuario complejos y psicología del color aplicada a interfaces.",
        logros="Premio Extraordinario al mejor proyecto final de máster 2017.",
        fecha="2017-07-15",
        en_curso=False,
        tipo="Postgrado"
    ),
    FormacionItem(
        titulo="Grado en Diseño Gráfico y Comunicación Visual",
        institucion="Escuela de Arte de Sevilla",
        descripcion="Fundamentos de tipografía, composición, teoría del diseño y branding.",
        logros="Matrícula de honor en Proyectos Editoriales.",
        fecha="2014-06-20",
        en_curso=False,
        tipo="Grado Universitario"
    ),
    FormacionItem(
        titulo="Certificación en Google UX Design",
        institucion="Coursera / Google",
        descripcion="Enfoque profesional en el proceso de diseño: empatizar, definir, idear, prototipar y probar.",
        logros=None,
        fecha="2021-02-10",
        en_curso=False,
        tipo="Certificación Internacional"
    )
])

# Idiomas
langs = Idiomas(idiomas=[
    Idioma(nombre="Español", nivel="Nativo"),
    Idioma(nombre="Inglés", nivel="C1 - Avanzado (Cambridge Advanced)"),
    Idioma(nombre="Francés", nivel="B2 - Intermedio"),
    Idioma(nombre="Alemán", nivel="A1 - Básico")
])

# Experiencia Laboral Ampliada
xp = Experiencia(experiencia=[
    ExperienciaItem(
        puesto="Senior Product Designer",
        organizacion="Creative Minds Agency",
        tipo="Remoto",
        descripcion="Liderazgo creativo en el rediseño de la plataforma fintech 'PayLite'. Reduje el 'churn rate' en un 15% mediante la simplificación del flujo de onboarding y la creación de un Design System propio en Figma utilizado por 3 equipos de desarrollo.",
        fecha_inicio="2020-05-01"
    ),
    ExperienciaItem(
        puesto="UX/UI Designer & Researcher",
        organizacion="TechStart Lab",
        tipo="Presencial",
        descripcion="Encargada de realizar tests de usabilidad con usuarios reales y moderar sesiones de Lean UX. Diseño de dashboards de análisis de datos masivos para clientes gubernamentales.",
        fecha_inicio="2017-09-01"
    ),
    ExperienciaItem(
        puesto="Junior Visual Designer",
        organizacion="Estudio Gráfico Imprime",
        tipo="Híbrido",
        descripcion="Creación de identidades visuales para startups, diseño de materiales de marketing digital y apoyo en la maquetación de landings.",
        fecha_inicio="2014-10-01"
    )
])

# Habilidades Ampliadas
skills = Habilidades(habilidades=[
    Habilidad(nombre="Figma & Auto Layout", nivel="Experto", categoria="Diseño"),
    Habilidad(nombre="Design Systems", nivel="Avanzado", categoria="Estrategia"),
    Habilidad(nombre="User Research", nivel="Experto", categoria="Investigación"),
    Habilidad(nombre="Prototipado (Principle/Protopie)", nivel="Avanzado", categoria="Herramientas"),
    Habilidad(nombre="HTML5 & CSS3 (Flexbox/Grid)", nivel="Intermedio", categoria="Tecnología"),
    Habilidad(nombre="Accesibilidad Web (WCAG)", nivel="Avanzado", categoria="Estándares"),
    Habilidad(nombre="Metodologías Ágiles (Scrum)", nivel="Avanzado", categoria="Gestión"),
    Habilidad(nombre="Adobe Creative Suite", nivel="Experto", categoria="Diseño")
])

# Portafolio y Méritos Ampliados
folio = Portafolio(
    proyectos=[
        Proyecto(
            nombre="EcoApp Mobile",
            descripcion="Aplicación móvil para la gestión de huella de carbono personal. Incluye gamificación y red social.",
            categoria="UX/UI Design & Strategy",
            tecnologias=["Figma", "User Testing", "Lottie Animations"],
            web="https://behance.net/ecoapp"
        ),
        Proyecto(
            nombre="AquaSphere Web Portal",
            descripcion="Plataforma de gestión de recursos hídricos para Smart Cities. Interfaz compleja de mapas y gráficos.",
            categoria="Dashboard Design",
            tecnologias=["Figma", "Design Systems", "D3.js integration"],
            web="https://aquasphere.io"
        ),
        Proyecto(
            nombre="FinTrack Extension",
            descripcion="Extensión de navegador para control de gastos mediante IA.",
            categoria="Product Design",
            tecnologias=["Adobe XD", "UI Motion"],
            web=None
        )
    ],
    meritos=[
        Merito(nombre="Awwwards Honorable Mention 2022", descripcion="Reconocimiento por el diseño visual y experiencia de usuario del proyecto AquaSphere."),
        Merito(nombre="Top Designer en Behance (UX)", descripcion="Inclusión en la galería 'Best of Behance' en 3 ocasiones durante 2023."),
        Merito(nombre="Ponente en UX Spain 2023", descripcion="Charla magistral sobre 'Sistemas de Diseño en equipos remotos'."),
        Merito(nombre="Publicación en Smashing Magazine", descripcion="Artículo técnico sobre microinteracciones y feedback emocional.")
    ]
)
