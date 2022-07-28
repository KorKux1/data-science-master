# Introducción al Procesamiento Distribuido de Datos

Profesor: Gabriel Tamura.

## Introducción al Big Data

### **Para Recordar**

- Leer [Data Scientist the sexiest job of the 21st century](https://hbr.org/2012/10/data-scientist-the-sexiest-job-of-the-21st-century&ab=Article-Links-End_of_Page_Recirculation)

### **Palabras Claves**

- **Big Data:** Campo de estudio que trata de extraer valor de grandes volúmenes de datos, tanto estructurados como no estructurados.
Se caracteriza por las 4 V: su volumen, velocidad, variedad y veracidad.

### **Preguntas Importantes**

### Notas

- El big data es el detonante de la ciencia de datos.
- Como científicos de datos, debemos conocer objeto de estudio de la ciencia de datos. En este caso los datos, por lo tanto debemos conocer todo lo relacionado con los datos.

### ¿Qué es el Big Data?

- El campo que que trata formas de analizar, extraer información de datasets que son muy grandes o muy complejos para las formas de procesamiento de datos tradicionales.
- Es el objeto de estudio de la ciencia de datos.

### Símil entre la química y la ciencia de datos

![Untitled](resources/Untitled.png)

- Un científico en química, domina todo sobre los fundamentos de la materia: átomos y moléculas.
- Científico de datos debe dominar todo sobre los fundamentos de los datos.

### ¿Qué es la ciencia de datos y el científico de datos?

![Untitled](resources/Untitled%201.png)

- La ciencia de datos permite analizar fenómenos actuales con los datos.
  - Describir el fenómeno que ocurre → Analítica descriptiva → Es el qué ocurre, explica que fue lo que ocurrió.
    Observar el fenomeno, recoger muchos datos, explicar el fenomeno.
  - Analitica de Diagnostico → Razón por la que el fenomeno ocurre.
  - Análitica Predictiva: Como entiendo el fenomeno ahora puedo hacer predicciones sobre esto.
  Se modela el fenomeno.
  - Construir solucciones con los datos y modelos obtenidos.

### Los origenes de la ciencia de datos

![Untitled](resources/Untitled%202.png)

### ¿Qué hace un cientifico de datos como un profesional?

- Hacer descubrimientos mientras se nada en los datos.
- Encontrar los fenomenos apartir de los datos.
    - ¿Cómo hacemos que el fenomeno ocurra más fuerte? ¿Cómo le sacamos más provecho?
- Es capaz de estructurar datos
- Encontrar estructura de datos.
- Analizar los datos.
- Puede mantener conversaciones fluidas con los datos.

### Habilidades del cientifico de datos.

- Es importante que el cientifico de datos tenga un dominio de experticie (El área de negocio con el que va a trabajar, es necesario conocerla).

![Untitled](resources/Untitled%203.png)

¿Qué ocurre en internet en un minuto?

![Untitled](resources/Untitled%204.png)

### El ciclo de vida del Big Data.

![Untitled](resources/Untitled%205.png)

- Ingesta de datos: Almacenamiento
- Hay que ponerlo en acción
- Hay que asegurarse que los datos pueden ser explotables en la posteridad.
    - Alguien sacó los datos del clima desde 1899. Que ahora se usan para predecir el clima y ver la evolución del calentamiento global.

### Crecimiento del Big Data

- Tiene un crecimiento exponencial.

![Untitled](resources/Untitled%206.png)

![Untitled](resources/Untitled%207.png)

![Untitled](resources/Untitled%208.png)

- Hay que interiorizar las medidas de los datos.

![Untitled](resources/Untitled%209.png)

### Las 4 V de IBM para el Big Data

![Untitled](resources/Untitled%2010.png)

- Volumen: Es la principal caracteristica del big data.
    - Hay 7 billones de personas
    - Hay 6 Billones de telefono
    
    ![Untitled](resources/Untitled%2011.png)
    
- Velocidad: Velocidad con la que se produce los datos
    - Procesar datos realtime suele ser el problema más complejo.
    - Si los datos no se capturan en el momento que se produce. El dato se pierde.
    
    ![Untitled](resources/Untitled%2012.png)
    
- Variedad:
    - Tiene que estar acompañada de la velocidad y el volumen.
    - Cuando hay mucha variedad de datos en grandes volumenes o en velocidades muy altas. Se vuelve un problema del big data.
    
    ![Untitled](resources/Untitled%2013.png)
    
    ![Untitled](resources/Untitled%2014.png)
    
    ![Untitled](resources/Untitled%2015.png)
    
- Veracidad
    - Es la más dificil de lidiar.
    - Hay muchos datos, y cada vez más datos se quieren. (Entre más datos se tenga en teoría, genera más confianza)
    - Muchos datos tienen falta de veracidad y confiabilidad
        - Por ejemplos datos de encuestas.
    
    ![Untitled](resources/Untitled%2016.png)
    
    - ¿Por qué los sensores aunque generan muchos datos son los menos confiables?
        - Falta de calibración.
        - Calidad de los sensores.
        - Al manipularlos también se puede dañar esa data capturada.
- Valor (Quinta):
    - Habilita la posibilidad de obtener valor a traves de la análitica.

<aside>
📌 **RESUMEN**:

</aside>

## Big Data

### **Para Recordar**

### **Palabras Claves**

### **Preguntas Importantes**

### Implicaciones del Big Data

- Esta es la cantidad de datos que genera dos motores de los vuelos de un boing 737.
Si quiero hacer análisis de estos motores para saber cuando hacer el mantenimiento ¿Cómo se le daría manejo a esta cantidad de datos?

![Untitled](resources/Untitled%2017.png)

Si se quisiera trabajar con estos dos datos toca resolver los problemas de:

- Adquisición de los datos
- Almacenamiento de los datos.
- Recuperación: Estos datos se generan muy rápido ¿Cómo se le da mejo?
- ¿Cómo se distribuye esta información?
- ¿Cómo se procesa?

![Untitled](resources/Untitled%2018.png)

- Algunas preguntas que surgen al manejar big data:

![Untitled](resources/Untitled%2019.png)

- ¿Qué otras variables afectan a los datos que estamos almacenando y que no los estamos contemplado?

### Ciencia de Datos

- La ciencia de datos surge a partir de la big data.

![Untitled](resources/Untitled%2020.png)

- Definitivamente no se deben borrar los datos.
No sabemos que datos son importantes como para borrarlos.
- Hacer procesamiento secuencial de big data puede ser muy demorado, normalmente es mejor usar procesamiento distribuido.

### ¿La nube nos soluciona los retos de big data?

- No en todos los casos.
- Por si solo usar una maquina cloud con grandes recursos para trabajar en Big Data no en todos los casos nos funciona.

![Untitled](resources/Untitled%2021.png)

![Untitled](resources/Untitled%2022.png)

- Con Big Data hablamos de problemas grandes:

3 Dimensiones:

![Untitled](resources/Untitled%2023.png)

Hay muchos problemas ¿Y las soluciones?

- Para las soluciones nos remontamos hasta el tema de los BI.
- Los data warehouse para algunas organizaciones sigue siendo muy bueno.
    - A pesar de que los data warehouse son antiguos aún son validos para varios casos de análitica.

![Untitled](resources/Untitled%2024.png)

- Los datos pueden estar en varias fuentes, pero los centralizamos para el uso de todos.
- Aunque ya en teoría se tenía soluciones tecnologías el big data crea problemas de estrategia y arquitectura.
- Se plantea los data swarmp para almacenar datos.

![Untitled](resources/Untitled%2025.png)

- Una evolución de los data swamp son los data lake donde se busca tener los datos más organizados que un data swarm y que nos permita más opciones.

![Untitled](resources/Untitled%2026.png)

- Los datos tenemos que tenerlos de una forma odenada (La gobernanza de los datos).
Todos deben seguir la gobernanza de los datos para que se pueda sacar el máximo provecho de los datos.

![Untitled](resources/Untitled%2027.png)

- Como ya con un solo computador no podemos procesar los datos, necesitamos distribuir.
- Distribuyendo apoyamos:
    - En la escalabilidad y rendimiento de los sistemas.
    - Tolerencia a fallas.
    Si un computador falla durante el procesamiento no perdemos todo el trabajo realizado.
    - Variedad de los formatos.
    - Muchas aplicaciones.
    - Agrega valor.
- La mejor solución que tenemos por ahora para estos problemas son los data lake: Distribución de datos y distribución de procesamiento.

### ¿Cual es la infraestructura para hacer procesamiento distribuido de big data?

Tres cosas claves: Hadward, software y conceptos básicos de redes.

- Hardware Infraestructura:
    - **Clusters. 7:30**
        - Se arma con los racks
    - Racks: Unidad de organización.
    Puede tener elementos de procesamiento o almacenamiento.
    Los elementos deben estar interconectados para que trabajen juntos.
        - Se debe escoger con cuidado las unidades de procesamiento y almacenamiento.
        
        ![Untitled](resources/Untitled%2028.png)
        
        - KVM: Comparte el mouse, teclado y pantalla que puede manejar una unidad de rack. Solo 1 a la vez.
        - Se accede de forma remotamente desde otro computador.
        
        ![Untitled](resources/Untitled%2029.png)
        
    - Debe ordenarse los clables para poder identificarlo. (Ingenieros telematicos o ingenieros de red). Esto no puede ser un desorden
    - Its components.

![Untitled](resources/Untitled%2030.png)

- Nodos de procesamiento:
    - Se debe controlar el calor.
    
    ![Untitled](resources/Untitled%2031.png)
    
    - Tiene dos interfaces de red para tener tolerancia de fallos.
- Elementos de red:

![Untitled](resources/Untitled%2032.png)

Red de computadores:

![Untitled](resources/Untitled%2033.png)

Almacenamiento:

La jerarquía de memoria.

![Untitled](resources/Untitled%2034.png)

El Nivel 5:

![Untitled](resources/Untitled%2035.png)

![Untitled](resources/Untitled%2036.png)

- Las latencias normalmente se miden por tipo de operación (escritura, actualizar, borrado, lectura)
- Hay que combinar el gobierno de datos con la arquitectura de datos. El gobierno por si solo no es suficiente.

DAS: 

![Untitled](resources/Untitled%2037.png)

- DAS (Direct Attached Storage): Caja de almacenamiento, no permite compartir datos con otros computadores.
- Se puede acceder a los datos de un DAS desde otros computadores a partir de la red y un software. Sin embargo, al conectar muchos computadores (4) de esta forma el rendimiento se viene al piso.
- El DAS sirve para empezar.
- Para organizaciones que el nivel de madurez es muy bajo.

NAS: 

![Untitled](resources/Untitled%2038.png)

- Si la empresa tiene un nivel de madurez más alto. Donde varios equipos tienen que acceder a los datos es mejor empezar por un NAS.
- Pensado para el uso concurrente por parte de diferentes equipos.
- Apróximadamente  hasta 15 personas haciendo tareas de analitica de forma concurrente.
- No se conecta directamente a un computaor.
- Solución para los problemas intermedios.

SAN: 

- Cuando los requerimientos sobrepasan las capacidades de un NAS, se pasa al SAN.
- Para procesamiento de datos más complejo.

![Untitled](resources/Untitled%2039.png)

- Se agrega una red solo para el almacenamiento de datos.

![Untitled](resources/Untitled%2040.png)

- Normalmente los servidores de procesamiento se deben conectar al switch de Fibra.
- Los cientificos de datos, correrían los modelos sobre los servidores.

![Untitled](resources/Untitled%2041.png)

### On Premise o Cloud

- Balance entre on premise y la nube.
- Empezar on premise, ahí se mirar la nube.
- La nube es costosa y requiere buen canal de subida y bajada.
- Si no se tiene experencia es mejor empezar on premise, dominando la tecnologia en sitio.
- Se interactura de la misma forma on premise o Cloud.
- Por detrás On Premise y Cloud funcionan igual.

### Tipos de escalamiento:

![Untitled](resources/Untitled%2042.png)

- Escalamiento Vertical: Scale Up
    - Tiene un limite
    - Se da según las necesidades de procesamiento y almacenamiento que se requieran.
    - Es costoso
    - Tiene mejor performance.
    - Costo de mantenimiento es caro.
    - Cuellos de botella
        - Al estar conectado a un switch para obtener los datos, los procesadores internos tienen que coordinarse para procesar los datos.
    - Limitado por la capavidad del servidor.
- Escalamiento horizontal: Scale out
    - Es mejor comprar varios computadores pequeños.
    - Genera más problemas para ciertas técnicas y modelos.
    - Operaciones más lentas.
    - Costo de transportar datos en la red (Tiempo).
    - Facil y flexible.
    - Relaticamente barato.

### Infraestructura en el negocio

![Untitled](resources/Untitled%2043.png)

- Los equipos de hardware se vuelven absoletos.
- Refrigeración.
- Energía regulada e inenterrumpida.

¿Comprar, Leasing o Rentar?

- Comprar y volverse obsoleto generará nuevos costos.

### Data Lake en la Cloud

![Untitled](resources/Untitled%2044.png)

- Temas legales. Dependiendo de los datos que pueden estar o no dentro del país.
- Buena conexión a internet y confiable.
- Almacenamiento de datos cobro 24-7.
- Se trata de arrendamiento de equipos sobre internet.
- Pago por demanda.

![Untitled](resources/Untitled%2045.png)

¿Qué clase de Soporte se necesita?

![Untitled](resources/Untitled%2046.png)

- IaaS:
    - Soluciona el problema de obselecencia.
    - Refrigeración.
    - Mantenimiento.
    - Ofrece la infraestructura.
    
    ![Untitled](resources/Untitled%2047.png)
    
- PaaS:
    - Se tiene todos los servicios genericos listos para usarlos.
    - Ya tiene listo sistemas operativos y todo.
    
    ![Untitled](resources/Untitled%2048.png)
    
- SaaS:
    - Dejan toda la infraestructura y plataforma montada lista para su uso.

![Untitled](resources/Untitled%2049.png)

### Retos, Pros y Contras de Cloud

![Untitled](resources/Untitled%2050.png)

Retos: 

- Aspectos legales que datos pueden estar o no fuera del país.
- Complejidad de los stack de software distribuido.
- Dependencias, upgrades y compatibilidad.

Cons:

- Estimar los recursos que se van a necesitar en la nube.
- Costos financieros.
- Requiere un buen ancho de banda e internet.

Pros:

![Untitled](resources/Untitled%2051.png)

- Disponibilidad de recursos instantaneo.
- Escalabilidad horizontal.
- Libre de mantenimiento del hardware.
- No se necesita un equipo muy grande para manejar hardware, network e infraestructura
- Te deja concentrar en los objetivos de negocio

![Untitled](resources/Untitled%2052.png)

### Como construir un Data Lake

- Primero hay que planear
- Pensar en el modelo que mejor encaja en las necesidades de la organización a largo plazo.
- Se construye pensando en su contexto más grande.
- Se debe construir pensando no solo en el data lake sino en todo lo que se va a construir alrededor del data lake.
- Se debe tener el contexto de la organización.

![Untitled](resources/Untitled%2053.png)

<aside>
📌 **RESUMEN**:

</aside>

## Del PC al DataLake: Operación básica de GNU/Linux y Configuración de Red

### **Para Recordar**

### **Palabras Claves**

### **Preguntas Importantes**

### Notas

- El computador es la herramienta básica de los cientificos de datos.
- 3 Formas para usar el PC para mainupular datos.
    - De forma Individual
    - Indivudual-virtualizada: Cuando se desarrolla parte de la tarea, se escala al cluster.
    - Parte de un cluster.
- Verificar instalación de herramientas

![Untitled](resources/Untitled%2054.png)

<aside>
📌 **RESUMEN**:

</aside>