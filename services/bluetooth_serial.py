"""
Comunicacion serial / Bluetooth con el ATmega32 (HC-05).

Pensado para usarse desde la app de Flet. Mantiene UNA sola conexion
abierta (singleton) para toda la app, en vez de abrir el puerto cada vez.

Uso tipico desde una vista:

    from services import bluetooth_serial as bt

    bt.conectar()                 # abre el puerto (una vez)
    bt.enviar_indice(5)           # manda el byte 0x05 al micro
    bt.iniciar_lectura(print)     # opcional: recibe respuestas del micro
    ...
    bt.desconectar()              # al cerrar la app
"""

import threading
import serial
import serial.tools.list_ports

# Configuracion por defecto. COM3 es donde SI llegan los datos del micro.
PUERTO_DEFAULT = "COM3"
BAUDRATE = 9600

# Estado interno del modulo (la conexion viva).
_ser: serial.Serial | None = None
_hilo_lectura: threading.Thread | None = None
_leyendo = False


# Mapeo EXPLICITO letra -> indice que espera el ATmega32.
# Tomado de assets/Documentacion/PatronLetras.txt.
# Si tu firmware usa otro orden o tiene saltos, edita SOLO este diccionario.
LETRA_A_INDICE = {
    "A": 0,  "B": 1,  "C": 2,  "D": 3,  "E": 4,  "F": 5,  "G": 6,
    "H": 7,  "I": 8,  "J": 9,  "K": 10, "L": 11, "M": 12, "N": 13,
    "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20,
    "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25,
}


def enviar_letra(letra: str) -> bool:
    """
    Manda una LETRA al guante buscando su indice en LETRA_A_INDICE.
    Pensada para usarse desde cualquier view: bt.enviar_letra("C").
    Devuelve True si se envio bien, False si la letra no existe o falla.
    """
    indice = LETRA_A_INDICE.get(letra.upper())
    if indice is None:
        print(f"[bluetooth] Letra no reconocida: {letra!r}")
        return False
    return enviar_indice(indice)


def encontrar_puerto() -> str | None:
    """Busca un puerto que parezca ser el HC-05 / adaptador BT."""
    for p in serial.tools.list_ports.comports():
        texto = (p.device + " " + p.description).lower()
        if any(k in texto for k in ("bluetooth", "hc-05", "hc05", "ch340")):
            return p.device
    return None


def esta_conectado() -> bool:
    return _ser is not None and _ser.is_open


def conectar(puerto: str = PUERTO_DEFAULT) -> bool:
    """
    Abre el puerto serial. Devuelve True si quedo conectado.
    Si ya estaba conectado, no hace nada y devuelve True.

    write_timeout=2  -> si la escritura se bloquea (puerto equivocado,
                        link caido) lanza SerialTimeoutException en vez
                        de colgarse para siempre.
    timeout=1        -> readline() no se queda atorado indefinidamente.
    """
    global _ser
    if esta_conectado():
        return True
    try:
        _ser = serial.Serial(puerto, BAUDRATE, timeout=1, write_timeout=2)
        return True
    except Exception as e:
        _ser = None
        print(f"[bluetooth] No se pudo abrir {puerto}: {e}")
        return False


def enviar_indice(indice: int) -> bool:
    """
    Manda el byte crudo (ej. 0x05, NO el ASCII '5') al micro.
    Devuelve True si se envio bien.
    """
    if not esta_conectado():
        print("[bluetooth] No conectado: llama conectar() primero")
        return False
    if not (0 <= indice <= 25):
        print(f"[bluetooth] Indice fuera de rango (0-25): {indice}")
        return False
    try:
        _ser.write(bytes([indice]))
        _ser.flush()  # fuerza la salida inmediata del byte
        return True
    except serial.SerialTimeoutException:
        print("[bluetooth] Escritura bloqueada (puerto BT equivocado o enlace caido)")
        return False
    except Exception as e:
        print(f"[bluetooth] Error al enviar: {e}")
        return False


def iniciar_lectura(on_dato) -> None:
    """
    Arranca un hilo que escucha respuestas del micro.
    'on_dato' es una funcion que recibe el texto recibido (str).
    Opcional: solo si te interesa la respuesta de vuelta.
    """
    global _hilo_lectura, _leyendo
    if _leyendo or not esta_conectado():
        return
    _leyendo = True

    def _loop():
        while _leyendo and esta_conectado():
            try:
                dato = _ser.readline().decode(errors="ignore").strip()
                if dato:
                    on_dato(dato)
            except Exception as e:
                print(f"[bluetooth] Error de lectura: {e}")
                break

    _hilo_lectura = threading.Thread(target=_loop, daemon=True)
    _hilo_lectura.start()


def desconectar() -> None:
    """Cierra el puerto y detiene la lectura. Llamar al cerrar la app."""
    global _ser, _leyendo
    _leyendo = False
    if _ser is not None:
        try:
            _ser.close()
        except Exception:
            pass
    _ser = None
