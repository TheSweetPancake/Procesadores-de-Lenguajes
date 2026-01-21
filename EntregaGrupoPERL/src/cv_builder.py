from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, List, Dict, Any

from datosPersonales import DatosPersonales
from formacion import Formacion, FormacionItem
from idiomas import Idiomas, Idioma
from experiencia import Experiencia, ExperienciaItem
from habilidades import Habilidades, Habilidad
from portafolio import Portafolio, Proyecto, Merito

from E3Visitor import E3Visitor
from E3Parser import E3Parser


# ---------- helpers de texto ----------
def _resolve_var(
    s: str,
    _local_vars: Dict[str, str],
    _global_vars: Dict[str, str],
) -> str:
    s = s.strip()

    # Solo resolvemos si viene entre comillas
    if len(s) >= 2 and s[0] == '"':
        key = s.split('=')[0].strip()

        # Primero variables locales
        if key in _local_vars:
            return _local_vars[key]

        # Luego globales
        if key in _global_vars:
            return _global_vars[key]

        # Si no existe, devolvemos el literal sin comillas
        return key

    return s


def _inside_parens(s: str) -> str:
    """
    Convierte:
      'nomyape(Antonio Lobato)' -> 'Antonio Lobato'
      '(Antonio Lobato)'       -> 'Antonio Lobato'
    Si no hay paréntesis, devuelve el string original.
    """
    s = s.strip()
    if "(" in s and s.endswith(")"):
        return s[s.find("(") + 1 : -1].strip()
    if s.startswith("(") and s.endswith(")"):
        return s[1:-1].strip()
    return s


def _ctx_text(ctx) -> str:
    return ctx.getText().strip()

def _ctx_value(ctx, visitor: "BuildObjectsVisitor") -> str:
    raw = _inside_parens(_ctx_text(ctx))
    return _resolve_var(raw, visitor._local_vars, visitor._global_vars)

def _ctx_value_var(ctx, visitor: "BuildObjectsVisitor") -> str:
    s = _ctx_text(ctx).strip()
    if "=" in s and s.endswith(";"):
        return s[s.find("=") + 1 : -1].strip()
    if s.startswith("=") and s.endswith(";"):
        return s[1:-1].strip()
    return _resolve_var(s, visitor._local_vars, visitor._global_vars)


def _split_tecnologias(s: str) -> List[str]:
    raw = s.strip()
    if not raw:
        return []
    if "," in raw:
        return [t.strip() for t in raw.split(",") if t.strip()]
    return [t.strip() for t in raw.split() if t.strip()]


@dataclass
class CVObjects:
    global_vars: Dict[str, str]
    cv_id: str
    local_vars: Dict[str, str]
    datos: DatosPersonales
    formacion: Formacion
    idiomas: Optional[Idiomas]
    experiencia: Optional[Experiencia]
    habilidades: Optional[Habilidades]
    portafolio: Optional[Portafolio]


class BuildObjectsVisitor(E3Visitor):
    def __init__(self) -> None:
        super().__init__()
        self._global_vars: Dict[str, str] = {}
        self._cv_id: str = "CV"
        self._local_vars: Dict[str, str] = {}
        self._datos: Optional[DatosPersonales] = None
        self._form: Optional[Formacion] = None
        self._idiomas: Optional[Idiomas] = None
        self._xp: Optional[Experiencia] = None
        self._skills: Optional[Habilidades] = None
        self._folio: Optional[Portafolio] = None


    def result(self) -> CVObjects:
        if self._datos is None:
            raise ValueError("datospersonales no parseados")
        if self._form is None:
            raise ValueError("formacion no parseada")
        return CVObjects(
            global_vars=self._global_vars,
            cv_id=self._cv_id,
            local_vars=self._local_vars,
            datos=self._datos,
            formacion=self._form,
            idiomas=self._idiomas,
            experiencia=self._xp,
            habilidades=self._skills,
            portafolio=self._folio,
        )

    # ---------- ENTRY ----------
    def visitStart(self, ctx: E3Parser.StartContext):
        return self.visit(ctx.cvs())
    
    def visitGlobal_var(self, ctx: E3Parser.Global_varContext):
        for v in ctx.variable():
            name = v.IDENT().getText()
            value = _ctx_value_var(v, self)
            self._global_vars[name] = value
        return None

    def visitLocal_var(self, ctx: E3Parser.Local_varContext):
        for v in ctx.variable():
            name = v.IDENT().getText()
            value = _ctx_value_var(v, self)
            self._local_vars[name] = value
        return None

    def visitCvs(self, ctx: E3Parser.CvsContext):
        cvs = ctx.cv()
        if not cvs:
            raise ValueError("No se encontró ningún bloque cv en el archivo.")
        # Si hay varios cv, aquí podrías iterar. Por ahora, usamos el primero:
        return self.visit(cvs[0])

    # ---------- CV ----------
    def visitCv(self, ctx: E3Parser.CvContext):
        # Reset de variables locales al iniciar CV
        self._local_vars = {}

        # Primero procesamos las variables locales
        if ctx.local_var():
            self.visit(ctx.local_var())

        # Procesar nombre del CV
        if hasattr(ctx, "IDENT") and ctx.IDENT():
            self._cv_id = _resolve_var(ctx.IDENT().getText(), self._local_vars, self._global_vars)
        else:
            # fallback: intenta capturar el "nombre" desde el texto completo
            full = _ctx_text(ctx)
            head = full.split("{", 1)[0].strip()
            head = head[2:].strip() if head.lower().startswith("cv") else head
            self._cv_id = _resolve_var(head, self._local_vars, self._global_vars) if head else "CV"

        # Procesar secciones del CV
        self.visit(ctx.datospersonales())
        self.visit(ctx.formacion())
        if ctx.idiomas():
            self.visit(ctx.idiomas())
        if ctx.experiencia():
            self.visit(ctx.experiencia())
        if ctx.habilidades():
            self.visit(ctx.habilidades())
        if ctx.portafolio():
            self.visit(ctx.portafolio())

        return self.result()

    # ---------- DATOS PERSONALES ----------
    def visitDatospersonales(self, ctx: E3Parser.DatospersonalesContext):
        nombre = _ctx_value(ctx.nomyape(), self)
        datos = DatosPersonales(nombre=nombre)

        if ctx.foto():
            datos.foto = _ctx_value(ctx.foto(), self)
        if ctx.fecha():
            datos.fecha_nacimiento = _ctx_value(ctx.fecha(), self)
        if ctx.bio():
            datos.bio = _ctx_value(ctx.bio(), self)

        c = ctx.contacto()
        datos.email = _ctx_value(c.email(), self)
        datos.telefono = _ctx_value(c.telefono(), self)

        if c.redes():
            redes = c.redes()
            if redes.linkedin():
                datos.linkedin = _ctx_value(redes.linkedin(), self)
            if redes.github():
                datos.github = _ctx_value(redes.github(), self)
            if redes.web():
                datos.web = _ctx_value(redes.web(), self)

        self._datos = datos
        return None

    # ---------- FORMACIÓN ----------
    def visitFormacion(self, ctx: E3Parser.FormacionContext):
        items: List[FormacionItem] = []

        for o in ctx.oficial():
            titulo = _ctx_value(o.titulo(), self)
            inst = _ctx_value(o.expedidor(), self)
            desc = _ctx_value(o.descripcion(), self) if o.descripcion() else None
            logros = _ctx_value(o.logros(), self) if o.logros() else None
            fecha = _ctx_value(o.fecha(), self)

            items.append(
                FormacionItem(
                    titulo=titulo,
                    institucion=inst,
                    tipo="oficial",
                    descripcion=desc,
                    logros=logros,
                    fecha=fecha,
                    en_curso=False,
                )
            )

        # Si tienes complementaria en tu gramática, descomenta y adapta:
        if hasattr(ctx, "complementaria"):
            for c in ctx.complementaria() or []:
                titulo = _ctx_value(c.titulo(), self)
                inst = _ctx_value(c.expedidor(), self) if hasattr(c, "expedidor") and c.expedidor() else "—"
                fecha = _ctx_value(c.fecha(), self) if hasattr(c, "fecha") and c.fecha() else None
                en_curso = (fecha or "").strip().lower() in {"en_curso", "encurso", "en curso"}
                items.append(
                    FormacionItem(
                        titulo=titulo,
                        institucion=inst,
                        tipo="complementaria",
                        descripcion=None,
                        logros=None,
                        fecha=fecha,
                        en_curso=en_curso,
                    )
                )

        self._form = Formacion(items=items)
        return None

    # ---------- IDIOMAS ----------
    def visitIdiomas(self, ctx: E3Parser.IdiomasContext):
        lst: List[Idioma] = []
        for it in ctx.idioma():
            # En muchas gramáticas: idioma( Inglés nivel(B2) expedidor(...) )
            # Como no usamos value(), cogemos texto y buscamos sub-nodos:
            nombre = ""
            if hasattr(it, "CONJPALYNUM") and it.CONJPALYNUM():
                nombre = it.CONJPALYNUM().getText()
            else:
                nombre = _ctx_text(it).strip("()").strip()

            niv = _ctx_value(it.nivel(), self) if hasattr(it, "nivel") and it.nivel() else ""
            exp = _ctx_value(it.expedidor(), self) if hasattr(it, "expedidor") and it.expedidor() else None
            lst.append(Idioma(nombre=_resolve_var(nombre, self._local_vars, self._global_vars), nivel=niv, expedidor=exp))

        self._idiomas = Idiomas(idiomas=lst)
        return None

    # ---------- EXPERIENCIA ----------
    def visitExperiencia(self, ctx: E3Parser.ExperienciaContext):
        items: List[ExperienciaItem] = []

        for l in ctx.laboral() or []:
            f = self._read_xp_block(l)
            items.append(
                ExperienciaItem(
                    tipo="laboral",
                    organizacion=f.get("organizacion", "—"),
                    puesto=f.get("puesto", "—"),
                    descripcion=f.get("descripcion"),
                    horas=int(f["horas"]) if "horas" in f and f["horas"] is not None else None,
                )
            )

        for v in ctx.voluntariado() or []:
            f = self._read_xp_block(v)
            items.append(
                ExperienciaItem(
                    tipo="voluntariado",
                    organizacion=f.get("organizacion", "—"),
                    puesto=f.get("puesto", "—"),
                    descripcion=f.get("descripcion"),
                    horas=int(f["horas"]) if "horas" in f and f["horas"] is not None else None,
                )
            )

        self._xp = Experiencia(experiencias=items)
        return None

    def _read_xp_block(self, ctx) -> Dict[str, Any]:
        out: Dict[str, Any] = {}

        if hasattr(ctx, "organizacion") and ctx.organizacion():
            out["organizacion"] = _ctx_value(ctx.organizacion(), self)
        if hasattr(ctx, "puesto") and ctx.puesto():
            out["puesto"] = _ctx_value(ctx.puesto(), self)
        if hasattr(ctx, "horas") and ctx.horas():
            # horas(NUM) normalmente
            try:
                out["horas"] = _ctx_value(ctx.horas(), self)
            except Exception:
                out["horas"] = None

        # laboral: responsabilidades(...)
        if hasattr(ctx, "responsabilidades") and ctx.responsabilidades():
            out["descripcion"] = _ctx_value(ctx.responsabilidades(), self)

        # voluntariado: descripcion(...)
        if hasattr(ctx, "descripcion") and ctx.descripcion():
            out["descripcion"] = _ctx_value(ctx.descripcion(), self)

        return out

    # ---------- HABILIDADES ----------
    def visitHabilidades(self, ctx: E3Parser.HabilidadesContext):
        hs: List[Habilidad] = []

        # soft?  -> ctx.soft() es None o SoftContext (NO lista)
        s = ctx.soft()
        if s:
            for h in s.habilidad():
                hs.append(Habilidad(nombre=_ctx_value(h, self), tipo="soft"))

        # hard? -> ctx.hard() es None o HardContext (NO lista)
        hd = ctx.hard()
        if hd:
            # Si tu hard usa categoria{...} como en tu ejemplo:
            if hasattr(hd, "categoria") and hd.categoria():
                for cat in hd.categoria():
                    txt = _ctx_text(cat)
                    cat_nombre = self._extract_field(txt, "nombre")
                    hab_nombre = self._extract_field(txt, "habilidad")
                    nivel = self._extract_field(txt, "nvhab")
                    if hab_nombre:
                        hs.append(Habilidad(nombre=hab_nombre, tipo="hard", categoria=cat_nombre, nivel=nivel))
            else:
                # fallback si tu gramática hard es la antigua (habilidad/categoria/nvhab sueltos)
                # (deja esto si no aplica; no hace daño)
                pass

        self._skills = Habilidades(habilidades=hs)
        return None


    def _extract_field(self, block_text: str, field: str) -> str:
        """
        Extrae field(...) de un texto como:
          categoria{nombre(Venta)habilidad(Vender coches)nvhab(alto)}
        """
        key = field + "("
        i = block_text.find(key)
        if i == -1:
            return ""
        j = block_text.find(")", i)
        if j == -1:
            return ""
        return _resolve_var(block_text[i + len(key) : j].strip(), self._local_vars, self._global_vars)

    # ---------- PORTAFOLIO ----------
    def visitPortafolio(self, ctx: E3Parser.PortafolioContext):
        proyectos: List[Proyecto] = []
        meritos: List[Merito] = []

        if hasattr(ctx, "proyecto") and ctx.proyecto():
            for p in ctx.proyecto():
                nombre = _ctx_value(p.nombre(), self) if hasattr(p, "nombre") and p.nombre() else ""
                desc = _ctx_value(p.descripcion(), self) if hasattr(p, "descripcion") and p.descripcion() else ""
                tec = _split_tecnologias(_ctx_value(p.tecnologias(), self)) if hasattr(p, "tecnologias") and p.tecnologias() else []
                proyectos.append(Proyecto(nombre=nombre, descripcion=desc, tecnologias=tec))

        # Si en tu gramática existen meritos(), también podrías leerlos:
        if hasattr(ctx, "meritos") and ctx.meritos():
            for m in ctx.meritos():
                n = _ctx_value(m.nombre(), self) if hasattr(m, "nombre") and m.nombre() else ""
                d = _ctx_value(m.descripcion(), self) if hasattr(m, "descripcion") and m.descripcion() else ""
                meritos.append(Merito(nombre=n, descripcion=d))

        self._folio = Portafolio(proyectos=proyectos, meritos=meritos)
        return None
