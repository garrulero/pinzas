# 🔍 Visión Computacional para el Control de Calidad Industrial: Detección de Defectos en Pinzas con YOLOv8

Este repositorio contiene un proyecto de Visión Computacional integral (*end-to-end*) diseñado para automatizar el control de calidad en entornos de fabricación. Utilizando la arquitectura **YOLOv8**, el modelo es capaz de detectar, localizar y clasificar pinzas industriales en tiempo real en dos categorías: funcionales (`pinza_apta`) y defectuosas (`pinza_defectuosa`).

Desarrollado como proyecto principal de porfolio durante mi Bootcamp de Ciencia de Datos e Inteligencia Artificial.

---

## 🛠️ Tecnologías y Herramientas
* **Lenguaje:** Python 3.x
* **Framework Principal:** Ultralytics YOLOv8
* **Entorno de Entrenamiento:** Google Colab (Acelerado por GPU)
* **Gestión de Dataset y Etiquetado:** Roboflow (Proyecto: `MVP_Pinzas_Feria`)

## 📊 Rendimiento y Evaluación del Modelo
El modelo fue evaluado utilizando un conjunto de prueba independiente, mostrando métricas sólidas y listas para las restricciones de un despliegue en entornos industriales:

| Métrica | Valor |
| :--- | :--- |
| **mAP@50** (Global) | **92.1%** |
| **Precisión (Precision)** | **97.2%** |
| **Exhaustividad (Recall)** | **94.7%** |
| **F1-Score** | **95.9%** |

### Precisión por Clase (mAP@50)
* **`pinza_apta` (Funcional):** 100%
* **`pinza_defectuosa` (Defectuosa):** 92.0%

> 💡 **Insight Clave:** El modelo alcanza una tasa de precisión casi perfecta (97.2%), lo que significa que los falsos positivos se minimizan al máximo. Este es un requisito crítico en las líneas de control de calidad para evitar descartar componentes que están en perfecto estado.

---

## ⚙️ Configuración del Entrenamiento (`args.yaml`)
Para garantizar la total reproducibilidad del proyecto, el proceso de entrenamiento se rigió estrictamente por los parámetros documentados en el archivo `args.yaml`[cite: 1]:

* **Pesos Base:** `yolov8s.pt` (YOLOv8 Small - seleccionado por su equilibrio óptimo entre velocidad de inferencia en tiempo real y precisión en defectos pequeños)[cite: 1].
* **Modo de Tarea:** Detección de Objetos (`task: detect`, `mode: train`)[cite: 1].
* **Resolución de Entrada (`imgsz`):** 640x640 píxeles[cite: 1].
* **Épocas (Epochs):** 50[cite: 1].
* **Tamaño de Lote (Batch Size):** 16[cite: 1].
* **Aumentación de Datos:** Se aplicaron técnicas avanzadas como Mosaic (1.0)[cite: 1] y giros horizontales (`fliplr: 0.5`)[cite: 1] para aumentar la resiliencia del modelo ante variaciones de iluminación, rotación y colocación de la cámara en la planta de producción.

---

## 📁 Estructura del Repositorio
Aunque el dataset completo de imágenes de entrenamiento permanece privado debido a las restricciones de la licencia de la plataforma, este repositorio proporciona un entorno de pruebas completamente funcional:

```text
├── data/
│   ├── sample_images/     # Imágenes en bruto para probar la inferencia del modelo
│   └── data.yaml          # Definición de clases del dataset
├── models/
│   └── best.pt            # Pesos finales del modelo entrenado listos para producción
├── src/
│   └── predict.py         # Script personalizado en Python para pipelines de inferencia
└── args.yaml              # Archivo original de hiperparámetros[cite: 1]