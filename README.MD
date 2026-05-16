# Agenda Personal

Proyecto final de Programación I — Universidad de Manizales

## Descripción
Aplicación web desarrollada en Python con Flask que permite gestionar eventos personales como citas médicas, reuniones y recordatorios. Aplica los principios de Programación Orientada a Objetos.

## Conceptos de POO aplicados

- **Clase base:** `Evento` con constructor, atributos privados y métodos getters/setters
- **Herencia:** las clases `Cita`, `Reunion` y `Recordatorio` heredan de `Evento`
- **Polimorfismo:** cada subclase tiene su propia versión de `tipo()` y `to_dict()`
- **Encapsulamiento:** todos los atributos son privados con validaciones en los setters
- **Instancia de objetos:** la clase `Agenda` gestiona la colección de eventos

## Estructura del proyecto

- agenda.py — Clases POO (Evento, Cita, Reunion, Recordatorio, Agenda)
- app.py — Servidor Flask con rutas
- templates/index.html — Interfaz web

## Funcionalidades

- Agregar citas, reuniones y recordatorios
- Eliminar eventos
- Ordenar eventos por fecha o tipo
- Modo oscuro
- Cambio de color del tema
- Cambio de fuente
- Preferencias guardadas automáticamente

## Capturas de pantalla

### Modo oscuro
![Modo oscuro](Captura%201%20modo%20oscuro.png)

### Panel de configuración
![Configuración](Captura%202%20modo%20claro-cambio%20tipo%20de%20evento-Panel%20de%20configuración%20visible.png)

### Filtros de ordenamiento
![Filtros](Captura%203%20filtros%20por%20tipo%20o%20tiempo%20de%20creación.png)

## Tecnologías usadas

- Python 3
- Flask
- HTML / CSS / JavaScript

## Cómo ejecutar

1. Instalar Flask: pip install flask
2. Correr el servidor: python app.py
3. Abrir en el navegador: http://127.0.0.1:5000