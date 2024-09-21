from tkinter import *
from tkinter import ttk
import speech_recognition as sr
from gtts import gTTS
import pygame
from PIL import ImageTk, Image
import csv

def interface1():
    root = Tk()
    root.geometry('850x500')
    root.resizable(0,0)
    root.title("Instructions!!!")

    background_image = Image.open(r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\Project 4th Sem\Language_Translator\R.jpg") 
    resized_image = background_image.resize((850, 500))

    bg_image = ImageTk.PhotoImage(resized_image)

    background_label = Label(root, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    root_label = Label(text ="Language Translator Using Python", font = 'Arial 12 bold')
    root_label.place(x=325, y = 10)

    root_label1 = Label(text ="Instructions for Language Translator", font = 'Arial 12 bold')
    root_label1.place(x=300, y = 50)

    root_label1 = Label(text ="1. You can give input only in English Language", font = 'Arial 12 bold')
    root_label1.place(x=200, y = 100)

    root_label1 = Label(text ="2. There are only 5 languages supported for translation.", font = 'Arial 12 bold')
    root_label1.place(x=200, y = 150)

    root_label1 = Label(text ="3. Due to limited datasets, you can only translate simple words.", font = 'Arial 12 bold')
    root_label1.place(x=200, y = 200)

    root_label1 = Label(text ="4. Be sure to include punctuations and make no errors. ", font = 'Arial 12 bold')
    root_label1.place(x=200, y = 250)

    root_label1 = Label(text ="5. You can also help us improve our dataset by pressing Provide Translation Button. ", font = 'Arial 12 bold')
    root_label1.place(x=200, y = 300)

    root_label1 = Label(text ="Press Use Language Translator button to begin your translation. ", font = 'Arial 12 bold ', )
    root_label1.place(x=250, y = 350)

    def open_translation_interface():
            
                root.destroy()

                def back1():
                    root2.destroy()
                    interface1()

                def translate_text():
                    error = "No translation found in the dataset"
                    target_lang = language_codes[dest_lang_combo.get()]

                    # Initialize the recognizer
                    recognizer = sr.Recognizer()

                    # Capture audio from the microphone for input
                    with sr.Microphone() as source:
                        print("Speak something:")
                        audio = recognizer.listen(source)

                    # Recognize the input speech
                    input_text = recognizer.recognize_google(audio)

                    if target_lang == 'es':
                        def load_dataset(file_path):
                            dataset = []
                            with open(file_path, 'r', encoding='utf-8') as file:
                                reader = csv.reader(file)
                                for row in reader:
                                    dataset.append(row)
                            return dataset

                        def get_spanish_translation(english_sentence, dataset):
                            for pair in dataset:
                                if pair[0] == english_sentence:
                                    return pair[1]
                            return error

                        file_path = r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\Project 4th Sem\Language_Translator\en to es.csv"
                        dataset = load_dataset(file_path)

                        input_sentence = input_text

                        spanish_translation = get_spanish_translation(input_sentence, dataset)

                        # Use gTTS to convert input and output into speech
                        input_audio = gTTS(input_text, lang='en')
                        output_audio = gTTS(spanish_translation, lang='es')

                        input_audio.save(r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\Project 4th Sem\Language_Translator\input.mp3")
                        output_audio.save(r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\Project 4th Sem\Language_Translator\output.mp3")

                        pygame.mixer.init()
                        pygame.mixer.music.load(r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\Project 4th Sem\Language_Translator\input.mp3")
                        pygame.mixer.music.play()
                        while pygame.mixer.music.get_busy():
                            pygame.time.Clock().tick(5)

                        pygame.mixer.music.load(r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\Project 4th Sem\Language_Translator\output.mp3")
                        pygame.mixer.music.play()
                        while pygame.mixer.music.get_busy():
                            pygame.time.Clock().tick(5)

                    elif(target_lang == 'fr'):
                        def load_dataset(file_path):
                            dataset= []
                            with open(file_path, 'r', encoding='utf-8') as file:
                                reader = csv.reader(file)
                                for row in reader:
                                    dataset.append(row)
                            return dataset
                            
                        def get_french_translation(english_sentence, dataset):
                            for pair in dataset:
                                if pair[0] == english_sentence:
                                    return pair[1]
                            return error
                            
                        file_path = r"C:\Users\hp\OneDrive\Desktop\Kakeru\Project 4th Sem\Language_Translator\en to fr.csv"
                        dataset = load_dataset(file_path)
                        
                        input_sentence = input_text
                        
                        french_translation = get_french_translation(input_sentence, dataset)
                        
                        Output_text.delete("1.0", END)
                        Output_text.insert(END, french_translation)

                    elif(target_lang == 'de'):
                        def load_dataset(file_path):
                            dataset= []
                            with open(file_path, 'r', encoding='utf-8') as file:
                                reader = csv.reader(file)
                                for row in reader:
                                    dataset.append(row)
                            return dataset
                            
                        def get_german_translation(english_sentence, dataset):
                            for pair in dataset:
                                if pair[0] == english_sentence:
                                    return pair[1]
                            return error
                            
                        file_path = r"C:\Users\hp\OneDrive\Desktop\Kakeru\Project 4th Sem\Language_Translator\en to de.csv"
                        dataset = load_dataset(file_path)
                        
                        input_sentence = input_text
                        
                        german_translation = get_german_translation(input_sentence, dataset)
                        
                        Output_text.delete("1.0", END)
                        Output_text.insert(END, german_translation)

                    elif(target_lang == 'ja'):
                        def load_dataset(file_path):
                            dataset= []
                            with open(file_path, 'r', encoding='utf-8') as file:
                                reader = csv.reader(file)
                                for row in reader:
                                    dataset.append(row)
                            return dataset
                            
                        def get_japanese_translation(english_sentence, dataset):
                            for pair in dataset:
                                if pair[0] == english_sentence:
                                    return pair[1]
                            return error
                            
                        file_path = r"C:\Users\hp\OneDrive\Desktop\Kakeru\Project 4th Sem\Language_Translator\en to ja.csv"
                        dataset = load_dataset(file_path)
                        
                        input_sentence = input_text
                        
                        japanese_translation = get_japanese_translation(input_sentence, dataset)
                        
                        Output_text.delete("1.0", END)
                        Output_text.insert(END, japanese_translation)
                    
                    else:
                        def load_dataset(file_path):
                            dataset= []
                            with open(file_path, 'r', encoding='utf-8') as file:
                                reader = csv.reader(file)
                                for row in reader:
                                    dataset.append(row)
                            return dataset
                            
                        def get_nepali_translation(english_sentence, dataset):
                            for pair in dataset:
                                if pair[0] == english_sentence:
                                    return pair[1]
                            return error
                            
                        file_path = r"C:\Users\hp\OneDrive\Desktop\Kakeru\Project 4th Sem\Language_Translator\en to ne.csv"
                        dataset = load_dataset(file_path)
                        
                        input_sentence = input_text
                        
                        nepali_translation = get_nepali_translation(input_sentence, dataset)
                        
                        Output_text.delete("1.0", END)
                        Output_text.insert(END, nepali_translation)

                root2 = Tk()
                root2.geometry('850x500')  
                root2.resizable(0, 0)
                root2.title('Language Translator')

                background_image2 = Image.open(r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\Project 4th Sem\Language_Translator\Image.jpg") 
                resized_image2 = background_image2.resize((850, 500))

                bg_image2 = ImageTk.PhotoImage(resized_image2)

                background_label2 = Label(root2, image=bg_image2)
                background_label2.place(x=0, y=0, relwidth=1, relheight=1)

                title_label = Label(root2, text="Language Translator", font='Arial 20 bold')
                title_label.pack(pady=20)

                language_codes = {
                    'Spanish': 'es',
                    'French': 'fr',
                    'German': 'de',
                    'Japanese': 'ja',
                    'Nepali': 'ne'
                }

                # Frame for input and output
                io_frame = Frame(root2)
                io_frame.pack(pady=20)

                # Input Frame
                input_frame = Frame(io_frame)
                input_frame.grid(row=0, column=0, padx=20, pady=10, sticky="n")  

                enter_text_label = Label(input_frame, text="Enter Text in English :", font="Arial 12 bold")
                enter_text_label.pack(pady=10)

                Input_text = Text(input_frame, width=30, height=10, font='Arial 12') 
                Input_text.pack(pady=10)

                # Output Frame
                output_frame = Frame(io_frame)
                output_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n") 

                output_label = Label(output_frame, text='Output Text:', font='Arial 12 bold')
                output_label.pack(pady=10)

                Output_text = Text(output_frame, width=30, height=10, font='Arial 12')  
                Output_text.pack(pady=10)

                # Language Selection Frame - Output
                output_lang_frame = Frame(output_frame)
                output_lang_frame.pack()

                output_lang_label = Label(output_lang_frame, text='Select Target Language:', font='Arial 12 bold')
                output_lang_label.pack(side=LEFT, padx=10)

                dest_lang_combo = ttk.Combobox(output_lang_frame, values=list(language_codes), width=15, font='Arial 12')  # Reduce the width of the output language combobox
                dest_lang_combo.pack(padx=10)
                dest_lang_combo.set('Choose Target Language')

                # Translate Button
                trans_btn = Button(root2, text='Translate', font='Arial 12 bold', pady=5, command=translate_text, bg='grey', fg='white')
                trans_btn.pack(pady=10)

                back_btn = Button(root2, text='Back', font='Arial 12 bold',command=back1, pady=5, bg='red', fg='white')
                back_btn.place(x=700, y = 425)

                root2.mainloop()

    def provide_translation():
                
                root.destroy()
                
                def back():
                    
                    root3.destroy()

                    interface1()

                def save_translation():
                    input = Input_text3.get("1.0", "end-1c")
                    output = Output_text3.get("1.0", "end-1c")
                    target_lang = language_codes[dest_lang_combo3.get()]

                    if(target_lang == 'es'):

                        file_path = r"C:\Users\hp\OneDrive\Desktop\Kakeru\Project 4th Sem\Language_Translator\en to es.csv"
                        with open(file_path, 'a', newline='', encoding='utf-8') as file:
                            writer = csv.writer(file)
                            writer.writerow([input, output])

                    elif(target_lang == 'fr'):
                        file_path = r"C:\Users\hp\OneDrive\Desktop\Kakeru\Project 4th Sem\Language_Translator\en to fr.csv"
                        with open(file_path, 'a', newline='', encoding='utf-8') as file:
                            writer = csv.writer(file)
                            writer.writerow([input, output])

                    elif(target_lang == 'de'):
                        file_path = r"C:\Users\hp\OneDrive\Desktop\Kakeru\Project 4th Sem\Language_Translator\en to de.csv"
                        with open(file_path, 'a', newline='', encoding='utf-8') as file:
                            writer = csv.writer(file)
                            writer.writerow([input, output])

                    elif(target_lang == 'ja'):
                        file_path = r"C:\Users\hp\OneDrive\Desktop\Kakeru\Project 4th Sem\Language_Translator\en to ja.csv"
                        with open(file_path, 'a', newline='', encoding='utf-8') as file:
                            writer = csv.writer(file)
                            writer.writerow([input, output])

                    else:
                        file_path = r"C:\Users\hp\OneDrive\Desktop\Kakeru\Project 4th Sem\Language_Translator\en to ne.csv"
                        with open(file_path, 'a', newline='', encoding='utf-8') as file:
                            writer = csv.writer(file)
                            writer.writerow([input, output])

        
                root3 = Tk()
                root3.geometry('850x500+200+100')  
                root3.resizable(0, 0)
                root3.title('Language Translator')

                background_image3 = Image.open(r"C:\Users\hp\OneDrive\Desktop\Kakeru\Project 4th Sem\Language_Translator\Image.jpg") 
                resized_image3 = background_image3.resize((850, 500), Image.ANTIALIAS)

                bg_image3 = ImageTk.PhotoImage(resized_image3)

                background_label3 = Label(root3, image=bg_image3)
                background_label3.place(x=0, y=0, relwidth=1, relheight=1)

                title_label3 = Label(root3, text="Language Translator", font='Arial 20 bold')
                title_label3.pack(pady=20)

                language_codes = {
                    'Spanish': 'es',
                    'French': 'fr',
                    'German': 'de',
                    'Japanese': 'ja',
                    'Nepali': 'ne'
                }

                # Frame for input and output
                io_frame3 = Frame(root3)
                io_frame3.pack(pady=20)

                # Input Frame
                input_frame3 = Frame(io_frame3)
                input_frame3.grid(row=0, column=0, padx=20, pady=10, sticky="n")  

                enter_text_label3 = Label(input_frame3, text="Enter Text in English :", font="Arial 12 bold")
                enter_text_label3.pack(pady=10)

                Input_text3 = Text(input_frame3, width=30, height=10, font='Arial 12') 
                Input_text3.pack(pady=10)

                # Output Frame
                output_frame3 = Frame(io_frame3)
                output_frame3.grid(row=0, column=1, padx=10, pady=10, sticky="n") 

                output_label = Label(output_frame3, text='Output Text:', font='Arial 12 bold')
                output_label.pack(pady=10)

                Output_text3 = Text(output_frame3, width=30, height=10, font='Arial 12')  
                Output_text3.pack(pady=10)

                # Language Selection Frame - Output
                output_lang_frame3 = Frame(output_frame3)
                output_lang_frame3.pack()

                output_lang_label3 = Label(output_lang_frame3, text='Select Target Language:', font='Arial 12 bold')
                output_lang_label3.pack(side=LEFT, padx=10)

                dest_lang_combo3 = ttk.Combobox(output_lang_frame3, values=list(language_codes), width=15, font='Arial 12')  # Reduce the width of the output language combobox
                dest_lang_combo3.pack(padx=10)
                dest_lang_combo3.set('Choose Target Language')

                # Translate Button

                trans_btn3 = Button(root3, text='Save Translation', command=save_translation, font='Arial 12 bold', pady=5, bg='grey', fg='white')
                trans_btn3.pack(pady=10)

                back_btn = Button(root3, text='Back', font='Arial 12 bold',command=back, pady=5, bg='red', fg='white')
                back_btn.place(x=700, y = 425)

                root3.mainloop()

    login_btn = Button(root, text='Use Language Translator', font='Arial 12 bold', pady=5, command=open_translation_interface, bg='grey', fg='white')
    login_btn.place(x=150, y = 400)

    login_btn2 = Button(root, text='Provide Translation', font='Arial 12 bold',command=provide_translation, pady=5, bg='grey', fg='white')
    login_btn2.place(x=600, y = 400)

    root.mainloop()

interface1()