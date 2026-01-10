from datosPersonales import DatosPersonales
from formacion import Formacion, FormacionItem
from idiomas import Idiomas, Idioma
from experiencia import Experiencia, ExperienciaItem
from habilidades import Habilidades, Habilidad
from portafolio import Portafolio, Proyecto, Merito

# Datos de la tercera persona - Lucía Méndez Riva
datos = DatosPersonales(
    nombre="Lucía Méndez Riva",
    foto=None,  # poner ruta de la imagen
    fecha_nacimiento="1990-11-05",
    bio="Especialista en Ciberseguridad y Ethical Hacking con 10 años de experiencia protegiendo infraestructuras críticas y liderando auditorías de seguridad en entornos cloud.",
    email="lucia.mendez@security.net",
    telefono="+34 600 111 222",
    linkedin="/in/luciamendezsec",
    github="/lusec-dev",
    web="https://lusec.io"
)

form = Formacion(items=[
    FormacionItem(
        titulo="Grado en Ingeniería de Ciberseguridad",
        institucion="Universidad Rey Juan Carlos",
        descripcion="Enfoque en criptografía avanzada y seguridad en redes.",
        logros="Premio al mejor proyecto fin de carrera en seguridad ofensiva",
        fecha="2013-07-10",
        en_curso=False,
        tipo="oficial"
    ),
    FormacionItem(
        titulo="Certified Information Systems Security Professional (CISSP)",
        institucion="ISC2",
        descripcion=None,
        logros=None,
        fecha="2021-05-15",
        en_curso=False,
        tipo="complementaria"
    ),
    FormacionItem(
        titulo="Offensive Security Certified Professional (OSCP)",
        institucion="Offensive Security",
        descripcion=None,
        logros=None,
        fecha="2019-11-30",
        en_curso=False,
        tipo="complementaria"
    ),
    FormacionItem(
        titulo="Especialista en Análisis Forense Digital",
        institucion="SANS Institute",
        descripcion=None,
        logros=None,
        fecha="2024-01-20",
        en_curso=True,
        tipo="complementaria"
    ),
])

langs = Idiomas(idiomas=[
    Idioma(nombre="Español", nivel="Nativo"),
    Idioma(nombre="Inglés", nivel="C2 - Bilingüe", expedidor="Cambridge Proficiency - 2020"),
    Idioma(nombre="Alemán", nivel="Intermedio", expedidor="B1")
])

xp = Experiencia(experiencias=[
    ExperienciaItem(
        tipo="laboral",
        organizacion="CyberShield Defense Corp",
        puesto="Head of Security Operations (SOC)",
        descripcion="Gestión de incidentes de seguridad a gran escala. Implementación de políticas Zero Trust y supervisión de auditorías externas. Mejora del tiempo de detección de intrusiones en un 60%.",
        horas=45
    ),
    ExperienciaItem(
        tipo="laboral",
        organizacion="Global Bank Solutions",
        puesto="Cybersecurity Analyst",
        descripcion="Pentesting periódico de aplicaciones bancarias y respuesta ante incidentes de fraude digital. Aseguramiento de cumplimiento con normativas ISO 27001.",
        horas=40
    ),
    ExperienciaItem(
        tipo="laboral",
        organizacion="SecureNet Consulting",
        puesto="Security Junior Consultant",
        descripcion="Auditoría de vulnerabilidades en redes corporativas y despliegue de firewalls perimetrales para clientes gubernamentales.",
        horas=40
    ),
    ExperienciaItem(
        tipo="voluntariado",
        organizacion="HackForGood",
        puesto="Mentor de Seguridad",
        descripcion="Asesoramiento en proyectos de impacto social enfocados en la privacidad de datos de usuarios vulnerables.",
        horas=10
    ),
])

skills = Habilidades(habilidades=[
    Habilidad(nombre="Ethical Hacking", tipo="hard", categoria="Seguridad", nivel="Avanzado"),
    Habilidad(nombre="Análisis Forense", tipo="hard", categoria="Seguridad", nivel="Intermedio"),
    Habilidad(nombre="Cloud Security (Azure/AWS)", tipo="hard", categoria="Infraestructura", nivel="Avanzado"),
    Habilidad(nombre="Python (Security Scripts)", tipo="hard", categoria="Programación", nivel="Avanzado"),
    Habilidad(nombre="C++", tipo="hard", categoria="Programación", nivel="Intermedio"),
    Habilidad(nombre="SIEM (Splunk/ELK)", tipo="hard", categoria="Herramientas", nivel="Avanzado"),
    Habilidad(nombre="Kali Linux", tipo="hard", categoria="Herramientas", nivel="Avanzado"),
    Habilidad(nombre="Wireshark", tipo="hard", categoria="Redes", nivel="Avanzado"),
    Habilidad(nombre="VPN & Firewalling", tipo="hard", categoria="Redes", nivel="Avanzado"),
    Habilidad(nombre="Liderazgo de equipos", tipo="soft", categoria="Gestión", nivel="Avanzado"),
    Habilidad(nombre="Gestión de Crisis", tipo="soft", categoria="Gestión", nivel="Avanzado"),
    Habilidad(nombre="Pensamiento Crítico", tipo="soft", categoria="Metodología", nivel="Avanzado"),
])

folio = Portafolio(
    proyectos=[
        Proyecto(
            nombre="Framework de Respuesta Automática ante Incidentes",
            descripcion="Sistema basado en IA para la contención automática de ataques de denegación de servicio (DDoS). Integrado con balanceadores de carga en la nube.",
            categoria="Software de Seguridad",
            tecnologias=["Python", "TensorFlow", "AWS Lambda", "Terraform", "Go"],
            web="https://github.com/lusec-dev/auto-response-framework",
            grupo=["Lucía Méndez", "Roberto Sanz"]
        ),
        Proyecto(
            nombre="Herramienta de Auditoría de Permisos Cloud",
            descripcion="Escáner multicloud para detectar configuraciones erróneas en cubos S3 y roles IAM con privilegios excesivos.",
            categoria="Herramientas Cloud",
            tecnologias=["Go", "Bash", "Azure SDK", "AWS CLI"],
            web="https://github.com/lusec-dev/cloud-audit-scanner"
        ),
        Proyecto(
            nombre="Protocolo de Comunicación Post-Quantum",
            descripcion="Investigación y prototipado de un sistema de mensajería resistente a la computación cuántica usando algoritmos de red.",
            categoria="I+D Criptografía",
            tecnologias=["C++", "OpenSSL", "Rust"],
            web="https://github.com/lusec-dev/pq-messenger",
            grupo=["Lucía Méndez", "Dr. Hans Mueller"]
        ),
    ],
    meritos=[
        Merito(nombre="Hallazgo de Vulnerabilidad Crítica (CVE)", descripcion="Descubrimiento y reporte responsable de una vulnerabilidad de ejecución remota de código en un kernel Linux"),
        Merito(nombre="Ganadora de Capture The Flag (CTF) DEF CON", descripcion="Primer puesto con el equipo 'SecGroup' en la competición internacional de 2022"),
        Merito(nombre="Contribuidora al Proyecto OWASP", descripcion="Co-autora de la guía de seguridad para APIs de servicios financieros"),
        Merito(nombre="Top 1% en TryHackMe", descripcion="Reconocimiento por completar desafíos avanzados de explotación y defensa"),
    ]
)