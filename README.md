# Simulación de la cinemática de un brazo robot

Bienvenido al repositorio de la presentación "Simulación de la cinemática de un brazo robotico" Este proyecto demuestra los principios fundamentales de un brazo robotico a travez de una simulación utilizando python y sus librerias.
<p align="center">
  <img src="./images/logo.png" alt="logo">
</p> 

## Descripción general

Esta presentacion incluye conceptos basicos de la cinematica directa e inversa de un brazo robotico de 2 articulaciones y 2 eslabones. La simulación da un idea visual e interactiva para entender la funcionalidad desde un punto de vista matemático y poder programarlo para alcanzar posiciones y orientaciones especificas.

## Características

- **Simulación interactiva**: Correr  el archivo robot_experiments.py para experimentar como afecta el cambio de parámetros en el movimiento del robot.
- **Demostración visual**: Correr el archivo app.py para demostrar visualmente la cinemática del brazo robot.
- **Modificar parámetros**: El usuario puede cambiar los parámetros de la applicación: a0, a1, (x,y) en el archivo  robot_arm.py. 

## Tabla de contenido

- [Instalación](#1-instalación)
- [Utilización](#2-utilización)
- [Características](#3-características)
- [Agradecimientos](#4-agradecimientos)

### 1. Instalación:
```bash
# Clonar el repositorio
git clone https://github.com/paodanchacon/pyday_robot_arm_kinematics.git
```
```bash
# Ir al directorio
cd nombreproyecto
```
```bash
#Instalar dependencias
pip install -r requirements.txt
```
### 2. Utilización

```bash
# Correr el script
python app.py
```
### 3. Características 

Experimentar cambiando los valores, en el notebook [robot_experiments](/robot_experiments.ipynb). Puedes cambiar los valores de q0 y q1 para la cinematica directa y/o valores de (x,y) para la cinematica inversa.

También se incluyen los archivos de formulación matemática de la cinemática [directa](/forward_kinematics_test.ipynb) e [inversa](/inverse_kinematics_test.ipynb). Archivos desarrollados especialmente para experimentar y analizar la resolución de las transformaciones del efector final.

### 4. Agradecimientos

- Ing. Jose Laruta 
- Peter Corke, Robotics, Vision and Control

### 5. Contacto
Desarrollado por [Daniela](www.linkedin.com/in/daniela-chambilla). Si tienes alguna duda o quisieras profundizar el tema puedes escribirme.
