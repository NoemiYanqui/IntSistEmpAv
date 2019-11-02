# Lab. 5: MÓDULO VENTAS

## Desarrollo

1.  Instalación de Módulo Ventas.
2.  Creación de Cotización a cliente
    ![Github i1](images/2.4.png)

    - Verifiación de la creación de la cotización

3)  Entrega de productos de una Cotización
    ![Github i1](images/ComprovandoValidacionStockSuficiente.png)

    - Se verifica que el stock disminuye porque ya se hizo la entrega
      ![Github i1](images/DisminucionDelStock.png)
    - Se envió por correo
      ![Github i1](images/SendMail.png)
    - Se vio la impresión en .pdf
      ![Github i1](images/Print.png)

4)  Facturación y registro de pago de una Cotización
    ![Github i1](images/FacturaValidada.png)

    - Verificación de la conexion de la factura con el cliente.
      ![Github i1](images/DeudaCliente.png)
    - Factura/registrar pago
      ![Github i1](images/RegistrandoPago.png)
    - Se observa la factura como abierta por tener un saldo pendiente.
      ![Github i1](images/FacturaAbierta.png)

5)  Configuración de envío de Correos
    ![Github i1](images/FacturaAbierta.png)

    - Se edito el correo y la contraseña en el correo saliente
      ![Github i1](images/5.2.AgregarCorreo.png)
    - Configurando el correo saliente, editando datos
      ![Github i1](images/ConfigurandoCorreoSaliente.png)
    - Se acepta el correo de salida al hacer la verificación
      ![Github i1](images/PruebaSatisfactoria.png)
    - Verificación de la llegada del email al cliente
      ![Github i1](images/FacturaRecibida.png)

6)  Cambio de secuencia

    - Se edita el tamaño y formato de una cotización
      ![Github i1](images/EditSecuencias.png)
    - Verificacion de la secuencia editada
      ![Github i1](images/CambioEfectuado.png)

7)  Listas de precios

    - Se hace cambio en Ajustes para habilitar la opción de múltiples precios de un producto
      ![Github i1](images/HabilitarMultiplesPRECIOS.png)
    - Se agrega al producto las tarifas de nayorista y tarifa pública
      ![Github i1](images/AgregarListaDePrecios.png)
    - Se crea una cotización viendo la opción de Lista De Precios.
      ![Github i1](images/CreandoCotizaciónConPrecios.png)
    - En la edición de cliente se observa que aparece la opcion de Lista de precios de venta en la subpestaña Ventas y Compras.
      ![Github i1](images/OpcionClienteConPrecios.png)
    - También podemos habilitar la opción de precios calculados a partir de fórmulas como descuentos , márgenes y redondeos.

8)  Portal del cliente
    - Editando el acceso al cliente para que tenga acceso al portal
      ![Github i1](images/Acceso.png)
    - Se ve el correo que llega al haberle dado acceso al cliente.
      ![Github i1](images/Correo.png)
    - Estableciendo una nueva contraseña
      ![Github i1](images/8.5.png)
    - Verificación del acceso al portal
      ![Github i1](images/8.6.png)
    - Verificación que el cliente puede actualziar sus datos
      ![Github i1](images/ActualizarDatos.png)

## **Tarea**

1. Crear una cotización, validarla y registrar una factura por pago previo (La cotización será de S/1000.00 y la primera factura será de S/200.00, la otra por el restante)

   - Creamos la cotización
     ![Github i1](images/CreandoCot.png)
   - Se confirma la Venta y el presupuesto ha sido enviado.
   - Ahora se ve que aparece la conexión con el módulo inventario como una oden de entrega por hacer
     ![Github i1](images/VistaInventarios.png)
   - Validación para realizar la entrega
     ![Github i1](images/Validacion.png)
   - Creación de Factura
     ![Github i1](images/Factura.png)
   - Veremos por la validacion
     ![Github i1](images/ValidacionDeFactura.png)
   - Ahora se Registra El Pago, donde se pondra dos montos para pagar
     ![Github i1](images/Pay.png)
     -Se hace el pago y se registra el segundo pago
     ![Github i1](images/SegundoPago.png)

- DESDE EL LADO DEL CLIENTE

  - Ahora hacemos el envio de la primera factura
    ![Github i1](images/EnviarPrimeraFact.png)
  - Verificación del envio de la Favtura
    ![Github i1](images/MsnFactura.png)
  - Verificación del segundo envío de la factura
    ![Github i1](images/FAC2.png)

2. Adjunte una captura del proceso, de cómo verá el cliente mediante su portal web a la factura, al inicio de ser emitida, luego del primer pago, y finalmente cuando está pagada totalmente.

   - Ingresar al link de portal desde gmail
     ![Github i1](images/msnPortal.png)
   - Ingresar las credenciales
     ![Github i1](images/IngresoCred.png)
     ![Github i1](images/VistaPortal.png)

## Observaciones y Conclusiones

- Se vió que los componentes del módulo de ventas permite
- crear una cotización, donde podemos editar la informacion del cliente ; esta cotización pasa por tres etapas la de ser cotización , convertirse en presupuesto enviado y finalmente ordenes de venta.Al convertirse en orden de venta falta hacer la entrega de la misma y la facturación.
- Se aprendió que al realizar la cotizacion y convertirse en orden de entrega este proceso pasa al módulo de Inventario como una orden pendiente , una orden de entrega, que nos permite comprobar la disponibilidad en cuanto al stock.
- Se observó que una orden de entrega dentro de inventarios tiene como estados, borrador, esperando, listo y realizando.
- Se vio el elemento de Facturación que se puede hacer de 4 modos, linea de factura con o sin deduccion de pagos anticipados, adelanto d epago por % y pago anticipago con cantidad fija.

- Una factura posee los procesos de borrador , abierto y pagado.
- Se observa la conexión entre los módulos de inventarios y ventas.
- ODOO utiliza un servdor SMTP de correo también aprendimos que un cliente
  puede tener acceso al portal de odoo para que tengo accesoa al actualziacion de sus datos,a demas de ver sus facturas o pedidos realziados.
