import doctest

class Test():
    def get_listado_movimientos(array_movimientos, id_cuenta):
        '''Return the factorial of n, an exact integer >= 0.

        >>> get_listado_movimientos(((1, 1, 1, 420.0, datetime.date(2022, 1, 1), 'Transferencia Caja Ahorro', Decimal('60.00'), 'Peso', Decimal('1.00'), Decimal('1.00')), (1, 1, 2, 310.0, datetime.date(2022, 1, 11), 'Transferencia Caja Ahorro', Decimal('60.00'), 'Peso', Decimal('1.00'), Decimal('1.00'))), 1)
        (1, 1, 1, 420.0, datetime.date(2022, 1, 1), 'Transferencia Caja Ahorro', Decimal('60.00'), 'Peso', Decimal('1.00'), Decimal('1.00')), (1, 1, 2, 310.0, datetime.date(2022, 1, 11), 'Transferencia Caja Ahorro', Decimal('60.00'), 'Peso', Decimal('1.00'), Decimal('1.00'))]

        '''
        store_resultados= []
        for item in array_movimientos:
            if int(item[0]) == int(id_cuenta):
                store_resultados.append(item)
        return store_resultados

    print("***TEST_1****",doctest.testmod())
    
    def id_logeado(id_usuario_login, id):
        '''
        RECIBE UN id DEL USUARIO LOGEADO Y RETORNA UN ARRAY CON EL id
        >>> valor_variable(1)
        [1]
        
        '''
        id_usuario_login.append(id)

    print("***TEST_2****",doctest.testmod())


    

