import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from fpdf import FPDF
from datetime import datetime
import random


def generar_factura():

    nombre_cliente = nombre_cliente_entry.get()
    apellidos_cliente = apellidos_cliente_entry.get()
    telefono_cliente = telefono_cliente_entry.get()
    dni_cliente = dni_cliente_entry.get()
    ciudad_cliente = ciudad_cliente_entry.get()
    nombre_servicio = nombre_servicio_entry.get()
    descripcion_servicio = descripcion_servicio_entry.get()
    total_servicio = total_servicio_entry.get()

    fecha_factura = datetime.now().strftime('%d/%m/%Y')

    identificador_factura = 'F' + str(random.randint(1000000, 9999999))

    pdf = FPDF()
    pdf.add_page()

    logo_path = 'logo.png'
    pdf.image(logo_path, x=160, y=8, w=40)

    pdf.set_xy(10, 10)
    pdf.set_font('Arial', size=12)
    pdf.cell(0, 10, 'SySCursos Company', ln=True)
    pdf.cell(0, 10, 'Calle No existe N30 CP 21020', ln=True)
    pdf.cell(0, 10, 'B32312312', ln=True)
    pdf.cell(0, 10, f'Fecha: {fecha_factura}', ln=True)

    pdf.ln(20)


    pdf.set_font('Arial', size=16)
    pdf.cell(0,10, txt='FACTURA', ln=True, align='C')

    pdf.set_font('Arial', size=12)
    pdf.cell(0,10, f'Numero Factura: {identificador_factura}', ln=True, align='C')

    pdf.set_font('Arial', size=12)
    pdf.cell(0,10, '------------------------------------', ln=True, align='L')

    pdf.cell(0,10, 'Datos del Cliente', ln=True, align='L')
    pdf.cell(0,10, f'Nombre: {nombre_cliente}', ln=True, align='L')
    pdf.cell(0,10, f'Apellidos: {apellidos_cliente}', ln=True, align='L')
    pdf.cell(0,10, f'Teléfono: {telefono_cliente}', ln=True, align='L')
    pdf.cell(0,10, f'DNI: {dni_cliente}', ln=True, align='L')
    pdf.cell(0,10, f'Ciudad: {ciudad_cliente}', ln=True, align='L')

    pdf.cell(0,10, 'Detalles del Servicio', ln=True, align='L')

    pdf.cell(0,10, '---------------------------------', ln=True, align='L')
    pdf.cell(60,10, 'Nombre del servicio', border=1)
    pdf.cell(80,10, 'Descripción del servicio', border=1)
    pdf.cell(30,10, 'Total', border=1, ln=True)

    pdf.cell(60,10, nombre_servicio, border=1)
    pdf.cell(80,10, descripcion_servicio, border=1)
    pdf.cell(30,10, total_servicio, border=1, ln=True)

    pdf.cell(0,10, '================================================', ln=True, align='L')
    pdf.cell(0,10, 'Gracias por su compra!', ln=True, align='C')


    pdf_file = f'Factura_{nombre_cliente}_{apellidos_cliente}.pdf'
    pdf.output(pdf_file,'F')
    messagebox.showinfo('Factura Generada')



root = tk.Tk()
root.title('Generador de Facturas')

frame = ttk.Frame(root, padding='10')
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text ='Nombre del Cliente').grid(row=0, column=0, sticky=tk.W)
nombre_cliente_entry = ttk.Entry(frame, width=30)
nombre_cliente_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text ='Apellidos del cliente').grid(row=1, column=0, sticky=tk.W)
apellidos_cliente_entry = ttk.Entry(frame, width=30)
apellidos_cliente_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text ='Teléfono del cliente').grid(row=2, column=0, sticky=tk.W)
telefono_cliente_entry = ttk.Entry(frame, width=30)
telefono_cliente_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text ='DNI del Cliente').grid(row=3, column=0, sticky=tk.W)
dni_cliente_entry = ttk.Entry(frame, width=30)
dni_cliente_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text ='Ciudad del Cliente').grid(row=4, column=0, sticky=tk.W)
ciudad_cliente_entry = ttk.Entry(frame, width=30)
ciudad_cliente_entry.grid(row=4, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text ='Nombre del servicio').grid(row=5, column=0, sticky=tk.W)
nombre_servicio_entry = ttk.Entry(frame, width=30)
nombre_servicio_entry.grid(row=5, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text ='Descripción del servicio').grid(row=6, column=0, sticky=tk.W)
descripcion_servicio_entry = ttk.Entry(frame, width=30)
descripcion_servicio_entry.grid(row=6, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text ='Total(€)').grid(row=7, column=0, sticky=tk.W)
total_servicio_entry = ttk.Entry(frame, width=30)
total_servicio_entry.grid(row=7, column=1, sticky=(tk.W, tk.E))

generar_factura_btn = ttk.Button(frame, text='Generar Factura', command=generar_factura)
generar_factura_btn.grid(row=8, column=0, columnspan=2)

root.mainloop()
