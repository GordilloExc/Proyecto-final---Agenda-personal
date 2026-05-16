class Evento:
    def __init__(self, id, titulo, fecha, descripcion):
        self.__id = id
        self.__titulo = titulo
        self.__fecha = fecha
        self.__descripcion = descripcion

    # Getters
    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_fecha(self):
        return self.__fecha

    def get_descripcion(self):
        return self.__descripcion

    # Setters
    def set_titulo(self, titulo):
        if len(titulo) > 0:
            self.__titulo = titulo

    def set_descripcion(self, descripcion):
        if len(descripcion) > 0:
            self.__descripcion = descripcion

    # Método que cada subclase va a personalizar
    def tipo(self):
        return "Evento"

    def to_dict(self):
        return {
            "id": self.__id,
            "titulo": self.__titulo,
            "fecha": self.__fecha,
            "descripcion": self.__descripcion,
            "tipo": self.tipo()
        }

class Cita(Evento):
    def __init__(self, id, titulo, fecha, descripcion, lugar, doctor):
        super().__init__(id, titulo, fecha, descripcion)
        self.__lugar = lugar
        self.__doctor = doctor

    def get_lugar(self):
        return self.__lugar

    def get_doctor(self):
        return self.__doctor

    def tipo(self):
        return "Cita"

    def to_dict(self):
        datos = super().to_dict()
        datos["lugar"] = self.__lugar
        datos["doctor"] = self.__doctor
        return datos


class Reunion(Evento):
    def __init__(self, id, titulo, fecha, descripcion, participantes):
        super().__init__(id, titulo, fecha, descripcion)
        self.__participantes = participantes

    def get_participantes(self):
        return self.__participantes

    def tipo(self):
        return "Reunion"

    def to_dict(self):
        datos = super().to_dict()
        datos["participantes"] = self.__participantes
        return datos


class Recordatorio(Evento):
    def __init__(self, id, titulo, fecha, descripcion, persona):
        super().__init__(id, titulo, fecha, descripcion)
        self.__persona = persona

    def get_persona(self):
        return self.__persona

    def tipo(self):
        return "Recordatorio"

    def to_dict(self):
        datos = super().to_dict()
        datos["persona"] = self.__persona
        return datos

class Agenda:
    def __init__(self):
        self.__eventos = []
        self.__contador = 1

    def agregar_evento(self, evento):
        self.__eventos.append(evento)
        self.__contador += 1

    def get_eventos(self):
        return self.__eventos

    def get_siguiente_id(self):
        return self.__contador

    def eliminar_evento(self, id):
        self.__eventos = [e for e in self.__eventos if e.get_id() != id]

    def buscar_evento(self, id):
        for evento in self.__eventos:
            if evento.get_id() == id:
                return evento
        return None