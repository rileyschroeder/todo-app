import splice_fxns as sf
import PySimpleGUI as psg


label_s1 = psg.Text("Enter the first start postion: ")
label_e1 = psg.Text("Enter the first end postion: ")
label_s2 = psg.Text("Enter the second start postion: ")
label_e2 = psg.Text("Enter the second end postion: ")

input_s1 = psg.InputText(key="start1")
input_e1 = psg.InputText(key="end1")
input_s2 = psg.InputText(key="start2")
input_e2 = psg.InputText(key="end2")

splice_button = psg.Button("Splice", key="splice")
completed = psg.Text(key="completed")
window = psg.Window("Worklist Alternator",
                    layout=[[label_s1, input_s1], [label_e1, input_e1], [label_s2, input_s2], [label_e2, input_e2],
                            [splice_button, completed]])

while True:
    event, values = window.read()
    match event:
        case "splice":
            print(event)
            print(values)
            sf.splice_wells(values["start1"], values["end1"], values["start2"], values["end2"])
            window["completed"].update(value="Splice completed. Check the .txt files for output.")
        case psg.WIN_CLOSED:
            break

window.close()