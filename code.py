from locate_pixelcolor_cpppragma import search_colors
import numpy as np
from fast_ctypes_screenshots import (
    ScreenshotOfOneMonitor,
)
from mousekey import MouseKey
mkey = MouseKey()
mkey.enable_failsafekill('ctrl+e')

verde = 42, 127, 25
azul_claro = 44, 156, 251
azul_escuro = 34, 62, 141
cpus = 4
altura_min = 500
altura_max = 700
largura_min = 850
largura_max = 1000
r_verde = np.array([list(reversed(verde))], dtype=np.uint8)
r_azul_claro = np.array([list(reversed(azul_claro))], dtype=np.uint8)
r_azul_escuro = np.array([list(reversed(azul_escuro))], dtype=np.uint8)
co = 0
with ScreenshotOfOneMonitor(
        monitor=0, ascontiguousarray=False
) as screenshots_monitor:
    while True:
        co+=1
        print(co, end='\r')

        pic = screenshots_monitor.screenshot_one_monitor()

        resultado_verde = search_colors(pic=pic, colors=r_verde, cpus=cpus)
        resultado_azul_claro = search_colors(pic=pic, colors=r_azul_claro, cpus=cpus)
        resultado_azul_escuro = search_colors(pic=pic, colors=r_azul_escuro, cpus=cpus)
        resultado_verde_filtro = resultado_verde[((resultado_verde[..., 1] > largura_min)
                                                  & (resultado_verde[..., 1] < largura_max)) & (
                                                             (resultado_verde[..., 0] > altura_min)
                                                             & (resultado_verde[..., 0] < altura_max))]
        resultado_azul_claro_filtro = resultado_azul_claro[((resultado_azul_claro[..., 1] > largura_min)
                                                  & (resultado_azul_claro[..., 1] < largura_max)) & (
                                                             (resultado_azul_claro[..., 0] > altura_min)
                                                             & (resultado_azul_claro[..., 0] < altura_max))]
        resultado_azul_escuro_filtro = resultado_azul_escuro[((resultado_azul_escuro[..., 1] > largura_min)
                                                  & (resultado_azul_escuro[..., 1] < largura_max)) & (
                                                             (resultado_azul_escuro[..., 0] > altura_min)
                                                             & (resultado_azul_escuro[..., 0] < altura_max))]
        if np.any(resultado_azul_claro_filtro) and np.any(resultado_azul_escuro_filtro) and np.any(resultado_verde_filtro):
            x,y=int(np.mean(resultado_verde_filtro[...,1])),int(np.mean(resultado_verde_filtro[...,0]))
            mkey.left_click_xy(x, y)

#cv2.imwrite('c:\\resultadoimagen.png', pic)
