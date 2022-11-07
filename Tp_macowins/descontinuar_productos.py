from macowins import *

def main():
  print(str(datetime.now()) + " : descontinuando productos")

if __name__ == "__main__":
   main()
   sucursales = cargar_todos()
   for sucursal in sucursales.keys():
       sucu = cargar(sucursal)
       sucu.descontinuar_productos()
       sucu.ver_productos()
       guardar(sucursal,sucu)


        

        
