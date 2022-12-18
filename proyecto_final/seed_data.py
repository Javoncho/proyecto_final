# from ejemplo.models import Familiar
# Familiar(nombre="Oscar", direccion="9 dde Julio 745", numero_pasaporte=123123).save()
# Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
# Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
# Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()
# print("Se cargo con éxito los usuarios de pruebas")

from ejemplo.models import Familiar
Familiar(nombre="Oscar", direccion="9 dde Julio 745", numero_pasaporte=123123, fec_nacimiento="1980-10-20").save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890, fec_nacimiento="1980-11-24").save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345, fec_nacimiento="1980-10-31").save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567, fec_nacimiento="1980-12-12").save()
print("Se cargo con éxito los usuarios de pruebas")
