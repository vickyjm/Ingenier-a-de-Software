# -*- coding: utf-8 -*-

from django.core.validators import RegexValidator
from django.db import models
from django.forms import ModelForm


class Estacionamiento(models.Model):
	# propietario=models.ForeignKey(Propietario)
	Propietario = models.CharField(max_length = 50, help_text = "Nombre Propio")
	Nombre = models.CharField(max_length = 50)
	Direccion = models.TextField(max_length = 120)

	Telefono_1 = models.CharField(blank = True, null = True, max_length = 30)
	Telefono_2 = models.CharField(blank = True, null = True, max_length = 30)
	Telefono_3 = models.CharField(blank = True, null = True, max_length = 30)

	Email_1 = models.EmailField(blank = True, null = True)
	Email_2 = models.EmailField(blank = True, null = True)

	Rif = models.CharField(max_length = 12)

	Tarifa = models.CharField(max_length = 50, blank = True, null = True)
	opciones_esquema = (("Hora", " Por hora"), ("Minuto"," Por minuto"))
	Esquema = models.CharField(max_length = 6, choices = opciones_esquema, null = True)
	Apertura = models.TimeField(blank = True, null = True)
	Cierre = models.TimeField(blank = True, null = True)
	Reservas_Inicio = models.TimeField(blank = True,null = True)
	Reservas_Cierre = models.TimeField(blank = True, null = True)
	NroPuesto = models.IntegerField(blank = True, null = True)


class ReservasModel(models.Model):
	Estacionamiento = models.ForeignKey(Estacionamiento)
	Puesto = models.IntegerField()
	InicioReserva = models.DateTimeField()
	FinalReserva = models.DateTimeField()
	
class PagoReservaModel(models.Model):
	Reserva = models.ForeignKey(ReservasModel)
	opciones_tarjeta = (('Vista','Vista'), ('Mister','Mister'), ('Xpres','Xpres'))
	TipoTarjeta = models.CharField(max_length = 6, choices = opciones_tarjeta)
	NumTarjeta = models.CharField(max_length = 19)
	MontoPago = models.DecimalField(max_digits = 12, decimal_places = 2)
