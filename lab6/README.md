# Lab. 6: MÓDULO COMPRAS

## Desarrollo

1.  Instalación de Módulo Compras.
    ![Github i1](images/int.png)

2.  Creación de Solicitud de presupuesto
    ![Github i1](images/CreandoSol.png)

    - Configuracion del idioma español(PE)
      ![Github i1](images/Idioma.png)
    - Cuando editamos el separador de decimales y el separador de miles
      ![Github i1](images/ConfIdioma.png)
    - Se ve que se puede progrmar la fecha prevista, el plazo de pago al proveedor y la fecha de aprobación.
      ![Github i1](images/EntregasYFacturas.png)
    - Se confirma el pedido para luego recibir los productos, asimismo se habilita la opción de envío.
      ![Github i1](images/2.6.png)

3.  Recepción de compras

    - Al dar clic en recibir producto nos lleva a un formulario de trnasferencia.
      ![Github i1](images/Recepcion.png)
    - Al editar la transferencia podemos editar la cantidad de Realizado y luego validar estos datos de esa manera creamos una entrega parcial.
      ![Github i1](images/EntregaParcial.png)
    - Se generó dos transferencias por sólo una cotización, y podemos verificarlo de la siguiente manera
      ![Github i1](images/VerificacionDeDosTransferencias.png)

4.  Facturación de proveedores
    ![Github i1](images/Fact.png)
    ![Github i1](images/4.2.png)

    - Podemos observar los detalles del Proveedor en el menu de Compras /Compras /Proveedores.
      ![Github i1](images/Detall.png)
    - Agregamos una cuenta bancaria en la subpestaña de Ventas y Compras desde la Edición de datos del proveedor
      ![Github i1](images/CuentaBanc.png)
    - Se realiza el Pago de la factura y se evidencia como saldo 0
    - ![Github i1](images/4.4.png)

5.  Tarifas de proveedores

    - Se observa que este producto esta asociado con un proveedor del mismo en la subpestaña de compras de la información del producto.Vemos la Tarifa del Proveedor de este producto , pudiendo tener varios proveedores del mismo producto y tomar una buena decisión.
      ![Github i1](images/5.1.png)
    - Ahora Activamor la opción de Tarifas de compra
      ![Github i1](images/5,2.png)
    - Se habilita la tarifa de Compra, donde establecemos distintos precios para un mismo producto considerando la cntidad mínima asi como también la validez para un periodo de fechas.
      ![Github i1](images/5.3.png)

6.  Licitaciones

    - Una licitación permite la realización de un concurso y escoger la compra dependiendo del mejor postor,ahora veremos la habilitacion de Acuerdos de Compra
      ![Github i1](images/6.1.png)
    - Se crea EL ACUERDO DE COMPRA ingresando la fecha límite y la fecha de entrega , para guardarla y luego validarla.
      ![Github i1](images/6.4.png)
    - Se observa que un acuerdo de compra pasa por los procesos de validar; Confirmar y Nuevo Presupuesto
    - Se observa que se crearon 2 pressupuestos para una sola licitación
      ![Github i1](images/Licitaciones.png)

7.  Módulos de Terceros
    ![Github i1](images/TopBuying.png)

    - Instalación del módulo Toponimos de Perú
      ![Github i1](images/Top.png)

    ![Github i1](images/Evidencia.png)

## TAREA

1. Cómo elegir un ganador a dicha licitación, realizar la facturación y la entrega. Adjunte imágenes de todo lo relatado.

- Validamos el Acuerdo de Compra(Licitación)
  ![Github i1](images/}.png)
- Ahora nos aparece la opcion de Realizado, y el proceso como seleccion de oferta.Realizado significa que la licitacion esta hecha, para ello debemos seleccionar un RFQ (seleccionar una solicitud de presupuesto)
  ![Github i1](images/2.png)
- Seleccionamos el presupuesto más conveniente de la Licitacion TE00001
  [Github i1](images/3.png)
- Confirmamos Pedido
  [Github i1](images/4.png)
- Ahora Recibimos los productos
  ![Github i1](images/RecibirProductos.png)

- REALIZA LA FACTURACIÓN y entrega del producto
  ![Github i1](images/F1.png)
- Creando factura al pedido de compra que ganó la licitación y/o AcuerDo de Compra.
  ![Github i1](images/F2.png)
- Ahora Registramos el pago de la Factura para que se realice la entrega
  ![Github i1](images/F3.png)
- Ahora verificamos el stock del producto
  ![Github i1](images/I1.png)

2. Módulos de terceros

- Se ingresa al portal de apps de odoo para acceder al catálogo de módulos creados por ODOO. Hay todo tipo de módulo, de todo rubro entreg gratuitos y pagantes

- Buscando el módulo de Topo Buying Products
  ![Github i1](images/7.2.png)
- Configurando la ruta para el acceso de módulo de terceros en el archivo odoo.conf
  ![Github i1](images/7.5.png)
- Ahora se realiza la actualizacion de lista de aplicaciones, con el fin de obtener la app descargada anteriormente.
  ![Github i1](images/7.6.png)

## Observaciones y Conclusiones

- Se crearon solicitudes de presupuesto, asimismo cómo editar informacipon del idioma, donde podemos cambiar el separador de decimales y miles entre otras opciones
- Se vio que una solicitud de presupuesto puede convertirse en una compra en la que se ven entrega y facturas.
- Se aprendió que una transferncia se puede hacer en más de una parte , además que en la edición del perfil de un proveedor se puede agregar cuenta bancaria.
- Se aprendió a realizar tarifas de precios a un mismo proveedor, desde cómo configurarlo hasta hacer muchas tarifas de precio de un producto de un mismo proveedor, considerando sus variantes.
- Se observó que en este módulo podemos utilizar Los Acuerdos de Compra , habilitando esta opción podemos tener varios presupuestos de distintos proveedores.
