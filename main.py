import os
os.system("clear")

from PIL import ImageTk
import PIL.Image

from tkinter import *
         
def main():
    
    
    
    
                global ventana
                ventana = Tk()

                
                ventana.geometry("1100x780")
                ventana.title("Plazo Fijo Banco V.S compra/ahorro/venta futuro de Dólar:")
  
                
                 #-----------------------------WIDGETS GENERALES---------------------------------------------------------------------
 
                titulo_porcentaje = Message(text=r"% interes anual:",anchor=W,aspect=1000)
                titulo_porcentaje.place(x=42,y=130,width=100)
                #----------------------------- 
                global porcentaje_entry
                porcentaje_entry_variable = StringVar()
                
                porcentaje_entry = Entry(textvariable=porcentaje_entry_variable)
                porcentaje_entry_variable.trace_add('write',escuchador_entry_calculo)
                porcentaje_entry.insert(0,float(110.931517))
                porcentaje_entry.place(x=40,y=150,width=100,height=40)
                   
                #-----------------------------                              
                global titulo_entry
                titulo_entry = Message(text="Inversion inicial en pesos:",anchor=W,aspect=1000)
                titulo_entry.place(x=152,y=130,width=200)           
                global entry_calculo
                entry_calculo_variable = StringVar()
                entry_calculo = Entry(textvariable= entry_calculo_variable)
                entry_calculo_variable.trace_add('write',escuchador_entry_calculo)
                entry_calculo.place(x=157,y=150,width=250,height=40)
 
                #----------------------------- 
                
                global opcion
                opcion = IntVar()
                global meses_entry
                global titulo_meses
                global meses_entry_variable
                meses_entry_variable = StringVar()
                
                global opcion_dolar
                opcion_dolar = IntVar()
                #----------------------------- 
                titulo_meses = Message(text="Meses:",aspect=1000)
                titulo_meses.place(x=420,y=130,width=60)
                
                #----------------------------- 
                meses_entry = Entry(textvariable=meses_entry_variable)
                meses_entry_variable.trace_add('write',escuchador_entry_calculo)
                meses_entry.place(x=425,y=150,width=55,height=40)
                
#------------SELECCION DE TIPO DE CALCULO SI POR MONTO DE INVERSION O POR MONTO DE GANANCIA ESPERADA:                
       
 #RADIOBUTONS DE SELECCION DE O POR INVERSION O POR GANANCIA:
                
                opcion_inversion = Radiobutton(ventana, 
                                               text="Calculo por Monto de inversion",
                                               variable=opcion,
                                               value=1,
                                               command=seleccionar_con_o_sin_meses)
                opcion_inversion.place(x=30,y=30)
                opcion_inversion.select()
                
                opcion_ganancia = Radiobutton(ventana,
                                              text="Calculo por ganancia esperada",
                                              variable=opcion,
                                              value=2,
                                              command=seleccionar_con_o_sin_meses)
                
                opcion_ganancia.place(x=30,y=50)

                btn_calcular = Button(text = "calcular",command=calcular)
                btn_calcular.place(x=40,y=80, width=1015,height=40)

                btn_quit = Button(text = "Salir", command = quit_program)
                btn_quit.place(x=488,y=702, width=120,height=40)
                
                
               
                #------------FRAME PESOS DATOS OUTPUT---------------------------------------------
                
                global frame_pesos
                frame_pesos = LabelFrame(ventana, text="Datos")
                frame_pesos.place(x=40,y=220,width=500,height=260)
                frame_pesos["bg"]="white"

                global mensaje_pesos
                mensaje_pesos= Text(frame_pesos,fg="black",bg="white",bd=0,font=("Helvetica",17),spacing2=0,highlightthickness = 0)
                mensaje_pesos.insert("1.0","")
                mensaje_pesos.place(x=0, y=0, width=480,height=360)
                mensaje_pesos.config(state="disabled")
                
#--------------------------PHOTO DE BILLETES DE MIL PESOS-----------------------------------------------
                
                img  = PIL.Image.open("/Users/FaustoEzquerra/Desktop/wetransfer_billetes-de-mil-jpg_2023-11-14_0146/billetes-de-mil.jpg") 
                
                resized_image= img.resize((498,180))
                new_image= ImageTk.PhotoImage(resized_image)
                
                lab=Label(ventana, image=new_image).place(x=38,y=500)
                
                
#------PARTE GRAFICA DE DOLAR--------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
                

#----------------BOTON TITULO Y ENTRY DE DOLAR HOY--------------------------------------------------------------------
                global dolar_blue_hoy
                global titulo_dolar_blue_hoy
               
            #titulo dolar blue HOY
                
                titulo_dolar_blue_hoy = Message(text="Valor Dolar Blue Hoy:",aspect=1000)
                titulo_dolar_blue_hoy.place(x=542,y=130,width=150)
                
            #entry dolar blue HOY
                 
                dolar_blue_hoy_variable = StringVar()      
                dolar_blue_hoy = Entry(textvariable= dolar_blue_hoy_variable)
                dolar_blue_hoy_variable.trace_add('write',escuchador_entry_calculo)
                dolar_blue_hoy.place(x=550,y=150,width=130,height=40)
                
                #---------------------------------------------------------

                
#-------------------BOTON TITULO Y ENTRY DE DOLAR FUTURO--------------------------------------
                global dolar_blue_futuro
                global titulo_dolar_blue_futuro
            
            #titulo dolar blue FUTURO
                titulo_dolar_blue_futuro = Message(text="Valor dolar blue futuro:",aspect=1000)
                titulo_dolar_blue_futuro.place(x=698,y=130,width=150)
               
            #entry dolar blue FUTURO
    
                dolar_blue_futuro_variable = StringVar()
                dolar_blue_futuro = Entry(textvariable= dolar_blue_futuro_variable)
                dolar_blue_futuro_variable.trace_add('write',escuchador_entry_calculo)
                dolar_blue_futuro.place(x=700,y=150,width=150,height=40)
                
#--------------------TEXTO A MOSTRAR DE DOLAR-------------------------------------
                
                global frame_dolar
                frame_dolar = LabelFrame(ventana, text="Datos")
                frame_dolar.place(x=550,y=220,width=500,height=260)
                frame_dolar["bg"]="white"

                global mensaje_dolar
                mensaje_dolar= Text(frame_dolar,fg="black",bg="white",bd=0,font=("Helvetica",17),spacing2=0,highlightthickness = 0)
                mensaje_dolar.insert("1.0","")
                mensaje_dolar.place(x=0, y=0, width=480,height=360)
                mensaje_dolar.config(state="disabled")
                
                
                
#-------------------------RADIOBUTTON ELECCION DE SI QUIERO CALCULAR EN DOLARES O NO--------------------------

                opcion_comparacion_dolar = Radiobutton(ventana, 
                                               text="Calcular comparacion compra de dòlares blue:",
                                               variable=opcion_dolar,
                                               value=1,
                                               command=seleccionar_con_o_sin_dolar)
                opcion_comparacion_dolar.place(x=600,y=30)
                opcion_comparacion_dolar.select()
                
                opcion_no_comparacion_dolar = Radiobutton(ventana,
                                              text="NO Calcular con comparacion compra de dòlares blue:",
                                              variable=opcion_dolar,
                                              value=2,
                                              command=seleccionar_con_o_sin_dolar)
                
                opcion_no_comparacion_dolar.place(x=600,y=50)

#-----------------------------------------------------------------------
#--------------------------PHOTO DE DOLARES AL PIE DE PAGINA-------------------------------
                

            
                # Crear el label para la imagen del dólar
                
                global label_dolar
                label_dolar = Label(ventana)
                label_dolar.place(x=548, y=500)                
                
                
                
                global foto_dolar_pie
                img_dolar_pie = PIL.Image.open("/Users/FaustoEzquerra/Desktop/wetransfer_billetes-de-mil-jpg_2023-11-14_0146/dolar.jpg")
                img_dolar_pie = img_dolar_pie.resize((498, 180))
                foto_dolar_pie = ImageTk.PhotoImage(img_dolar_pie)
                label_dolar.config(image=foto_dolar_pie)

                ventana.resizable(False, False)
                ventana.mainloop()    

#---------------FIN DEL MAIN PROGRAM------------------------------------------------------------------
#---------------FIN DEL MAIN PROGRAM------------------------------------------------------------------
#---------------FIN DEL MAIN PROGRAM------------------------------------------------------------------
#---------------FIN DEL MAIN PROGRAM------------------------------------------------------------------
#---------------FIN DEL MAIN PROGRAM------------------------------------------------------------------
#---------------FIN DEL MAIN PROGRAM------------------------------------------------------------------
#---------------FIN DEL MAIN PROGRAM------------------------------------------------------------------
#---------------FIN DEL MAIN PROGRAM------------------------------------------------------------------
#---------------FIN DEL MAIN PROGRAM------------------------------------------------------------------


#---------------MOSTRAR IMAGEN DE DOLAR O NO MOSTRAR IMAGEN DE DOLAR SEGUN ELECCION DEL RADIOBUTTON---------------

def mostrar_imagen_dolar():
    
        global foto_dolar_pie
        img_dolar_pie = PIL.Image.open("/Users/FaustoEzquerra/Desktop/wetransfer_billetes-de-mil-jpg_2023-11-14_0146/dolar.jpg")
        img_dolar_pie = img_dolar_pie.resize((498, 180))
        foto_dolar_pie = ImageTk.PhotoImage(img_dolar_pie)
        label_dolar.config(image=foto_dolar_pie)

def ocultar_imagen_dolar():
        label_dolar.config(image='')
        
#---------------MOSTRAR IMAGEN DE DOLAR O NO MOSTRAR IMAGEN DE DOLAR SEGUN ELECCION DEL RADIOBUTTON---------------
          
def escuchador_entry_calculo(var, index, mode):
    
    global entry_calculo
    if entry_calculo.get() != "":
                                    if not(entry_calculo.get()[len(entry_calculo.get())-1].isdigit()):           
                                            entry_calculo.delete(len(entry_calculo.get())-1,"end")
                 
                        
    if porcentaje_entry.get() != "":
                                    if porcentaje_entry.get()[len(porcentaje_entry.get())-1].isdigit() or (porcentaje_entry.get()[len(porcentaje_entry.get())-1] == "." and porcentaje_entry.get().count(".") <= 1 ):           
                                            pass
                                    else:
                                            porcentaje_entry.delete(len(porcentaje_entry.get())-1,"end")           

    if opcion.get() == 1: 
                    if meses_entry.get() != "":
                                                    if not(meses_entry.get()[len(meses_entry.get())-1].isdigit()):           
                                                        meses_entry.delete(len(meses_entry.get())-1,"end")
                                                        
    if opcion_dolar.get() == 1:
             
                    if dolar_blue_hoy.get() != "":                 
                                                    if not(dolar_blue_hoy.get()[len(dolar_blue_hoy.get())-1].isdigit() or (dolar_blue_hoy.get()[len(dolar_blue_hoy.get())-1] == "." and dolar_blue_hoy.get().count(".") <= 1)):
                                                        dolar_blue_hoy.delete(len(dolar_blue_hoy.get())-1,"end")
                                                                    
                    if dolar_blue_futuro.get() != "":                    
                                                    if not(dolar_blue_futuro.get()[len(dolar_blue_futuro.get())-1].isdigit() or (dolar_blue_futuro.get()[len(dolar_blue_futuro.get())-1] == "." and dolar_blue_futuro.get().count(".") <= 1)):
                                                        dolar_blue_futuro.delete(len(dolar_blue_futuro.get())-1,"end")
                    
                  
                        
    #--------------LOGICA DE SEPARADOR DE MILES EN EL ENTRY DE INVERSION---------------------------
    if entry_calculo.get() != "":

                    conversion_sin_separador_de_miles = entry_calculo.get()
                    conversion_sin_separador_de_miles = int(conversion_sin_separador_de_miles.replace(".",""))
                    entry_calculo_var = format(conversion_sin_separador_de_miles, ",.0f").replace(",",".")
                    entry_calculo.delete(0,"end")
                    entry_calculo.insert(0,entry_calculo_var)
           
 #-----------------CON O SIN PARTE GRAFICA DE MESES PARA EL CALCULO------------
 #---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------        
 #---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------  
 #---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------    
def seleccionar_con_o_sin_meses():
    
    #----------construir ENTRY MESES------------------------------ 
    global opcion
    global titulo_entry
    
    #opcion 1 es por entry de INVERSION
    if opcion.get() == 1:
          
                construir_meses_entry()

   
    #opcion 2 es por entry de GANACIA
    elif opcion.get() == 2:              
                
                destruir_meses_entry()

                titulo_entry.config(text="Ganancia mensual esperada en pesos:")
                
                titulo_entry.place(x=152,y=130,width=240)
       
def destruir_meses_entry():
    
            
    #----------DESTRUIR ENTRY MESES------------------------------ 

                global titulo_entry
                global meses_entry
                global entry_calculo
                
                meses_entry.destroy()  
                
                titulo_meses.config(text="")  
                #-------------------------------------------------------

                titulo_entry.config(text="Por ganancia ingresada en pesos:")
             
                entry_calculo.focus()           
            
def construir_meses_entry():

                global meses_entry
                global meses_entry_variable
                global titulo_entry
                global entry_calculo
                
                meses_entry_variable = StringVar()
                
                titulo_meses.config(text="Meses")
                
                meses_entry = Entry(textvariable=meses_entry_variable)
                meses_entry_variable.trace_add('write',escuchador_entry_calculo)
                meses_entry.place(x=425,y=150,width=55,height=40)
        
                titulo_entry.config(text="Inversion inicial en pesos:")
              

                entry_calculo.focus()    
            
#-------------CON PARTE GRAFICA DE DOLAR O SIN ELLA----------------------------- 
          
def seleccionar_con_o_sin_dolar():

    global opcion_dolar
    
    #-------------SLECIONAR SI O NO CALULO CON DOLAR
    if opcion_dolar.get() == 1:
          
                construir_dolar_blue_entrys()
            
    elif opcion_dolar.get() == 2:              
               
                destruir_dolar_blue_entrys()
                           
def destruir_dolar_blue_entrys():
    
                global titulo_dolar_blue_futuro
                global titulo_dolar_blue_hoy
                global dolar_blue_futuro
                global dolar_blue_hoy
                
                titulo_dolar_blue_hoy.config(text="")               
                titulo_dolar_blue_futuro.config(text="") 
                
                dolar_blue_futuro.destroy()
                dolar_blue_hoy.destroy()
                
                #destruye el frame de datos de dolares:
                global frame_dolar
                frame_dolar.destroy() 
                #destruye la imagen de dolares
               
                ocultar_imagen_dolar()
                                                            
def construir_dolar_blue_entrys():
    
                global titulo_dolar_blue_hoy
                global titulo_dolar_blue_futuro
                
                titulo_dolar_blue_hoy.config(text="Valor dolar blue hoy:")
                titulo_dolar_blue_futuro.config(text="Valor dolar blue futuro:")
                
                global dolar_blue_futuro
                global dolar_blue_futuro_variable
                dolar_blue_futuro_variable = StringVar()
                dolar_blue_futuro = Entry(textvariable= dolar_blue_futuro_variable)
                dolar_blue_futuro_variable.trace_add('write',escuchador_entry_calculo)
                dolar_blue_futuro.place(x=700,y=150,width=150,height=40)
                
                global dolar_blue_hoy
                global dolar_blue_hoy_variable
                dolar_blue_hoy_variable = StringVar()      
                dolar_blue_hoy = Entry(textvariable= dolar_blue_hoy_variable)
                dolar_blue_hoy_variable.trace_add('write',escuchador_entry_calculo)
                dolar_blue_hoy.place(x=550,y=150,width=130,height=40)
                
                                
                global frame_dolar
                frame_dolar = LabelFrame(ventana, text="Datos")
                frame_dolar.place(x=550,y=220,width=500,height=260)
                frame_dolar["bg"]="white"

                global mensaje_dolar
                mensaje_dolar= Text(frame_dolar,fg="black",bg="white",bd=0,font=("Helvetica",17),spacing2=0,highlightthickness = 0)
                mensaje_dolar.insert("1.0","")
                mensaje_dolar.place(x=0, y=0, width=480,height=360)
                mensaje_dolar.config(state="disabled")
                
#--------------------------PHOTO DE DOLARES AL PIE DE PAGINA-------------------------------
                 

                mostrar_imagen_dolar()
                
#-------------FUNCIONES DE CALCULO--------------------------------------------- 
                              
def calcular():
     
     global opcion
     #opcion = 1 es calculo por inversion, que necesita de meses,
     #opcion_dolar = 1, es con calculo de dolares
     
     if opcion.get() == 1  and opcion_dolar.get() == 1:  
        #con meses y con dolares, por inversion  
         calculo_con_dolar_y_por_inversion()   
     if opcion.get() == 2  and opcion_dolar.get() == 1:  
        #con ganancia y con dolares, por ganancia 
         calculo_con_dolar_y_por_ganancia()   
     if opcion.get() == 1 and opcion_dolar.get() == 2:
         calculo_sin_dolar_y_por_inversion()
     if opcion.get() == 2 and opcion_dolar.get() == 2:
         calculo_sin_dolar_y_por_ganancia()
                          
def calculo_con_dolar_y_por_inversion():
        
#---------CALCULO DE PESOS PRIMERO------------------------------------------------------------------------
        
     #FILTRO DE DATOS QUE ESTEN TODOS INGRESADOS LOS DE PESOS Y LOS DE DOLARES TAMBIEN
     global meses_entry
     global porcentaje_entry
     
     if not(entry_calculo.get() != "" and str(porcentaje_entry.get()).replace(".","0").isdigit() and meses_entry.get().isdigit() and str(dolar_blue_hoy.get()).replace(".","0").isdigit() and str(dolar_blue_futuro.get()).replace(".","0").isdigit()):
                                 
                
                mensaje_pesos= Text(frame_pesos,fg="black",bg="white",bd=0,font=("Helvetica",17),spacing1=0,highlightthickness = 0)
                mensaje_pesos.config(state="normal")
                mensaje_pesos.delete("1.0","end")
                mensaje_pesos.insert("1.0"," FALTAN DATOS, O DATOS ERRONEOS")
                mensaje_pesos.place(x=0, y=0, width=480,height=360)
                mensaje_pesos.config(state="disabled")
                
                mensaje_pesos= Text(frame_dolar,fg="black",bg="white",bd=0,font=("Helvetica",17),spacing1=0,spacing3=0,highlightthickness = 0)
                mensaje_pesos.config(state="normal")
                mensaje_pesos.delete("1.0","end")
                mensaje_pesos.insert("1.0"," FALTAN DATOS, O DATOS ERRONEOS")
                mensaje_pesos.place(x=0, y=0, width=480,height=360)
                mensaje_pesos.config(state="disabled")
                
                
     else:
            
                #----CALCULO DE PESOS-----------------------------------------------------
                
                monto=entry_calculo.get().replace(".","")  
                interes = porcentaje_entry.get()            
                interes=float(interes)
                monto=int(monto)                 
                acumulado=monto
                
                meses=meses_entry.get()
                meses=int(meses)
                for x in range(1,(meses+1)):
                    
                    ganancia_del_ultimo_mes=(acumulado*interes/100)/12
                    acumulado= acumulado + ganancia_del_ultimo_mes
                    
                    if x==1:
                        ganancia_primer_mes=acumulado-monto

                porcentaje_ganancia_pesos= (acumulado*100/monto)-100
                
                ganancia_total_pesos = acumulado - monto

#--------OUTPUT DE TEXTO RESULTADOS PESOS----------------------------------------------
                texto_pesos =    f''' el valor acumulado total en pesos es: {format(int(acumulado), ',.0f').replace(",",".")} $\n
 el porcentaje de ganancia es: {int(porcentaje_ganancia_pesos)}% \n
 ganancia del primer mes en pesos: {format(int(ganancia_primer_mes), ',.0f').replace(",",".")} $\n
 ganancia del último mes en pesos: {format(int(ganancia_del_ultimo_mes), ',.0f').replace(",",".")} $\n
 ganancia total acumulada: {format(int(ganancia_total_pesos), ',.0f').replace(",",".")} $'''

                #---------MUESTRO DATOS EN FRAME------------------------------------------------------------------------
                
                
                mensaje_pesos= Text(frame_pesos,fg="black",bg="white",bd=0,font=("Helvetica",17),spacing1=0,spacing3=0,highlightthickness = 0)
                mensaje_pesos.config(state="normal")
                mensaje_pesos.delete("1.0","end")
                mensaje_pesos.insert("1.0",texto_pesos)
                mensaje_pesos.place(x=0, y=0, width=480,height=360)
                mensaje_pesos.config(state="disabled")

 #-------------------------------------------------------------------------------------------------               
 #-------------------------------------------------------------------------------------------------                
 #-------------------------------------------------------------------------------------------------                
                #--------CALCULO DE DOLARES SEGUN INVERSION-----------------------
                
                dolares_comprados = float(monto)/float(dolar_blue_hoy.get())
                pesos_por_dolares_vendidos = dolares_comprados*float(dolar_blue_futuro.get())
                diferencia_pesos_ganados = int(pesos_por_dolares_vendidos - monto)
                porcentaje_de_ganancia_dolar = float(diferencia_pesos_ganados*100/monto)   
                incremento_mensual_de_dolar_blue = (int(dolar_blue_futuro.get()) - int(dolar_blue_hoy.get()))/int(meses_entry.get())
                
                #------------------------------------------------------------------
                
                
                
                texto_dolar = f''' Dolares comprados hoy según\n dolar blue del día: {format(int(dolares_comprados), ',.0f').replace(",",".")} U$D \n
 ganancia en pesos por compra/venta\n de los dólares: {format(int(diferencia_pesos_ganados), ',.0f').replace(",",".")}$ \n 
 Incremento mensual de aumento del dolar blue \n hasta el último mes ingresado: {format(int(incremento_mensual_de_dolar_blue), ',.0f').replace(",",".")} U$D por mes\n
 porcentaje de ganancia segun lo invertido: {int(porcentaje_de_ganancia_dolar)}% \n'''

                #---------MUESTRO DATOS EN FRAME------------------------------------------------------------------------
                
                
                mensaje_dolar= Text(frame_dolar,fg="black",bg="white",bd=0,font=("Helvetica",17),spacing1=0,spacing3=0,highlightthickness = 0)
                mensaje_dolar.config(state="normal")
                mensaje_dolar.delete("1.0","end")
                mensaje_dolar.insert("1.0",texto_dolar)
                mensaje_dolar.place(x=0, y=0, width=480,height=360) 
                mensaje_dolar.config(state="disabled")   
                
    

def calculo_con_dolar_y_por_ganancia():
#FILTRO DE DATOS QUE ESTEN TODOS INGRESADOS LOS DE PESOS Y LOS DE DOLARES TAMBIEN

    global entry_calculo
    
    if not(entry_calculo.get() != "" and str(porcentaje_entry.get()).replace(".","0").isdigit() and str(dolar_blue_hoy.get()).replace(".","0").isdigit() and str(dolar_blue_futuro.get()).replace(".","0").isdigit()):
                
                
                mensaje_pesos= Text(frame_pesos,fg="black",bg="white",bd=0,font=("Helvetica",17),spacing1=0,spacing3=0,highlightthickness = 0)
                mensaje_pesos.config(state="normal")
                mensaje_pesos.delete("1.0","end")
                mensaje_pesos.insert("1.0"," FALTAN DATOS, O DATOS ERRONEOS")
                mensaje_pesos.place(x=0, y=0, width=480,height=360)
                mensaje_pesos.config(state="disabled")
                
                mensaje_pesos= Text(frame_dolar,fg="black",bg="white",bd=0,font=("Helvetica",17),spacing1=0,spacing3=0,highlightthickness = 0)
                mensaje_pesos.config(state="normal")
                mensaje_pesos.delete("1.0","end")
                mensaje_pesos.insert("1.0"," FALTAN DATOS, O DATOS ERRONEOS")
                mensaje_pesos.place(x=0, y=0, width=480,height=360)
                mensaje_pesos.config(state="disabled")
                
    else:
                
            
                #----CALCULO DE PESOS-----------------------------------------------------
                
                ganancia_esperada_mensual =entry_calculo.get().replace(".","")
                interes = porcentaje_entry.get()            
                interes=float(interes)
                ganancia_esperada_mensual=int(ganancia_esperada_mensual)                 
                
                
                monto_de_inversion_por_ganancia = ((ganancia_esperada_mensual*12)*100)/interes   
                porcentaje_de_ganancia_mensual = (100*ganancia_esperada_mensual)/monto_de_inversion_por_ganancia

#--------OUTPUT DE TEXTO RESULTADOS PESOS----------------------------------------------
                texto_pesos =    f''' Inversión necesaria para ganar lo ingresado el primer mes: \n {format(int(monto_de_inversion_por_ganancia), ',.0f').replace(",",".")} $\n
 el porcentaje de ganancia mensual segun inversión es: \n {int(porcentaje_de_ganancia_mensual)}% \n'''
 

                #---------MUESTRO DATOS EN FRAME------------------------------------------------------------------------
                
                
                mensaje_pesos= Text(frame_pesos,fg="black",bg="white",bd=0,font=("Helvetica",17),spacing1=0,spacing3=0,highlightthickness = 0)
                mensaje_pesos.config(state="normal")
                mensaje_pesos.delete("1.0","end")
                mensaje_pesos.insert("1.0",texto_pesos)
                mensaje_pesos.place(x=0, y=0, width=480,height=360)
                mensaje_pesos.config(state="disabled")
 #-------------------------------------------------------------------------------------------------               
 #-------------------------------------------------------------------------------------------------                
 #-------------------------------------------------------------------------------------------------                
                #--------CALCULO DE DOLARES SEGUN INVERSION-----------------------
                
                dolares_comprados = int(monto_de_inversion_por_ganancia/float(dolar_blue_hoy.get()))
                pesos_por_dolares_vendidos = int(dolares_comprados*float(dolar_blue_futuro.get()))
                diferencia_pesos_ganados = pesos_por_dolares_vendidos - monto_de_inversion_por_ganancia  
                porcentaje_de_ganancia_dolar = diferencia_pesos_ganados*100/monto_de_inversion_por_ganancia  
                 
                
                #------------------------------------------------------------------
                
                
                
                texto_dolar = f''' Dolares comprados hoy según\n dolar blue del día: {format(int(dolares_comprados), ',.0f').replace(",",".")} U$D \n
 ganancia en pesos por compra/venta \n de los dólares ántes comprados: {format(int(diferencia_pesos_ganados), ',.0f').replace(",",".")}$ \n
 porcentaje de ganancia segun lo invertido: {int(porcentaje_de_ganancia_dolar)}% \n'''
 
                #---------MUESTRO DATOS EN FRAME------------------------------------------------------------------------
                
                
                mensaje_dolar= Text(frame_dolar,fg="black",bg="white",bd=0,font=("Helvetica",17),spacing1=0,spacing3=0,highlightthickness = 0)
                mensaje_dolar.config(state="normal")
                mensaje_dolar.delete("1.0","end")
                mensaje_dolar.insert("1.0",texto_dolar)
                mensaje_dolar.place(x=0, y=0, width=480,height=360)   
                mensaje_dolar.config(state="disabled")
                
def calculo_sin_dolar_y_por_inversion():
     
 #---------CALCULO DE PESOS PRIMERO------------------------------------------------------------------------
     
     global entry_calculo
     global meses_entry
     global porcentaje_entry
        
     #FILTRO DE DATOS QUE ESTEN TODOS INGRESADOS LOS DE PESOS Y LOS DE DOLARES TAMBIEN
     if not(entry_calculo.get() != "" and str(porcentaje_entry.get()).replace(".","0").isdigit() and meses_entry.get().isdigit()):
                
                
                mensaje_pesos= Text(frame_pesos,fg="black",bg="white",bd=0,font=("Helvetica",17),spacing1=0,spacing3=0,highlightthickness = 0)
                mensaje_pesos.config(state="normal")
                mensaje_pesos.delete("1.0","end")
                mensaje_pesos.destroy()
                mensaje_pesos.insert("1.0"," FALTAN DATOS, O DATOS ERRONEOS")
                mensaje_pesos.place(x=0, y=0, width=480,height=360)
                mensaje_pesos.config(state="disabled")
                
                mensaje_pesos= Text(frame_dolar,fg="black",bg="white",bd=0,font=("Helvetica",17),spacing1=0,spacing3=0,highlightthickness = 0)
                mensaje_pesos.config(state="normal")
                mensaje_pesos.delete("1.0","end")
                mensaje_pesos.destroy()
                mensaje_pesos.insert("1.0"," FALTAN DATOS, O DATOS ERRONEOS")
                mensaje_pesos.place(x=0, y=0, width=480,height=360)
                mensaje_pesos.config(state="disabled")
                

     else:
                #----CALCULO DE PESOS-----------------------------------------------------
                
                monto=entry_calculo.get().replace(".","")  
                interes = porcentaje_entry.get()            
                interes=float(interes)
                monto=int(monto)                 
                acumulado=monto
                
                meses=meses_entry.get()
                meses=int(meses)
                for x in range(1,(meses+1)):
                    
                    ganancia_del_ultimo_mes=(acumulado*interes/100)/12
                    acumulado= acumulado + ganancia_del_ultimo_mes
                    
                    if x==1:
                        ganancia_primer_mes=acumulado-monto

                porcentaje_ganancia_pesos= (acumulado*100/monto)-100
                
                ganancia_total_pesos = acumulado - monto

#--------OUTPUT DE TEXTO RESULTADOS PESOS----------------------------------------------
                texto_pesos =    f''' el valor acumulado total en pesos es: {format(int(acumulado), ',.0f').replace(",",".")} $\n
 el porcentaje de ganancia es: {int(porcentaje_ganancia_pesos)}% \n
 ganancia del primer mes en pesos: {format(int(ganancia_primer_mes), ',.0f').replace(",",".")} $\n
 ganancia del último mes en pesos: {format(int(ganancia_del_ultimo_mes), ',.0f').replace(",",".")} $\n
 ganancia total acumulada: {format(int(ganancia_total_pesos), ',.0f').replace(",",".")} $'''

                #---------MUESTRO DATOS EN FRAME------------------------------------------------------------------------
                
                
                mensaje_pesos= Text(frame_pesos,fg="black",bg="white",bd=0,font=("Helvetica",17),spacing1=0,spacing3=0,highlightthickness = 0)
                mensaje_pesos.config(state="normal")
                mensaje_pesos.delete("1.0","end")
                mensaje_pesos.insert("1.0",texto_pesos)
                mensaje_pesos.place(x=0, y=0)
                mensaje_pesos.config(state="disabled")
 
def calculo_sin_dolar_y_por_ganancia():
    
     global entry_calculo
     global meses_entry
     global porcentaje_entry

     #FILTRO DE DATOS QUE ESTEN TODOS INGRESADOS LOS DE PESOS Y LOS DE DOLARES TAMBIEN
     if not(entry_calculo.get() != "" and str(porcentaje_entry.get()).replace(".","0").isdigit()):
                
                            
                mensaje_pesos= Text(frame_pesos,fg="black",bg="white",bd=0,font=("Helvetica",17),spacing1=0,spacing3=0,highlightthickness = 0)
                mensaje_pesos.config(state="normal") 
                mensaje_pesos.delete("1.0","end")
                mensaje_pesos.insert("1.0"," FALTAN DATOS, O DATOS ERRONEOS")
                mensaje_pesos.place(x=0, y=0, width=480,height=360)
                mensaje_pesos.config(state="disabled")
                
                mensaje_pesos= Text(frame_dolar,fg="black",bg="white",bd=0,font=("Helvetica",17),spacing1=0,spacing3=0,highlightthickness = 0)
                mensaje_pesos.config(state="normal")
                mensaje_pesos.delete("1.0","end")
                mensaje_pesos.insert("1.0"," FALTAN DATOS, O DATOS ERRONEOS")
                mensaje_pesos.place(x=0, y=0, width=480,height=360)
                mensaje_pesos.config(state="disabled")
     else:
                #----CALCULO DE PESOS-----------------------------------------------------
                

                
                ganancia_esperada_mensual =entry_calculo.get().replace(".","")
                interes = porcentaje_entry.get()            
                interes=float(interes)
                ganancia_esperada_mensual=int(ganancia_esperada_mensual)                 
                
                
                monto_de_inversion_por_ganancia = ((ganancia_esperada_mensual*12)*100)/interes   
                porcentaje_de_ganancia_mensual = (100*ganancia_esperada_mensual)/monto_de_inversion_por_ganancia

#--------OUTPUT DE TEXTO RESULTADOS PESOS----------------------------------------------
                texto_pesos =    f''' Inversión necesaria para ganar lo ingresado el primer mes: \n\n {format(int(monto_de_inversion_por_ganancia), ',.0f').replace(",",".")} $\n
 el porcentaje de ganancia mensual segun inversión es: \n\n {int(porcentaje_de_ganancia_mensual)}% \n'''
 

                #---------MUESTRO DATOS EN FRAME------------------------------------------------------------------------
                
                
                mensaje_pesos= Text(frame_pesos,fg="black",bg="white",bd=0,font=("Helvetica",17),spacing1=0,spacing3=0,highlightthickness = 0)
                mensaje_pesos.config(state="normal")
                mensaje_pesos.delete("1.0","end")
                mensaje_pesos.insert("1.0",texto_pesos)
                mensaje_pesos.place(x=0, y=0, width=480,height=360)
                mensaje_pesos.config(state="disabled")
            
                #---------------fin----------------------------------------------------------------------------------                

def quit_program():
      
                ventana.quit()
                
if __name__ == "__main__":
        main()


