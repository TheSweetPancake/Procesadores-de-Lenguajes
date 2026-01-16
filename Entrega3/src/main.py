import os
import sys
import argparse
import subprocess
from pathlib import Path


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
        print(f"Ejecutando: java -cp .:antlr-4.13.2-complete.jar org.antlr.v4.gui.TestRig E3 cvs -tokens {entrada_path}")
        subprocess.run(
            ["java", "-cp", ".:antlr-4.13.2-complete.jar", "org.antlr.v4.gui.TestRig", "E3", "cvs", "-tokens", str(entrada_path)]
        )
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
        print(f"Ejecutando: java parser {entrada_path}")
        subprocess.run(
            ["java", "parser", str(entrada_path)]
        )
    finally:
        os.chdir(original_dir)


def main():
    parser = argparse.ArgumentParser(
        description="Procesa un CV usando ANTLR o CUP",
        usage="python3 main.py <archivo.txt>"
    )
    
    parser.add_argument(
        'entrada',
        help='Archivo de entrada (.txt) con el CV'
    )
    
    args = parser.parse_args()

    print("\n=== Selecciona el analizador ===")
    print("1. CUP")
    print("2. ANTLR")
    
    opcion = input("\nOpción (1 o 2): ").strip()
    
    try:
        if opcion == '1':
            ejecutar_cup(args.entrada)
        elif opcion == '2':
            ejecutar_antlr(args.entrada)
        else:
            print("Error: Opción no válida. Use 1 o 2", file=sys.stderr)
            sys.exit(1)
    
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
