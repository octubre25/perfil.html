from django.shortcuts import render
from datetime import date

from .models import*
from .funciones import*

def listar_clientes(request):
	clientes = Cliente.objects.all()
	return render(
					request,
					 './cliente/listar_clientes.html',
					 {
						'clientes' : clientes					 
					 }
				)

def ver_cliente(request):
	if request.method == "POST":
		form = FormularioFiltroCliente(request.POST)
		if form.is_valid():
			cliente = Cliente.objects.get(identidad = request.POST.get['identidad'])
			facturas = EncabezadoFactura.objects.filter(cliente = request.POST.get['identidad'])
			return render(request, './cliente/perfil.html',{ 'cliente': cliente, 'facturas'})
		else:
			form = FormularioFiltroCliente()
		return render(request, './cliente/reportepersonalizado.html', {'form'.form})

def listar_habitaciones(request):
	habitaciones = Habitacion.objects.all()
	return render(
					request,
					 './habitaciones/listar_habitaciones.html',
					 {
						'habitaciones' : habitaciones					 
					 }
				)
def listar_habitaciones_ocupadas(request):
	habitaciones = HabitacionesOcupadas.objects.filter(
								fecha_retiro__gte=date.today())
	return render(
					request,
					'./habitaciones/listar_habitaciones_ocupadas.html',
					{
						'habitaciones_ocupadas': habitaciones
					}
				)
def listar_encabezado_factura(request):
	facturas = EncabezadoFactura.objects.all()
	return render(
					request,
					'./facturas/listar_encabezado_factura.html',
					{
						'encabezado_factura': facturas
					}
				)
def listar_facturas_rango(request)
	if request.method == "POST":
		form = FormularioFiltroFacturas(request.POST)
		if form.is_valid():
			fecha_inicial = form.cleaned_data['fecha_inicial']
			fecha_final = form.cleaned_data['fecha_final']
			facturas = EncabezadoFactura.objects.filter(fecha_proceso_range = (fecha_inicial, fecha_final))
			return render(request, './facturas/listar_facturas.html', { 'facturas': facturas  })
	else:
		form = FormularioFiltroFacturas()
	return render(request, './facturas/reporte.html', {'form':form})


def ver_factura(request, uuid_factura):
	encabezado = EncabezadoFactura.objects.get(factura = uuid_factura)
	detalle = DetalleFactura.objects.filter(factura = uuid_factura)
	total_pagar = obtener_total(detalle)
	return render(
					request,
					'./facturas/comprobante.html',
					{
						'encabezado': encabezado,
						'detalle': detalle,
						'total': total_pagar
					}
				)