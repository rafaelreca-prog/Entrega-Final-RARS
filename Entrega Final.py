import dataset
miBase = dataset.connect("sqlite:///base.db")
Lista_Disponible= miBase["Productos"]

while True:
    opciones = input("\n A - Agregar\n L - Listar\n R - Remover por Nombre\nID - Remover por ID\nAC - Actualizar Todo\nBT - Buscar Todo\nS - Salir\n").upper()
    
    match opciones:
        
        case "A":
            agregarProducto = input("\nProducto:  ").strip()
            agregarPrecio = float(input("\nPrecio: ").strip())
            agregarCategoria = input("\nCategoria: ").strip()
        
            agregar = {"Nombre":agregarProducto,"Precio":agregarPrecio,"Categoria":agregarCategoria}
            
            Lista_Disponible.insert(agregar)
            
        case "S":
            break

        case "L":
            if Lista_Disponible:
                for items in Lista_Disponible:
                    print(f'ID:{items["id"]} | Producto: {items["Nombre"]} | Precio: {items["Precio"]} | Categoria: {items["Categoria"]}')
            else:
                    print(f'\nNo hay productos disponibles en la lista')
                    
        case "R":
            removerNombre = input("\nProducto a Remover: ").strip()
            Lista_Disponible.delete(Nombre=removerNombre)
            print(f"\n{removerNombre} se ha quitado con Exito!\n")
        
        case "ID":
            removerID = int(input("\nID de producto a Remover: ").strip())
            Lista_Disponible.delete(id=removerID)
            
            print(f"\nEl Producto cuyo ID es {removerID} se ha quitado con Éxito!\n")
            
        case "BT":
            buscarTodo = input("\nProducto a Buscar: ")
            encontrados = Lista_Disponible.find(Nombre=buscarTodo)
           
            if encontrados:
                for encontrado in encontrados:
                    print(f'\nSe encontró en ID: {encontrado["id"]}')
                else:
                    print(f'\nNo se ha encontrado en la lista')
                
        case "AC":
            idBuscar = int(input("\nID a Actualizar: "))
            nombreActualizar = input("\nNombre Nuevo: ")
            precioActualizar = float(input("\nPrecio Nuevo: "))
            catActualizar = input("\nCategoria Nueva: ")
            
            actualizar = {"id":idBuscar,"Nombre":nombreActualizar}
            Lista_Disponible.upsert(actualizar,["id"])

