import subprocess
from VideoCensor import styles
import BackEnd as b
import os

# Import all the pages.
from VideoCensor.pages import *

color = "rgb(107,99,246)"
import reflex as rx

class FormState(rx.State):
    vid : list[str]
    form_data: dict = {}
    words: str = ""
    processing = False
    complete = False
    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        f = open("bad_words.txt","w")
        f.write(form_data["words"])
        f.close()
    async def handle_upload(
            self, files: list[rx.UploadFile]
    ):
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_asset_path("Test.mp4")

            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

            self.vid.append(file.filename)
    def run_backend(self):
        b.run()
        self.complete = True



@rx.page(route="/", title="index")
def index():
    
    return rx.box(
        rx.vstack(
        rx.form(
            rx.vstack(
                inputText(),
                rx.button("Submit", type_="submit", id = "inputButton"),
                
            ),
            on_submit=FormState.handle_submit,
        ),
        uploadButton(),
        Process_button(),
        
        )
    )
    

def uploadButton():
    return rx.vstack(
        rx.upload(
            rx.vstack(
                rx.button(
                    "Select File",
                    color=color,
                    bg="white",
                    border=f"1px solid {color}",
                    id = "button1"
                ),
                rx.text(
                    "Drag and drop files here or click to select files",
                    id = "uploadtext"

                ),
            ),
            border=f"1px dotted {color}",
            padding="5em",
            id = "vstackform"
        ),
        rx.hstack(rx.foreach(rx.selected_files, rx.text)),
        rx.button(
            "Upload",
            on_click=lambda: FormState.handle_upload(
                rx.upload_files()
            ),
            id = "UploadButton"
        ),
        rx.foreach(
            FormState.vid, 
            lambda vid: rx.video(
                url=vid,
                height="450px",
                width="600px",
                controls = True
                
            ),
        ),
        padding="20em",
        padding_bottom = "55em",
        padding_left = "85em",
        align_items="center",
        
        )
'''def AfterProcessVid():
    return rx.vstack(
        rx.cond(
        FormState.complete,
        rx.video(
                url="censoredvideo.mp4",
                height="250px",
                width="400px",
                controls = True
                
            ),
        ),
        padding="20em",
        padding_left = "85em",
        align_items="right",
    )'''

def Process_button():
    return rx.button(
        "Process",
        on_click = FormState.run_backend,
        id = "ProcessButton",
    )
def text1():
    return rx.text(
        "Supported formats: mp4",
        id = "text1"
    )

def inputText():
    return rx.vstack(
        rx.heading(FormState.words, id = "heading"),
        rx.text_area(
            placeholder= "Enter the words you want to be censored seperated in new lines",
            id = "words",
            value=FormState.words,
            on_change=FormState.set_words,
        ),
    )
def index0():
    text1(), inputText()

app = rx.App(style=styles.style)
app.compile()
