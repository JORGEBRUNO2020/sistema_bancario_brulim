"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

"""

def test1(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> get_listado_movimientos(((1, 1, 1, 420.0, datetime.date(2022, 1, 1), 'Transferencia Caja Ahorro', Decimal('60.00'), 'Peso', Decimal('1.00'), Decimal('1.00')), (1, 1, 2, 310.0, datetime.date(2022, 1, 11), 'Transferencia Caja Ahorro', Decimal('60.00'), 'Peso', Decimal('1.00'), Decimal('1.00'))), 1)
    (1, 1, 1, 420.0, datetime.date(2022, 1, 1), 'Transferencia Caja Ahorro', Decimal('60.00'), 'Peso', Decimal('1.00'), Decimal('1.00')), (1, 1, 2, 310.0, datetime.date(2022, 1, 11), 'Transferencia Caja Ahorro', Decimal('60.00'), 'Peso', Decimal('1.00'), Decimal('1.00'))]

    """




    def get_listado_movimientos(array_movimientos, id_cuenta):
        store_resultados= []
        print(array_movimientos[0][4])
        for item in array_movimientos:
            if int(item[0]) == int(id_cuenta):
                store_resultados.append(item)
        return store_resultados


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())