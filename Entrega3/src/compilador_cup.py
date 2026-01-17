"""
Módulo para compilar y ejecutar analizadores CUP/JFlex.
"""

import os
import sys
import subprocess
from pathlib import Path


def compilar_cup() -> None:
    """Compila la gramática CUP y JFlex."""
    script_dir = Path(__file__).parent
    flexcup_gramatica_dir = script_dir.parent / "gramatica" / "flexcup"
    
    if not flexcup_gramatica_dir.exists():
        raise FileNotFoundError(f"Directorio FlexCUP no encontrado: {flexcup_gramatica_dir}")
    
    original_dir = os.getcwd()
    try:
        os.chdir(flexcup_gramatica_dir)
        print("\nCompilando JFlex...")
        print("Ejecutando: jflex CV_Ascendente.flex")
        
        result = subprocess.run(
            ["jflex", "CV_Ascendente.flex"],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"Error: {result.stderr}", file=sys.stderr)
            raise RuntimeError("Error compilando JFlex")
        
        print("JFlex compilado exitosamente")
        
        print("\nCompilando CUP...")
        print("Ejecutando: cup CV_Ascendente.cup")
        
        result = subprocess.run(
            ["cup", "CV_Ascendente.cup"],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"Error: {result.stderr}", file=sys.stderr)
            raise RuntimeError("Error compilando CUP")
        
        print("CUP compilado exitosamente")

        print("\nCompilando archivos Java...")
        print("Ejecutando: javac *.java")
        
        java_files = list(Path(".").glob("*.java"))
        if not java_files:
            raise RuntimeError("No hay archivos .java para compilar")
        
        result = subprocess.run(
            ["javac"] + [str(f) for f in java_files],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"Error: {result.stderr}", file=sys.stderr)
            raise RuntimeError("Error compilando Java")
        
        print("Archivos Java compilados exitosamente")
        
    finally:
        os.chdir(original_dir)


def ejecutar_cup(archivo_entrada: str) -> None:
    """Ejecuta CUP con el archivo de entrada."""
    script_dir = Path(__file__).parent
    flexcup_gramatica_dir = script_dir.parent / "gramatica" / "flexcup"
    test_dir = script_dir.parent / "test"
    
    if not flexcup_gramatica_dir.exists():
        raise FileNotFoundError(f"Directorio FlexCUP no encontrado: {flexcup_gramatica_dir}")
    
    entrada_path = test_dir / archivo_entrada
    if not entrada_path.exists():
        raise FileNotFoundError(f"Archivo de entrada no encontrado: {entrada_path}")
    
    original_dir = os.getcwd()
    try:
        os.chdir(flexcup_gramatica_dir)
        print(f"\nEjecutando: java parser {entrada_path}")
        subprocess.run(
            ["java", "parser", str(entrada_path)]
        )
    finally:
        os.chdir(original_dir)
