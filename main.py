import random
import nltk
import tkinter as tk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize


def generate_candidate_description(name, role, skills, experience, career_goal, payrate):
    # Create a list of sentence templates with placeholders for the candidate's information
    sentence_templates = [
        "{} has been working as a {} for over {} years, and has honed their skills in {}.",
        "With over {} years of experience as a {}, {} has developed a deep understanding of the field and an impressive set of skills, including {}.",
        "{} is seeking a role as a {} where they can leverage their skills in {} to achieve their career goal of {}.",
        "{} is an experienced {} with skills in {}, seeking a new opportunity to achieve their career goal of {}.",
        "As a skilled {}, {} is well-versed in {} and is seeking a new opportunity to grow their career and earn a pay rate of {}."
    ]

    # Shuffle the order of the sentence templatesgit
    random.shuffle(sentence_templates)

    # Select a random variation for each of the candidate's information fields
    name_variation = random.choice(["This candidate", "The candidate", "They"])
    role_variation = random.choice(["a software engineer", "an IT specialist", "a data analyst"])
    skills_variation = random.choice(["Python, Java, and C#", "JavaScript and SQL", "C++, PHP, and Ruby"])
    experience_variation = random.choice([f"{experience} years of experience", f"over {experience + 2} years of experience", f"{experience - 1} years of relevant experience"])
    career_goal_variation = random.choice([f"to become a lead {role}", f"to work on innovative projects and collaborate with a team", f"to specialize in a new area of technology"])
    payrate_variation = random.choice([f"${payrate}", f"${int(payrate) - 10000} - ${int(payrate) + 10000}", f"a competitive salary based on their skills and experience"])

    # Use the selected variations to fill in the sentence templates
    sentences = [template.format(name_variation, role_variation, experience_variation, skills_variation, career_goal_variation, payrate_variation) for template in sentence_templates]

    # Join the sentences into a paragraph
    description = " ".join(sentences)

    # Use NLTK to tokenize the paragraph into sentences and reassemble them in a more natural-sounding order
    tokenized_sentences = sent_tokenize(description)
    random.shuffle(tokenized_sentences)
    description = " ".join(tokenized_sentences)

    # Return the final paragraph description
    return description


def generate_description():
    name = name_entry.get()
    role = role_entry.get()
    skills = skills_entry.get()
    experience = int(experience_entry.get())
    career_goal = career_goal_entry.get()
    payrate = int(payrate_entry.get())

    description = generate_candidate_description(name, role, skills, experience, career_goal, payrate)

    # Update the text in the output label
    output_label.config(text=description)


# Create a new tkinter window
root = tk.Tk()
root.title("Candidate Description Generator")

# Create the input labels and text fields
name_label = tk.Label(root, text="Candidate Name:")
name_entry = tk.Entry(root)

role_label = tk.Label(root, text="Current Role:")
role_entry = tk.Entry(root)

skills_label = tk.Label(root, text="Skills:")
skills_entry = tk.Entry(root)

experience_label = tk.Label(root, text="Experience (years):")
experience_entry = tk.Entry(root)

career_goal_label = tk.Label(root, text="Career Goal:")
career_goal_entry = tk.Entry(root)

payrate_label = tk.Label(root, text="Desired Payrate ($/hr):")
payrate_entry = tk.Entry(root)
# Create the output label

output_label = tk.Label(root, text="")
# Create the generate button

generate_button = tk.Button(root, text="Generate Description", command=generate_description)
# Add the input labels and text fields to the window

name_label.pack()
name_entry.pack()
role_label.pack()
role_entry.pack()
skills_label.pack()
skills_entry.pack()
experience_label.pack()
experience_entry.pack()
career_goal_label.pack()
career_goal_entry.pack()
payrate_label.pack()
payrate_entry.pack()
# Add the generate button and output label to the window

generate_button.pack()
output_label.pack()
# Start the tkinter event loop

root.mainloop()