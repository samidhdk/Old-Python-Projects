## Blur_Detector

Permite mover las imagenes borrosas de un directorio a otro con la misma estructura que el primero (la copia de subdirectorios depende de la ruta dada), adicionalmente genera un reporte en formato JSON.


## Ejemplo caso de uso:

python3 blur_detector.py -i ”./pictures/google_photos_backup” -t ”./pictures/blurred_images” -r ”./report.json”

O

python3 blur_detector.py --image_folder=”./pictures/google_photos_backup” --trash_folder=”./pictures/blurred_images” --report_folder=”./report.json”

## Explicación

Argumentos: 

 (Obligatorio) -i / --image_folder: "Ruta del directorio que contine las imagenes a filtrar" / "Path of the directory that contains the images to filter"
 
 (Obligatorio) -t / --trash_folder: "Ruta del directorio que recibirá las imagenes borrosas" / "Path of the directory that will recive the blurred images "
 
 (Opcional)    -r / --report_folder: "Ruta del archivo .json que recibirá los resultados de la ejecución" /  "Path of the .json file that will recive the report"

## Ejemplo reporte JSON:

    {
    "elapsed_time": "0.12 seconds",
    "total_images": 5,
    "blurred_images": 2,
    "accepted": [
       {
          "path": "./pictures/google_photos_backup/image1.jpg",
          "score": 70
       },
       {
          "path": "./pictures/google_photos_backup/image3.jpg",
          "score": 90
       },
       {
          "path": "./pictures/google_photos_backup/image4.jpg",
          "score": 74
       }
    ],
    "discarded": [
        {
          "path": "./pictures/google_photos_backup/image2.jpg",
          "score": 10
        },
        {
        "path": "./pictures/google_photos_backup/image5.jpg",
        "score": 10
        }
    ]
    }
