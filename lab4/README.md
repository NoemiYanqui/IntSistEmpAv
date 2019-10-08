# Lab. 4: MÒDULO LOGÌSTICA

## Desarrollo

1.  Creando base de datos
    ![Github i1](images/creando_bd.png)
    1.1. Instalaciòn del modulo de inventarios
    ![Github i1](images/instalacionModuloInventario.png)
2.  Configuración de Almacenes
    ![Github i1](images/Expectativas.png)
    2.1. Configurando la opcion de Multialmacen
    ![Github i1](images/Multialamacen.png)
    2.11 Agregar contacto y dirección
    ![Github i1](images/AddContact.png)
    2.13 Verificación de creación de rutas para dicho almacén
    ![Github i1](images/RutasDelAlmacen.png)

3.  Tipo de operaciones
    3.1 Acceder a tipos de operaciones dentreo del submenu de Gestion de almacenes
    3.2 Visualización de las operaciones permitidas por el sistema.
    3.3 Visualización de personalización;Tipo de operación Recepciones.
    ![Github i1](images/Recepciones.png)
    3.4 Configuración rutas Multietapa
    ![Github i1](images/HabilitandoRutasMultietapa.png)
4.  Gestión de Productos
    4.1. Menu productos
    4.2. Creando un Producto(Observacion de la existencias de tipos de productos, como Producto Almacenable)
    4.3.Tipo de producto (Servicio)
    4.4. Ver caracteristicas de un producto Consumible
    ![Github i1](images/creandoUsuario.png)
    4.4. crear nuevo contacto de la compañia
    4.5. Ver datos adicionales del producto.
    4.6. Creando nuevo producto de Manzana Verde.
    4.7. Actualizar cantidad disponible.
    4.8. Verificación del stock A mano aparece 15(Aunque se configuró 10 en el almacen principal y 5 en el almacen secundaria)
    ![Github i1](images/VerStockAMano.png)
    4.9. Impresión de etiquetas(útiles para pegar en los anaqueles de venta)
    4.10. Movimientos de producto, nos permite rastrear todos los traslados de un producto
    ![Github i1](images/MovimientosDeProducto.png)

5.  Importación y Exportacion masiva de productos

    5.6. Exportando Excel
    ![Github i1](images/ExportandoExcelDeProductos.png)  
    5.8. Veremos como probar la importación
    ![Github i1](images/ProbarImportaciones.png)
    5.9. Veremos los cambios subidos al sistema.
    ![Github i1](images/VerificaciónDeImportaciónDeProductos.png)

6.  Ajustes de Inventarios
    6.1. Realizando ajuste de inventario (por medio del submenu de operaciones)
    ![Github i1](images/VerificaciónDeImportaciónDeProductos.png)
    6.2. Realizando ajustes de inventario para agregar nuevo stock de cada producto.
    ![Github i1](images/NuevosStocks.png)

7.  Transferencias internas

    7.4. configurando para hacer la Transferencia
    ![Github i1](images/RealizandoTransferencia.png)
    7.7. Observamos que al hacer clic en stock a mano este si aparece departido en dos opciones
    ![Github i1](images/ReparticionDeStock.png)
    7.8. Viendo la vista tablero, se observa la cantidad de transferencias realizadas.

8.  Informes

    8.1. Se observa el submenú de Inventario dentro de Informes
    ![Github i1](images/InformesInventario.png)
    8.2. Se observa el submenú de Movimientos de Stock dentro de Informes
    ![Github i1](images/MovimientosDeStock.png)
    8.3. Se observa el submenú de Movimientos de producto dentro de Informes
    ![Github i1](images/MovDeProductos.png)

## **Tarea**

9.

9.1. Habilite las opciones Atributos y variantes, y Unidades de medida. Vaya a la ficha de producto e indique las diferencias, así como adjunte imágenes de productos con varios atributos y/o unidades de medida distintas.

Se observa la habilitación en cConfiguración/Producto
![Github i1](images/ConfiguracionHabilitandoAtributosyUnidades.png)
Se visualiza la creacion del atributo Tipo en el caso de pinturas
![Github i1](images/CreandoAtributo.png)
Observando atributos y unidades
![Github i1](images/Caracteristicas.png)
Productos con varios atributos
![Github i1](images/VariantesDeProducto.png)
![Github i1](images/VariantesDeUnProducto.png)
Las diferencias radican en que por cada valor de un atributo se puede configurar un precio distinto.

9.2. Entre al menú Reglas de abastecimiento e intente crear una. Indique en que caso puede servir este proceso.
![Github i1](images/CreandoReglaDeAbastecimiento.png)
Esta regla se viasualiza en los productos ingresados.
![Github i1](images/VisualizaciónDeReglaDeAbastecimiento.png)

## Observaciones y Conclusiones

- Se vió que se puede imprimir etiquetas de un producto, en el que se muestra el nombre del producto y el código de barras.
- Se aprendió a realizar configuraciones en el módulo de Inventarios; donde
  se aprendió a realizar operaciones como transferencias de un almacen a otro dentro o fuera de un local.
- Se vio sobre las reglas de abastecimiento que nos ayuda a poner un stock minimo y/ estock máximo y cuandi dicho producto llega a ese stock se genera una cotización
- Se vió cómo hacer la instalación donde podemos creae nuestros almacenes, adempas nos permite hacerlo por medio de la ahabilitacion de multialmacenes, puesto que en el mismo local creamos 2 alamcenes el principal y el secundario.
- Se aprendio a ver las ubicaciones de almacenamiento asi como las rutas multietapa.
- Se aperndio a importar y esxportar los productos, esto pueden ser de 3 tipos, almacenables, servicio y consumble.
- Se aprendió a ver las operaciones, aimismo como agregar stock ver el stock de los productos por fecha.
- Este modulo tambien nos permite tener reportes, asimismo podemos habilitar los ajustes de atributos de un producto y/o unidades del mismo.
