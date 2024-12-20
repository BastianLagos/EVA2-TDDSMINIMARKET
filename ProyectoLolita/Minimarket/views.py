from django.shortcuts import render
from Minimarket.models import Producto
from Minimarket.models import Compra
from Minimarket.models import Cliente
from django.db.models import Q

#---- PRODUCTO - ADMIN---
def mostrarRegistrarPro(request):
    estadoSesion = request.session.get("estadoSesion")
    emaUsuario = request.session.get("emaUsuario")

    if estadoSesion is True:
        if emaUsuario.upper() == "ADMIN@INACAPMAIL.CL":
            return render(request, 'registrar_pro.html')
        else:
            datos = { 'r2' : 'No Tiene Permisos Suficientes Para Acceder!!' }
            return render(request, 'login.html',datos)
    else:
        datos = { 'r2' : 'Debe Iniciar Sesión Para Acceder!!' }
        return render(request, 'login.html',datos)

def mostrarListadoPro(request):
    estadoSesion = request.session.get("estadoSesion")
    emaUsuario = request.session.get("emaUsuario")

    if estadoSesion is True:
        if emaUsuario.upper() == "ADMIN@INACAPMAIL.CL":
            pro = Producto.objects.all().values()
            datos = {'pro':pro}
            return render(request,"listar_pro.html", datos)
        else:
            datos = { 'r2' : 'No Tiene Permisos Suficientes Para Acceder!!' }
            return render(request, 'login.html',datos)
    else:
        datos = { 'r2' : 'Debe Iniciar Sesión Para Acceder!!' }
        return render(request, 'login.html',datos)
    

def registrarPro(request):
    try:
        if request.method == "POST":
            cod = request.POST['txtcod']
            nom = request.POST['txtnom']
            tip = request.POST['txttip']
            pre = request.POST['txtpre']
            can = request.POST['txtcan']

            try:
                ima = request.FILES['txtfot']
            except:
                ima = "imagenes_bd/noimagen.jpg"
        
            pro = Producto(codigo = cod, nombre = nom, tipo = tip, precio = pre, cantidad = can, imagen = ima)
            pro.save()
            datos = {'r':'Porducto Correctamente Registrado!'}
            return render(request, 'registrar_pro.html', datos)

        else:
            datos = {'r2':'No Se Pudo Registrar el Producto!'}
            return render(request, 'registrar_pro.html', datos)
    except:
        pro = Producto.objects.all().values()
        datos = {'pro' : pro, 'r2':'No se Pudo Registrar el Producto. Puede Que el Codigo ya Exista en la Base de Datos, Intente con Otro!'}
        return render(request, "registrar_pro.html", datos)

def eliminarPro(request, id):
    try:
        pro = Producto.objects.get(id = id)
        codpro = pro.codigo
        nompro = pro.nombre
        tippro = pro.tipo
        prepro = pro.precio
        canpro = pro.cantidad
        ruta_foto = "media/"+str(pro.imagen)
        pro.delete()

        import os 
        if ruta_foto != "media/imagenes_bd/noimagen.jpg":
            os.remove(ruta_foto)

        pro = Producto.objects.all().values()
        datos = {'pro' : pro, 'r':'Producto Eliminado Correctamente!'}
        return render(request, "listar_pro.html", datos)

    except:
        pro = Producto.objects.all().values()
        datos = {'pro':pro, 'r2':'El Producto No Existe, Imposible Eliminar!'}
        return render(request, "listar_pro.html",datos)



def mostrarActualizarPro(request, id):
    estadoSesion = request.session.get("estadoSesion")
    emaUsuario = request.session.get("emaUsuario")

    if estadoSesion is True:
        if emaUsuario.upper() == "ADMIN@INACAPMAIL.CL":
                try:
                    pro = Producto.objects.get(id=id)
                    datos = {'pro': pro}
                    return render(request,'actualizar_pro.html',datos)
                except:
                    pro = Producto.objects.all().values()
                    datos = {'pro':pro, 'r2':"El Producto con ID ("+str(id)+") No Existe, Imposible Actualizar!"    }
                    return render(request,'listar_pro.html',datos)
        else:
            datos = { 'r2' : 'No Tiene Permisos Suficientes Para Acceder!!' }
            return render(request, 'login.html',datos)
    else:
        datos = { 'r2' : 'Debe Iniciar Sesión Para Acceder!!' }
        return render(request, 'login.html',datos)

def actualizarPro(request, id):
    try:
        cod = request.POST['txtcod']
        nom = request.POST['txtnom']
        tip = request.POST['txttip']
        pre = request.POST['txtpre']
        can = request.POST['txtcan']

        pro = Producto.objects.get(id=id)

        try:
            ima = request.FILES['txtfot']
            ruta_foto = "media/"+str(pro.imagen)
            import os
            if ruta_foto != "media/imagenes_bd/noimagen.jpg":
                os.remove(ruta_foto)
        except:
            ima = pro.imagen
        
        pro.codigo = cod
        pro.nombre = nom
        pro.tipo = tip
        pro.precio = pre
        pro.cantidad = can
        pro.imagen = ima
        pro.save()

        pro = Producto.objects.all().values()
        datos = {'pro':pro, 'r':'Producto Actualizado Correctamente!'}
        return render(request, 'listar_pro.html', datos)

    except:
        pro = Producto.objects.all().values()
        datos = {'pro':pro, 'r2':'El codigo del Producto ya Existe, No Se Pudo Actualizar!'}
        return render(request, 'listar_pro.html', datos)

#---- PRODUCTO- ADMIN/ ----

def agregarPro(request, id):
    try:
        pro = Producto.objects.get(id=id)
        cod = pro.codigo
        nom = pro.nombre
        pre = pro.precio

        com = Compra(codigo = cod, nombre = nom, precio = pre)
        com.save()
        com = Compra.objects.all().values()
        datos = {'com':com,'r':'Producto Agregado Correctamente al Carro de Compras!'}
        return render(request, 'listado.html', datos)

    except:
        pro = Producto.objects.all().values()
        datos = {'pro':pro, 'r2':'No se ha Añadido el Producto al Carrito de Compras!'}
        return render(request, 'catalogo.html', datos)
    
def eliminarProAgre(request, id):
    try:
        com = Compra.objects.get(id = id)
        codcom = com.codigo
        nomcom = com.nombre
        precom = com.precio
        com.delete()

        com = Compra.objects.all().values()
        datos = {'com' : com, 'r':'Producto Eliminado Correctamente del Carro de Compras!'}
        return render(request, "listado.html", datos)

    except:
        com = Compra.objects.all().values()
        datos = {'com':com, 'r2':'El Producto No Existe, Imposible Eliminar!'}
        return render(request, "listado.html",datos)

def mostrarCatalogo(request):
    estadoSesion = request.session.get("estadoSesion")
    emaUsuario = request.session.get("emaUsuario")

    if estadoSesion is True:
        if emaUsuario.upper():
            pro = Producto.objects.all().values()
            datos = {'pro':pro}
            return render(request,"catalogo.html",datos)
        else:
            datos = { 'r2' : 'No Tiene Permisos Suficientes Para Acceder!!' }
            return render(request, 'login.html',datos)

    else:
        datos = { 'r2' : 'Debe Iniciar Sesión Para Acceder!!' }
        return render(request, 'login.html',datos)


def mostrarListado(request):
    estadoSesion = request.session.get("estadoSesion")
    emaUsuario = request.session.get("emaUsuario")

    if estadoSesion is True:
        com = Compra.objects.all().values()
        datos = {'com':com}
        return render(request,"listado.html", datos)

    else:
        datos = { 'r2' : 'Debe Iniciar Sesión Para Acceder!!' }
        return render(request, 'login.html',datos)

#---------REGISTRAR CLIENTE----------------

def mostrarFormulario(request):
    return render(request,"form.html")

def registrarCliente(request):
    try:
        if request.method == "POST":
            nom = request.POST['txtnom']
            rut = request.POST['txtrut']
            ema = request.POST['txtema']
            dir = request.POST['txtdir']
            con1 = request.POST['txtcon1']
            con2 = request.POST['txtcon2']

            if con1==con2:
                cli = Cliente(nombre = nom, rut = rut,correo=ema,direccion=dir,contraseña1=con1,contraseña2=con2)
                cli.save()
                datos = {'r':'Usuario Registrado con Éxito!'}
                return render(request, 'login.html', datos)

            else:
                datos = {'r2':'No se Pudo Registrar el Usuario, Puede que Las Contraseñas no Coincidan!'}
                return render(request, 'form.html', datos)
    except:
        datos = {'r2':'No se Pudo Registrar El Usuario! Puede que el RUT Ya Exista'}
        return render(request, "form.html", datos)

#------------INICIAR SESION-------------------
def mostrarLogin(request):
    return render(request,"login.html")

def iniciarSesion(request):
    if request.method == "POST":
        ema = request.POST["txtema"]
        pas = request.POST["txtpas"]

        comprobarLogin = Cliente.objects.filter(correo =ema, contraseña1=pas).values()

        if comprobarLogin:
            request.session["estadoSesion"] = True
            request.session["idUsuario"] = comprobarLogin[0]['id']
            request.session["emaUsuario"] = ema.upper()

            datos = { 'emaUsuario' : ema.upper() }


            if ema.upper() == "ADMIN@INACAPMAIL.CL":
                return render(request, 'registrar_pro.html', datos)
            else:
                pro = Producto.objects.all().values()
                datos={'pro':pro}
                return render(request, 'catalogo.html', datos)
        
        else:
            datos = { 'r2' : 'Error De Usuario y/o Contraseña!!' }
            return render(request, 'login.html', datos)
    else:
        datos = { 'r2' : 'No Se Puede Procesar La Solicitud!!' }
        return render(request, 'login.html', datos)

def cerrarSesion(request):
    try:
        del request.session["estadoSesion"]
        del request.session["idUsuario"]
        del request.session["emaUsuario"]

        return render(request, 'login.html')
    except:
        return render(request, 'login.html')

#-------------BARRA DE BUSQUEDA--------------

def mostrarBusqueda(request):
    estadoSesion = request.session.get("estadoSesion")
    emaUsuario = request.session.get("emaUsuario")

    if estadoSesion is True:
        try:
            bus= request.POST['buspro']
            pro = Producto.objects.all().values()

            if bus:
                pro = Producto.objects.filter(
                    Q(id__icontains = bus) |
                    Q(codigo__icontains = bus) |
                    Q(nombre__icontains = bus) |
                    Q(tipo__icontains = bus)
                ).distinct()

            datos = {'pro': pro}
            return render(request,'buscar.html',datos)
        except:
            pro = Producto.objects.all().values()
            datos = {'pro':pro, 'r2':"El Producto No Existe!!"    }
            return render(request,'catalogo.html',datos)

    else:
        datos = { 'r2' : 'Debe Iniciar Sesión Para Acceder!!' }
        return render(request, 'login.html',datos)

 
def mostrarBuscar(request):
    estadoSesion = request.session.get("estadoSesion")
    emaUsuario = request.session.get("emaUsuario")

    if estadoSesion is True:
        return render(request,"buscar.html")

    else:
        datos = { 'r2' : 'Debe Iniciar Sesión Para Acceder!!' }
        return render(request, 'login.html',datos)