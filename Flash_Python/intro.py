from flask import Flask, render_template, request

app = Flask(__name__)
#Agregarun configuración desde archivo Configuracion
app.config.from_object('Configuracion.DevConfig')

@app.route('/') # Creando una rutas con decoradores
def index(): # Creando una vista
 #return '<h1>Hola desde Flask...... </h1>'
  cursos = ['Java', 'Python','Kottlin', 'HTML', 'CSS']
  data = {
   'titulo': 'Página Principlal',
   'saludo': 'Bienvenido',
   'cursos': cursos,
   'numero_cursos': 0#len(cursos)
  }
  return render_template('index.html', data = data, name='Isaakiin')


@app.route('/login')
def login():
  data = {
   'titulo': 'Login de Usario',
   'email': 'itj.18478@gmail.com',
   'password': '1234'

  }

  return render_template('login.html', data=data)


#Rutas Dinámicas
@app.route('/contacto/<nombre>/<int:edad>') #recibe por parametro un string
def contacto(nombre, edad):
    data = {
     'titulo': contacto,
     'nombre': nombre,
     'edad': edad
    }
    return render_template('contacto.html', data=data)
    #return f'<h1>Nombre de contacto: {data["nombre"]}</h1>'

def query_string():
    print(request)
    print(request.args)
    print("Edad: ",request.args.get('nombre'))
    print("edad: ",request.args.get('edad'))
    print("sexo: ",request.args.get('sexo'))
    return 'OK'

if __name__ == '__main__':
 # Agregar una ruta
 app.add_url_rule('/query_string', view_func=query_string)
 app.run()

