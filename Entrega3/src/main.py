import sys
import argparse
from compilador_antlr import compilar_antlr, ejecutar_antlr
from compilador_cup import compilar_cup, ejecutar_cup


def mostrar_menu_principal():
    print("\n" + "="*50)
    print("   PROCESADOR DE CVs - ANTLR vs CUP")
    print("="*50)
    print("\n¿Qué deseas hacer?")
    print("1. Compilar gramática ANTLR")
    print("2. Compilar gramáticas CUP/JFlex")
    print("3. Ejecutar analizador ANTLR")
    print("4. Ejecutar analizador CUP")
    print("5. Compilar y ejecutar ANTLR")
    print("6. Compilar y ejecutar CUP")
    print("0. Salir")
    return input("\nOpción (0-6): ").strip()


def main():
    parser = argparse.ArgumentParser(
        description="Procesa un CV usando ANTLR o CUP",
        usage="python3 main.py <archivo.txt>"
    )
    
    parser.add_argument('entrada', help='Archivo de entrada (.txt) con el CV')
    args = parser.parse_args()
    
    while True:
        opcion = mostrar_menu_principal()
        
        try:
            if opcion == '0':
                print("\nFinalizado")
                break
            elif opcion == '1':
                compilar_antlr()
            elif opcion == '2':
                compilar_cup()
            elif opcion == '3':
                ejecutar_antlr(args.entrada)
            elif opcion == '4':
                ejecutar_cup(args.entrada)
            elif opcion == '5':
                compilar_antlr()
                ejecutar_antlr(args.entrada)
            elif opcion == '6':
                compilar_cup()
                ejecutar_cup(args.entrada)
            else:
                print("Error: Opción no válida", file=sys.stderr)
        
        except FileNotFoundError as e:
            print(f"Error: {e}", file=sys.stderr)
        except RuntimeError as e:
            print(f"Error: {e}", file=sys.stderr)
        except Exception as e:
            print(f"Error inesperado: {e}", file=sys.stderr)


if __name__ == '__main__':
    main()
