# Lab. 10: Consumo de API Externa 

## Desarrollo

- 1.  Configuración inicial<br>
- 2.  Creación de modelo Documentos <br>
- 3.  Relación con contactos <br>
    - 3.5 Visualizacion de la tabla facturacion_series en la base de datos y declarada en el modelo series.<br>
    ![Github i1](images/3.5TablaFacturacionSeries.png)<br>
    - 3.6 Visualizacion de la vista del menuitem<br>
    ![Github i1](images/3.6MenuItemSeries.png)<br>
    - 3.7 Verificación del Modulo creado de Facturacion<br> 
    ![Github i1](images/3.7FuncionamientoDelModuloCreado.png)<br>

- 4.  Consumo de API externa<br>
    - 4.5 Metodo Onchange. Log de Odoo.<br>
    ![Github i1](images/5.2Busqueda.gif)<br>
    - 4.9  GIF mostrando como selecciona DNI e ingresa su DNI y hacer click fuera del campo, Odoo autocompleta su Nombre.<br> 
    ![Github i1](images/4.9.seleccionDni.gif)<br>
    - 4.9.2  GIF mostrando como selecciona RUC e ingresa el RUC de la empresa Saga Falabella (debe googlear esta información) y lo que autocompleta Odoo.<br>
    ![Github i1](images/4.9.seleccionRucSaga.gif)<br>
- 5.  Constraint o limitantes<br>
    - 5.3 GIF mostrando dicha advertencia al intentar crear otra vez un contacto con su mismo DNI. 
    ![Github i1](images/5.eContacatoExiste.gif)<br>

- 6. Campos relacionados<br>
    - 6.4 Nuevo campo que relaciona la seleccion de una serie de boleta o una serie de factura
    ![Github i1](images/6.CamposRelacionados.gif)<br>


## Observaciones y Conclusiones

- Se vió el consumo de una APIexterna para obtener el nombre tanto si se le pasas el rus o dni por medio de APIS peru , através de un token y una url y conectividad 
-  Para poder trabajar con la API, se vió la importacion de request, json .
- Observamos la sintaxis @api. seguidos de multi, onchange y constrains.
- Se vio la herencia de modelos por medio de _inherit ="nombre del modelo a heredar"
