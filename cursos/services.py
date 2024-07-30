from .models import Estudiante, Profesor, Curso, Direccion

# Crear curso
def crear_curso(codigo, nombre, version, profesor_rut):
    profesor = Profesor.objects.get(rut=profesor_rut)
    curso = Curso(codigo=codigo, nombre=nombre, version=version)
    curso.save()
    curso.profesores.add(profesor)
    curso.save()
    return curso

# Crear profesor
def crear_profesor(rut, nombre, apellido, activo, creacion_registro, modificacion_registro, creado_por):
    profesor = Profesor(
        rut=rut, nombre=nombre, apellido=apellido, activo=activo, 
        creacion_registro=creacion_registro, modificacion_registro=modificacion_registro, creado_por=creado_por
    )
    profesor.save()
    return profesor

# Crear estudiante
def crear_estudiante(nombre, apellido, fecha_nac, activo, creacion_registro, modificacion_registro, creado_por, direccion_data):
    estudiante = Estudiante(
        nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, activo=activo, 
        creacion_registro=creacion_registro, modificacion_registro=modificacion_registro, creado_por=creado_por
    )
    estudiante.save()
    direccion = Direccion(estudiante=estudiante, **direccion_data)
    direccion.save()
    return estudiante

# Crear dirección
def crear_direccion(calle, numero, dpto, comuna, ciudad, region, estudiante_rut):
    estudiante = Estudiante.objects.get(rut=estudiante_rut)
    direccion = Direccion(calle=calle, numero=numero, dpto=dpto, comuna=comuna, ciudad=ciudad, region=region, estudiante=estudiante)
    direccion.save()
    return direccion

# Obtener estudiante
def obtener_estudiante(rut):
    estudiante = Estudiante.objects.get(rut=rut)
    return estudiante

# Obtener profesor
def obtener_profesor(rut):
    profesor = Profesor.objects.get(rut=rut)
    return profesor

# Obtener curso
def obtener_curso(codigo):
    curso = Curso.objects.get(codigo=codigo)
    return curso

# Agregar profesor a curso
def agregar_profesor_a_curso(profesor_rut, curso_codigo):
    profesor = Profesor.objects.get(rut=profesor_rut)
    curso = Curso.objects.get(codigo=curso_codigo)
    curso.profesores.add(profesor)
    curso.save()
    return curso

# Agregar cursos a estudiante
def agregar_cursos_a_estudiante(estudiante_rut, curso_codigos):
    estudiante = Estudiante.objects.get(rut=estudiante_rut)
    cursos = Curso.objects.filter(codigo__in=curso_codigos)
    estudiante.cursos.add(*cursos)
    estudiante.save()
    return estudiante

# Imprimir cursos de un estudiante
def imprime_estudiante_cursos(estudiante_rut):
    estudiante = Estudiante.objects.get(rut=estudiante_rut)
    cursos = estudiante.cursos.all()
    for curso in cursos:
        print(f"Curso: {curso.nombre}, Código: {curso.codigo}")
