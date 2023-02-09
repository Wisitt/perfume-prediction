#0=Men 1=Women
gender=["Men","Men","Women","Men","Women","Men","Women","Men","Men","Men","Women","Men","Women","Men","Women","Women","Women","Men","Women","Men"]
#0=Elder 1=Studying 2=Working
age=["Studying","Studying","Working","Elder","Working","Studying","Working","Working","Studying","Elder","Elder","Studying","Working","Studying","Studying","Elder","Elder","Working","Studying","Working"]
#0=Cool 1=Formal 2=Sport 
lifestyle=["Sport","Sport","Cool","Formal","Cool","Formal","Formal","Sport","Cool","Cool","Cool","Sport","Formal","Sport","Cool","Cool","Formal","Formal","Sport","Sport"]
#0=Fresh 1=Oriental 2=Woody
scent=["Fresh","Fresh","Oriental","Woody","Fresh","Oriental","Woody","Fresh","Oriental","Woody","Woody","Oriental","Oriental","Fresh","Woody","Oriental","Oriental","Fresh","Woody","Woody"]


import os
import tkinter as tk
from tkinter import Label
import tkinter
import customtkinter
import winsound




winsound.PlaySound("hey", winsound.SND_FILENAME)
from sklearn import preprocessing
le = preprocessing.LabelEncoder()

gender_encoder=le.fit_transform(gender)
age_encoder=le.fit_transform(age)
lifestyle_encoder=le.fit_transform(lifestyle)
scent_encoder=le.fit_transform(scent)
#print("gender",gender_encoder)
#print("age",age_encoder)
#print("lifestyle",lifestyle_encoder)
#print("scent",scent_encoder)

features=list(zip(gender_encoder,age_encoder,lifestyle_encoder))
#print(features)

X = features
y = scent_encoder
scent_encoder = scent

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model = model.fit(X_train,y_train)

from sklearn import metrics
y_pred = model.predict(X_test)
y_score = metrics.accuracy_score(y_test,y_pred)
print(y_score)




customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

         # configure window
        self.title("Mini-project-ทำนายกลิ่นน้ำหอมตามวันเกิด")
        self.geometry(f"{1100}x{580}")
        self.configure(bacegroundg='#fff')


        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((1, 2, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Perfume Prediction", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))



        def button_fuction():
            selected_value1 = self.optionmenu_1.get()
            index_of_selected_value1 = self.optionmenu_1.cget("values").index(selected_value1)
            selected_value2 = self.optionmenu_2.get()
            index_of_selected_value2 = self.optionmenu_2.cget("values").index(selected_value2)
            selected_value3 = self.optionmenu_3.get()
            index_of_selected_value3 = self.optionmenu_3.cget("values").index(selected_value3)
            
            predicted=model.predict([[int(index_of_selected_value1),int(index_of_selected_value2),int(index_of_selected_value3)]])
            if predicted == 0:
                self.textbox.insert("0.0", "\n\n" + str("Fresh"))
            elif predicted == 1:
                self.textbox.insert("0.0", "\n\n" + str("Oriental"))
            elif predicted == 2:
                self.textbox.insert("0.0", "\n\n" + str("Woody"))
            else:
                print("Error")
        
        
        self.main_button_1 = customtkinter.CTkButton(master=self,command=button_fuction, fg_color="transparent", border_width=2, text_color=("gray10", "#fff"),text="Result")
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=100 , height=100)
        self.textbox.grid(row=1, column=1, padx=(10, 0), pady=(10, 0), sticky="nsew")

        # create tabview


        self.tabview = customtkinter.CTkTabview(self, width=100, height=100 )
        self.tabview.grid(row=0, column=1, padx=(10, 0), pady=(10, 0), sticky="nsew")
        self.tabview.grid_columnconfigure(1, weight=0)

        self.tabview.add("Select Input")
        
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Select Input"), dynamic_resizing=False,
                                                        values=["Men", "Women"])
        self.optionmenu_1.grid(row=0, column=1, padx=20, pady=(10, 10))

        self.optionmenu_2 = customtkinter.CTkOptionMenu(self.tabview.tab("Select Input"), dynamic_resizing=False,
                                                        values=["Studying", "Working", "Elder"])
        self.optionmenu_2.grid(row=0, column=2, padx=20, pady=(10, 10))

        self.optionmenu_3 = customtkinter.CTkOptionMenu(self.tabview.tab("Select Input"), dynamic_resizing=False,
                                                        values=["Sport", "Cool", "Formal"])
        self.optionmenu_3.grid(row=0, column=3, padx=20, pady=(10, 10))

        
        
        
        # create slider and progressbar frame
    
        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.optionmenu_1.set("Gender")
        self.optionmenu_2.set("Age")
        self.optionmenu_3.set("Lifestyle")


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

if __name__ == "__main__":
    app = App()
    app.mainloop()