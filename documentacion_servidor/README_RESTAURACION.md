# Restauración del servidor KMS

Este documento conserva la información necesaria para reconstruir el entorno
del Sistema KMS a partir del estado respaldado como VERSION 12 KMS.

Fecha del respaldo: 1 de octubre de 2026.

## 1. Entorno original

El servidor original utilizaba:

- Ubuntu 20.04.4 LTS
- Node.js 16.14.2
- npm 8.5.0
- Python 3.8.10
- MySQL 8.0.42
- Nginx
- PM2

Las versiones exactas también están almacenadas en:

    documentacion_servidor/versiones_servidor.txt

## 2. Aplicación KMS

Ruta utilizada en el servidor original:

    /root/SistemaKMS

Proceso principal:

    node /root/SistemaKMS/server.js

La aplicación escucha localmente en:

    127.0.0.1:3333

PM2 administraba el proceso identificado como:

    server

## 3. Nginx

Nginx escucha en el puerto 80 y funciona como proxy inverso.

Flujo original:

    Cliente
       |
       v
    Nginx :80
       |
       v
    127.0.0.1:3333
       |
       v
    SistemaKMS/server.js

La configuración original se encuentra en:

    documentacion_servidor/nginx_default

En el servidor original correspondía a:

    /etc/nginx/sites-available/default

y estaba habilitada mediante:

    /etc/nginx/sites-enabled/default

## 4. Base de datos

Motor utilizado:

    MySQL 8

Base de datos:

    kms

La aplicación utilizaba MySQL local:

    DB_HOST=localhost
    DB_PORT=3306
    DB_USER=root
    DB_DATABASE=kms

Las contraseñas NO se almacenan en este documento ni deben publicarse
en el repositorio.

Existe un respaldo privado de la base de datos realizado al retirar el
servidor:

    kms_2026-09-30.sql

Para restaurarlo en un nuevo servidor, después de crear la base `kms`:

    mysql -u root -p kms < kms_2026-09-30.sql

El archivo SQL debe conservarse de manera privada y no debe publicarse
en Git.

## 5. Variables de entorno

El servidor original utilizaba un archivo:

    /root/SistemaKMS/.env

Existe un respaldo privado denominado:

    env_kms_respaldo

Este archivo puede contener contraseñas y secretos, por lo que NO debe
subirse a un repositorio público.

Al reconstruir el servidor deberá colocarse nuevamente como:

    /root/SistemaKMS/.env

o adaptarse a la nueva ubicación de despliegue.

## 6. Dependencias

Las dependencias propias del proyecto deben instalarse utilizando los
archivos de dependencias/versiones incluidos en el repositorio.

También se conservó una fotografía de los paquetes Python instalados en
el servidor:

    documentacion_servidor/python_requirements_servidor.txt

Y de los paquetes npm instalados globalmente:

    documentacion_servidor/npm_global_servidor.txt

Estos archivos representan el entorno existente al momento del respaldo
y sirven como referencia para reconstrucción.

## 7. PM2

El servidor utilizaba PM2 para mantener en ejecución la aplicación Node.

La configuración del servicio systemd original está respaldada en:

    documentacion_servidor/pm2-nodejs.service

La información observada de procesos y puertos está en:

    documentacion_servidor/ejecucion_servidor.txt

Al momento del respaldo, el KMS estaba ejecutándose mediante:

    node /root/SistemaKMS/server.js

en el puerto:

    3333

## 8. Archivos privados de respaldo

Además del repositorio Git, al retirar el servidor se generaron los
siguientes respaldos privados:

    SistemaKMS_completo_2026-10-01.tar.gz
    kms_2026-09-30.sql
    env_kms_respaldo

`SistemaKMS_completo_2026-10-01.tar.gz` es una copia literal del
directorio `/root/SistemaKMS` existente en el servidor al momento del
respaldo.

Estos archivos deben conservarse fuera del repositorio Git.

## 9. Rama de respaldo

El estado final del servidor fue respaldado en Git en la rama:

    respaldo-servidor-2026-10-01

Commit:

    VERSION 12 KMS

Esta rama se creó para preservar el estado del servidor antes de su
retiro.

## 10. Orden recomendado de restauración

1. Preparar un servidor Linux.
2. Instalar las versiones compatibles de Node.js, npm, Python, MySQL,
   Nginx y PM2.
3. Clonar el repositorio.
4. Utilizar como referencia la rama `respaldo-servidor-2026-10-01`.
5. Instalar las dependencias del proyecto.
6. Crear la base de datos `kms`.
7. Importar el respaldo `kms_2026-09-30.sql`.
8. Restaurar/configurar el archivo `.env` privado.
9. Verificar que el proyecto pueda iniciar mediante `server.js`.
10. Comprobar que responda localmente por el puerto 3333.
11. Configurar PM2.
12. Restaurar/adaptar la configuración de Nginx.
13. Probar el sistema antes de exponerlo a producción.

## 11. Observaciones

El servidor también tenía un proceso Node independiente:

    /var/www/html/hello.js

escuchando en:

    127.0.0.1:3000

Este proceso NO era el destino configurado en Nginx para el Sistema KMS.
El proxy de Nginx apuntaba al puerto 3333.

No se recomienda reemplazar versiones, actualizar dependencias o modificar
la base de datos durante una restauración inicial. Primero debe lograrse
reproducir el entorno respaldado y comprobar el funcionamiento del sistema.
