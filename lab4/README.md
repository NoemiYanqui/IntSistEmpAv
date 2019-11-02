# Lab. 4: MÒDULO LOGÌSTICA

## Desarrollo

1.  Creando base de datos
    ![Github i1](images/creando_bd.png)
    1.1. Instalaciòn del modulo de inventarios<br />
    ![Github i1](images/instalacionModuloInventario.png)
2.  Configuración de Almacenes<br />
    ![Github i1](images/Expectativas.png)<br />
    2.1. Configurando la opcion de Multialmacen<br />
    ![Github i1](images/Multialamacen.png)<br />
    2.11 Agregar contacto y dirección<br />
    ![Github i1](images/AddContact.png)<br />
    2.13 Verificación de creación de rutas para dicho almacén<br />
    ![Github i1](images/RutasDelAlmacen.png)<br />

3.  Tipo de operaciones
    3.1 Acceder a tipos de operaciones dentreo del submenu de Gestion de almacenes<br />
    3.2 Visualización de las operaciones permitidas por el sistema.<br />
    3.3 Visualización de personalización;Tipo de operación Recepciones.<br />
    ![Github i1](images/Recepciones.png)<br />
    3.4 Configuración rutas Multietapa<br />
    ![Github i1](images/HabilitandoRutasMultietapa.png)<br />
4.  Gestión de Productos<br />
    4.1. Menu productos<br />
    4.2. Creando un Producto(Observacion de la existencias de tipos de productos, como Producto Almacenable)<br />
    4.3.Tipo de producto (Servicio)<br />
    4.4. Ver caracteristicas de un producto Consumible<br />
    4.4. crear nuevo contacto de la compañia<br />
    4.5. Ver datos adicionales del producto.<br />
    4.6. Creando nuevo producto de Manzana Verde.<br />
    4.7. Actualizar cantidad disponible.<br />
    4.8. Verificación del stock A mano aparece 15(Aunque se configuró 10 en el almacen principal y 5 en el almacen secundaria)<br />
    ![Github i1](images/VerStockAMano.png)<br />
    4.9. Impresión de etiquetas(útiles para pegar en los anaqueles de venta)<br />
    4.10. Movimientos de producto, nos permite rastrear todos los traslados de un producto<br />
    ![Github i1](images/MovimientosDeProducto.png)<br />

5.  Importación y Exportacion masiva de productos<br />

    5.6. Exportando Excel
    ![Github i1](images/ExportandoExcelDeProductos.png) <br />
    5.8. Veremos como probar la importación<br />
    ![Github i1](images/ProbarImportaciones.png)<br />
    5.9. Veremos los cambios subidos al sistema.<br />
    ![Github i1](images/VerificaciónDeImportaciónDeProductos.png)<br />

6.  Ajustes de Inventarios
    6.1. Realizando ajuste de inventario (por medio del submenu de operaciones)<br />
    ![Github i1](images/VerificaciónDeImportaciónDeProductos.png)<br />
    6.2. Realizando ajustes de inventario para agregar nuevo stock de cada producto.<br />
    ![Github i1](images/NuevosStocks.png)<br />

7.  Transferencias internas

    7.4. configurando para hacer la Transferencia<br />
    ![Github i1](images/RealizandoTransferencia.png)<br />
    7.7. Observamos que al hacer clic en stock a mano este si aparece departido en dos opciones<br />
    ![Github i1](images/ReparticionDeStok.png)<br />
    7.8. Viendo la vista tablero, se observa la cantidad de transferencias realizadas.<br />

8.  Informes

    8.1. Se observa el submenú de Inventario dentro de Informes<br />
    ![Github i1](images/InformesInventario.png)<br />
    8.2. Se observa el submenú de Movimientos de Stock dentro de Informes<br />
    ![Github i1](images/MovimientosDeStock.png)<br />
    8.3. Se observa el submenú de Movimientos de producto dentro de Informes
    ![Github i1](images/MovDeProductos.png)<br />

## **Tarea**

9.

9.1. Habilite las opciones Atributos y variantes, y Unidades de medida. Vaya a la ficha de producto e indique las diferencias, así como adjunte imágenes de productos con varios atributos y/o unidades de medida distintas.<br />

Se observa la habilitación en Configuración/Producto<br />
![Github i1](images/ConfiguracionHabilitandoAtributosyUnidades.png)<br />
Se visualiza la creacion del atributo Tipo en el caso de pinturas<br />
![Github i1](images/CreandoAtributo.png)<br />
Observando atributos y unidades<br />
![Github i1](images/caracteristicas.png)<br />
Productos con varios atributos<br />
![Github i1](images/VariantesDeProducto.png)<br />
![Github i1](images/VariantesDeUnProducto.png)<br />
Las diferencias radican en que por cada valor de un atributo se puede configurar un precio distinto.<br />

9.2. Entre al menú Reglas de abastecimiento e intente crear una. Indique en que caso puede servir este proceso.<br />
![Github i1](images/CreandoReglaDeAbastecimiento.png)<br />
Esta regla se viasualiza en los productos ingresados.<br />
![Github i1](images/VisualizaciónDeReglaDeAbastecimiento.png)<br />

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
