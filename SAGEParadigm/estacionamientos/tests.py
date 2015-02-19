# -*- coding: utf-8 -*-

import datetime
from django.test import Client
from django.test import TestCase
import unittest

from estacionamientos.controller import *
from estacionamientos.forms import *
from estacionamientos.forms import *
from estacionamientos.models import *


###################################################################
#                    ESTACIONAMIENTO VISTA DISPONIBLE
###################################################################
class SimpleTest(unittest.TestCase):
	# normal
	def setUp(self):
		self.client = Client()

	# normal
	def test_primera(self):
		response = self.client.get('/estacionamientos/')
		self.assertEqual(response.status_code, 200)



###################################################################
#                    ESTACIONAMIENTO_ALL FORM
###################################################################

class SimpleFormTestCase(TestCase):

	# malicia
	def test_CamposVacios(self):
		form_data = {}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_SoloUnCampoNecesario(self):
		form_data = {
			'propietario': 'Pedro'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_DosCamposNecesarios(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_TresCamposNecesarios(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_TodosLosCamposNecesarios(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# malicia
	def test_PropietarioInvalidoDigitos(self):
		form_data = {
			'propietario': 'Pedro132',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_PropietarioInvalidoSimbolos(self):
		form_data = {
			'propietario': 'Pedro!',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_RIFtamanoinvalido(self):
		form_data = {
			'propietario': 'Pedro132',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V1234567'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_RIFformatoinvalido(self):
		form_data = {
			'propietario': 'Pedro132',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'Kaa123456789'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_AgregarTLFs(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789',
			'telefono_1': '02129322878',
			'telefono_2': '04149322878',
			'telefono_3': '04129322878'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# malicia
	def test_FormatoInvalidoTLF(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789',
			'telefono_1': '02119322878'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_TamanoInvalidoTLF(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789',
			'telefono_1': '0219322878'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_AgregarCorreos(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789',
			'telefono_1': '02129322878',
			'telefono_2': '04149322878',
			'telefono_3': '04129322878',
			'email_1': 'adminsitrador@admin.com',
			'email_2': 'usua_rio@users.com'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# malicia
	def test_CorreoInvalido(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789',
			'telefono_1': '02129322878',
			'telefono_2': '04149322878',
			'telefono_3': '04129322878',
			'email_1': 'adminsitrador@a@dmin.com'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

###################################################################
# ESTACIONAMIENTO_EXTENDED_FORM
###################################################################

	# malicia
	def test_EstacionamientoExtendedForm_UnCampo(self):
		form_data = { 'puestos': 2}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_DosCampos(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0)}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_TresCampos(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0)}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_CuatroCampos(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0)}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_EstacionamientoExtendedForm_CincoCampos(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0)}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_EstacionamientoExtendedForm_TodosCamposBien(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
								'esquema':'Hora',
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# caso borde
	def test_EstacionamientoExtendedForm_Puestos0(self):
		form_data = { 'puestos': 0,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
								'esquema':'Minuto',
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# caso borde
	def test_EstacionamientoExtendedForm_HoraInicioIgualHoraCierre(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(6, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
								'esquema':'Hora',
								'tarifa': '30'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# caso borde
	def test_EstacionamientoExtendedForm_HoraIniReserIgualHoraFinReser(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(7, 0),
								'esquema':'Minuto',
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# malicia
	def test_EstacionamientoExtendedForm_StringEnPuesto(self):
		form_data = { 'puestos': 'hola',
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_StringHoraInicio(self):
		form_data = { 'puestos': 2,
								'horarioin': 'holaa',
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_NumeroNegativoHoraInicio(self):
		form_data = { 'puestos': 2,
								'horarioin':-1,
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_NoneEntarifa(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
								'tarifa': None}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_NoneEnHorarioReserva(self):
		form_data = { 'puestos': 2,
								'horarioin': 'holaa',
								'horarioout': datetime.time(19, 0),
								'horario_reserin': None,
								'horario_reserout': datetime.time(14, 0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_listaEnHoraReserva(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': [datetime.time(14, 0)],
								'esquema':'hora',
								'tarifa': 12}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

######################################################################
# ESTACIONAMIENTO_EXTENDED pruebas controlador
###################################################################

	# normal
	def test_HorariosValidos(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 18, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (True, ''))

	# malicia
	def test_HorariosInvalido_HoraCierre_Menor_HoraApertura(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 11, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 18, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de apertura debe ser menor al horario de cierre'))

	# caso borde
	def test_HorariosInvalido_HoraCierre_Igual_HoraApertura(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 18, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de apertura debe ser menor al horario de cierre'))

	# caso borde
	def test_HorariosInvalido_HoraCierreReserva_Menor_HoraAperturaReserva(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 11, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de inicio de reserva debe ser menor al horario de fin de reserva'))

	# caso borde
	def test_HorariosInvalido_HoraCierreReserva_Igual_HoraAperturaReserva(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 12, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de inicio de reserva debe ser menor al horario de fin de reserva'))

	# caso borde
	def test_Limite_HorarioValido_Apertura_Cierre(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 12, minute = 0, second = 1)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 12, minute = 0, second = 1)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (True, ''))

	# caso borde
	def test_Limite_Superior_HorarioValido_Apertura_Cierre(self):
		HoraInicio = datetime.time(hour = 0, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 23, minute = 59, second = 59)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 23, minute = 59, second = 59)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (True, ''))

	# caso borde
	def test_InicioReserva_Mayor_HoraCierreEstacionamiento(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 19, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 20, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de comienzo de reserva debe ser menor al horario de cierre del estacionamiento'))

	# caso borde
	def test_InicioReserva_Mayor_HoraCierreEstacionamiento2(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 19, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 20, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de comienzo de reserva debe ser menor al horario de cierre del estacionamiento'))

	# malicia
	def test_CierreReserva_Mayor_HoraCierreEstacionamiento(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 17, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 20, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de cierre de estacionamiento debe ser mayor o igual al horario de finalizacion de reservas'))

	# malicia
	def test_CierreReserva_Menos_HoraInicioEstacionamiento(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 10, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 11, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de inicio de reserva debe mayor o igual al horario de apertura del estacionamiento'))



###################################################################
# ESTACIONAMIENTO_RESERVA_FORM
###################################################################

	# malicia
	def test_EstacionamientoReserva_Vacio(self):
		form_data = {}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_EstacionamientoReserva_UnCampo(self):
		form_data = {'inicio':datetime.time(6, 0)}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# normal
	def test_EstacionamientoReserva_TodosCamposBien(self):
		form_data = {'fechaInicio': datetime.date(2015,10,5),'horaInicio':datetime.time(6, 0),'fechaFinal': datetime.date(2015,10,5), 'horaFinal':datetime.time(12, 0)}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# malicia
	def test_EstacionamientoReserva_InicioString(self):
		form_data = {'inicio':'hola',
								'final':datetime.time(12, 0)}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoReserva_FinString(self):
		form_data = {'inicio':datetime.time(6, 0),
								'final':'hola'}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoReserva_InicioNone(self):
		form_data = {'inicio':None,
								'final':datetime.time(12, 0)}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoReserva_finalNone(self):
		form_data = {'inicio':datetime.time(6, 0),
								'final':None}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

###################################################################
# PRUEBAS DE FUNCIONES DEL CONTROLADOR
###################################################################

##############################################################
# Estacionamiento Reserva Controlador
###################################################################

# HorarioReserva, pruebas Unitarias

	# normal
	def test_HorarioReservaValido(self):
		ReservaInicio = datetime.datetime(2015,10,5,8,5)
		ReservaFin = datetime.datetime(2015,10,5,13,17)
		HoraApertura = datetime.time(hour = 8, minute = 0, second = 0)
		HoraCierre = datetime.time(hour = 18, minute = 0, second = 0)
		horaActual = datetime.datetime(2015,10,5,8,5)
		x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre,horaActual)
		self.assertEqual(x, (True, ''))

	# caso borde
	def test_HorarioReservaInvalido_InicioReservacion_Mayor_FinalReservacion(self):
		ReservaInicio = datetime.datetime(year = 2015, month = 10, day = 5,hour = 13, minute = 0)
		ReservaFin = datetime.datetime(year = 2015, month = 10, day = 5,hour = 12, minute = 59)
		HoraApertura = datetime.time(hour = 12, minute = 0, second = 0)
		HoraCierre = datetime.time(hour = 18, minute = 0, second = 0)
		horaActual = datetime.datetime(year = 2015,month = 10, day = 5, hour = 12,minute = 50)
		x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre,horaActual)
		self.assertEqual(x, (False, 'El horario de inicio de reserva debe ser menor que le horario de fin de reserva'))

	# caso borde
	def test_HorarioReservaInvalido_TiempoTotalMenor1h(self):
		ReservaInicio = datetime.datetime(year = 2015, month = 10, day = 5,hour = 13, minute = 0, second = 0)
		ReservaFin = datetime.datetime(year = 2015, month = 10, day = 5,hour = 13, minute = 59, second = 59)
		HoraApertura = datetime.time(hour = 12, minute = 0, second = 0)
		HoraCierre = datetime.time(hour = 18, minute = 0, second = 0)
		horaActual = datetime.datetime(year = 2015,month = 10, day = 5, hour = 12,minute = 50)
		x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre,horaActual)
		self.assertEqual(x, (False, 'El tiempo de reserva debe ser al menos de 1 hora'))

	# caso borde
	def test_HorarioReservaInvalido_ReservaFinal_Mayor_HorarioCierre(self):
		ReservaInicio = datetime.datetime(year = 2015, month = 10, day = 5,hour = 13, minute = 0)
		ReservaFin = datetime.datetime(year = 2015, month = 10, day = 5,hour = 18, minute = 1)
		HoraApertura = datetime.time(hour = 12, minute = 0, second = 0)
		HoraCierre = datetime.time(hour = 18, minute = 0, second = 0)
		horaActual = datetime.datetime(year = 2015,month = 10, day = 5, hour = 12,minute = 50)
		x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre,horaActual)
		self.assertEqual(x, (False, 'El horario de inicio de reserva debe estar en un horario valido'))

	# caso borde
	def test_HorarioReservaInvalido_ReservaInicial_Menor_HorarioApertura(self):
		ReservaInicio = datetime.datetime(year = 2015, month = 10, day = 5,hour = 11, minute = 59, second = 59)
		ReservaFin = datetime.datetime(year = 2015, month = 10, day = 5,hour = 15, minute = 0, second = 1)
		HoraApertura = datetime.time(hour = 12, minute = 0, second = 0)
		HoraCierre = datetime.time(hour = 18, minute = 0, second = 0)
		horaActual = datetime.datetime(year = 2015,month = 10, day = 5, hour = 12,minute = 50)
		x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre, horaActual)
		self.assertEqual(x, (False, 'El horario de cierre de reserva debe estar en un horario valido'))

	# malicia
	def test_Reservacion_CamposVacios(self):
		form_data = {'fechaInicio': datetime.date(2015,10,5),'horaInicio':datetime.time(6, 0),'fechaFinal': datetime.date(2015,10,5), 'horaFinal':datetime.time(12, 0)}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), True)

# Binaria, Pruebas Unitarias

	# caso borde
	def test_Binaria_lista_vacia(self):
		valor = datetime.time(hour = 10, minute = 0, second = 0)
		lista = []
		x = binaria(valor, 0, len(lista), lista)
		self.assertEqual(x, 0)

	# caso borde
	def test_Binaria_lista_un_elem(self):
		valor = datetime.time(hour = 10, minute = 0, second = 0)
		Hora1In = datetime.time(hour = 8, minute = 0, second = 0)
		Hora1Out = datetime.time(hour = 9, minute = 0, second = 0)
		lista = []
		lista.append([Hora1In, Hora1Out])
		x = binaria(valor, 0, len(lista), lista)
		self.assertEqual(x, 1)

	# caso borde
	def test_Binaria_horas_borde(self):
		valor = datetime.time(hour = 10, minute = 0, second = 0)
		Hora1In = datetime.time(hour = 0, minute = 0, second = 0)
		Hora1Out = datetime.time(hour = 0, minute = 0, second = 0)
		Hora2In = datetime.time(hour = 23, minute = 59, second = 59)
		Hora2Out = datetime.time(hour = 23, minute = 59, second = 59)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora2In, Hora2Out])
		x = binaria(valor, 0, len(lista), lista)
		self.assertEqual(x, 1)

	# caso borde
	def test_Binaria_horas_borde2(self):
		valor = datetime.time(hour = 0, minute = 0, second = 0)
		Hora1In = datetime.time(hour = 0, minute = 0, second = 1)
		Hora1Out = datetime.time(hour = 0, minute = 0, second = 1)
		Hora2In = datetime.time(hour = 23, minute = 59, second = 59)
		Hora2Out = datetime.time(hour = 23, minute = 59, second = 59)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora2In, Hora2Out])
		x = binaria(valor, 0, len(lista), lista)
		self.assertEqual(x, 0)

	# caso borde
	def test_Binaria_horas_borde3(self):
		valor = datetime.time(hour = 23, minute = 59, second = 59)
		Hora1In = datetime.time(hour = 0, minute = 0, second = 0)
		Hora1Out = datetime.time(hour = 0, minute = 0, second = 0)
		Hora2In = datetime.time(hour = 23, minute = 59, second = 58)
		Hora2Out = datetime.time(hour = 23, minute = 59, second = 58)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora2In, Hora2Out])
		x = binaria(valor, 0, len(lista), lista)
		self.assertEqual(x, 2)

	# malicia
	def test_Binaria_horas_mal_orden(self):
		valor = datetime.time(hour = 20, minute = 10, second = 13)
		Hora1In = datetime.time(hour = 0, minute = 1, second = 0)
		Hora1Out = datetime.time(hour = 0, minute = 0, second = 30)
		Hora2In = datetime.time(hour = 23, minute = 59, second = 59)
		Hora2Out = datetime.time(hour = 23, minute = 59, second = 58)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora2In, Hora2Out])
		x = binaria(valor, 0, len(lista), lista)
		self.assertEqual(x, 1)

	# malicia
	def test_Binaria_horas_mal_orden2(self):
		valor = datetime.time(hour = 20, minute = 10, second = 13)
		Hora1In = datetime.time(hour = 0, minute = 1, second = 0)
		Hora1Out = datetime.time(hour = 0, minute = 0, second = 30)
		Hora2In = datetime.time(hour = 23, minute = 59, second = 59)
		Hora2Out = datetime.time(hour = 19, minute = 59, second = 58)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora2In, Hora2Out])
		x = binaria(valor, 0, len(lista), lista)
		self.assertEqual(x, 1)

	# malicia
	def test_Binaria_horas_mal_orden3(self):
		valor = datetime.time(hour = 20, minute = 10, second = 13)
		Hora1In = datetime.time(hour = 0, minute = 1, second = 0)
		Hora1Out = datetime.time(hour = 0, minute = 0, second = 30)
		Hora2In = datetime.time(hour = 23, minute = 59, second = 59)
		Hora2Out = datetime.time(hour = 19, minute = 59, second = 58)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora2In, Hora2Out])
		x = binaria(valor, 0, len(lista), lista)
		self.assertEqual(x, 1)

# busquedaBin, Pruebas Integracion, funcion 'binaria' con 'busquedaBin'

	# caso borde
	def test_BusquedaBin_horarios_todoeldia(self):
		Hora1In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora2In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora2In, Hora2Out])
		HoraIn = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		HoraOut = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		x = busquedaBin(HoraIn, HoraOut, lista)
		self.assertEqual(x, (1, True))

	# caso borde
	def test_BusquedaBin_noDisponible(self):
		Hora1In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora2In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		Hora3In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora3Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora3In, Hora3Out])
		lista.append([Hora2In, Hora2Out])
		HoraIn = datetime.datetime(year = 2015,month = 10,day = 5,hour = 7, minute = 0, second = 0)
		HoraOut = datetime.datetime(year = 2015,month = 10,day = 5,hour = 9, minute = 0, second = 0)
		x = busquedaBin(HoraIn, HoraOut, lista)
		self.assertEqual(x, (2, False))

	# normal
	def test_BusquedaBin_noDisponible_reservarTodoElDia(self):
		Hora1In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora2In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		Hora3In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora3Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora3In, Hora3Out])
		lista.append([Hora2In, Hora2Out])
		HoraIn = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		HoraOut = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		x = busquedaBin(HoraIn, HoraOut, lista)
		self.assertEqual(x, (1, False))

	# caso borde
	def test_BusquedaBin_lista_solo_maxmin(self):
		Hora1In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora2In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora2In, Hora2Out])
		HoraIn = datetime.datetime(year = 2015,month = 10,day = 5,hour = 12, minute = 0, second = 0)
		HoraOut = datetime.datetime(year = 2015,month = 10,day = 5,hour = 18, minute = 0, second = 0)
		x = busquedaBin(HoraIn, HoraOut, lista)
		self.assertEqual(x, (1, True))

	# caso borde
	def test_BusquedaBin_horasIguales_Inicio(self):
		Hora1In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora2In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora2In, Hora2Out])
		HoraIn = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		HoraOut = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		x = busquedaBin(HoraIn, HoraOut, lista)
		self.assertEqual(x, (1, True))

	# caso borde
	def test_BusquedaBin_horasIguales_Fin(self):
		Hora1In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora2In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora2In, Hora2Out])
		HoraIn = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		HoraOut = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		x = busquedaBin(HoraIn, HoraOut, lista)
		self.assertEqual(x, (1, True))

	# malicia
	def test_BusquedaBin_lista_no_inicializada(self):
		lista = []
		HoraIn = datetime.time(hour = 6, minute = 0, second = 0)
		HoraOut = datetime.time(hour = 12, minute = 0, second = 0)
		x = busquedaBin(HoraIn, HoraOut, lista)
		self.assertEqual(x, (0, True))

	# malicia
	def test_BusquedaBin_lista_None(self):
		lista = None
		HoraIn = datetime.time(hour = 6, minute = 0, second = 0)
		HoraOut = datetime.time(hour = 12, minute = 0, second = 0)
		x = busquedaBin(HoraIn, HoraOut, lista)
		self.assertEqual(x, (0, False))

	# malicia
	def test_BusquedaBin_lista_noLista(self):
		lista = 'String'
		HoraIn = datetime.time(hour = 6, minute = 0, second = 0)
		HoraOut = datetime.time(hour = 12, minute = 0, second = 0)
		x = busquedaBin(HoraIn, HoraOut, lista)
		self.assertEqual(x, (0, False))

	# malicia
	def test_BusquedaBin_horaIngreso_None(self):
		Hora1In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.time(hour = 6, minute = 0, second = 0)
		Hora2In = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.time(hour = 22, minute = 0, second = 0)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora2In, Hora2Out])
		HoraIn = None
		HoraOut = datetime.time(hour = 22, minute = 0, second = 0)
		x = busquedaBin(HoraIn, HoraOut, lista)
		self.assertEqual(x, (0, False))

	# malicia
	def test_BusquedaBin_horaSalida_None(self):
		Hora1In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.time(hour = 6, minute = 0, second = 0)
		Hora2In = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.time(hour = 22, minute = 0, second = 0)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora2In, Hora2Out])
		HoraIn = datetime.time(hour = 6, minute = 0, second = 0)
		HoraOut = None
		x = busquedaBin(HoraIn, HoraOut, lista)
		self.assertEqual(x, (0, False))

	# malicia
	def test_BusquedaBin_horaIngreso_no_datetime(self):
		Hora1In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.time(hour = 6, minute = 0, second = 0)
		Hora2In = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.time(hour = 22, minute = 0, second = 0)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora2In, Hora2Out])
		HoraIn = 'String'
		HoraOut = datetime.time(hour = 22, minute = 0, second = 0)
		x = busquedaBin(HoraIn, HoraOut, lista)
		self.assertEqual(x, (0, False))

	# malicia
	def test_BusquedaBin_horaSalida_no_datetime(self):
		Hora1In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.time(hour = 6, minute = 0, second = 0)
		Hora2In = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.time(hour = 22, minute = 0, second = 0)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora2In, Hora2Out])
		HoraIn = datetime.time(hour = 6, minute = 0, second = 0)
		HoraOut = 'String'
		x = busquedaBin(HoraIn, HoraOut, lista)
		self.assertEqual(x, (0, False))

	# normal
	def test_BusquedaBin_todoEn_None(self):
		lista = None
		HoraIn = None
		HoraOut = None
		x = busquedaBin(HoraIn, HoraOut, lista)
		self.assertEqual(x, (0, False))

# buscar, Pruebas Integracion, funcion 'busquedaBin' con 'buscar'

	# normal
	def test_buscar_funcionalidadOK(self):
		Hora1In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora2In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora2In, Hora2Out])
		estacionamiento = [lista for x in range(2)]
		HoraIn = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		HoraOut = datetime.datetime(year = 2015,month = 10,day = 5,hour = 12, minute = 0, second = 0)
		x = buscar(HoraIn, HoraOut, estacionamiento)
		self.assertEqual(x, (0, 1, True))

	# caso borde
	def test_buscar_horas_Iguales(self):
		Hora1In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora2In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora2In, Hora2Out])
		estacionamiento = [lista for x in range(2)]
		HoraIn = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		HoraOut = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		x = buscar(HoraIn, HoraOut, estacionamiento)
		self.assertEqual(x, (0, 1, True))

	# caso borde
	def test_buscar_estacionamientoLleno(self):
		Hora1In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3Out = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2In = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.time(hour = 22, minute = 0, second = 0)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora3In, Hora3Out])
		lista.append([Hora2In, Hora2Out])
		estacionamiento = [lista for x in range(2)]
		HoraIn = datetime.time(hour = 6, minute = 0, second = 0)
		HoraOut = datetime.time(hour = 12, minute = 0, second = 0)
		x = buscar(HoraIn, HoraOut, estacionamiento)
		self.assertEqual(x, (-1, -1, False))

	# malicia
	def test_buscar_estacionamiento_None(self):
		estacionamiento = None
		HoraIn = datetime.time(hour = 6, minute = 0, second = 0)
		HoraOut = datetime.time(hour = 12, minute = 0, second = 0)
		x = buscar(HoraIn, HoraOut, estacionamiento)
		self.assertEqual(x, (-1, -1, False))

	# malicia
	def test_buscar_estacionamiento_noLista(self):
		estacionamiento = 'String'
		HoraIn = datetime.time(hour = 6, minute = 0, second = 0)
		HoraOut = datetime.time(hour = 12, minute = 0, second = 0)
		x = buscar(HoraIn, HoraOut, estacionamiento)
		self.assertEqual(x, (-1, -1, False))

	# malicia
	def test_buscar_estacionamiento_noInicializado(self):
		estacionamiento = []
		HoraIn = datetime.time(hour = 6, minute = 0, second = 0)
		HoraOut = datetime.time(hour = 12, minute = 0, second = 0)
		x = buscar(HoraIn, HoraOut, estacionamiento)
		self.assertEqual(x, (-1, -1, False))

	# malicia
	def test_buscar_horaIngreso_None(self):
		Hora1In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3Out = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2In = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.time(hour = 22, minute = 0, second = 0)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora3In, Hora3Out])
		lista.append([Hora2In, Hora2Out])
		estacionamiento = [lista for x in range(2)]
		HoraIn = None
		HoraOut = datetime.time(hour = 12, minute = 0, second = 0)
		x = buscar(HoraIn, HoraOut, estacionamiento)
		self.assertEqual(x, (-1, -1, False))

	# malicia
	def test_buscar_horaFin_None(self):
		Hora1In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3Out = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2In = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.time(hour = 22, minute = 0, second = 0)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora3In, Hora3Out])
		lista.append([Hora2In, Hora2Out])
		estacionamiento = [lista for x in range(2)]
		HoraIn = datetime.time(hour = 6, minute = 0, second = 0)
		HoraOut = None
		x = buscar(HoraIn, HoraOut, estacionamiento)
		self.assertEqual(x, (-1, -1, False))

	# malicia
	def test_buscar_horaIngreso_noDatetime(self):
		Hora1In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3Out = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2In = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.time(hour = 22, minute = 0, second = 0)
		lista = []
		lista.append([Hora1In, Hora1Out])
		lista.append([Hora3In, Hora3Out])
		lista.append([Hora2In, Hora2Out])
		estacionamiento = [lista for x in range(2)]
		HoraIn = 'String'
		HoraOut = datetime.time(hour = 12, minute = 0, second = 0)
		x = buscar(HoraIn, HoraOut, estacionamiento)
		self.assertEqual(x, (-1, -1, False))

	# normal
	def test_buscar_todo_None(self):
		estacionamiento = None
		HoraIn = None
		HoraOut = None
		x = buscar(HoraIn, HoraOut, estacionamiento)
		self.assertEqual(x, (-1, -1, False))

	# normal
	def test_buscar_todo_invalido(self):
		estacionamiento = 'String'
		HoraIn = 42
		HoraOut = 42
		x = buscar(HoraIn, HoraOut, estacionamiento)
		self.assertEqual(x, (-1, -1, False))


# insertarReserva, Pruebas Unitarias
# no se requiere unas pruebas exaustivas de esta funcion, ya que esta funcion
# solo agrega una tupla a la lista otorgada utilizando la funcion 'insert' de las listas
# de python, la cual presumo que ha sido probada en gran cantidad de oportunidades

	# normal
	def test_insertarReserva_funcionalidadOk(self):
		Hora1In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora3In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora3Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		Hora2In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		lista = []
		lista.append((Hora1In, Hora1Out))
		lista.append((Hora2In, Hora2Out))
		lista2 = []
		lista2.append((Hora1In, Hora1Out))
		lista2.append((Hora3In, Hora3Out))
		lista2.append((Hora2In, Hora2Out))
		x = insertarReserva(Hora3In, Hora3Out, 1, lista)
		self.assertEqual(x, lista2)

	# malicia
	def test_insertarReserva_lista_None(self):
		Hora3In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3Out = datetime.time(hour = 22, minute = 0, second = 0)
		lista = None
		x = insertarReserva(Hora3In, Hora3Out, 1, lista)
		self.assertEqual(x, None)

	# malicia
	def test_insertarReserva_lista_noLista(self):
		Hora3In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3Out = datetime.time(hour = 22, minute = 0, second = 0)
		lista = 'String'
		x = insertarReserva(Hora3In, Hora3Out, 1, lista)
		self.assertEqual(x, None)

	# malicia
	def test_insertarReserva_horaIngreso_None(self):
		Hora1In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3In = None
		Hora3Out = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2In = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.time(hour = 22, minute = 0, second = 0)
		lista = []
		lista.append((Hora1In, Hora1Out))
		lista.append((Hora2In, Hora2Out))
		x = insertarReserva(Hora3In, Hora3Out, 1, lista)
		self.assertEqual(x, lista)

	# malicia
	def test_insertarReserva_horaSalida_None(self):
		Hora1In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3Out = None
		Hora2In = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.time(hour = 22, minute = 0, second = 0)
		lista = []
		lista.append((Hora1In, Hora1Out))
		lista.append((Hora2In, Hora2Out))
		x = insertarReserva(Hora3In, Hora3Out, 1, lista)
		self.assertEqual(x, lista)

	# malicia
	def test_insertarReserva_horaIngreso_noDatetime(self):
		Hora1In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3In = 42
		Hora3Out = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2In = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.time(hour = 22, minute = 0, second = 0)
		lista = []
		lista.append((Hora1In, Hora1Out))
		lista.append((Hora2In, Hora2Out))
		x = insertarReserva(Hora3In, Hora3Out, 1, lista)
		self.assertEqual(x, lista)

	# malicia
	def test_insertarReserva_horaSalida_noDatetime(self):
		Hora1In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3Out = 42
		Hora2In = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.time(hour = 22, minute = 0, second = 0)
		lista = []
		lista.append((Hora1In, Hora1Out))
		lista.append((Hora2In, Hora2Out))
		x = insertarReserva(Hora3In, Hora3Out, 1, lista)
		self.assertEqual(x, lista)

	# malicia
	def test_insertarReserva_todo_None(self):
		lista = None
		x = insertarReserva(None, None, 1, lista)
		self.assertEqual(x, None)

# reservar, Pruebas Integracion, funciones 'reservar', 'buscar' e 'insertarReserva'

	# normal
	def test_reservar_funcionalidadOk(self):
		Hora1In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora3In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 8, minute = 0, second = 0)
		Hora3Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 12, minute = 0, second = 0)
		Hora2In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		lista = []
		lista.append((Hora1In, Hora1Out))
		lista.append((Hora2In, Hora2Out))
		estacionamiento = [lista for x in range(2)]
		lista2 = []
		lista2.append((Hora1In, Hora1Out))
		lista2.append((Hora3In, Hora3Out))
		lista2.append((Hora2In, Hora2Out))
		estacionamiento2 = []
		estacionamiento2.append(lista2)
		estacionamiento2.append(lista)
		x = reservar(Hora3In, Hora3Out, estacionamiento)
		self.assertEqual(x, estacionamiento2)

	# caso frontera
	def test_reservar_estacionamiento_full(self):
		Hora1In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3Out = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2In = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.time(hour = 22, minute = 0, second = 0)
		lista = []
		lista.append((Hora1In, Hora1Out))
		lista.append((Hora3In, Hora3Out))
		lista.append((Hora2In, Hora2Out))
		estacionamiento = [lista for x in range(2)]
		x = reservar(Hora3In, Hora3Out, estacionamiento)
		self.assertEqual(x, 1)

	# caso frontera
	def test_reservar_ultimoPuestoAReservar(self):
		Hora1In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 6, minute = 0, second = 0)
		Hora3In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 8, minute = 0, second = 0)
		Hora3Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 12, minute = 0, second = 0)
		Hora2In = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.datetime(year = 2015,month = 10,day = 5,hour = 22, minute = 0, second = 0)
		lista = []
		lista.append((Hora1In, Hora1Out))
		lista.append((Hora2In, Hora2Out))
		lista2 = []
		lista2.append((Hora1In, Hora1Out))
		lista2.append((Hora3In, Hora3Out))
		lista2.append((Hora2In, Hora2Out))
		estacionamiento = []
		estacionamiento.append(lista2)
		estacionamiento.append(lista)
		estacionamiento2 = []
		estacionamiento2.append(lista2)
		estacionamiento2.append(lista2)
		x = reservar(Hora3In, Hora3Out, estacionamiento)
		self.assertEqual(x, estacionamiento2)

	# malicia
	def test_reservar_estacionamiento_None(self):
		Hora3In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3Out = datetime.time(hour = 22, minute = 0, second = 0)
		estacionamiento = None
		x = reservar(Hora3In, Hora3Out, estacionamiento)
		self.assertEqual(x, 1)

	# malicia
	def test_reservar_estacionamiento_noLista(self):
		Hora3In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3Out = datetime.time(hour = 22, minute = 0, second = 0)
		estacionamiento = 'String'
		x = reservar(Hora3In, Hora3Out, estacionamiento)
		self.assertEqual(x, 1)

	# malicia
	def test_reservar_horaIngreso_None(self):
		Hora1In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3In = None
		Hora3Out = datetime.time(hour = 12, minute = 0, second = 0)
		Hora2In = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.time(hour = 22, minute = 0, second = 0)
		lista = []
		lista.append((Hora1In, Hora1Out))
		lista.append((Hora2In, Hora2Out))
		estacionamiento = [lista for x in range(2)]
		lista2 = []
		lista2.append((Hora1In, Hora1Out))
		lista2.append((Hora3In, Hora3Out))
		lista2.append((Hora2In, Hora2Out))
		estacionamiento2 = []
		estacionamiento2.append(lista2)
		estacionamiento2.append(lista)
		x = reservar(Hora3In, Hora3Out, estacionamiento)
		self.assertEqual(x, 1)

	# malicia
	def test_reservar_horaSalida_None(self):
		Hora1In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3In = datetime.time(hour = 8, minute = 0, second = 0)
		Hora3Out = None
		Hora2In = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.time(hour = 22, minute = 0, second = 0)
		lista = []
		lista.append((Hora1In, Hora1Out))
		lista.append((Hora2In, Hora2Out))
		estacionamiento = [lista for x in range(2)]
		lista2 = []
		lista2.append((Hora1In, Hora1Out))
		lista2.append((Hora3In, Hora3Out))
		lista2.append((Hora2In, Hora2Out))
		estacionamiento2 = []
		estacionamiento2.append(lista2)
		estacionamiento2.append(lista)
		x = reservar(Hora3In, Hora3Out, estacionamiento)
		self.assertEqual(x, 1)

	# malicia
	def test_reservar_horaIngreso_noLista(self):
		Hora1In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3In = 'String'
		Hora3Out = datetime.time(hour = 12, minute = 0, second = 0)
		Hora2In = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.time(hour = 22, minute = 0, second = 0)
		lista = []
		lista.append((Hora1In, Hora1Out))
		lista.append((Hora2In, Hora2Out))
		estacionamiento = [lista for x in range(2)]
		lista2 = []
		lista2.append((Hora1In, Hora1Out))
		lista2.append((Hora3In, Hora3Out))
		lista2.append((Hora2In, Hora2Out))
		estacionamiento2 = []
		estacionamiento2.append(lista2)
		estacionamiento2.append(lista)
		x = reservar(Hora3In, Hora3Out, estacionamiento)
		self.assertEqual(x, 1)

	# malicia
	def test_reservar_horaSalida_noLista(self):
		Hora1In = datetime.time(hour = 6, minute = 0, second = 0)
		Hora1Out = datetime.time(hour = 6, minute = 0, second = 0)
		Hora3In = datetime.time(hour = 8, minute = 0, second = 0)
		Hora3Out = 'String'
		Hora2In = datetime.time(hour = 22, minute = 0, second = 0)
		Hora2Out = datetime.time(hour = 22, minute = 0, second = 0)
		lista = []
		lista.append((Hora1In, Hora1Out))
		lista.append((Hora2In, Hora2Out))
		estacionamiento = [lista for x in range(2)]
		lista2 = []
		lista2.append((Hora1In, Hora1Out))
		lista2.append((Hora3In, Hora3Out))
		lista2.append((Hora2In, Hora2Out))
		estacionamiento2 = []
		estacionamiento2.append(lista2)
		estacionamiento2.append(lista)
		x = reservar(Hora3In, Hora3Out, estacionamiento)
		self.assertEqual(x, 1)

	# malicia
	def test_reservar_todo_None(self):
		x = reservar(None, None, None)
		self.assertEqual(x, 1)

#################################################################
#		Pruebas calculo de tarifa por horas 
################################################################
	
	global min_tarifa, max_tarifa, estacionamiento, esq15, esq20, esq30, esqmin, esqmax
	global esq15M,esq20M,esq30M,esqminM,esqmaxM,esq15HF,esq20HF,esq30HF,esqminHF,esqmaxHF
	global esq15D,esq20D,esq30D,esqminD,esqmaxD
	min_tarifa = Decimal(0)
	max_tarifa = Decimal(9999999.99)
	estacionamiento = Estacionamiento(Propietario="DUBI",Nombre="Patty",Direccion="Richard",Rif="J-123456789")
	esq15=Hora(Estacionamiento=estacionamiento,Tarifa=Decimal(15))
	esq20=Hora(Estacionamiento=estacionamiento,Tarifa=Decimal(20))
	esq30=Hora(Estacionamiento=estacionamiento,Tarifa=Decimal(30))
	esqmin=Hora(Estacionamiento=estacionamiento,Tarifa=Decimal(min_tarifa))
	esqmax=Hora(Estacionamiento=estacionamiento,Tarifa=Decimal(max_tarifa))
	esq15M=Minuto(Estacionamiento=estacionamiento,Tarifa=Decimal(15))
	esq20M=Minuto(Estacionamiento=estacionamiento,Tarifa=Decimal(20))
	esq30M=Minuto(Estacionamiento=estacionamiento,Tarifa=Decimal(30))
	esqminM=Minuto(Estacionamiento=estacionamiento,Tarifa=Decimal(min_tarifa))
	esqmaxM=Minuto(Estacionamiento=estacionamiento,Tarifa=Decimal(max_tarifa))
	esq15HF=HoraFraccion(Estacionamiento=estacionamiento,Tarifa=Decimal(15))
	esq20HF=HoraFraccion(Estacionamiento=estacionamiento,Tarifa=Decimal(20))
	esq30HF=HoraFraccion(Estacionamiento=estacionamiento,Tarifa=Decimal(30))
	esqminHF=HoraFraccion(Estacionamiento=estacionamiento,Tarifa=Decimal(min_tarifa))
	esqmaxHF=HoraFraccion(Estacionamiento=estacionamiento,Tarifa=Decimal(max_tarifa))
	
	# El minimo tiempo de reserva es de 1 hora
	# El máximo tiempo de reserva es de 7 dias
		
	# Extremo
	def test_tarifaPorHoraMinTiempo(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,5,19,25,0,0)
		self.assertEqual(esq15.calcularMonto(inires, finres), Decimal(15))
		
	# Extremo 
	def test_tarifaPorHoraMaxTiempo(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,12,18,25,0,0)
		self.assertEqual(esq15.calcularMonto(inires, finres), Decimal(15*24*7))
	
	# Extremo
	def test_tarifaPorHoraFraccion1Min(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,5,19,26,0,0)
		self.assertEqual(esq20.calcularMonto(inires, finres), Decimal(20*2))
		
	# Extremo
	def test_tarifaPorHoraHorasExactasMismoDia(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,5,21,25,0,0)
		self.assertEqual(esq30.calcularMonto(inires, finres), Decimal(30*3))
	
	# Extremo
	def test_tarifaPorHoraHorasExactasDiferentesDia(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,8,18,25,0,0)
		self.assertEqual(esq30.calcularMonto(inires, finres), Decimal(72*30))
	
	# Extremo
	def test_tarifaPorHoraFraccion59Min(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,5,20,24,0,0)
		self.assertEqual(esq20.calcularMonto(inires, finres), Decimal(20*2))
		
	# Extremo
	def test_tarifaPorHora1MinMenosQueTiempoMaximo(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,12,18,24,0,0)
		self.assertEqual(esq20.calcularMonto(inires, finres), Decimal(7*24*20))
	
	# Extremo
	def test_tarifaPorHoraMinimaTarifa(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,6,15,0,0,0)
		self.assertEqual(esqmin.calcularMonto(inires, finres), Decimal(0))
		
	# Extremo
	def test_tarifaPorHoraMaximaTarifa(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,5,20,0,0,0)
		self.assertEqual(esqmax.calcularMonto(inires, finres), Decimal(9999999.99*2).quantize(Decimal(10)**-2))
	
	# Exquina	
	def test_tarifaPorHoraMaxTarifaMaxTiempo(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,12,18,25,0,0)
		self.assertEqual(esqmax.calcularMonto(inires, finres), Decimal(9999999.99*7*24).quantize(Decimal(10)**-2))
		
#################################################################
#		Pruebas calculo de tarifa por minutos 
#################################################################

	# El minimo tiempo de reserva es de 1 hora
	# El máximo tiempo de reserva es de 7 dias

	# Extremo
	def test_tarifaPorMinutoMinTiempo(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,5,19,25,0,0)
		self.assertEqual(esq15M.calcularMonto(inires, finres), Decimal(15))
		
	# Extremo 
	def test_tarifaPorMinutoMaxTiempo(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,12,18,25,0,0)
		self.assertEqual(esq15M.calcularMonto(inires, finres), Decimal(15*24*7).quantize(Decimal(10)**-2))
		
	# Extremo
	def test_tarifaPorMinutoFraccion1Min(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,5,20,26,0,0)
		self.assertEqual(esq20M.calcularMonto(inires, finres), Decimal(20*2 + 20/60).quantize(Decimal(10)**-2))
	
	# Extremo
	def test_tarifaPorMinutoFraccion59Min(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,5,22,24,0,0)
		self.assertEqual(esq20M.calcularMonto(inires, finres), Decimal(20*3 + 59 *(20/60)).quantize(Decimal(10)**-2))
	
	# Extremo
	def test_tarifaPorMinutoHorasExactasMismoDia(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,5,21,25,0,0)
		self.assertEqual(esq30M.calcularMonto(inires, finres), Decimal(30*3))
	
	# Extremo
	def test_tarifaPorMinutoHorasExactasDiferentesDia(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,8,18,25,0,0)
		self.assertEqual(esq30M.calcularMonto(inires, finres), Decimal(72*30))
		
	# Extremo
	def test_tarifaPorMinuto1MinMenosQueTiempoMaximo(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,12,18,24,0,0)
		self.assertEqual(esq20M.calcularMonto(inires, finres), Decimal(round(6*24*20 + 23*20 + 20/60*59,2)).quantize(Decimal(10)**-2))
	
	# Extremo
	def test_tarifaPorMinutoMinimaTarifa(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,6,15,0,0,0)
		self.assertEqual(esqminM.calcularMonto(inires, finres), Decimal(0))
	
	# Extremo
	def test_tarifaPorMinutoMaximaTarifa(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,5,20,0,0,0)
		self.assertEqual(esqmaxM.calcularMonto(inires, finres), Decimal(9999999.99+9999999.99/60*35).quantize(Decimal(10)**-2))
	
	# Esquina
	def test_tarifaPorMinutoMaxTarifaMaxTiempo(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,12,18,25,0,0)
		self.assertEqual(esqmaxM.calcularMonto(inires, finres), Decimal(9999999.99*7*24).quantize(Decimal(10)**-2))

#################################################################
#		Pruebas calculo de tarifa por hora y fracion
#################################################################

	# El minimo tiempo de reserva es de 1 hora
	# El máximo tiempo de reserva es de 7 dias

	# Extremo
	def test_tarifaPorHoraYFraccionMinTiempo(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,5,19,25,0,0)
		self.assertEqual(esq15HF.calcularMonto(inires, finres), Decimal(15))
			
	# Extremo 
	def test_tarifaPorHoraYFraccionMaxTiempo(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,12,18,25,0,0)
		self.assertEqual(esq15HF.calcularMonto(inires, finres), Decimal(15*24*7).quantize(Decimal(10)**-2))
		
	# Extremo
	def test_tarifaPorHoraYFraccionFraccion1Min(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,5,20,26,0,0)
		self.assertEqual(esq20HF.calcularMonto(inires, finres), Decimal(20*2 + 10).quantize(Decimal(10)**-2))
	
	#  Extremo
	def test_tarifaPorHoraYFraccionFraccion30Min(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,5,20,55,0,0)
		self.assertEqual(esq20HF.calcularMonto(inires, finres), Decimal(20*2 + 10).quantize(Decimal(10)**-2))
	
	# Extremo
	def test_tarifaPorHoraYFraccionFraccion31Min(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,5,20,56,0,0)
		self.assertEqual(esq20HF.calcularMonto(inires, finres), Decimal(20*2 + 20).quantize(Decimal(10)**-2))
	
	# Extremo
	def test_tarifaPorHoraYFraccionFraccion59Min(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,5,22,24,0,0)
		self.assertEqual(esq20HF.calcularMonto(inires, finres), Decimal(20*3 + 20).quantize(Decimal(10)**-2))
	
	# 
	def test_tarifaPorHoraYFraccionHorasExactasMismoDia(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,5,21,25,0,0)
		self.assertEqual(esq30HF.calcularMonto(inires, finres), Decimal(30*3))
	
	# 
	def test_tarifaPorHoraYFraccionHorasExactasDiferentesDia(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,8,18,25,0,0)
		self.assertEqual(esq30HF.calcularMonto(inires, finres), Decimal(72*30))
	
	# Extremo
	def test_tarifaPorHoraYFraccion1MinMenosQueTiempoMaximo(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,12,18,24,0,0)
		self.assertEqual(esq20HF.calcularMonto(inires, finres), Decimal(6*24*20 + 23*20 + 20).quantize(Decimal(10)**-2))

	# Extremo
	def test_tarifaPorHoraYFraccionMinimaTarifa(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,6,15,0,0,0)
		self.assertEqual(esqminHF.calcularMonto(inires, finres), Decimal(0))
		
	# Extremo
	def test_tarifaPorHoraYFraccionMaximaTarifa(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,5,20,0,0,0)
		self.assertEqual(esqmaxHF.calcularMonto(inires, finres), Decimal(9999999.99*2).quantize(Decimal(10)**-2))
		
	# Esquina
	def test_tarifaPorHoraYFraccionMaxTarifaMaxTiempo(self):
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,12,18,25,0,0)
		self.assertEqual(esqmaxHF.calcularMonto(inires, finres), Decimal(9999999.99*7*24).quantize(Decimal(10)**-2))



#################################################################
#		Pruebas calculo de tarifa diferencido por hora
#################################################################

	# El minimo tiempo de reserva es de 1 hora
	# El máximo tiempo de reserva es de 7 dias
	# El mínimo tiempo del horario pico es de 1 minuto
	# El máximo tiempo del horario pico es de 24 horas
	
	# Extremo
	def test_tarifaDiferenciadoPorHoraMinTiempoFueraHoraPico(self):
		tarifa = Decimal(15)
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,5,19,25,0,0)
		tarifapico = Decimal(20)
		iniciopico = datetime.time(12,0,0)
		finpico = datetime.time(15,0,0)
		esq=DifHora(Estacionamiento=estacionamiento,Tarifa=tarifa,PicoIni=iniciopico,PicoFin=finpico,TarifaPico=tarifapico)
		
		self.assertEqual(esq.calcularMonto(inires, finres), Decimal(15))
	
	# Extremo	
	def test_tarifaDiferenciadoPorHoraMinTiempoDentroHoraPico(self):
		tarifa = Decimal(15)
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,5,19,25,0,0)
		tarifapico = Decimal(20)
		iniciopico = datetime.time(15,0,0)
		finpico = datetime.time(20,0,0)
		esq=DifHora(Estacionamiento=estacionamiento,Tarifa=tarifa,PicoIni=iniciopico,PicoFin=finpico,TarifaPico=tarifapico)
		
		self.assertEqual(esq.calcularMonto(inires, finres), Decimal(20))

	# Extremo
	def test_tarifaDiferenciadoPorHoraReserva1MinutoAntesDeTerminarHorarioPico(self):
		tarifa = 20	
		inires = datetime.datetime(2015,7,5,12,25,0,0)
		finres = datetime.datetime(2015,7,5,15,59,0,0)
		tarifapico = 25
		iniciopico = datetime.time(14,0,0)
		finpico = datetime.time(16,0,0)
		esq=DifHora(Estacionamiento=estacionamiento,Tarifa=tarifa,PicoIni=iniciopico,PicoFin=finpico,TarifaPico=tarifapico)
	
		self.assertEqual(esq.calcularMonto(inires, finres), Decimal(20+35*20/60+25+25*59/60).quantize(Decimal(10)**-2))
			
	#  Extremo
	def test_tarifaDiferenciadoPorHoraMaxTiempo(self):
		tarifa = Decimal(15)
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,12,18,25,0,0)
		tarifapico = Decimal(20)
		iniciopico = datetime.time(15,0,0)
		finpico = datetime.time(20,0,0)
		esq=DifHora(Estacionamiento=estacionamiento,Tarifa=tarifa,PicoIni=iniciopico,PicoFin=finpico,TarifaPico=tarifapico)
		
		self.assertEqual(esq.calcularMonto(inires, finres), Decimal(5*20*7+19*15*7).quantize(Decimal(10)**-2))
		
	# Extremo
	def test_tarifaDiferenciadoPorHora1MinMenosQueTiempoMaximo(self):
		tarifa = Decimal(20)
		inires = datetime.datetime(2015,7,5,18,25,0,0)
		finres = datetime.datetime(2015,7,12,18,24,0,0)
		tarifapico = Decimal(25)
		iniciopico = datetime.time(15,0,0)
		finpico = datetime.time(20,0,0)
		esq=DifHora(Estacionamiento=estacionamiento,Tarifa=tarifa,PicoIni=iniciopico,PicoFin=finpico,TarifaPico=tarifapico)
		
		self.assertEqual(esq.calcularMonto(inires, finres), Decimal(5*25*7+19*20*7-25/60).quantize(Decimal(10)**-2))

	# Esquina
	def test_tarifaDiferenciadoPorHoraReservaIgualQueHoraPico(self):
		tarifa = Decimal(20)
		inires = datetime.datetime(2015,7,5,13,25,0,0)
		finres = datetime.datetime(2015,7,5,18,25,0,0)
		tarifapico = Decimal(25)
		iniciopico = datetime.time(13,25,0,0)
		finpico = datetime.time(18,25,0,0)
		esq=DifHora(Estacionamiento=estacionamiento,Tarifa=tarifa,PicoIni=iniciopico,PicoFin=finpico,TarifaPico=tarifapico)
		
		self.assertEqual(esq.calcularMonto(inires, finres), Decimal(25*5).quantize(Decimal(10)**-2))

	# Extremo		
	def test_tarifaDiferenciadoPorHoraMinimoTiempoDeHoraPico(self):
		tarifa = Decimal(20)
		inires = datetime.datetime(2015,7,5,12,25,0,0)
		finres = datetime.datetime(2015,7,5,16,0,0,0)
		tarifapico = Decimal(25)
		iniciopico = datetime.time(15,0,0)
		finpico = datetime.time(15,1,0)
		esq=DifHora(Estacionamiento=estacionamiento,Tarifa=tarifa,PicoIni=iniciopico,PicoFin=finpico,TarifaPico=tarifapico)
	
		self.assertEqual(esq.calcularMonto(inires, finres), Decimal(214*20/60+25/60).quantize(Decimal(10)**-2))

	# Extremo
	def test_tarifaDiferenciadoPorHoraMaximoTiempoDeHoraPico(self):
		tarifa = Decimal(20)
		inires = datetime.datetime(2015,7,5,12,25,0,0)
		finres = datetime.datetime(2015,7,5,16,0,0,0)
		tarifapico = Decimal(25)
		iniciopico = datetime.time(0,0,0)
		finpico = datetime.time(23,59,0)
		esq=DifHora(Estacionamiento=estacionamiento,Tarifa=tarifa,PicoIni=iniciopico,PicoFin=finpico,TarifaPico=tarifapico)
		
		self.assertEqual(esq.calcularMonto(inires, finres), Decimal(215*25/60).quantize(Decimal(10)**-2))

	# Esquina
	def test_tarifaDiferenciadoPorHoraMaxTiempoFueraDeHoraPicoSinLimitesIncluidos(self):
		tarifa = Decimal(20)
		inires = datetime.datetime(2015,7,5,20,1,0,0)
		finres = datetime.datetime(2015,7,6,14,59,0,0)
		tarifapico = Decimal(25)
		iniciopico = datetime.time(15,0,0)
		finpico = datetime.time(20,0,0)
		esq=DifHora(Estacionamiento=estacionamiento,Tarifa=tarifa,PicoIni=iniciopico,PicoFin=finpico,TarifaPico=tarifapico)
		
		self.assertEqual(esq.calcularMonto(inires, finres), Decimal(19*20-20/60*2).quantize(Decimal(10)**-2))
	
	# Esquina	
	def test_tarifaDiferenciadoPorHoraMaxTiempoFueraDeHoraPicoConLimitesIncluidos(self):
		tarifa = Decimal(20)
		inires = datetime.datetime(2015,7,5,20,0,0,0)
		finres = datetime.datetime(2015,7,6,15,0,0,0)
		tarifapico = Decimal(25)
		iniciopico = datetime.time(15,0,0)
		finpico = datetime.time(20,0,0)
		esq=DifHora(Estacionamiento=estacionamiento,Tarifa=tarifa,PicoIni=iniciopico,PicoFin=finpico,TarifaPico=tarifapico)
		self.assertEqual(esq.calcularMonto(inires, finres), Decimal(19*20).quantize(Decimal(10)**-2))	

	# Extremo
	def test_tarifaDiferenciadoPorHoraMinTarifaEnHorarioValle(self):
		tarifa = min_tarifa
		inires = datetime.datetime(2015,7,5,12,25,0,0)
		finres = datetime.datetime(2015,7,6,3,25,0,0)
		tarifapico = Decimal(30)
		iniciopico = datetime.time(14,0,0)
		finpico = datetime.time(16,0,0)
		esq=DifHora(Estacionamiento=estacionamiento,Tarifa=tarifa,PicoIni=iniciopico,PicoFin=finpico,TarifaPico=tarifapico)
		self.assertEqual(esq.calcularMonto(inires, finres), Decimal(30*2).quantize(Decimal(10)**-2))

	# Extremo	
	def test_tarifaDiferenciadoPorHoraMaxTarifaEnHorarioPico(self):
		tarifa = max_tarifa-Decimal(0.01)
		inires = datetime.datetime(2015,7,5,12,25,0,0)
		finres = datetime.datetime(2015,7,6,3,25,0,0)
		tarifapico = max_tarifa
		iniciopico = datetime.time(14,0,0)
		finpico = datetime.time(16,0,0)
		esq=DifHora(Estacionamiento=estacionamiento,Tarifa=tarifa,PicoIni=iniciopico,PicoFin=finpico,TarifaPico=tarifapico)
		self.assertEqual(esq.calcularMonto(inires, finres), Decimal(9999999.99*2+9999999.98*95/60+9999999.98*11+9999999.98*25/60).quantize(Decimal(10)**-2))

	# Esquina maliciosa
	def test_tarifaDiferenciadoPorHoraMaxTiempoDeHoraPicoMaximoTiempoReserva(self):
		tarifa = Decimal(20)
		inires = datetime.datetime(2015,7,5,12,25,0,0)
		finres = datetime.datetime(2015,7,12,12,25,0,0)
		tarifapico = Decimal(30)
		iniciopico = datetime.time(0,0,0)
		finpico = datetime.time(23,58,0)
		esq=DifHora(Estacionamiento=estacionamiento,Tarifa=tarifa,PicoIni=iniciopico,PicoFin=finpico,TarifaPico=tarifapico)
		self.assertEqual(esq.calcularMonto(inires, finres), Decimal(24*7*30-2*30/60).quantize(Decimal(10)**-2))

###################################################################
#		Pruebas para validar horario pico
###################################################################

	def test_validarPicosHorarioPicoValido(self):

		horaPicoIni = datetime.time(12,0,0)
		horaPicoFin = datetime.time(14,0,0)
		inicioReservas = datetime.time(6,0,0)
		finReservas = datetime.time(18,0,0)
		tarifa = Decimal(20)
		tarifaPico = Decimal (30)
		
		respuesta = validarPicos(inicioReservas,finReservas,horaPicoIni,horaPicoFin,tarifa,tarifaPico)
		self.assertEqual(respuesta, (True, ''))
		
	def test_validarPicosInicioHorarioPicoMayorFinHorarioPico(self):

		horaPicoIni = datetime.time(14,0,0)
		horaPicoFin = datetime.time(12,0,0)
		inicioReservas = datetime.time(6,0,0)
		finReservas = datetime.time(18,0,0)
		tarifa = Decimal(20)
		tarifaPico = Decimal (30)

		respuesta = validarPicos(inicioReservas,finReservas,horaPicoIni,horaPicoFin,tarifa,tarifaPico)
		self.assertEqual(respuesta, (False, 'La hora de inicio de la hora pico debe ser menor que el fin de la hora pico'))
			
	def test_validarPicosTarifaPicoIgualTarifaValle(self):

		horaPicoIni = datetime.time(12,0,0)
		horaPicoFin = datetime.time(14,0,0)
		inicioReservas = datetime.time(6,0,0)
		finReservas = datetime.time(18,0,0)
		tarifa = Decimal(30)
		tarifaPico = Decimal (30)

		respuesta = validarPicos(inicioReservas,finReservas,horaPicoIni,horaPicoFin,tarifa,tarifaPico)
		self.assertEqual(respuesta, (False, 'La tarifa para el horario pico debe ser mayor que la tarifa para el horario valle'))
		
	
	def test_validarPicosInicioHorarioPicoMenorQueHorarioReservas(self):

		horaPicoIni = datetime.time(5,0,0)
		horaPicoFin = datetime.time(14,0,0)
		inicioReservas = datetime.time(6,0,0)
		finReservas = datetime.time(18,0,0)
		tarifa = Decimal(20)
		tarifaPico = Decimal (30)

		respuesta = validarPicos(inicioReservas,finReservas,horaPicoIni,horaPicoFin,tarifa,tarifaPico)
		self.assertEqual(respuesta, (False,'El horario pico debe estar dentro del horario de reservas del estacionamiento'))
	
	def test_validarPicosFinHorarioPicoMayorQueHorarioReservas(self):

		horaPicoIni = datetime.time(12,0,0)
		horaPicoFin = datetime.time(19,0,0)
		inicioReservas = datetime.time(6,0,0)
		finReservas = datetime.time(18,0,0)
		tarifa = Decimal(20)
		tarifaPico = Decimal (30)

		respuesta = validarPicos(inicioReservas,finReservas,horaPicoIni,horaPicoFin,tarifa,tarifaPico)
		self.assertEqual(respuesta, (False,'El horario pico debe estar dentro del horario de reservas del estacionamiento'))
	
