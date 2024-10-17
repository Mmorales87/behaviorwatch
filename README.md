# BehaviorWatch

BehaviorWatch es una aplicación en Python diseñada para monitorear el chat de voz y texto en tiempo real, detectando insultos y generando reportes cuando se detectan comportamientos inapropiados. La aplicación utiliza técnicas de procesamiento de audio y texto para identificar insultos en el chat y grabar la pantalla y el audio cuando se detecta un insulto.

## Características

- Monitoreo en tiempo real del chat de voz y texto.
- Detección de insultos a partir de una lista predefinida.
- Grabación de pantalla y audio al detectar un insulto.
- Generación de reportes en formato JSON con detalles del insulto y el usuario.

## Requisitos

- Python 3.6 o superior
- Las siguientes bibliotecas de Python:
  - opencv-python
  - pyaudio
  - numpy
  - SpeechRecognition

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/BehaviorWatch.git
   cd BehaviorWatch
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   ```

3. Activa el entorno virtual:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```


## Configuración de la Contraseña de Aplicación para Gmail

Para evitar el uso de tu contraseña principal de Gmail en la aplicación, es recomendable utilizar una contraseña de aplicación. A continuación, se describen los pasos para generar una contraseña de aplicación en tu cuenta de Google:

1. **Accede a tu cuenta de Google**:
   - Ve a [https://myaccount.google.com/security](https://myaccount.google.com/security).

2. **Habilita la verificación en dos pasos**:
   - Busca la sección "Verificación en dos pasos".
   - Si no está activada, haz clic en "Activar" y sigue las instrucciones para configurarla.

3. **Genera una contraseña de aplicación**:
   - Desplázate hacia abajo hasta la sección "Contraseñas de aplicaciones".
   - Haz clic en la flecha para abrir la nueva página.
   - En el campo "Seleccionar aplicación", elige "Otro (nombre personalizado)".
   - Escribe un nombre para la aplicación, por ejemplo, "Valorant Behavior Report Tool".
   - Haz clic en "Crear".

4. **Copia la contraseña generada**:
   - Se abrirá un modal que muestra la contraseña de aplicación generada.
   - Copia esta contraseña.

5. **Actualiza tu archivo `config.json`**:
   - Abre el archivo `config.json` en tu proyecto.
   - Pega la contraseña de aplicación copiada en el campo `sender_password` como valor.

   ```json
   {
     "email": {
         "sender_email": "tu_correo@gmail.com",
         "sender_password": "tu_contraseña_de_aplicación_aquí",
         "destinatarios": ["correo_soporte_juego@gmail.com", "test@test.com"]
         },
      "insult_words": [
         "aqui todos los",
         "insultos que",
         "quieras",
         "capturar",
      ],
     ...
   }
   ```

Con estos pasos, habrás configurado correctamente una contraseña de aplicación para usar en lugar de tu contraseña principal de Gmail, mejorando así la seguridad de tu cuenta.



## Uso

1. Configura el archivo `config.json` con los detalles necesarios, como las credenciales de correo electrónico y la lista de insultos.
2. Ejecuta la aplicación:
   ```bash
   python src/services/monitor_service.py
   ```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

