"""
Módulo para compilar y ejecutar analizadores ANTLR.
"""

import os
import sys
import subprocess
from pathlib import Path


def compilar_antlr() -> None:
    """Compila la gramática ANTLR."""
    script_dir = Path(__file__).parent
    antlr_gramatica_dir = script_dir.parent / "gramatica" / "antlr"
    
    if not antlr_gramatica_dir.exists():
        raise FileNotFoundError(f"Directorio ANTLR no encontrado: {antlr_gramatica_dir}")
    
    original_dir = os.getcwd()
    try:
        os.chdir(antlr_gramatica_dir)
        print("\nCompilando gramática ANTLR...")
        print("Ejecutando: java -jar antlr-4.13.2-complete.jar -Dlanguage=Java E3.g4")
        
        result = subprocess.run(
            ["java", "-jar", "antlr-4.13.2-complete.jar", "-Dlanguage=Java", "E3.g4"],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"Error: {result.stderr}", file=sys.stderr)
            raise RuntimeError("Error compilando ANTLR")
        
        print("Gramática ANTLR compilada exitosamente")
        
    finally:
        os.chdir(original_dir)


def ejecutar_antlr(archivo_entrada: str) -> None:
    """Ejecuta ANTLR con el archivo de entrada."""
    script_dir = Path(__file__).parent
    antlr_gramatica_dir = script_dir.parent / "gramatica" / "antlr"
    test_dir = script_dir.parent / "test"
    
    if not antlr_gramatica_dir.exists():
        raise FileNotFoundError(f"Directorio ANTLR no encontrado: {antlr_gramatica_dir}")

    entrada_path = test_dir / archivo_entrada
    if not entrada_path.exists():
        raise FileNotFoundError(f"Archivo de entrada no encontrado: {entrada_path}")
    
    original_dir = os.getcwd()
    try:
        os.chdir(antlr_gramatica_dir)
        print(f"\nEjecutando: java -cp .:antlr-4.13.2-complete.jar org.antlr.v4.gui.TestRig E3 cvs -tokens {entrada_path}")
        subprocess.run(
            ["java", "-cp", ".:antlr-4.13.2-complete.jar", "org.antlr.v4.gui.TestRig", "E3", "cvs", "-tokens", str(entrada_path)]
        )
    finally:
        os.chdir(original_dir)
