# temp stage
FROM python:3.9.16@sha256:e9c9630a11241d1f4ff674e67f4813466d4078dc875f8e7a11d285ae24c19f68

ARG USERNAME=valstro
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ENV HOST=0.0.0.0
ENV PORT=3000

WORKDIR /app

COPY . .

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt update && apt install tini && pip install "python-socketio[client]"

USER $USERNAME

ENTRYPOINT python app.py --host ${HOST} --port ${PORT}