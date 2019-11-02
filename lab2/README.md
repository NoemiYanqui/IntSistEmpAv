# Lab. 2: ADMINISTRACIÓN DE MÓDULOS ODOO

## Desarrollo

3.6. Aplique los Filtros “Apps” e “instalado” simultáneamente para ver los módulos instalados actualmente:
![Github i1](/images/evidencia.png)

4.1 Identificación del “Tablero” de opciones

Tablero1--> Gestión de Ausencias
Tablero2-->Módulo Punto de Venta
Tablero3--> Módulo Gestión de Ventas

4.2. Opciones de configuración de ODOO. Elija la opción Configuración

Se observa que en el menu de ajustes o configuración se tiene la opción de
activar el modo desarrollador , que nos brinda más opciones en el tablero, ademas
que nos muestra un menú pensdo e nlos desarrolladores

5. Creación de un módulo en ODOO
   ![Github i1](/images/comandoParaCrearModulo.png)
   5.7 Verificacion de la existencia de la carpeta testmodulo1
   ![Github i1](/images/moduloCreado.png)
   ComandoParaCrearModulo.png
   5.9 Archivo **init**.py
   ![Github i1](/images/init.py.png)
   5.10. **manifest**.py
   ![Github i1](/images/CambiosManifest.py.png)
   5.14 Instalando módulo creado testmodulo1
   ![Github i1](/images/testmodulo1Instalado.png)
   5.15.Ver Opcion de desinstalar
   ![Github i1](/images/DescripcionModulo1.png)
   5.17. Desinstalando el módulo testmódulo1
   ![Github i1](/images/DesintalandoModulo1.png)

## **Tarea**

1. Tabla de funcionalidades:
   ![Github i1](/images/EstructuraDeUnModuloEnOdoo.png)

## Observaciones y Conclusiones

- Se observa que odoo cuenta con una herramienta que nos permite crear módulos completos para
  poder empezar a programar, además se ve que para crear un módulo es necesario
  hacerlo desde la raiz de odoo , ingresar al servidor
- Se observa que los módulos de odoo se encuentran en la carpeta addons
- Se observa que ODoo UTILIZA una arquitectura MVC
- Se vió que la diferencia entre los módulos o aplicaciones; es que en los primeros son bloques
  para la construccion de las apps de odoo, un módulo puede agregar o modificar caracteriticas
  en odoo.En cambio las apps proporcionan una caracteristica central, alrededor de la cual otros módulos
  agregan características.
- Se leyó en la documentación de odoo11 la recomendación de no modificar modulos existentes , esto es
  considerado un mala práctica, pero si debemos crear módulos nuevos que sean plaicados sobe los módulos que
  queremos modificar, e implementar , ya que odoo permite realizar herencia .
- Este laboratorio permitió:Instalar Aplicaciones, Crear un módulo , actualizar la tabla en el servidor de oddo e instalar el módulo creado
- Se pueden realizar busquedas avanzadas, por medio de filtros, Agrupaciones y/o favoritos;
  asimismo se vió como instalacr una aplicación o un módulo.
- Al instalar una aplicación se observa que en la barra de menu aparece una nuevo menu,
  en cambio al instalar un módulo aparecen mas de una aplicacion instalada , de modo que se añade más
  de un menú en la barra de menús
- Identificación del tablero de opciones.
- Diferencia entre aplicaciones y modulos.
- Se observa que al instalar una app se muesta como un menu extra en la parte superior
  oca github , es el repositorio para buscar de maner confiable.
