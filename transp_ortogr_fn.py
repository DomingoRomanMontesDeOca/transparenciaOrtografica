import matplotlib.pyplot as plt
import numpy as np


# INTRO: Índice de transparencia ortográfica
# Índice de transparencia ortográfica
# Este programa entrega un número relacionado con la transparencia ortográfica
# cuando el texto es totalmente transparente, el número es bajo
# mientras más alto es el número, menos tranparente es; en otras palabras
# es una manera de cuantificar la posible dificultad ortográfica
# Está pensado originalmente para evaluar textos destinados al
# aprendizaje de la lectura en español, tanto de niños como adultos.
# El número entregado es un coeficiente de transparencia.
# Cuando es 1.0, el texto es totalmente transparente;
# o sea, no tiene dificultad ortográfica.
# En la medida en que aumenta la dificultad (opacidad ortográfica o falta de transparencia)
# el número empieza a ser inferior a 1.
# Las interpretaciones entre paréntesis son referenciales, e impresionistas
# Mi pata patea   = 1.000 (No tiene dificultad)
# Tu pato te toca = 0.8 (Tiene dificultad, leve)
# Su zapato choca = 0.591 (tiene alta dificultad)
# Cesa la lluvia  = 0.522 (Dificultad alta)
# El programa se puede probar con pseudopalabras
# Tu pima te tofa= 1 1
# Solo mide la transparencia u opacidad ortográfica; no está asociado
# a cuestiones de frecuencia léxica, morfológicas, longitud de palabra, etc.
# al menos en esta versión inicial

def borra_signos_puntuacion(texto):
    """En esta función se borran los signos de puntuación
    """
    texto1 = texto.replace(".", "")
    texto2 = texto1.replace(",", "")
    texto3 = texto2.replace(";", "")
    texto4 = texto3.replace("¿", "")
    texto5 = texto4.replace("?", "")
    texto6 = texto5.replace("¡", "")
    texto7 = texto6.replace("!", "")
    texto8 = texto7.replace("(", "")
    texto9 = texto8.replace(")", "")
    texto10 = texto9.replace("-", "")
    texto11 = texto10.replace("—", "")
    texto12 = texto11.replace(":", "")
    texto_sin_puntuacion = texto12.replace('"', "")
    return texto_sin_puntuacion

def minusculador_sin_espacio(texto_sin_puntuacion):
    """minusculador convierte el texto a letras minúsculas.
    Cuenta los espacios en blanco
    cuenta el número caracteres y resta los espacios en blanco
    """
    #   baja a minúscula
    texto_bajo = texto_sin_puntuacion.lower()
    #   cuenta espacios
    espacios = texto_bajo.count(" ")
#   Longitud de cadena en letras
    largo_texto = len(texto_bajo) - espacios
    return(texto_bajo,largo_texto)

def contador_multiple(texto):
    """ Contador múltiple cuenta las ocurrencias de
    cada letra, en algunos casos, categorizada combinatoriamente
    """
    letra_a = texto.count("a")
    letra_aton = texto.count("á")
    letra_b = texto.count("b")
    letra_ch = texto.count("ch")
    letra_c_aou = texto.count("ca") + texto.count("cá") \
                  + texto.count("co") + texto.count("có") \
                  + texto.count("cu") + texto.count("cú")
    letra_c_ei = texto.count("ce") + texto.count("cé") \
                 + texto.count("ci") + texto.count("cí")
    letra_d = texto.count("d")
    letra_e = texto.count("e")
    letra_eton = texto.count("é")
    letra_f = texto.count("f")
    letra_g_aou = texto.count("ga") + texto.count("gá") \
                 + texto.count("go") + texto.count("gó")
    letra_g_ei = texto.count("ge") + texto.count("gé") \
                 + texto.count("gi") + texto.count("gí")
    letra_gu_ei = texto.count("gue") + texto.count("gué") \
                  + texto.count("gui") + texto.count("guí")
    letra_h = texto.count("h")-letra_ch
    letra_i = texto.count("i")
    letra_iton = texto.count("í")
    letra_j = texto.count("j")
    letra_k = texto.count("k")
    letra_ll = texto.count("ll")
    letra_l = texto.count("l") - (letra_ll*2)
    letra_m = texto.count("m")
    letra_n = texto.count("n")
    letra_ñ = texto.count("ñ")
    letra_o = texto.count("o")
    letra_oton = texto.count("ó")
    letra_p = texto.count("p")
    letra_q = texto.count("q")
    letra_rr = texto.count("rr")
    letra_r = texto.count("r") - letra_rr
    letra_s_aou = texto.count("sa") + texto.count("sá") \
                  + texto.count("so") + texto.count("só") \
                  + texto.count("su") + texto.count("sú")
    letra_s_ei = texto.count("se") + texto.count("sé") \
                 + texto.count("si") + texto.count("sí")
    letra_t = texto.count("t")
    letra_u_q = texto.count("qu")
    letra_u = texto.count("u")-letra_u_q
    letra_uton = texto.count("ú")
    letra_u_crem = texto.count("ü")
    letra_v = texto.count("v")
    letra_w = texto.count("w")
    letra_x = texto.count("x")
    letra_y = texto.count("y")
    letra_z = texto.count("z")

    return letra_a, letra_aton, letra_b, letra_ch, \
           letra_c_aou, letra_c_ei, letra_d, letra_e, \
           letra_eton, letra_f, letra_g_aou, letra_g_ei, \
           letra_gu_ei, letra_h, letra_i, letra_iton, \
           letra_j, letra_k, letra_ll, letra_l, letra_m, \
           letra_n, letra_ñ, letra_o, letra_oton, letra_p, \
           letra_q, letra_rr, letra_r, letra_s_aou, \
           letra_s_ei, letra_t, letra_u_q, letra_u, letra_uton, \
           letra_u_crem, letra_v, letra_w, letra_x, letra_y, letra_z

def dificultad_de_letras(letra_a, letra_aton, letra_b, letra_ch,
                         letra_c_aou, letra_c_ei, letra_d, letra_e,
                         letra_eton, letra_f, letra_g_aou, letra_g_ei,
                         letra_gu_ei, letra_h, letra_i, letra_iton,
                         letra_j, letra_k, letra_ll, letra_l, letra_m,
                         letra_n, letra_ñ, letra_o, letra_oton, letra_p,
                         letra_q, letra_rr, letra_r, letra_s_aou,
                         letra_s_ei, letra_t, letra_u_q, letra_u,
                         letra_uton, letra_u_crem, letra_v, letra_w,
                         letra_x, letra_y, letra_z):
    """ Esta función multiplica el grado de dificultad de cada letra,
        (en algunos casos, tomando en cuenta la combinatoria)
        por el número de ocurrencias
    """
    contador = 0
    if letra_a >= 1:
        contador = contador + letra_a
    if letra_aton >= 1:
        contador = contador + (letra_aton*2)
    if letra_b >= 1:
        contador = contador + (letra_b * 3)
    if letra_c_aou >= 1:
        contador = contador + (letra_c_aou * 4)
    if letra_c_ei >= 1:
        contador = contador + (letra_c_ei * 5)
    if letra_ch >= 1:
        contador = contador + (letra_ch * 2)
    if letra_d >= 1:
        contador = contador + letra_d
    if letra_e >= 1:
        contador = contador + letra_e
    if letra_eton >= 1:
        contador = contador + (letra_eton * 2)
    if letra_f >= 1:
        contador = contador + letra_f
    if letra_g_aou >= 1:
        contador = contador + (letra_g_aou * 2)
    if letra_g_ei >= 1:
        contador = contador + (letra_g_ei * 4)
    if letra_h >= 1:
        contador = contador + (letra_h * 3)
    if letra_i >= 1:
        contador = contador + letra_i
    if letra_iton >= 1:
        contador = contador + (letra_iton * 2)
    if letra_j >= 1:
        contador = contador + (letra_j * 3)
    if letra_k >= 1:
        contador = contador + (letra_k * 3)
    if letra_ll >= 1:
        contador = contador + (letra_ll * 3)
    if letra_l >= 1:
        contador = contador + (letra_l * 2)
    if letra_m >= 1:
        contador = contador + letra_m
    if letra_n >= 1:
        contador = contador + letra_n
    if letra_ñ >= 1:
        contador = contador + letra_ñ
    if letra_o >= 1:
        contador = contador + letra_o
    if letra_oton >= 1:
        contador = contador + (letra_oton * 2)
    if letra_p >= 1:
        contador = contador + letra_p
    if letra_q >= 1:
        contador = contador + (letra_q * 4)
    if letra_rr >= 1:
        contador = contador + (letra_rr * 3)
    if letra_r >= 1:
        contador = contador + (letra_r * 3)
    if letra_s_aou >= 1:
        contador = contador + (letra_s_aou * 4)
    if letra_s_ei >= 1:
        contador = contador + (letra_s_ei * 4)
    if letra_t >= 1:
        contador = contador + letra_t
    if letra_u_q >= 1:
        contador = contador + (letra_u_q * 2)
    if letra_uton >= 1:
        contador = contador + (letra_uton * 2)
    if letra_u >= 1:
        contador = contador + letra_u
    if letra_u_crem >= 1:
        contador = contador * (letra_u_crem * 3)
    if letra_v >= 1:
        contador = contador + (letra_v * 3)
    if letra_w >= 1:
        contador = contador + (letra_w * 4)
    if letra_x >= 1:
        contador = contador + (letra_x * 5)
    if letra_y >= 1:
        contador = contador + (letra_y * 3)
    if letra_z >= 1:
        contador = contador + (letra_z * 4)
    return contador

def calcula_transparencia(contador,largo_texto):
    """ Esta función hace los cálculos para obtener el índice
    de transparencia/opacidad ortográfica
    """
#    intro = round(contador/largo_texto, 3)
    coeficiente = round(largo_texto/contador, 3)
#    return intro, intro_inv
    return coeficiente

def entrada_texto():
    """Se despeja la función para la entrada del texto
    que será analizado
    """
    texto = input("Texto: ")
    return texto

def grafica_coeficiente (coeficiente):
    plt.ylim(-5, 5)
    plt.xlim(0,1)
    plt.plot([0, 5], [0, 0], color="green")
    plt.plot([coeficiente, coeficiente], [-0.5, 0.5], color="red")
    plt.grid()
    plt.show()