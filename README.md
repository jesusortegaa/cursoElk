# Proyecto ELK Stack

Este repositorio contiene los archivos necesarios para configurar un entorno de ELK Stack utilizando Docker Compose.

## Contenido

- `docker-compose.yml`: Archivo de configuración Docker Compose para levantar los contenedores de Elasticsearch, Logstash y Kibana.
- `Logstash/`: Carpeta con recursos y ejercicios para Logstash.

## Requisitos

- Docker

## Instrucciones

1. Clona o descarga este repositorio:

    ```bash
    git clone https://github.com/tu_usuario/proyecto-elk-stack.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd proyecto-elk-stack
    ```

3. Levanta los contenedores de ELK Stack usando Docker Compose:

    ```bash
    docker-compose up -d
    ```


## Configuración Adicional

- **Logstash:** La carpeta `Logstash/` contiene ejemplos de configuración para Logstash, así como ejercicios prácticos para aprender a utilizarlo.

## Notas Importantes

- Asegúrate de no tener servicios que utilicen los puertos 9200, 5044 y 5601, ya que estos son utilizados por Elasticsearch, Logstash y Kibana, respectivamente.
- Modifica la configuración según tus necesidades en el archivo `docker-compose.yml`.
