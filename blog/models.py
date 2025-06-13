from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(default="test@email.com")

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    ranking = models.IntegerField(null=True, blank=True)
    club = models.CharField(max_length=100, blank=True)
    foto = models.ImageField(upload_to='jugadores/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Pareja(models.Model):
    jugador1 = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='pareja_jugador1')
    jugador2 = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='pareja_jugador2')

    def __str__(self):
        return f"{self.jugador1.nombre} y {self.jugador2.nombre}"

class Torneo(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateField()
    lugar = models.CharField(max_length=200)
    jugadores = models.ManyToManyField(Jugador, blank=True)
    ganador = models.ForeignKey(Pareja, on_delete=models.SET_NULL, null=True, blank=True, related_name='torneos_ganados')
    imagen = models.ImageField(upload_to='torneos/', blank=True, null=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Entrada(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    torneo = models.ForeignKey(Torneo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo