from utils import(create_connection,close_connection,create_cursor,
                  close_cursor,execute_query,commit_dml)
from typing import Any

def get_all_products(cursor)->list:
   
    query = "select products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name from products inner join uom on products.uom_id=uom.uom_id"
    cursor=execute_query(query)
    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    return response

def insert_new_product(cursor:Any, product:dict)->Any:

    query= (
        f"INSERT INTO products (name, uom_id, price_per_unit) "
        f"VALUES ('{product['product_name']}', {product['uom_id']}, {product['price_per_unit']})"
    )
    cursor=execute_query(query)
    commit_dml(cursor)

    return cursor.lastrowid

def delete_product(cursor:Any, product_id:int)->Any:
    query = (f"DELETE FROM products where product_id=" + {str(product_id)})
    query=execute_query(query)
    commit_dml(cursor)

    return cursor.lastrowid

if __name__ == '__main__':
    conn=create_connection(user='root@localhost', password="root1234", host="", database="")
    cursor=create_cursor(conn)
    print(insert_new_product(conn, {
        'product_name': 'potatoes',
        'uom_id': '1',
        'price_per_unit': 10
    }))
    close_cursor(cursor)
    close_connection(conn)