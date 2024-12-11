import tkinter as tk
from tkinter import messagebox
from zeep import Client

# URL del WSDL de tu servicio
wsdl_url = 'http://localhost:8080/Servidor/CalculadoraService?WSDL'
client = Client(wsdl_url)

# Funciones para realizar operaciones con el servicio
def realizar_operacion(operador):
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        
        if operador == 'sumar':
            resultado = client.service.sumar(num1, num2)
        elif operador == 'restar':
            resultado = client.service.restar(num1, num2)
        elif operador == 'multiplicar':
            resultado = client.service.multiplicar(num1, num2)
        elif operador == 'dividir':
            if num2 == 0:
                messagebox.showerror("Error", "División por cero no permitida")
                return
            resultado = client.service.dividir(num1, num2)
        
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, str(resultado))
        
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Calculadora SOAP")
root.geometry("300x250")

# Entradas de números
tk.Label(root, text="Número 1:").grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Número 2:").grid(row=1, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# Botones de operaciones
tk.Button(root, text="+", width=5, command=lambda: realizar_operacion('sumar')).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text="-", width=5, command=lambda: realizar_operacion('restar')).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="*", width=5, command=lambda: realizar_operacion('multiplicar')).grid(row=3, column=0, padx=5, pady=5)
tk.Button(root, text="/", width=5, command=lambda: realizar_operacion('dividir')).grid(row=3, column=1, padx=5, pady=5)

# Salida de resultado
tk.Label(root, text="Resultado:").grid(row=4, column=0, padx=5, pady=5)
entry_resultado = tk.Entry(root)
entry_resultado.grid(row=4, column=1, padx=5, pady=5)

# Cerrar aplicación
tk.Button(root, text="Cerrar", command=root.quit).grid(row=5, column=0, columnspan=2, pady=10)

# Ejecutar interfaz
root.mainloop()
