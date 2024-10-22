from tkinter import *

from tkinter import messagebox
from tkinter import ttk

from projet import *



u1=Utilisateur("l64547","nouhaila","ahrra","nouhaila","21","nouhaila@trsxjcgy")
u2=Utilisateur("l64547","adnan","ahrra","adnan","22","nouhaila@trsxjcgy")
u3=Utilisateur("l64547","mounia","ahrra","nouhaila","23","nouhaila@trsxjcgy")
lu=[u1,u2,u3]
lislu=Listutilisateur(lu)


c1=Client("l1234","nouhaila","ahrram",1234,123456)
c2=Client("l4567","adnan","ahrram",4567,45678)
c3=Client("l789","mounia","ahrram",789,78912)
lc=[c1,c2,c3]
liscl=ListeClient(lc)


v1=Voiture("976138964","bm","dsl",453,98)
v2=Voiture("976138964","bm","dsl",453,98)
v3=Voiture("976138964","bm","dsl",453,98)
lv=[v1,v2,v3]
liv=ListVoitur(lv)




















w=Tk()
w.geometry('400x500')
w.title('Authentificatio ')
w.resizable(0,0)
w.configure(bg="#000066")
photo=PhotoImage(file="log.PNG",width='120')
lm=Label(w,image=photo).place(x=140,y=20)


login=Label(w,text='LOGIN :',bg='white' )
login.place(x=140,y=200)
entrylogin=Entry(w,width=20,border=0)
entrylogin.place(x=140,y=230)


mdp=Label(w,text='MOT DE PASS :',bg='white')
mdp.place(x=140,y=280)
entrymdp=Entry(w,width=20,border=0,show='*')
entrymdp.place(x=140,y=310)


#Command
def authentifier():
        login=entrylogin.get()
        mdp=entrymdp.get()
        
        if  lislu.Authentifier(login,mdp)==True:
       
               messagebox.showinfo('Reussur',"        BIENVENUE        ")
               w.destroy()
               
        else:
            messagebox.showinfo('Message D Erreur',"        cette utilisateur n'existe pas      ")

connecter=Button(w,text="SE CONNECTER",font="arial",fg="#000d33",bg='#994422', command=authentifier)
connecter.place(x=140,y=375)
w.mainloop()


#Menu
q=Tk()
q.geometry('500x500')
q.title('Accueil ')
q.resizable(0,0)
q.configure(bg='#000066')
def alert():
        messagebox.showinfo("alerte",   "BRAVO")
def prevPge():
        ajout1.destory()
def ajout1():
    ajout=Tk()
    ajout.geometry('500x500')
    ajout.title('Ajouter Utilisateur ')
    ajout.configure(bg='#000066')


    cin=Label(ajout,text='CIN:')
    cin.place(x=100,y=80)
    entrycin=Entry(ajout)
    entrycin.place(x=190,y=80)

    nom=Label(ajout,text='Nom:')
    nom.place(x=100,y=120)
    entrynom=Entry(ajout)
    entrynom.place(x=190,y=120)


    prenom=Label(ajout,text='Prenom:')
    prenom.place(x=100,y=160)
    entryprenom=Entry(ajout)
    entryprenom.place(x=190,y=160)


    log=Label(ajout,text='LOGIN:')
    log.place(x=100,y=200)
    entrylog=Entry(ajout)
    entrylog.place(x=190,y=200)



    modp=Label(ajout,text='MOT DE PASS:')
    modp.place(x=100,y=240)
    entrymodp=Entry(ajout,show='*')
    entrymodp.place(x=190,y=240)



    email=Label(ajout,text='Email:')
    email.place(x=100,y=280)
    entryemail=Entry(ajout)
    entryemail.place(x=190,y=280)



    def ajouterutil():
            cin= entrycin.get()
            nom=entrynom.get
            prenom=entryprenom.get()
            log=entrylog.get()
            mdp=entrymodp.get()
            email=entryemail.get()
            utilisateur=Utilisateur(cin,nom,prenom,log,mdp,email)
            valide=lislu.Ajouter( utilisateur)
            if valide:
                    messagebox.showinfo('Message succe',"    Bien Ajouter  ")
            else:
                     messagebox.showinfo('Message Erreur', "     Utilisateur exist deja")
                    
            
    enregistrer=Button(ajout,text='Enregistrer',command=lambda:ajouterutil())
    enregistrer.place(x=330,y=330)
    
    
  

def ajout2():
    ajout=Tk()
    ajout.geometry('500x500')
    ajout.title('Ajouter Client ')
    ajout.configure(bg='#000066')


    cin=Label(ajout,text='CIN:')
    cin.place(x=100,y=80)
    entrycin=Entry(ajout)
    entrycin.place(x=190,y=80)

    nom=Label(ajout,text='Nom:')
    nom.place(x=100,y=120)
    entrynom=Entry(ajout)
    entrynom.place(x=190,y=120)


    prenom=Label(ajout,text='Prenom:')
    prenom.place(x=100,y=160)
    entryprenom=Entry(ajout)
    entryprenom.place(x=190,y=160)


    nump=Label(ajout,text='NumPermis:')
    nump.place(x=100,y=200)
    entrynump=Entry(ajout)
    entrynump.place(x=190,y=200)



    tele=Label(ajout,text='Tele:')
    tele.place(x=100,y=240)
    entrytele=Entry(ajout)
    entrytele.place(x=190,y=240)



   



    def ajoutercli():
        cin= entrycin.get()
        nom=entrynom.get
        prenom=entryprenom.get()
        nump=entrynump.get()
        tele=entrytele.get()
        client=Client(cin,nom,prenom,nump,tele)
        valide=liscl.AjouterClient(client)
        if valide:
                messagebox.showinfo('Message succe',"    Bien Ajouter  ")
        else:
                messagebox.showinfo('Message Erreur', "     Client exist deja")
                    
            
    enregistrer=Button(ajout,text='Enregistrer',command=lambda:ajoutercli())
    enregistrer.place(x=330,y=330)
            

    

    
def ajout3():
    ajout=Tk()
    ajout.geometry('500x500')
    ajout.title('Ajouter Voiture Citadinne ')
    ajout.configure(bg='#000066')


    imatricule=Label(ajout,text='Immatriculation,:')
    imatricule.place(x=100,y=80)
    entryimatricule=Entry(ajout)
    entryimatricule.place(x=230,y=80)

    marq=Label(ajout,text='Marque:')
    marq.place(x=100,y=120)
    entrymarq=Entry(ajout)
    entrymarq.place(x=230,y=120)


    carburant=Label(ajout,text='Carburant:')
    carburant.place(x=100,y=160)
    entrycarburant=Entry(ajout)
    entrycarburant.place(x=230,y=160)


    model=Label(ajout,text='Model:')
    model.place(x=100,y=200)
    entrymodel=Entry(ajout)
    entrymodel.place(x=230,y=200)



    puis=Label(ajout,text='Puissance Fiscal:')
    puis.place(x=100,y=240)
    entrypuis=Entry(ajout)
    entrypuis.place(x=230,y=240)


    def ajoutervoi():
        imatricule= entryimatricule.get()
        marq=entrymarq.get
        carburant=entrycarburant.get()
        model=entrymodel.get()
        puis=entrypuis.get()
        voiture=Voiture(imatricule,marq,carburant, model,puis)
        valide=liv.AjouterVoiture(voiture)
        if valide:
                messagebox.showinfo('Message succe',"    Bien Ajouter  ")
        else:
                messagebox.showinfo('Message Erreur', "    Voiture n'exist deja")
                    
            
    enregistrer=Button(ajout,text='Enregistrer',command=lambda:ajoutervoi())
    enregistrer.place(x=330,y=330)



   



   
    

def ajout4():
    ajout=Tk()
    ajout.geometry('500x500')
    ajout.title('Ajouter Location  ')
    ajout.configure(bg='#000066')
   

    dat=Label(ajout,text='Date De Location:')
    dat.place(x=100,y=80)
    entrydat=Entry(ajout)
    entrydat.place(x=230,y=80)

    dur=Label(ajout,text='Duree:')
    dur.place(x=100,y=120)
    entrydur=Entry(ajout)
    entrydur.place(x=230,y=120)


    prix=Label(ajout,text='Prix:')
    prix.place(x=100,y=160)
    entryprix=Entry(ajout)
    entryprix.place(x=230,y=160)


    


    client=Button(ajout,text='Client',command=lambda:ajout2())
    client.place(x=100,y=210)
    voiture=Button(ajout,text='VoitureCitadine',command=lambda:ajout3())
    voiture.place(x=170,y=210)
    voiture=Button(ajout,text='VoitureVip',command=lambda:ajout3())
    voiture.place(x=300,y=210)





    enregistrer=Button(ajout,text='Enregistrer',command=lambda:ajout4())
    
    enregistrer.place(x=330,y=280)
   

def afficher1():
    afficher=Tk()
    afficher.geometry('900x500')
    afficher.title('Ajouter Voiture Citadinne ')
    afficher.configure(bg='#000066')
    value=[]

    def selectItem(a):
            curItem=tree.focus()
            value=tree.item(curItem).get("values")

    def supprimerutil():
             curItem=tree.focus()
             value=tree.item(curItem).get("values")
             lislu.supprimer(str(value[3]))
             selected_item=tree.selection()[0]
             tree.delete(selected_item)
        
    def modifieutil():
            curItem=tree.focus()
            value=tree.item(curItem).get("values")
            affich=Toplevel(afficher)
            affich.geometry('500x500')
            affich.title('Ajouter Voiture Citadinne ')
            affich.configure(bg='#000066')
            selected_item=tree.selection()[0]

            cin=Label( affich,text='CIN:')
            cin.place(x=100,y=80)
            entrycin=Entry(affich)
            entrycin.place(x=190,y=80)
            entrycin.insert(END,str (value[0]))
            entrycin.config(state='disabled')


            nom=Label(affich,text='Nom:')
            nom.place(x=100,y=120)
            entrynom=Entry(affich)
            entrynom.place(x=190,y=120)
            entrynom.insert(END,str (value[1]))


            prenom=Label(affich,text='Prenom:')
            prenom.place(x=100,y=160)
            entryprenom=Entry(affich)
            entryprenom.place(x=190,y=160)
            entryprenom.insert(END,str (value[2]))


            log=Label(affich,text='LOGIN:')
            log.place(x=100,y=200)
            entrylog=Entry(affich)
            entrylog.place(x=190,y=200)
            entrylog.insert(END,str (value[3]))



            modp=Label(affich,text='MOT DE PASS:')
            modp.place(x=100,y=240)
            entrymodp=Entry(affich,show='*')
            entrymodp.place(x=190,y=240)
            entrymodp.insert(END,str (value[4]))



            email=Label(affich,text='Email:')
            email.place(x=100,y=280)
            entryemail=Entry(affich)
            entryemail.place(x=190,y=280)
            entryemail.insert(END,str (value[5]))


            def modefie():
                    cin= entrycin.get()
                    nom=entrynom.get()
                    prenom=entryprenom.get()
                    log=entrylog.get()
                    mdp=entrymodp.get()
                    email=entryemail.get()
                    utilisateur=Utilisateur(cin,nom,prenom,log,mdp,email)
                    lislu. Modifier(utilisateur)
                    tree.delete(selected_item)
                    row=[cin,nom,prenom,log,mdp,email]
                    tree.insert('',END, values=row)

            modifier=Button(affich,text='Modifier',command=lambda:modefie())
            modifier.place(x=330,y=330)



    modifier=Button(afficher,text='Modifier',command=lambda:modifieutil())
    modifier.place(x=270,y=360)
    Supprimer=Button(afficher,text='Supprimer',command=lambda:supprimerutil())
    Supprimer.place(x=370,y=360)



    tree=ttk.Treeview(afficher,columns=(1,2,3,4,5,6),heigh=5,show="headings")
    tree.place(x=50,y=50,width=750,height=225)

    tree.heading(1,text="CIN")
    tree.heading(2,text="NOM")
    tree.heading(3,text="PRENOM")
    tree.heading(4,text="LOGIN")
    tree.heading(5,text="MOT DE PASS")
    tree.heading(6,text="EMAIL")

    tree.column(1,width=100)
    tree.column(2,width=100)
    tree.column(3,width=100)
    tree.column(4,width=100)
    tree.column(5,width=100)
    tree.column(6,width=250)

                   
    for  i in lislu.Lut:

        row=[i.cin,i.nom,i.prenom,i.login,i.modp,i.email]
        tree.insert('',END,values=row)

    tree .bind('<ButtonRelease-1>',selectItem)

def afficher2():
    afficher=Tk()
    afficher.geometry('900x500')
    afficher.title('Ajouter Voiture Citadinne ')
    afficher.configure(bg='#000066')
    value=[]

    def selectItem(a):
            curItem=tree.focus()
            value=tree.item(curItem).get("values")

    def supprimercli():
             curItem=tree.focus()
             value=tree.item(curItem).get("values")
             liscl.supprimerclient(str(value[3]))
             selected_item=tree.selection()[0]
             tree.delete(selected_item)
        
    def modifiecli():
            curItem=tree.focus()
            value=tree.item(curItem).get("values")
            affich=Toplevel(afficher)
            affich.geometry('500x500')
            affich.title('Ajouter Voiture Citadinne ')
            affich.configure(bg='#000066')
            selected_item=tree.selection()[0]

            

            cin=Label( affich,text='CIN:')
            cin.place(x=100,y=80)
            entrycin=Entry(affich)
            entrycin.place(x=190,y=80)
            entrycin.insert(END,str (value[0]))
            entrycin.config(state='disabled')


            nom=Label(affich,text='Nom:')
            nom.place(x=100,y=120)
            entrynom=Entry(affich)
            entrynom.place(x=190,y=120)
            entrynom.insert(END,str (value[1]))


            prenom=Label(affich,text='Prenom:')
            prenom.place(x=100,y=160)
            entryprenom=Entry(affich)
            entryprenom.place(x=190,y=160)
            entryprenom.insert(END,str (value[2]))


            nump=Label(affich,text='NUMPERMIS:')
            nump.place(x=100,y=200)
            entrynump=Entry(affich)
            entrynump.place(x=190,y=200)
            entrynump.insert(END,str (value[3]))

            tele=Label(affich,text='TELE:')
            tele.place(x=100,y=240)
            entrytele=Entry(affich)
            entrytele.place(x=190,y=240)
            entrytele.insert(END,str (value[4]))


            def modefie():
                    cin= entrycin.get()
                    nom=entrynom.get()
                    prenom=entryprenom.get()
                    nump=entrynump.get()
                    tele=entrytele.get()
                    client=Client(cin,nom,prenom,nump,tele)
                    liscl.Modifierclient(client)
                    tree.delete(selected_item)
                    row=[cin,nom,prenom,nump,tele]
                    tree.insert('',END, values=row)
            modifier=Button(affich,text='Modifier',command=lambda:modefie())
            modifier.place(x=330,y=330)



    modifier=Button(afficher,text='Modifier',command=lambda:modifiecli())
    modifier.place(x=270,y=360)
    Supprimer=Button(afficher,text='Supprimer',command=lambda: supprimercli())
    Supprimer.place(x=370,y=360)



    tree=ttk.Treeview(afficher,columns=(1,2,3,4,5),heigh=5,show="headings")
    tree.place(x=50,y=50,width=750,height=225)

    tree.heading(1,text="CIN")
    tree.heading(2,text="NOM")
    tree.heading(3,text="PRENOM")
    tree.heading(4,text="NUMPERMIS")
    tree.heading(5,text="TELE")
    

    tree.column(1,width=100)
    tree.column(2,width=100)
    tree.column(3,width=100)
    tree.column(4,width=100)
    tree.column(5,width=100)
    



                   
    for  i in liscl.Lc :

        row=[i.cin,i.nom,i.prenom,i.numper,i.tele]
        tree.insert('',END,values=row)
    tree.bind('<ButtonRelease-1>',selectItem)

                     
"""def afficher3():
    afficher=Tk()
    afficher.geometry('900x500')
    afficher.title('Ajouter Voiture Citadinne ')
    afficher.configure(bg='#000066')
    value=[]

    def selectItem(a):
            curItem=tree.focus()
            value=tree.item(curItem).get("values")

    def supprimercli():
             curItem=tree.focus()
             value=tree.item(curItem).get("values")
             liscl.supprimerclient(str(value[3]))
             selected_item=tree.selection()[0]
             tree.delete(selected_item)
        
    def modifiecli():
            curItem=tree.focus()
            value=tree.item(curItem).get("values")
            affich=Toplevel(afficher)
            affich.geometry('500x500')
            affich.title('Ajouter Voiture Citadinne ')
            affich.configure(bg='#000066')
            selected_item=tree.selection()[0]

            

            cin=Label( affich,text='CIN:')
            cin.place(x=100,y=80)
            entrycin=Entry(affich)
            entrycin.place(x=190,y=80)
            entrycin.insert(END,str (value[0]))
            entrycin.config(state='disabled')


            nom=Label(affich,text='Nom:')
            nom.place(x=100,y=120)
            entrynom=Entry(affich)
            entrynom.place(x=190,y=120)
            entrynom.insert(END,str (value[1]))


            prenom=Label(affich,text='Prenom:')
            prenom.place(x=100,y=160)
            entryprenom=Entry(affich)
            entryprenom.place(x=190,y=160)
            entryprenom.insert(END,str (value[2]))


            nump=Label(affich,text='NUMPERMIS:')
            nump.place(x=100,y=200)
            entrynump=Entry(affich)
            entrynump.place(x=190,y=200)
            entrynump.insert(END,str (value[3]))

            tele=Label(affich,text='TELE:')
            tele.place(x=100,y=240)
            entrytele=Entry(affich)
            entrytele.place(x=190,y=240)
            entrytele.insert(END,str (value[4]))


            def modefie():
                    cin= entrycin.get()
                    nom=entrynom.get()
                    prenom=entryprenom.get()
                    nump=entrynump.get()
                    tele=entrytele.get()
                    client=Client(cin,nom,prenom,nump,tele)
                    liscl.Modifierclient(client)
                    tree.delete(selected_item)
                    row=[cin,nom,prenom,nump,tele]
                    tree.insert('',END, values=row)
            modifier=Button(affich,text='Modifier',command=lambda:modefie())
            modifier.place(x=330,y=330)



    modifier=Button(afficher,text='Modifier',command=lambda:modifiecli())
    modifier.place(x=270,y=360)
    Supprimer=Button(afficher,text='Supprimer',command=lambda: supprimercli())
    Supprimer.place(x=370,y=360)



    tree=ttk.Treeview(afficher,columns=(1,2,3,4,5),heigh=5,show="headings")
    tree.place(x=50,y=50,width=750,height=225)

    tree.heading(1,text="Imatricula")
    tree.heading(2,text="marque")
    tree.heading(3,text="PRENOM")
    tree.heading(4,text="NUMPERMIS")
    tree.heading(5,text="TELE")
    

    tree.column(1,width=100)
    tree.column(2,width=100)
    tree.column(3,width=100)
    tree.column(4,width=100)
    tree.column(5,width=100)
    



                   
    for  i in liscl.Lc :

        row=[i.cin,i.nom,i.prenom,i.numper,i.tele]
        tree.insert('',END,values=row)
    tree.bind('<ButtonRelease-1>',selectItem)"""

                     
                                        




   












    
        
       
menubar = Menu(q)
q.config(menu=menubar)

        
Utilisatuer_menu = Menu(menubar)

       
Utilisatuer_menu.add_command(label='Ajouter Utlisateur',command=lambda:ajout1())
Utilisatuer_menu.add_command(label='Afficher Utilisateur',command=lambda:afficher1())
Utilisatuer_menu.add_command(label='Quitter',command=q.destroy)
menubar.add_cascade(label="Gestion Utilisateur",menu= Utilisatuer_menu)

client_menu = Menu(menubar)
       
client_menu.add_command(label='Ajouter Client',command=lambda:ajout2())
client_menu.add_command(label='Afficher  Client',command=afficher2())
client_menu.add_command(label='Quitter',command=q.destroy)
menubar.add_cascade(label="Gestion  Client",menu=client_menu)

voiture_menu = Menu(menubar)

voiture_menu=Menu(voiture_menu,tearoff=0)
voiture_menu.add_command(label='Ajouter Voiture Cetadinne',command=lambda:ajout3() )
voiture_menu.add_command(label='Ajouter Voiture Vip',command=lambda:ajout3())
voiture_menu.add_command(label='Afficher  Voiture',command=q.destroy)
voiture_menu.add_command(label='Quitter')
menubar.add_cascade(label="Gestion  Voiture",menu=voiture_menu)


locatio_menu = Menu(menubar)

locatio_menu.add_command(label='Ajouter Location',comman=lambda:ajout4())
locatio_menu.add_command(label='Afficher  Location',command=q.destroy)
locatio_menu.add_command(label='Quitter',command=q.destroy)
menubar.add_cascade(label="Gestion  Location",menu=locatio_menu)
q.mainloop()



