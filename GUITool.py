import tkinter as tkn
import pandas as pd
import pickle

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
    

        self.button_frame = tkn.Frame()
        self.output_frame = tkn.Frame()

        # PDA
        # - Age (num)
        # - BMI (num)
        # - Sleep Hours (num)

        # - Gender (male, female)
        
        # - Smoking (yes, no)
        # - Family Heart Disease (yes, no)
        # - Diabetes (yes, no)
        # - High Blood Pressure (yes, no)

        # - Exercise Habits (low, med, high)
        # - Alcohol Consumption (low, med, high)
        # - Stress Level (low, med, high)
        # - Sugar Consumption (low, med, high)

        # num options
        # age
        self.age_label = tkn.Label(self.first_frame, text="Enter Age: ")
        self.age_entry = tkn.Entry(self.first_frame, bg="light blue", bd=2, width=10)
        self.age_label.pack(side="left")
        self.age_entry.pack(side="left")

        # BMI
        self.bmi_label = tkn.Label(self.second_frame, text="Enter BMI: ")
        self.bmi_entry = tkn.Entry(self.second_frame, bg="light blue", bd=2, width=10)
        self.bmi_label.pack(side="left")
        self.bmi_entry.pack(side="left")

        # Sleep Hours
        self.sleep_label = tkn.Label(self.third_frame, text="Enter Sleep Hours: ")
        self.sleep_entry = tkn.Entry(self.third_frame, bg="light blue", bd=2, width=10)
        self.sleep_label.pack(side="left")
        self.sleep_entry.pack(side="left")

        # yes and no or male and female options
        # options for gender
        self.gender_label = tkn.Label(self.fourth_frame, text="Gender: ")
        self.click_gender_var = tkn.StringVar()
        self.click_gender_var.set("Male")
        self.gender_input = tkn.OptionMenu(self.fourth_frame, self.click_gender_var, "Male",
                                                      "Female")
        self.gender_label.pack(side="left")
        self.gender_input.pack(side="left")

        # Smoking
        self.smoking_label = tkn.Label(self.fifth_frame, text="Smoking: ")
        self.click_smoking_var = tkn.StringVar()
        self.click_smoking_var.set("No")
        self.smoking_input = tkn.OptionMenu(self.fifth_frame, self.click_smoking_var, "Yes",
                                                      "No")
        self.smoking_label.pack(side="left")
        self.smoking_input.pack(side="left")

        # family heart disease
        self.fhd_label = tkn.Label(self.sixth_frame, text="Family Heart Disease: ")
        self.click_fhd_var = tkn.StringVar()
        self.click_fhd_var.set("No")
        self.fhd_input = tkn.OptionMenu(self.sixth_frame, self.click_fhd_var, "Yes",
                                                      "No")
        self.fhd_label.pack(side="left")
        self.fhd_input.pack(side="left")

        # diabetes
        self.diabetes_label = tkn.Label(self.seventh_frame, text="Diabetes: ")
        self.click_diabetes_var = tkn.StringVar()
        self.click_diabetes_var.set("No")
        self.diabetes_input = tkn.OptionMenu(self.seventh_frame, self.click_diabetes_var, "Yes",
                                                      "No")
        self.diabetes_label.pack(side="left")
        self.diabetes_input.pack(side="left")

        # high blood pressure
        self.hbp_label = tkn.Label(self.twelfth_frame, text="High Blood Pressure: ")
        self.click_hbp_var = tkn.StringVar()
        self.click_hbp_var.set("No")
        self.hbp_input = tkn.OptionMenu(self.twelfth_frame, self.click_hbp_var, "Yes",
                                                      "No")
        self.hbp_label.pack(side="left")
        self.hbp_input.pack(side="left")



        # Options used for low med and high

        # - Exercise Habits (low, med, high)
        self.exercise_label = tkn.Label(self.eighth_frame, text="Exercise Level: ")
        self.click_exercise_var = tkn.StringVar()
        self.click_exercise_var.set("Low")
        self.exercise_input = tkn.OptionMenu(self.eighth_frame, self.click_exercise_var, "Low",
                                                      "Medium", "High")
        self.exercise_label.pack(side="left")
        self.exercise_input.pack(side="left")

        # - Alcohol Consumption (low, med, high)
        self.alcohol_label = tkn.Label(self.ninth_frame, text="Alcohol Consumption: ")
        self.click_alcohol_var = tkn.StringVar()
        self.click_alcohol_var.set("Low")
        self.alcohol_input = tkn.OptionMenu(self.ninth_frame, self.click_alcohol_var, "Low",
                                                      "Medium", "High")
        self.alcohol_label.pack(side="left")
        self.alcohol_input.pack(side="left")

        # - Stress Level (low, med, high)
        self.stress_label = tkn.Label(self.tenth_frame, text="Stress Level: ")
        self.click_stress_var = tkn.StringVar()
        self.click_stress_var.set("Low")
        self.stress_input = tkn.OptionMenu(self.tenth_frame, self.click_stress_var, "Low",
                                                      "Medium", "High")
        self.stress_label.pack(side="left")
        self.stress_input.pack(side="left")

        # - Sugar Consumption (low, med, high)
        self.sugar_label = tkn.Label(self.eleventh_frame, text="Sugar Consumption: ")
        self.click_sugar_var = tkn.StringVar()
        self.click_sugar_var.set("Low")
        self.sugar_input = tkn.OptionMenu(self.eleventh_frame, self.click_sugar_var, "Low",
                                                      "Medium", "High")
        self.sugar_label.pack(side="left")
        self.sugar_input.pack(side="left")
        

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
    

        
        self.button_frame.pack()
        self.output_frame.pack()

        # main loop for window
        tkn.mainloop()


    def predict_disease(self):
        self.results.delete(0.0, tkn.END)

        # getting inputs
        age = self.age_entry.get()
        bmi = self.bmi_entry.get()
        sleep = self.sleep_entry.get()

        gender = self.click_gender_var.get()
        smoking = self.click_smoking_var.get()
        fhd = self.click_fhd_var.get()
        diabetes = self.click_diabetes_var.get()
        hbp = self.click_hbp_var.get()

        exercise = self.click_exercise_var.get()
        alcohol = self.click_alcohol_var.get()
        stress = self.click_stress_var.get()
        sugar = self.click_sugar_var.get()

        heart_disease_dict = {
            0: 'No',
            1: 'Yes'
        }

        levels_dict = {
            'Low': 1,
            'Medium': 2,
            'High': 0
        }

        gender_dict = {
            'Male': 1,
            'Female': 0 
        }
        desc_dict = {
            'Yes':1,
            'No': 0
        }

        gender = gender_dict[gender]

        smoking = desc_dict[smoking]
        fhd = desc_dict[fhd]
        diabetes = desc_dict[diabetes]
        hbp = desc_dict[hbp]


        exercise = levels_dict[exercise]
        alcohol = levels_dict[alcohol]
        stress = levels_dict[stress]
        sugar = levels_dict[sugar]



        # person_info = (age, gender, exercise, smoking, fhd, diabetes, bmi, alcohol, stress, sleep, sugar)

        data = pd.DataFrame({'Age': age, 
                         'Gender' : gender, 
                         'Exercise Habits' : exercise,
                         'Smoking' : smoking, 
                         'Family Heart Disease' : fhd,
                         'Diabetes' : diabetes,
                         'BMI' : bmi,
                         'High Blood Pressure' : hbp,
                         'Alcohol Consumption' : alcohol,
                         'Stress Level' : stress,
                         'Sleep Hours' : sleep,
                         'Sugar Consumption': sugar}, index=[0])

        model = pickle.load(open('best_model.pkl', 'rb'))

        # putting user input into model
        prediction = f"Heart Disease Status: {model.predict(data)[0]}"
        

        if prediction == 1:
            prediction = "true"
        else:
            prediction = "false"

        # outputs result
        self.results.insert("1.0", f"Heart disease is predicted as {prediction}")

my_predictor = Heart_GUI()