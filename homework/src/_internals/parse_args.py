import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Procesar carpetas de entrada y salida"
    )
    parser.add_argument("input_folder", type=str, help="Ruta de la carpeta de entrada")
    parser.add_argument("output_folder", type=str, help="Ruta de la carpeta de salida")
    args = parser.parse_args()
    return args.input_folder, args.output_folder
