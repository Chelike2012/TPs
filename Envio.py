class Envio:
    def __init__(self,codigo_postal,direccion,tipo_envio,forma_pago):
        self.codigo_postal = codigo_postal
        self.direccion = direccion
        self.tipo_envio = tipo_envio
        self.forma_pago = forma_pago

    def __str__(self):
        return(f"| {self.codigo_postal:<9} | {self.direccion:<20} | {self.tipo_envio} | {self.forma_pago} |")

