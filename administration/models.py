import pprint
from django.db import models
from django.forms import model_to_dict

# from usuarios import Cliente

class Empresa(models.Model):
   """
   Representa el registro de una empresa
   """
   nombre = models.CharField(max_length=100)
   direccion = models.CharField(max_length=100)

   def __str__(self):
      return self.nombre

   def toJSON(self):
      item = model_to_dict(self)
      item['nombre'] = self.nombre
      item['direccion'] = self.direccion

      return item


class Regional(models.Model):
   """
   Representa el registo de una regional
   """
   empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
   nombre = models.CharField(max_length=100)
   dia_lectura = models.DateField()
   horario_lectura = models.TimeField()

   def __str__(self):
      return self.nombre

   def toJSON(self):
      item = model_to_dict(self)
      item['empresa'] = self.empresa.toJSON()
      item['nombre'] = self.nombre
      item['dia_lectura'] = self.dia_lectura
      item['horario_lectura'] = self.horario_lectura

      return item


class SubEstacion(models.Model):
   """
   Representa el registo de una subestacion
   """
   regional = models.ForeignKey(Regional, on_delete=models.CASCADE)
   nombre = models.CharField(max_length=100)
   capacidad = models.CharField(max_length=100)

   def __str__(self):
      return self.nombre

   def toJSON(self):
      item = model_to_dict(self)
      item['regional'] = self.regional.toJSON()
      item['nombre'] = self.nombre
      item['capacidad'] = self.capacidad

      return item


class Alimentadora(models.Model):
   """
   Representa un registro de un alimentadora
   """
   regional = models.ForeignKey(Regional, on_delete=models.CASCADE)
   sub_estaciones = models.ForeignKey(SubEstacion, on_delete=models.CASCADE)
   nombre = models.CharField(max_length=100)
   descripcion = models.CharField(max_length=250)

   def __str__(self):
      return self.nombre

   def toJSON(self):
      item = model_to_dict(self)
      item['regional'] = self.regional.toJSON()
      item['nombre'] = self.nombre
      item['sub_estaciones'] = self.sub_estaciones.toJSON()
      item['descripcion'] = self.descripcion

      return item



class Transformador(models.Model):
   """
   Representa un registro de un transformador
   """
   regional = models.ForeignKey(Regional, on_delete=models.CASCADE)
   sub_estaciones = models.ForeignKey(SubEstacion, on_delete=models.CASCADE)
   alimentadora = models.ForeignKey(Alimentadora, on_delete=models.CASCADE)
   marca = models.CharField(max_length=100)
   codigo = models.IntegerField()
   kva = models.IntegerField()
   medidor = models.IntegerField()

   def __str__(self):
      return self.marca

   def toJSON(self):
      item = model_to_dict(self)
      item['regional'] = self.regional.toJSON()
      item['sub_estaciones'] = self.sub_estaciones.toJSON()
      item['alimentadora'] = self.alimentadora.toJSON()
      item['marca'] = self.marca
      item['codigo'] = self.codigo
      item['kva'] = self.kva
      item['medidor'] = self.medidor

      return item


class Suministro(models.Model):
   """
   Representa un registro de un Suministro
   """
   empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
   regional = models.ForeignKey(Regional, on_delete=models.CASCADE)
   sub_estacion = models.ForeignKey(SubEstacion, on_delete=models.CASCADE)
   transformador = models.ForeignKey(Transformador, on_delete=models.CASCADE)
   alimentadora = models.ForeignKey(Alimentadora, on_delete=models.CASCADE)
   cod_sumistro = models.CharField(max_length=100)
   cliente = models.CharField(max_length=100)
   # cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
   direccion = models.CharField(max_length=100)
   latitud = models.CharField(max_length=100)
   longitud = models.CharField(max_length=100)

   def __str__(self):
      return self.cod_sumistro

   def toJSON(self):
      item = model_to_dict(self)
      item['suministro_empresa'] = self.empresa.toJSON()
      item['suministro_regional'] = self.regional.toJSON()
      item['suministro_sub_estacion'] = self.sub_estacion.toJSON()
      item['suministro_transformador'] = self.transformador.toJSON()
      item['suministro_alimentadora'] = self.alimentadora.toJSON()
      item['cod_sumistro'] = self.cod_sumistro
      item['cliente'] = self.cliente
      item['direccion'] = self.direccion
      item['latitud'] = self.latitud
      item['longitud'] = self.longitud
      # pprint.pprint(item)

      return item


