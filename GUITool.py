import tkinter as tkn
import pandas as pd
from main import *

class Heart_GUI:
    def __init__(self):
        
        self.window = tkn.Tk()
        self.window.title("Heart Disease Predictor")

        # creating frames for each non target attribute
        self.first_frame = tkn.Frame()
        self.second_frame = tkn.Frame()
        self.third_frame = tkn.Frame()
        self.fourth_frame = tkn.Frame()
        self.fifth_frame = tkn.Frame()
        self.sixth_frame = tkn.Frame()
        self.seventh_frame = tkn.Frame()
        self.eighth_frame = tkn.Frame()
        self.ninth_frame = tkn.Frame()
        self.tenth_frame = tkn.Frame()
        self.eleventh_frame = tkn.Frame()
        self.twelfth_frame = tkn.Frame()
        self.thirteenth_frame = tkn.Frame()
        self.fourteenth_frame = tkn.Frame()
    

        self.button_frame = tkn.Frame()
        self.output_frame = tkn.Frame()

        # PDA
        # - age
        # - sex
        # - cp
        # - trestbps
        # - chol
        # - fbs
        # - restecg
        # - thalach
        # - exang
        # - oldpeak
        # - slope
        # - ca
        # - thal
        # - hd

        # Age
        self.age_label = tkn.Label(self.first_frame, text="Enter Age: ")
        self.age_entry = tkn.Entry(self.first_frame, bg="light blue", bd=2, width=10)
        self.age_label.pack(side="left")
        self.age_entry.pack(side="left")

        # Sex
        self.sex_label = tkn.Label(self.second_frame, text="Enter Sex: ")
        self.sex_entry = tkn.Entry(self.second_frame, bg="light blue", bd=2, width=10)
        self.sex_label.pack(side="left")
        self.sex_entry.pack(side="left")

        # chest pain cp
        self.cp_label = tkn.Label(self.third_frame, text="Enter Chest Pain: ")
        self.click_cp_var = tkn.StringVar()
        self.click_cp_var.set("Typical Angina")
        self.cp_input = tkn.OptionMenu(self.third_frame, self.click_cp_var,
                            "Typical Angina", "Atypical Angina", "Non--Anginal Pain", "Asymptotic")
        self.cp_label.pack(side="left")
        self.cp_input.pack(side="left")

        # Trestbps    
        self.trestbps_label = tkn.Label(self.fourth_frame, text="Enter Resting Blood Pressure: ")
        self.trestbps_entry = tkn.Entry(self.fourth_frame, bg="light blue", bd=2, width=10)
        self.trestbps_label.pack(side="left")
        self.trestbps_entry.pack(side="left")
        
        # chol
        self.chol_label = tkn.Label(self.fifth_frame, text="Serum Cholestorol: ")
        self.chol_entry = tkn.Entry(self.fifth_frame, bg="light blue", bd=2, width=10)
        self.chol_label.pack(side="left")
        self.chol_entry.pack(side="left")

        # fbs
        self.fbs_label = tkn.Label(self.sixth_frame, text="Fasting Blood Sugar: ")
        self.click_fbs_var = tkn.StringVar()
        self.click_fbs_var.set("No")
        self.fbs_input = tkn.OptionMenu(self.sixth_frame, self.click_fbs_var, "Yes",
                                                      "No")
        self.fbs_label.pack(side="left")
        self.fbs_input.pack(side="left")

        # restecg
        self.restecg_label = tkn.Label(self.seventh_frame, text="Resting ECG: ")
        self.click_restecg_var = tkn.StringVar()
        self.click_restecg_var.set("Normal")
        self.restecg_input = tkn.OptionMenu(self.seventh_frame, self.click_restecg_var, "Normal",
                                                      "Having ST-T wave abnormality", "left ventricular hyperthrophy")
        self.restecg_label.pack(side="left")
        self.restecg_input.pack(side="left")

        # thalach
        self.thalach_label = tkn.Label(self.eighth_frame, text="Max Heart Rate: ")
        self.thalach_entry = tkn.Entry(self.eighth_frame, bg="light blue", bd=2, width=10)
        self.thalach_label.pack(side="left")
        self.thalach_entry.pack(side="left")

        # exang
        self.exang_label = tkn.Label(self.ninth_frame, text="Exercise Induced Angina ")
        self.click_exang_var = tkn.StringVar()
        self.click_exang_var.set("No")
        self.exang_input = tkn.OptionMenu(self.ninth_frame, self.click_exang_var, "Yes", "No")
        self.exang_label.pack(side="left")
        self.exang_input.pack(side="left")

        # oldpeak
        self.oldpeak_label = tkn.Label(self.tenth_frame, text="ST Depression (Exercise followed by Rest): ")
        self.oldpeak_entry = tkn.Entry(self.tenth_frame, bg="light blue", bd=2, width=10)
        self.oldpeak_label.pack(side="left")
        self.oldpeak_entry.pack(side="left")

        # slope
        self.slope_label = tkn.Label(self.eleventh_frame, text="Slope (Peak exercise ST segment): ")
        self.click_slope_var = tkn.StringVar()
        self.click_slope_var.set("Upsloping")
        self.slope_input = tkn.OptionMenu(self.eleventh_frame, self.click_slope_var, "Upsloping", "Flat", "Downsloping")
        self.slope_label.pack(side="left")
        self.slope_input.pack(side="left")
        
        # ca - number of major amount of vessels colored by flouroscopy 
        self.ca_label = tkn.Label(self.twelfth_frame, text="Major Vessels Coloured by Flouroscopy: ")
        self.click_ca_var = tkn.StringVar()
        self.click_ca_var.set(0)
        self.ca_input = tkn.OptionMenu(self.twelfth_frame, self.click_ca_var, 0,1,2,3)
        self.ca_label.pack(side="left")
        self.ca_input.pack(side="left")

        # thalassemia
        self.thal_label = tkn.Label(self.thirteenth_frame, text="Thalassemia: ")
        self.click_thal_var = tkn.StringVar()
        self.click_thal_var.set("No")
        self.thal_input = tkn.OptionMenu(self.thirteenth_frame, self.click_thal_var, "Normal","Fixed Defect", "Reversible Defect")
        self.thal_label.pack(side="left")
        self.thal_input.pack(side="left")
        
        # prediction button
        self.predict_button = tkn.Button(self.button_frame, text="Predict", command=self.predict_disease)
        self.quit_button = tkn.Button(self.button_frame, text="Quit", command=self.window.destroy)
        self.predict_button.pack(side="left")
        self.quit_button.pack(side="left")

        self.results = tkn.Text(self.output_frame, bg="light blue", height=10, width=40)
        self.results.pack()


        # packing frames
        self.first_frame.pack()
        self.second_frame.pack()
        self.third_frame.pack()
        self.fourth_frame.pack()
        self.fifth_frame.pack()
        self.sixth_frame.pack()
        self.seventh_frame.pack()
        self.eighth_frame.pack()
        self.ninth_frame.pack()
        self.tenth_frame.pack()
        self.eleventh_frame.pack()
        self.twelfth_frame.pack()
        self.thirteenth_frame.pack()

        self.button_frame.pack()
        self.output_frame.pack()

        # main loop for window
        tkn.mainloop()


    def predict_disease(self):
        self.results.delete(0.0, tkn.END)
        
        age = self.age_entry.get()
        sex = self.sex_entry.get()
        cp = self.click_cp_var.get()
        trestbps = self.trestbps_entry.get()
        chol = self.chol_entry.get()
        fbs = self.click_fbs_var.get()
        restecg = self.click_restecg_var.get()
        thalach = self.thalach_entry.get()
        exang = self.click_exang_var.get()
        oldpeak = self.oldpeak_entry.get()
        slope = self.click_slope_var.get()
        ca = self.click_ca_var.get()
        thal = self.click_thal_var.get()

        sex_dict = {
            'Male': 1,
            'Female': 0
        }

        cp_dict = {
            "Typical Angina": 0,
            "Atypical Angina": 1,
            "Non--Anginal Pain": 2,
            "Asymptotic" : 3
        }    
            
        fbs_dict = {
            "Yes": 1,
            "No": 0
        }

        restecg_dict = {
            "Normal": 0,
            "Having ST-T wave abnormality": 1,
            "left ventricular hyperthrophy" : 2
        }

        exang_dict = {
            "Yes": 1,
            "No": 0
        }

        slope_dict = {
            "Upsloping": 0,
            "Flat": 1,
            "Downsloping": 2
        }

        thal_dict = {
            "Normal": 1,
            "Fixed Defect": 2,
            "Reversible Defect": 3
        }
  

        sex = sex_dict[sex]
        cp = cp_dict[cp]
        fbs = fbs_dict[fbs]
        restecg = restecg_dict[restecg]
        exang = exang_dict[exang]
        slope = slope_dict[slope]
        thal = thal_dict[thal]

        # - age
        # - sex
        # - cp
        # - trestbps
        # - chol
        # - fbs
        # - restecg
        # - thalach
        # - exang
        # - oldpeak
        # - slope
        # - ca
        # - thal
        # - hd
        


        
        patient_info = (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)


        prediction =  best_model.predict([patient_info])
        

        if prediction == [0]:
            prediction = "low chance of heart diseas"
        else:
            prediction = "high chance of heart disease"

        # outputs result
        self.results.insert("1.0", f"Heart disease is predicted as having a {prediction}")

        

my_predictor = Heart_GUI()