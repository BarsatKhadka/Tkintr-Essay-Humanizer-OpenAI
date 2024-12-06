import os 
import openai
import customtkinter as ctk

def generate():


    serious_level = humanize_levels.get()
    humanize_level = humanize_levels.get()
    style = type_label_value.get()
    bypass_ai = checkbox_1.get()
    bypass_plagiarism = checkbox_2.get()
    essay_input_here = essay_input.get("1.0","end")
    

    prompt = (
        f"I have an essay that needs to be refined and rewritten to make it feel more authentic, engaging, and human-like. The transformation should be done with a humanization level of {humanize_level}, which implies that the changes should carefully balance natural language flow and professional accuracy while avoiding over-simplification or excessive embellishment. "
        f"The writing style selected for this task is '{style}', so the output should align with the tone, language, and structure commonly associated with this style. "
        f"If the style is 'Simple,' the writing should prioritize clarity, straightforwardness, and a conversational tone, ensuring the ideas are easy to understand and approachable for a general audience. "
        f"If the style is 'Academic,' the output must adopt a formal and sophisticated tone, emphasizing precision, critical thinking, and academic rigor while maintaining smooth readability. "
        f"If the style is 'Informal,' it should include casual expressions, a friendly tone, and an approachable, personal narrative, reflecting how someone might speak naturally in an everyday setting. "
        f"Regardless of the style, the essay must flow seamlessly and remain cohesive while achieving a polished, engaging effect."
    )

    if bypass_ai or bypass_plagiarism:
        prompt += (
            f" In addition to the general improvements, there are specific technical requirements to address. "
        )
        if bypass_ai:
            prompt += (
                f"Ensure that the rewritten content avoids any predictable patterns, excessive uniformity, or over-reliance on syntactic structures that could trigger AI detection systems. "
                f"The output should feel organic, as though it were crafted entirely by a human without any digital intervention, relying on natural phrasing, subtle nuances, and varied sentence structures. "
            )
        if bypass_plagiarism:
            prompt += (
                f"Additionally, prioritize restructuring and rephrasing the content in a way that makes it unique and capable of passing plagiarism detection tools. "
                f"Reorganize ideas, change sentence constructions, and ensure no portion of the essay reflects any existing patterns or wording from the original text while preserving the core meaning and message. "
            )

    prompt += (
        f"Lastly, focus on preserving the original intent, meaning, and argumentation of the essay while significantly enhancing its readability and audience engagement. "
        f"Use rich vocabulary where appropriate, ensure logical progression of ideas, avoid redundancy, and add subtle stylistic variations to keep the reader's attention. "
        f"The final version should not only be coherent and compelling but also reflect a high degree of linguistic refinement, leaving an impression of thoughtful and meticulous writing. "
        f"Take care to implement these instructions thoroughly for a complete transformation that meets all criteria outlined above.\n\n"
        f"Original Essay:\n{essay_input_here}"
    )

    openai.api_key = "your api key"
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [ 
            {
                "role":"user" , "content":  prompt
            }
        ]

     )
    
    answer = response.choices[0].message.content
    print(answer)
    result.insert("0.0", answer)

root = ctk.CTk()
root.geometry("750x600")
root.title("Essay Humanizer Open AI")

ctk.set_appearance_mode("dark")

title_label = ctk.CTkLabel(root , text="Humanize your essay" , font= ctk.CTkFont(size=30 , weight="bold"))
title_label.pack(padx=10, pady=(40, 20))

frame = ctk.CTkFrame(root)
frame.pack(fill="x", padx=100)

humanize_level_frame = ctk.CTkFrame(frame)
humanize_level_frame.pack(padx=100, pady=(20, 5), fill="both")

humanize_level_label = ctk.CTkLabel(frame, text="How much do you want to humanize your essay?", font=ctk.CTkFont(weight="bold"))
humanize_level_label.pack(pady=10)
humanize_levels = ctk.CTkComboBox(humanize_level_frame, values=["0.25", "0.5", "0.75", "0.99"])
humanize_levels.pack(pady=10)

type_frame = ctk.CTkFrame(frame)
type_frame.pack(padx=100, pady=5, fill="both")
type_label = ctk.CTkLabel(type_frame, text="Style in which you prefer to be humanized", font=ctk.CTkFont(weight="bold"))
type_label.pack()
type_label_value = ctk.StringVar(value="Simple")
radioButton1 = ctk.CTkRadioButton(type_frame, text="Simple", variable=type_label_value, value="Simple")
radioButton1.pack(side="left", padx=(20, 10), pady=10)

radioButton2 = ctk.CTkRadioButton(type_frame, text="Academic", variable=type_label_value, value="Academic")
radioButton2.pack(side="left", padx=10, pady=10)

radioButton3 = ctk.CTkRadioButton(type_frame, text="Informal", variable=type_label_value, value="Informal")
radioButton3.pack(side="left", padx=10, pady=10)

top_priority = ctk.CTkFrame(frame)
top_priority.pack(padx=2, pady=5, fill="both")
top_priority_label = ctk.CTkLabel(top_priority, text="Set your priorities", font=ctk.CTkFont(weight="bold"))
top_priority_label.pack()

checkbox_1 = ctk.CTkCheckBox(top_priority, text="By pass AI checkers.")
checkbox_1.pack(side="left", padx=50, pady=10)
checkbox_2 = ctk.CTkCheckBox(top_priority, text="By pass plagiarism checkers.")
checkbox_2.pack(side="left", padx=50, pady=10)

essay_input_label = ctk.CTkLabel(root, text="Enter your essay below:", font=ctk.CTkFont(weight="bold"))
essay_input_label.pack(pady=(20, 10))

essay_input = ctk.CTkTextbox(root, font=ctk.CTkFont(size=15), height=150)
essay_input.pack(pady=10, fill="x", padx=100)

button = ctk.CTkButton(frame, text="Generate", command=generate)
button.pack()

result = ctk.CTkTextbox(root, font=ctk.CTkFont(size=15))
result.pack(pady=10, fill="x", padx=100)
root.mainloop()
