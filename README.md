# Proyecto ELK Stack

Este repositorio contiene los archivos necesarios para configurar un entorno de ELK Stack utilizando Docker Compose.
Además, se incluye una simulación en Python de una aplicación de transacciones que genera ciertas trazas.
Estas trazas se podrán insertar en el Stack de ELK para, por ejemplo, realizar visualizaciones en Kibana.

## Contenido
- `generador_logs/`: Contiene scripts en Python para generar ficheros de trazas o indexar directamente en Elasticsearch a través de su API.
- `logstash/`: Archivo de configuración de tuberías y trazas de ejemplo que indexar en Elasticsearch.
- `MOD Kibana Práctico.pdf`: Presentación con requisitos para desplegar el proyecto y ejercicios guiados.
- `docker-compose.yml`: Archivo de configuración Docker Compose para levantar los contenedores de Elasticsearch, Logstash y Kibana.

## Requisitos

- Docker: Se utilizará para desplegar contenedores para los servicios Logstash, Elasticsearch y Kibana.
- Editor de texto: Para modificar la configuración de las tuberías de Logstash.

## Instrucciones

1. Clona o descarga este repositorio.
2. Navega al directorio del proyecto.
3. Levanta los contenedores de ELK Stack utilizando Docker Compose:
    ```bash
    docker-compose up -d
    ```

## Notas Importantes

- Asegúrate de no tener servicios que utilicen los mismos puertos que estén establecidos en Elasticsearch, Logstash y Kibana.
