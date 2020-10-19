#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ivan Vladimir Meza Ruiz 2018
# GPL 3.0

import random

def random_planta(malestar,nombre_slot,db):
    """ Dado un malestar regrasa una planta aleatoria """
    opciones=[]
    basededatos=db['plantas']
    for fila in basededatos:
        if fila[0] == malestar:
            opciones.append(fila[1])
    msg = random.choice(opciones)
    return 'set_slot {0} "{1}"'.format(nombre_slot,msg)

