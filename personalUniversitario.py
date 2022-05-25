# Personal Universitario

class PersonalUniversitario():
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido

class Profesor(PersonalUniversitario):
  def __init__(self, nombre, apellido, fecha_ingreso):
    PersonalUniversitario.__init__(self, nombre, apellido)
    self.fecha_ingreso = fecha_ingreso

class Alumno(PersonalUniversitario):
  def __init__(self, nombre, apellido, nro_legajo):
    PersonalUniversitario.__init__(self, nombre, apellido)
    self.nro_legajo = nro_legajo

class ProfesorAyudante(Profesor, Alumno):
  def __init__(self, nombre, apellido, fecha_ingreso, nro_legajo):
    Profesor.__init__(self, nombre, apellido, fecha_ingreso)
    Alumno.__init__(self, nombre, apellido, nro_legajo)
    pass
    
  
# Instanciación de ejemplo
Juan = Profesor('Juan', 'Gomez', '01/01/2022')
Pedro = Alumno('Pedro', 'Diaz', 1234)
Mario = ProfesorAyudante('Mario', 'Gonzales', '01/01/2020', 11111)    

print(Juan.nombre, Juan.apellido, Juan.fecha_ingreso)      
print(Pedro.nombre, Pedro.apellido, Pedro.nro_legajo)      
print(Mario.nombre, Mario.apellido, Mario.fecha_ingreso, Mario.nro_legajo) 