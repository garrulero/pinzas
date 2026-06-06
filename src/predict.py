#!/usr/bin/env python3
import os
import argparse
from ultralytics import YOLO

def run_inference(model_path, source_path, conf_threshold, save_results):
    """
    Carga el modelo YOLOv8 y ejecuta la inferencia en las imágenes indicadas.
    """
    # Validar que existe el modelo
    if not os.path.exists(model_path):
        print(f"Error: No se encontró el modelo en la ruta '{model_path}'.")
        print("Por favor, asegúrate de colocar tu archivo 'best.pt' en la carpeta 'models/'.")
        return

    # Validar que existe la fuente de imágenes
    if not os.path.exists(source_path):
        print(f"Error: La ruta de origen '{source_path}' no existe.")
        return

    print(f"Cargando modelo YOLOv8 desde: {model_path}...")
    model = YOLO(model_path)

    print(f"Ejecutando inferencia sobre: {source_path}")
    print(f"Umbral de confianza: {conf_threshold}")

    # Ejecutar predicción
    results = model.predict(
        source=source_path,
        conf=conf_threshold,
        save=save_results
    )

    print("\n¡Predicción completada con éxito!")
    if save_results:
        print("Los resultados etiquetados se han guardado en la carpeta 'runs/detect/predict/'")

if __name__ == "__main__":
    # Configurar los argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Script de Inferencia para Detección de Pinzas con YOLOv8")
    
    parser.add_argument(
        "--model", 
        type=str, 
        default=os.path.join("models", "best.pt"), 
        help="Ruta al archivo de pesos del modelo (.pt)"
    )
    parser.add_argument(
        "--source", 
        type=str, 
        default=os.path.join("data", "sample_images"), 
        help="Ruta a la carpeta con imágenes de prueba"
    )
    parser.add_argument(
        "--conf", 
        type=float, 
        default=0.5, 
        help="Umbral de confianza para las detecciones (default: 0.5)"
    )
    parser.add_argument(
        "--no-save", 
        action="store_false", 
        dest="save", 
        help="Evita guardar las imágenes resultantes con las cajas pintadas"
    )

    args = parser.parse_args()

    run_inference(
        model_path=args.model,
        source_path=args.source,
        conf_threshold=args.conf,
        save_results=args.save
    )
