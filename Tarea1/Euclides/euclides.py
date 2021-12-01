#!/usr/bin/env python
# coding: utf-8

# # Tareas de SPSI
# 
# > Grupo 22
# >
# > Ana Buendía Ruiz-Azuaga
# >
# > Paula Villanueva Núñez

# ## Tarea 1
# **Algoritmo extendedido de Euclides**

# In[1]:


# not(m & 1) = ~m&1 -> Comprueba si el número es par. Devuelve true si es par

def bxeuc(m,n):
    '''
    Algoritmo extendido de euclides.
    Parametros: m,n dos enteros
    Devuelve: mcd y los coeficientes de Bezout
    '''
    shift = 0
    
    if m == 0:
        return n, 0, 1
    if n == 0:
        return m, 1, 0
    
    # Gestionamos numeros negativos
    signo_m = 1
    signo_n = 1
    
    if m < 0:
        m = -m
        signo_m = -1
    if n < 0:
        n = -n
        signo_n = -1
    
    
    while ~m&1 and ~n&1:
        m >>= 1
        n >>= 1
        
        shift += 1 
        
    # m0 y n0 son m y n quitando el factor comun 2, por ejemplo 4,2 pasa a 2,1
    m0 = m
    n0 = n
    
    sm = 1
    sn = 0
    
    tm = 0
    tn = 1
    
    # Se mantienen invariantes m = sm*m+sn*n, n=tm*m+tn*n
    
    
    while ~m&1: # Si m es par
        if not (~sm&1 and ~sn&1 ): # Si sm o sn alguno no es par
            # garantizamos que sm y sn sean pares
            sm = sm - n0
            sn = sn + m0
            
        # Quitamos el factor comun 2 de m, sm y sn, luego la identidad m = sm*m+sn*n se mantiene
        m >>= 1
        sm >>= 1
        sn >>= 1
    
    while n != 0:
        while ~n&1: # SI n par
            if not (~tm&1 and ~tn&1): # Si tm o tn alguno no es par
                # Aseguramos que tm y tn son pares
                tm = tm - n0
                tn = tn + m0
                
            # Eliminamos el factor comun 2 de n, tm y tn, luego la identidad n=tm*m+tn*n se mantiene
            n >>= 1
            tm >>= 1
            tn >>= 1
        
        # Si m>n intercambiamos las variables
        if m > n: 
            m, n, sm, tm, sn, tn = n, m, tm, sm, tn, sn
            
        
        # Vamos quitando tantas veces m a n
        n = n - m
        tm = tm - sm
        tn = tn - sn
        
    g = m << shift
    u = signo_m*sm
    v = signo_n*sn

    return g, u, v
    
    


# In[2]:


m = 693
n = 609

g, u, v = bxeuc(m, n)

print("Máximo común divisor obtenido por el algoritmo: {}".format(g))
print("Resultado de la identidad usando los coeficientes {}".format(u*m+v*n))

print(g == u*m+v*n)

