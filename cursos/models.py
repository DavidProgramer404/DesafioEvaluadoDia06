from django.db import models

class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    dpto = models.CharField(max_length=10, blank=True, null=True)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    estudiante = models.OneToOneField('Estudiante', on_delete=models.CASCADE, related_name='direccion')

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.dpto}, {self.comuna}, {self.ciudad}, {self.region}"


class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateTimeField(auto_now_add=True)
    modificacion_registro = models.DateTimeField(auto_now=True)
    creado_por = models.CharField(max_length=50)
    cursos = models.ManyToManyField('Curso', related_name='estudiantes')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateTimeField(auto_now_add=True)
    modificacion_registro = models.DateTimeField(auto_now=True)
    creado_por = models.CharField(max_length=50)
    cursos = models.ManyToManyField('Curso', related_name='profesores')

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut})"


class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    version = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
