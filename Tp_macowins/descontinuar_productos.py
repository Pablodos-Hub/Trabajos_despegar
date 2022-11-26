from macowins import *

def main():
  print(str(datetime.now()) + " : descontinuando productos")
  sucursales = cargar_todos()
  print (sucursales)
  for sucursal in sucursales.keys():
      sucu = cargar(sucursal)
      print (sucu)
      sucu.descontinuar_productos()
      sucu.ver_productos()
      guardar(sucursal,sucu)

if __name__ == "__main__":
   main()
