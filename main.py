import os 
import openai
import customtkinter as ctk

root = ctk.CTk()
root.geometry("750x550")
root.title("Essay Humanizer Open AI")

ctk.set_appearance_mode("dark")

title_label = ctk.CTkLabel(root , text="Humanize your essay" , font= ctk.CTkFont(size=30 , weight="bold"))
title_label.pack(padx = 10 , pady = (40,20))

frame = ctk.CTkFrame(root)
frame.pack(fill="x" , padx=100)

humanize_level_frame = ctk.CTkFrame(frame)
humanize_level_frame.pack(padx = 100, pady = (20,5) , fill = "both")

humanize_level_label = ctk.CTkLabel(frame , text="How much do you want to humanize your essay?" , font = ctk.CTkFont(weight="bold") )
humanize_level_label.pack(pady = 10)
humanize_levels = ctk.CTkComboBox(humanize_level_frame, values = ["0.25" , "0.5" ,"0.75" ,"0.99"])
humanize_levels.pack(pady = 10)


type_frame = ctk.CTkFrame(frame)
type_frame.pack(padx = 100 , pady = 5 , fill= "both")
type_label = ctk.CTkLabel(type_frame , text = "Style in which you prefer to be humanized" , font = ctk.CTkFont(weight="bold"))
type_label.pack()
type_label_value = ctk.StringVar(value="Simple")
radioButton1 = ctk.CTkRadioButton(type_frame, text="Simple" , variable= type_label_value , value = "Simple")
radioButton1.pack(side = "left" , padx = (20,10) ,pady = 10)

radioButton2 = ctk.CTkRadioButton(type_frame , text = "Academic" , variable = type_label_value , value = "Academic")
radioButton2.pack(side = "left" , padx = 10 , pady = 10)

radioButton3 = ctk.CTkRadioButton(type_frame , text = "Informal" , variable= type_label_value , value = "Informal")
radioButton3.pack(side = "left" ,padx  = 10 , pady = 10 )

top_priority = ctk.CTkFrame(frame)
top_priority.pack(padx = 2 , pady = 5 , fill = "both")
top_priority_label = ctk.CTkLabel(top_priority, text = "Set your priorities", font = ctk.CTkFont(weight = "bold"))
top_priority_label.pack()

checkbox_1 = ctk.CTkCheckBox(top_priority, text = "By pass AI checkers.")
checkbox_1.pack(side = "left", padx = 50 , pady = 10)
checkbox_2 = ctk.CTkCheckBox(top_priority, text="By pass plagarism checkers.")
checkbox_2.pack(side = "left", padx = 50 , pady = 10)


button = ctk.CTkButton(frame , text = "Generate" , command=generate)
button.pack()

result = ctk.CTkTextbox(root,font = ctk.CTkFont(size = 15))
result.pack(pady = 10 , fill = "x" , padx = 100)
root.mainloop()

