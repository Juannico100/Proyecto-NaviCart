# Proyecto-NaviCart

<img width="622" height="465" alt="Captura de pantalla 2025-07-25 a la(s) 12 35 08 p m" src="https://github.com/user-attachments/assets/6e534088-a37d-4b0c-a300-9dc3eb6fdf17" />


## Integrantes
* Jose David Artunduaga Rozo
* Juan Nicolás Martínez Franco
* Luis Alejandro Gamboa Bermúdez

## Descripción
En muchos espacios, el traslado manual de objetos supone una barrera para quienes tienen movilidad reducida. Este proyecto plantea el diseño de un carrito autónomo de dimensiones compactas, equipado con un sensor de ultrasonido, capaz de escanear su entorno, construyendo un mapa simplificado y trazar rutas seguras hacia un punto predefinido. De esta manera, se minimiza el esfuerzo físico y se reducen los riesgos de colisión durante el transporte de cargas ligeras.

El sistema se basa en un microcontrolador que procesa las lecturas del sensor de ultrasonido para identificar obstáculos y calcular la trayectoria más adecuada. Gracias a un algoritmo de navegación reactiva, el carrito ajusta su rumbo en tiempo real: si detecta un obstáculo inesperado, redirecciona su camino antes de continuar, garantizando un desplazamiento continuo y sin interrupciones. Su estructura compacta permite operar con agilidad en pasillos estrechos o espacios reducidos.

El objetivo principal es facilitar el traslado de objetos, por ejemplo, cajas, maletas o herramientas entre distintos puntos dentro de un mismo lugar, especialmente en beneficio de personas con discapacidad motriz. Al automatizar esta tarea, se promueve la autonomía del usuario y se alivia la carga física de aquellos que requieren asistencia constante. Además, el diseño modular del prototipo permite futuras mejoras, como la integración de nuevos sensores o la adaptación a diferentes tipos de terreno.

## Recomendaciones y conclusiones

### Concluciones

En este proyecto se logró desarrollar un prototipo funcional de carrito autónomo, bautizado como NaviCart, capaz de transportar cargas ligeras y esquivar obstáculos en tiempo real mediante un sensor ultrasonido HC-SR04 y un microcontrolador ESP32. La estructura fabricada por corte láser demostró ser resistente y modular, facilitando tanto el ensamblaje como el mantenimiento del sistema. Durante las pruebas de campo en pasillos de un metro de ancho, el algoritmo de navegación reactiva alcanzó una tasa de evasión de obstáculos del 95 % y el mapeo mantuvo un error bajo, validando la precisión y la confiabilidad de la solución. Además, la conectividad inalámbrica (Bluetooth/Wi-Fi) permitió el control remoto y la actualización de parámetros sin necesidad de acceso físico al dispositivo.

### Recomendaciones para trabajos futuros

Para enriquecer las capacidades de NaviCart y acercarlo a un producto final, se sugiere:

Integrar sensores adicionales (por ejemplo, infrarrojos o LIDAR de bajo coste) para mejorar la detección sobre superficies irregulares o en condiciones de baja reflectividad.
 * Desarrollar técnicas de fusión de datos (sensor fusion) y optimizar un esquema SLAM ligero que permita generar un mapa más detallado del entorno.
 * Implementar un sistema de gestión de energía avanzado, con monitorización de tensión en tiempo real y protocolos de ahorro automático cuando no se detecte movimiento.
 * Crear una aplicación móvil más completa que incluya rutas predefinidas, ajustes de velocidad y notificaciones de estado de batería, mejorando la experiencia de usuario.
 * Realizar estudios de usabilidad con personas con movilidad reducida para adaptar la interfaz de control y evaluar la ergonomía del carrito en escenarios reales.
 * Explorar materiales alternativos y recubrimientos impermeables para el chasis, con el fin de aumentar la durabilidad y permitir su uso en exteriores o entornos clínicos.

## WIKI

Para mas información sobre el proyecto, consulte la [Wiki](https://github.com/Juannico100/Proyecto-NaviCart/wiki).
 

