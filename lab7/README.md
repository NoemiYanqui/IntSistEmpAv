# Lab. 7: MÓDULO PUNTO DE VENTA

## Desarrollo

1.  Instalación de Módulo Punto de Venta
    Creación de una nueva baseDeDatos
    ![Github i1](images/db.png)
    Instalación del módulo de Punto de Venta
    ![Github i1](images/1.png)

2.  Funcionamiento del Punto de Venta
    Se hizo clic en nueva Sesión.
    Se visualzia una interaz que contiene todos los productos registrados en el sistema.
    ![Github i1](images/2.png)
    Creando un nuevo cliente y la selección del mismo
    ![Github i1](images/cliente.gif)
    Cuando presionamos en pagar
    ![Github i1](images/2.4.png)
    Generación del ticket para imprimir
    ![Github i1](images/ticket.png)
    Visualizando el control de cierre de turno
    Sesión de punto de venta cerrada, evidencia:
    ![Github i1](images/SesionCerrada.png)

3.  Añadiendo control al POS.
    Accediendo a la configuración de Punto de Venta
    ![Github i1](images/Conf.png)
    Configurando en control de precios. Editando la configuración del módulo de Punto de Venta.
    ![Github i1](images/conf1.png)
    En la sección Pagos,habilitamos la opción de Control de Efectivo
    ![Github i1](images/mast.png)
    Configurar un balance de apertura, cuando se desea una nueva sesión de venta, ya no redirige directamente al punto de venta , sino que aparece una ventana previa.Vemos que debemos configurar un balance de Apertura
    ![Github i1](images/3.3.png)
    Podemos controlar el efectivo con la cantidad de monedas y cheques con las que se apretura la caja y bajo qué turno , como se ve a continuación.
    ![Github i1](images/3.33.png)
    Se observa las maneras para efectuar el pago
    ![Github i1](images/ModosDePago.png)
    Creando usuario con permisos
    ![Github i1](images/3.5.png)
    Insertando pin de seguridad a usuario administrador
    ![Github i1](images/3.6.png)
    Cambio de Usuario para seleccinar el usuario con el que se harès uso del punto de venta
    ![Github i1](images/3.7.png)
    Visaulizaciòn de boton Precio deshabilitado porque el tipo de usuario es distinto al de administrador
    ![Github i1](images/3.7.2.png)

4.  Categorías de Productos
    Se crearon dos categorias en punto de venta/configuraciòn/productos/Categorìa PdV
    ![Github i1](images/4.2.png.png)
    Visualizaciònde productos creados en el Punto de venta
    ![Github i1](images/4.4.png.png)

5.  Configuración de restaurant.
    Se crea un nuevo Punto de Venta en Punto de venta/Configuracion/punto de venta/Nuevo
    ![Github i1](images/5.1.png)
    Se crea pisos y se le agrega a la opciòn de pisos.
    ![Github i1](images/5.2.png)
    Para cerrar sesiòn, necesitamos
    ![Github i1](images/SacarDinero.png)
    Ingresamos al nuevo punto de venta, despuès de cerrar el anterior Punto de venta, estableciendo el balance de cierre
    ![Github i1](images/5.4.png)
    Dibujamos las mesas de ambos pisos
    ![Github i1](images/mesas.png)
    Se visualiza la orden de diferentes mesas.
    ![Github i1](images/mesas1.gif)
    Se observa cómo ingresar una nota en una venta
    ![Github i1](images/5.6.png)
    Se observa cómo se tranfiere el pedido de la mesa T2 a la mesa T6
    ![Github i1](images/transferir.gif)
    Habilitamos la impredión de cuenta y la separación de cuentas.
    ![Github i1](images/5.8.png)
    Se observa la habilitaciòn del botòn Dividir, que sirve para poder dividir el pago del consumo de la cuenta
    ![Github i1](images/Separador.png)

## TAREA

1.  Instale el módulo pos_loyalty. Para esto debe descargar el repositorio: https://github.com/OCA/pos/tree/11.0 Tenga cuidado con descargar el branch correcto (Odoo 11). Adjunte los GIFs necesario de cómo funciona el módulo pos_loyalty. Para que tenga una idea, es una forma de añadir un programa de recompensa de fidelización a los clientes, para contabilizar puntos por consumo y canjearlos por productos o dinero.
    Veremos que una vez configurado el programa de Fidelización se debe configurar el Punto de venta.
    ![Github i1](images/configuracion.gif)
    Ahora visualizamos que se establecen puntos al seleccionar un cliente
    ![Github i1](images/puntos.gif)
    Se verifica que una vez pagado, los clientes poseen sus puntos.
    ![Github i1](images/verificacion.gif)

## Observaciones y Conclusiones

- Se observó que podemos utilizar sesiones para realizar el punto de venta que está asociado a clientes, , maneras de pago.
- Se vio el ciclo de vida de una sesión que consta en el procesos de control de Apertura; En Progreso; Control de Cierre y Cerrado & Contabilizado.
- Se aprendió términos como el balance de Apertura, que es el dinero inicial con que el cajero de turno comienza, de modo que es aqui donde se ingresa el efctivo que se le entrega y como recomndación es una buena practica entregar una cantidad estándar todos los días para facilitar este proceso.
- Se vió los medios de pago, que pueden ser con efectivo, medios combinados, medio bancarizado sin efectivo.
- Se aprendió las fuciones que se pueden realizar en un Punto de Venta , crear categorías,
  graficar mesas en caso de que este punto de venta esté configurado como restaurant.
- Gracias a la App de Odoo de pos_loyalty podemos asignar un programa de fidelización que se configura dando puntos por producto, por moneda asimismo dando recompensas , como regalos, descuentos y otros.
