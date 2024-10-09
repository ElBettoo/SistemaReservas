from flask import Flask,redirect,url_for,render_template,request
from capa_negocio.gestion_reserva import GestionReserva
from capa_negocio.date_time import DateTime

app=Flask(__name__)

def crear_sistema():
    sistema = GestionReserva()
    fecha1 = DateTime(2024, 10, 3, 20, 1, 32)
    fecha2 = DateTime(2024, 10, 3, 23, 1, 32)
    sistema.generar_reserva("Sala 1", fecha1, fecha2)
    sistema.generar_reserva("Sala 2", fecha1, fecha2)
    #TODO: Agregar salas y reservas acá
    return sistema

sistema_reservas = crear_sistema()

@app.route('/',methods=['GET'])
def index():
    reservas_data = sistema_reservas.get_reservas()

    reservas_data_traduced = []
    for sala, reservas in reservas_data.items():
        for reserva in reservas:
            reservas_data_traduced.append((sala.nombre, reserva.inicio.expresion, reserva.final.expresion))
    
    return render_template('index.html', reservas_data=reservas_data_traduced)

@app.route('/GenerarReserva', methods=['GET', 'POST'])
def generar_reserva():
    if request.method=='POST':
        sala_nombre = request.form["nombreSala"]
        fecha_inicio, tiempo_inicio = request.form["fechaInicio"].split("T")
        fecha_final, tiempo_final = request.form["fechaFinal"].split("T")

        datetime_inicio = DateTime.string_to_object(fecha_inicio, tiempo_inicio)
        datetime_final = DateTime.string_to_object(fecha_final, tiempo_final)

        sistema_reservas.generar_reserva(sala_nombre, datetime_inicio, datetime_final)
            
        return redirect('/')
    
    salas = [sala.nombre for sala in sistema_reservas.get_salas_disponibles()]
    return render_template('generar_reserva.html', salas=salas)

@app.route('/CancelarReserva/<int:reserva_index>/<string:sala_nombre>', methods=['POST'])
def cancelar_reserva(reserva_index, sala_nombre):
    print(reserva_index, sala_nombre)
    sistema_reservas.cancelar_reserva(sala_nombre, reserva_index)

    return redirect('/')

if __name__ == '__main__':
    app.run(port=5000,debug=True)