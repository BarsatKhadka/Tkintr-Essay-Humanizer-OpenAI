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
humanize_level_label.pack()
humanize_levels = ctk.CTkComboBox(humanize_level_frame, values = ["0.25" , "0.5" ,"0.75" ,"0.99"])
humanize_levels.pack(pady = 10)

root.mainloop()

