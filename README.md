AmaDeCasa Microservices Deployment
📘 Descripción general

El proyecto AmaDeCasa utiliza una arquitectura basada en microservicios Docker, organizados en dos entornos:

Desarrollo (dev): para pruebas, debugging y cambios rápidos.

Producción (prod): entorno estable para servicios en ejecución.

Cada microservicio es desplegado mediante Docker Compose, con redes compartidas y variables de entorno específicas.

🏗️ Estructura de carpetas
/srv/apps/amadecasa/
├── dev/
│   └── mc-notifier-telegram/
│       ├── Dockerfile
│       ├── docker-compose.yml
│       ├── .env.dev
│       └── app/...
└── prod/
    └── mc-notifier-telegram/
        ├── Dockerfile
        ├── docker-compose.yml
        ├── .env.prod
        └── app/...

⚙️ Configuración de redes

La red compartida amade-net conecta los distintos microservicios del sistema.

Para crearla manualmente (solo una vez):

sudo docker network create amadecasa_amade-net

🧩 Entorno de desarrollo

Ruta: /srv/apps/amadecasa/dev/mc-notifier-telegram/

services:
  notifier-telegram:
    build: .
    container_name: notifier-dev
    ports:
      - "8010:8000"
    env_file:
      - .env.dev
    networks:
      - amade-net
    restart: unless-stopped

networks:
  amade-net:
    external: true

Variables .env.dev
TELEGRAM_TOKEN=<tu_token_dev>
ENVIRONMENT=development

Comandos
cd /srv/apps/amadecasa/dev/mc-notifier-telegram
sudo docker compose up -d
sudo docker logs -f notifier-dev


Acceso local:

http://localhost:8010/docs

🚀 Entorno de producción

Ruta: /srv/apps/amadecasa/prod/mc-notifier-telegram/

services:
  notifier-telegram:
    image: mc-notifier-telegram:latest
    container_name: notifier-prod
    ports:
      - "9010:8000"
    env_file:
      - .env.prod
    networks:
      - amade-net
    restart: always

networks:
  amade-net:
    external: true

Variables .env.prod
TELEGRAM_TOKEN=<tu_token_prod>
ENVIRONMENT=production

Comandos
cd /srv/apps/amadecasa/prod/mc-notifier-telegram
sudo docker compose up -d
sudo docker logs -f notifier-prod


Acceso local:

http://localhost:9010/docs

🧠 Comandos útiles
Descripción	Comando
Listar contenedores activos	sudo docker ps
Ver logs del servicio	sudo docker logs -f <nombre>
Detener entorno dev	sudo docker compose down
Actualizar imagen prod	sudo docker compose pull && sudo docker compose up -d
Ver redes Docker	sudo docker network ls
🌐 Subdominios locales (opcional)

Editar /etc/hosts:

127.0.0.1 notifier.dev.amadecasa.local
127.0.0.1 notifier.prod.amadecasa.local


Luego acceder:

http://notifier.dev.amadecasa.local:8010/docs

http://notifier.prod.amadecasa.local:9010/docs