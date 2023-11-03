## System Security

In this section, we will want you to demonstrate your knowledge of security best practices. Write your answer to this
question in `security_question.md` either in English or Spanish.

Suppose you are the head of Engineering for an exciting new tech startup that installs solar panels via an app. 
It's Uber for Solar Panels! You are doing a security audit of your app's infrastructure. You are using the OWASP Top 10
for 2021 as a guide for what security issues might be a problem for you. 

Your infrastructure is deployed in Kubernetes containers on Amazon Web Services. It has these components:
- A mobile app for Android and iOS.
- A web frontend that the customer can use instead of the mobile app. This is written in Javascript with Next.js.
- A MySQL database that stores customer information, including passwords, home addresses, telephone numbers, etc. It \
  also contains customer order information.
- A Python backend implemented in FastAPI. This talks to the database and serves data to both the web frontend and the \
  mobile apps. 

You have 12 software engineer employees who have full access to the system, 3 customer support employees who can view
customer information and make changes to orders and accounts, and one sales employee. 

Using the OWASP Top 10, what would you look for to make your system secure?

Usando el OWASP Top 10, realizaría las siguientes acciones

### 1. Control de acceso roto
- Verificar que los permisos para todos los roles de usuario estén configurados y aplicados correctamente, garantizando que los ingenieros de software tengan solo el acceso necesario para realizar sus tareas.
- Implementar principios de privilegio mínimo, garantizando que los empleados de atención al cliente tengan acceso restringido, para que estos solo puedan ver y modificar la información del cliente según sea necesario.
- Registras cambios realizados en cuentas y permisos

### 2. Fallos criptográficos
- Asegurar que los datos seab confidenciales, como contraseñas e información personal, que estén cifrados tanto en tránsito como en reposo (flujo de datos).
- Utilizar HTTPS con TLS para la comunicación entre el frontend y el backend.
- Verificar la configuración de la base de datos, para que se puedan usar conexiones cifradas y que los datos se almacenen mediante cifrado

### 3. Inyección
- Proteger contra la inyección de SQL mediante el uso de consultas parametrizadas en el backend de Python.
- Escanear de manera periódica el código base en busca de fallas de inyección y validar las entradas tanto en el lado del cliente como en el del servidor.

### 4. Diseño inseguro
- Garantizar que la seguridad esté integrada en el ciclo de vida del desarrollo de software.
- Revisar y actualizar la arquitectura periódicamente para incorporar servicios de seguridad.

### 5. Configuración incorrecta de seguridad
- Mantener actualizados todos los sistemas, incluidos Kubernetes y los servicios de AWS.
- Reforzar las configuraciones de seguridad para todos los componentes de la infraestructura.

### 6. Componentes vulnerables y obsoletos
- Mantener actualizado el software, Next.js, FastAPI y los sistemas de bases de datos, para evitar vulnerabilidades y obsolencia.

### 7. Fallos de identificación y autenticación
- Implementar autenticación multifactor para los empleados que acceden al sistema.
- Implementar almacenamiento de contraseñas mediante algoritmos de hash.
- Implementar mecanismos de bloqueo de cuentas.

### 8. Fallos de integridad del software y de los datos
- Utilice canalizaciones de integración continua/implementación continua (CI/CD) con pruebas de seguridad automatizadas.
- Realizar comprobaciones de integridad del código antes de la implementación.
- Usar componentes o bibliotecas de terceros que provengan de fuentes confiables.

### 9. Fallos de seguimiento y registro de seguridad
- Implementar registro centralizado de eventos de seguridad y monitoreo regular.
- Configurar alertas para actividades sospechosas que podrían indicar un incidente de seguridad

### 10. Falsificación de solicitudes del lado del servidor (SSRF)
- Implementar validaciones del lado del servidor para prevenir ataques SSRF.
- Restringir el tráfico saliente desde el backend

