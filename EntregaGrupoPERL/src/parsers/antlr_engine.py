"""
Engine ANTLR: Parser CV → datos estructurados listos para Jinja2
"""
from pathlib import Path
from antlr4 import FileStream, CommonTokenStream

from E3Lexer import E3Lexer
from E3Parser import E3Parser
from cv_builder import BuildObjectsVisitor


def _to_jinja_dict(objs) -> dict:
    """Convierte objetos CV a diccionario para renderizar con Jinja2."""
    return {
        "cv_id": getattr(objs, "cv_id", ""),
        "datos": getattr(objs, "datos", None),
        "formacion": getattr(objs, "formacion", None),
        "idiomas": getattr(objs, "idiomas", None),
        "experiencia": getattr(objs, "experiencia", None),
        "habilidades": getattr(objs, "habilidades", None),
        "portafolio": getattr(objs, "portafolio", None),
    }


def parse_with_antlr(input_path: Path) -> dict:
    """
    Parsea un archivo .cv con ANTLR y devuelve datos estructurados.
    
    Args:
        input_path: Ruta al archivo .cv
        
    Returns:
        dict: Datos del CV listos para Jinja2
    """
    stream = FileStream(str(input_path), encoding="utf-8")
    lexer = E3Lexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = E3Parser(tokens)

    tree = parser.start()
    visitor = BuildObjectsVisitor()
    objs = visitor.visit(tree)

    return _to_jinja_dict(objs)
