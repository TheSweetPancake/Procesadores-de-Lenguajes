from datosPersonales import DatosPersonales
from formacion import Formacion, FormacionItem
from idiomas import Idiomas, Idioma
from experiencia import Experiencia, ExperienciaItem
from habilidades import Habilidades, Habilidad
from portafolio import Portafolio, Proyecto, Merito


# Datos de la segunda persona - Martín González Rodríguez
datos = DatosPersonales(
    nombre="Martín González Rodríguez",
    foto=None,  # poner ruta de la imagen
    fecha_nacimiento="1995-06-15",
    bio="Ingeniero de Software especializado en desarrollo fullstack con 6 años de experiencia en arquitectura de microservicios y optimización de rendimiento.",
    email="martin.gonzalez@email.com",
    telefono="+34 678 543 210",
    linkedin="/in/martingonzalez",
    github="/martingonzalez",
    web="https://martingonzalez.dev"
)

form = Formacion(items=[
    FormacionItem(
        titulo="Grado en Ingeniería Informática",
        institucion="Universitat Politècnica de València",
        descripcion="Especialización en ingeniería de software",
        logros="Calificación final: 7.8/10",
        fecha="2018-06-15",
        en_curso=False,
        tipo="oficial"
    ),
    FormacionItem(
        titulo="Certificación AWS Solutions Architect Associate",
        institucion="Amazon Web Services",
        descripcion=None,
        logros=None,
        fecha="2023-03-20",
        en_curso=False,
        tipo="complementaria"
    ),
    FormacionItem(
        titulo="Certificación Spring Professional",
        institucion="VMware",
        descripcion=None,
        logros=None,
        fecha="2022-11-10",
        en_curso=False,
        tipo="complementaria"
    ),
    FormacionItem(
        titulo="Curso Advanced React Patterns",
        institucion="Egghead.io",
        descripcion=None,
        logros=None,
        fecha="2023-09-15",
        en_curso=True,
        tipo="complementaria"
    ),
])

langs = Idiomas(idiomas=[
    Idioma(nombre="Español", nivel="Nativo"),
    Idioma(nombre="Inglés", nivel="Fluido", expedidor="IELTS 7.5 - 2022"),
    Idioma(nombre="Francés", nivel="Básico", expedidor="A2")
])

xp = Experiencia(experiencias=[
    ExperienciaItem(
        tipo="laboral",
        organizacion="TechVision Solutions",
        puesto="Senior Backend Developer",
        descripcion="Desarrollo y mantenimiento de microservicios usando Spring Boot y Node.js. Implementación de sistemas de caché distribuido con Redis. Reducción de tiempo de respuesta en 40%.",
        horas=40
    ),
    ExperienciaItem(
        tipo="laboral",
        organizacion="Innovatech Startup",
        puesto="Full Stack Developer",
        descripcion="Desarrollo de plataforma web de e-commerce con React y Django. Implementación de pasarela de pagos y sistema de notificaciones en tiempo real.",
        horas=40
    ),
    ExperienciaItem(
        tipo="laboral",
        organizacion="WebDevelopers Company",
        puesto="Junior Developer",
        descripcion="Desarrollo de aplicaciones web responsivas. Participación en refactorización de código legacy y mejora de cobertura de tests.",
        horas=40
    ),
    ExperienciaItem(
        tipo="autónomo",
        organizacion="Proyecto independiente",
        puesto="Freelancer Full Stack",
        descripcion="Desarrollo de soluciones web personalizadas para pequeñas empresas y startups.",
        horas=20
    ),
])

skills = Habilidades(habilidades=[
    Habilidad(nombre="Java", tipo="hard", categoria="Backend", nivel="Avanzado"),
    Habilidad(nombre="Spring Boot", tipo="hard", categoria="Backend", nivel="Avanzado"),
    Habilidad(nombre="Node.js", tipo="hard", categoria="Backend", nivel="Avanzado"),
    Habilidad(nombre="React", tipo="hard", categoria="Frontend", nivel="Avanzado"),
    Habilidad(nombre="TypeScript", tipo="hard", categoria="Frontend", nivel="Avanzado"),
    Habilidad(nombre="PostgreSQL", tipo="hard", categoria="Bases de Datos", nivel="Avanzado"),
    Habilidad(nombre="MongoDB", tipo="hard", categoria="Bases de Datos", nivel="Avanzado"),
    Habilidad(nombre="Docker", tipo="hard", categoria="DevOps", nivel="Intermedio"),
    Habilidad(nombre="Kubernetes", tipo="hard", categoria="DevOps", nivel="Intermedio"),
    Habilidad(nombre="AWS", tipo="hard", categoria="Cloud", nivel="Intermedio"),
    Habilidad(nombre="Git", tipo="hard", categoria="Control de versiones", nivel="Avanzado"),
    Habilidad(nombre="Agile/Scrum", tipo="soft", categoria="Metodología", nivel="Avanzado"),
])

folio = Portafolio(
    proyectos=[
        Proyecto(
            nombre="Sistema de Gestión de Inventario Inteligente",
            descripcion="Plataforma completa de inventario con predicción de demanda usando Machine Learning. Desarrollada con Spring Boot en backend y React en frontend.",
            categoria="E-commerce",
            tecnologias=["Spring Boot", "React", "PostgreSQL", "TensorFlow", "Docker", "Kubernetes"],
            web="https://github.com/martingonzalez/inventory-system",
            grupo=["Martín González", "Carlos López", "Ana Martínez"]
        ),
        Proyecto(
            nombre="API REST de Análisis de Datos en Tiempo Real",
            descripcion="API escalable para procesamiento y análisis de millones de eventos por día. Integración con Kafka y Elasticsearch para búsqueda avanzada.",
            categoria="Analytics",
            tecnologias=["Node.js", "Apache Kafka", "Elasticsearch", "MongoDB", "AWS"],
            web="https://github.com/martingonzalez/realtime-analytics-api"
        ),
        Proyecto(
            nombre="Aplicación de Redes Sociales Descentralizada",
            descripcion="Red social descentralizada con contratos inteligentes. Uso de Web3.js y Ethereum.",
            categoria="Blockchain",
            tecnologias=["Solidity", "Web3.js", "React", "Node.js", "Ethereum"],
            web="https://github.com/martingonzalez/decentralized-social",
            grupo=["Martín González", "Laura Fernández"]
        ),
    ],
    meritos=[
        Merito(nombre="Desarrollador del Año 2023", descripcion="Reconocimiento de TechVision Solutions por contribución técnica excepcional"),
        Merito(nombre="Speaker en JSConf Spain 2023", descripcion="Presentación sobre optimización de rendimiento en React"),
        Merito(nombre="Mentor de Coding Bootcamp", descripcion="Ha guiado a 15+ nuevos desarrolladores en su carrera profesional"),
        Merito(nombre="Publicaciones técnicas", descripcion="8 artículos en Medium sobre arquitectura de software"),
    ]
)
