import transp_ortogr_fn

funcion = transp_ortogr_fn

def main():
    texto = funcion.entrada_texto()

    texto_sin_puntuacion = funcion.borra_signos_puntuacion(texto)

    texto_bajo, largo_texto = funcion.minusculador_sin_espacio(texto_sin_puntuacion)

    letra_a, letra_aton, letra_b, letra_ch, letra_c_aou, \
    letra_c_ei, letra_d, letra_e, letra_eton, letra_f, \
    letra_g_aou, letra_g_ei, letra_gu_ei, letra_h, letra_i, \
    letra_iton, letra_j, letra_k, letra_ll, letra_l, letra_m, \
    letra_n, letra_ñ, letra_o, letra_oton, letra_p, letra_q, \
    letra_rr, letra_r, letra_s_aou, letra_s_ei, letra_t, \
    letra_u_q, letra_u, letra_uton, letra_u_crem, letra_v, \
    letra_w, letra_x, letra_y, letra_z = funcion.contador_multiple(texto_bajo)

    contador = funcion.dificultad_de_letras(letra_a, letra_aton, letra_b, letra_ch, letra_c_aou,
                                        letra_c_ei, letra_d, letra_e, letra_eton, letra_f,
                                        letra_g_aou, letra_g_ei, letra_gu_ei, letra_h,
                                        letra_i, letra_iton, letra_j, letra_k, letra_ll,
                                        letra_l, letra_m, letra_n, letra_ñ, letra_o,
                                        letra_oton, letra_p, letra_q, letra_rr, letra_r,
                                        letra_s_aou, letra_s_ei, letra_t, letra_u_q,
                                        letra_u, letra_uton, letra_u_crem, letra_v,
                                        letra_w, letra_x, letra_y, letra_z)

    coeficiente = funcion.calcula_transparencia(contador, largo_texto)

    print(texto)
    print(coeficiente)

    funcion.grafica_coeficiente(coeficiente)

main()