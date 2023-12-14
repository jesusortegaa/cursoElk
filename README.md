# Proyecto ELK Stack

Este repositorio contiene los archivos necesarios para configurar un entorno de ELK Stack utilizando Docker Compose.

## Contenido

- `docker-compose.yml`: Archivo de configuración Docker Compose para levantar los contenedores de Elasticsearch, Logstash y Kibana.
- `Logstash/`: Carpeta con recursos y ejercicios para Logstash.

## Requisitos

- Docker

## Instrucciones

1. Clona o descarga este repositorio:
2. Navega al directorio del proyecto:
3. Levanta los contenedores de ELK Stack usando Docker Compose:
    ```bash
    docker-compose up -d
    ```

## Configuración Adicional

- **Logstash:** La carpeta `Logstash/` contiene ejemplos de configuración para Logstash, así como ejercicios prácticos para aprender a utilizarlo.

## Notas Importantes

- Asegúrate de no tener servicios que utilicen los mismos puertos que estén establecidos en Elasticsearch, Logstash y Kibana.
