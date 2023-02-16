import random
import tkinter as tk
import json

def generate_candidate_description(name, company, scope, experience, skills, interests, payrate, proceeding, time):

    global nameDecorators
    global companyDecorators
    global scopeDecorators
    global experienceDecorators
    global toolsDecorators
    global interestDecorators
    global payrateDecorators
    global proceedingDecorators
    global notProceedingDecorators


    with open('responses.json', 'r') as inputFile:
        inputFile.seek(0)
        inputData = inputFile.read()

    data = json.loads(inputData)

    description = ""

    nameDecorators = data[nameDecorators]

    description += random.choice(nameDecorators) + " " + name + ". "

    randomMiddle = []
    randomMiddle.append(random.choice(data[companyDecorators]) + " " + company + ". " )
    randomMiddle.append(random.choice(data[scopeDecorators]) + " " + scope + ". " )
    randomMiddle.append(random.choice(data[experienceDecorators]) + " " + experience + " years of experience" + ". " )
    randomMiddle.append(random.choice(data[toolsDecorators]) + " " + skills + ". " )
    randomMiddle.append(random.choice(data[interestDecorators]) + " " + interests + ". " )
    randomMiddle.append(random.choice(data[payrateDecorators]) + " " + payrate + "$/hr" + ". " )

    random.shuffle(randomMiddle)

    for new in randomMiddle:
        description += new

    if proceeding:
        description += random.choice(data[proceedingDecorators]) + " " + time + "."
    else:
        description += random.choice(data[notProceedingDecorators]) + "."

    # Return the final paragraph description
    return description


def generate_description():
    global isOn

    name = name_entry.get()
    company = company_entry.get()
    scope = scope_entry.get()
    experience = experience_entry.get()
    skills = skills_entry.get()
    interests = interests_entry.get()
    payrate = payrate_entry.get()
    proceeding = isOn
    time = ""
    if isOn:
        time = time_entry.get()

    description = generate_candidate_description(name, company, scope, experience, skills, interests, payrate, proceeding, time)

    # Update the text in the output label
    output_label.config(text=description)
    generate_button.config(text="Regenerate")

def switch():
    global isOn
    global time_label
    global time_entry

    if isOn:
        isOn = False
        time_label.pack_forget()
        time_entry.pack_forget()
        proceed_entry.config(text="No")
    else:
        isOn = True
        time_label = tk.Label(root, text="Proceed Time")
        time_entry = tk.Entry(root)
        time_label.pack()
        time_entry.pack()
        generate_button.pack()
        output_label.pack()
        proceed_entry.config(text="Yes")


# Decorator name variables
nameDecorators = "nameDecorators"
companyDecorators = "companyDecorators"
scopeDecorators = "scopeDecorators"
experienceDecorators = "experienceDecorators"
toolsDecorators = "toolsDecorators"
interestDecorators = "interestDecorators"
payrateDecorators = "payRateDecorators"
proceedingDecorators = "proceedingDecorators"
notProceedingDecorators = "notProceedingDecorators"
isOn = True

# Create a new tkinter window
root = tk.Tk()
root.title("Candidate Description Generator")

# Create the input labels and text fields
name_label = tk.Label(root, text="Candidate Name:")
name_entry = tk.Entry(root)

company_label = tk.Label(root, text="Company Name:")
company_entry = tk.Entry(root)

scope_label = tk.Label(root, text="Scope:")
scope_entry = tk.Entry(root)

experience_label = tk.Label(root, text="Experience (years):")
experience_entry = tk.Entry(root)

skills_label = tk.Label(root, text="Skills:")
skills_entry = tk.Entry(root)

interests_label = tk.Label(root, text="Interested in:")
interests_entry = tk.Entry(root)

payrate_label = tk.Label(root, text="Desired Payrate ($/hr):")
payrate_entry = tk.Entry(root)

proceed_label = tk.Label(root, text="Proceeding?")
proceed_entry = tk.Button(root, text="Yes", bd=0, command=switch, height=5, width=10)

time_label = tk.Label(root, text="Proceed Time")
time_entry = tk.Entry(root)
# Create the output label

output_label = tk.Label(root, text="")
# Create the generate button

generate_button = tk.Button(root, text="Generate Description", command=generate_description)
# Add the input labels and text fields to the window

name_label.pack()
name_entry.pack()
company_label.pack()
company_entry.pack()
scope_label.pack()
scope_entry.pack()
experience_label.pack()
experience_entry.pack()
skills_label.pack()
skills_entry.pack()
interests_label.pack()
interests_entry.pack()
payrate_label.pack()
payrate_entry.pack()
proceed_label.pack()
proceed_entry.pack()
time_label.pack()
time_entry.pack()
# Add the generate button and output label to the window

generate_button.pack()
output_label.pack()
# Start the tkinter event loop

root.mainloop()