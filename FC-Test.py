import random
from fuzzywuzzy import fuzz

# Create a dictionary of flashcards, organized by stack
flashcard_stacks = {
    "IT Acronyms": {        
        "CPU": ("Central Processing Unit", "The CPU processes instructions from programs and manages data."),
        "RAM": ("Random Access Memory", "Temporary storage used by a computer to hold data and programs in use."),
        "HDD": ("Hard Disk Drive", "A traditional storage device with spinning disks to store data."),
        "SSD": ("Solid State Drive", "A faster storage device using flash memory."),
        "IP": ("Internet Protocol", "A set of rules for addressing and routing data across networks."),
        "DNS": ("Domain Name System", "Translates domain names into IP addresses."),
        "MAC": ("Media Access Control", "A unique identifier assigned to network interfaces."),
        "NIC": ("Network Interface Card", "Hardware for connecting a device to a network."),
        "BIOS": ("Basic Input Output System", "Firmware that initializes hardware during booting."),
        "RAID": ("Redundant Array of Independent Disks", "Data storage virtualization for performance and redundancy."),
    },

    "Hardware Components": {
        "Power Supply Unit": ("PSU", "Converts electrical power into usable power for internal components."),
        "Motherboard": ("Mainboard", "The main circuit board that connects all components."),
        "GPU": ("Graphics Processing Unit", "Handles rendering images, video, and animations."),
        "CMOS": ("Complementary Metal-Oxide-Semiconductor", "Stores BIOS settings and system time."),
        "Heat Sink": ("Cooling Component", "Dissipates heat from components like the CPU."),
    },

    "Networking Basics": {
        "OSI Model": ("Open Systems Interconnection Model", "A conceptual framework for networking protocols in 7 layers."),
        "LAN": ("Local Area Network", "A network that spans a small geographical area."),
        "WAN": ("Wide Area Network", "A network that spans large geographical areas."),
        "Ping": ("Packet Internet Groper", "A tool to test connectivity between two networked devices."),
        "Firewall": ("Network Security Device", "Monitors and controls incoming and outgoing network traffic."),
    },

    "Cybersecurity Basics": {
        "Phishing": ("Fraudulent Communication", "A cyberattack using fake emails to steal sensitive information."),
        "Firewall": ("Network Security Device", "Protects against unauthorized access to or from a private network."),
        "Antivirus": ("Malware Protection Software", "Detects and removes malicious software."),
        "Encryption": ("Data Protection Technique", "Converts data into a coded format to prevent unauthorized access."),
        "Two-Factor Authentication": ("2FA", "A security method that requires two forms of identity verification."),
    },

    "Troubleshooting Steps": {
        "Identify the Problem": ("First Step", "Gather information and identify the issue."),
        "Establish a Theory": ("Second Step", "Form a hypothesis about the root cause."),
        "Test the Theory": ("Third Step", "Verify the theory and identify the solution."),
        "Implement the Solution": ("Fourth Step", "Apply the fix and ensure it resolves the issue."),
        "Document the Results": ("Final Step", "Record the problem, solution, and process for future reference."),
    }
}


# Combine multiple stacks into one
def combine_stacks(stack_names):
    combined_stack = {}
    for stack_name in stack_names:
        if stack_name in flashcard_stacks:
            combined_stack.update(flashcard_stacks[stack_name])
    return combined_stack

# Practice mode
def practice(stack):
    questions = list(stack.keys())
    random.shuffle(questions)

    for question in questions:
        print(f"Question: {question}")
        input("Press Enter to reveal the answer...")
        meaning, definition = stack[question]
        print(f"Answer: {meaning}\nExplanation: {definition}\n")

    print("Practice session complete!")

# Test mode
def test(stack):
    questions = list(stack.keys())
    random.shuffle(questions)

    score = 0
    total_questions = len(questions)
    missed_questions = []

    for question in questions:
        meaning, definition = stack[question]
        print(question)
        user_answer = input("Your answer: ")

        if user_answer.lower() == 'exit':
            print("Exiting the quiz...")
            return

        # Check for exact match
        if user_answer.strip().lower() == meaning.lower():
            print("Correct!")
            score += 1
        elif fuzz.ratio(user_answer.lower(), meaning.lower()) >= 80:
            print("Correct! (Close enough)")
            score += 1
        else:
            missed_questions.append(question)
            print(f"Incorrect. The correct answer is: {meaning}")

    print(f"You got {score} out of {total_questions} correct.")

    if missed_questions:
        print("Let's try those missed questions again:")
        while missed_questions:
            question = random.choice(missed_questions)
            missed_questions.remove(question)
            meaning, definition = stack[question]
            print(question)
            user_answer = input("Your answer: ")

            if user_answer.lower() == 'exit':
                print("Exiting the quiz...")
                return

            if user_answer.strip().lower() == meaning.lower():
                print("Correct!")
            elif fuzz.ratio(user_answer.lower(), meaning.lower()) >= 80:
                print("Correct! (Close enough)")
            else:
                print(f"Incorrect. The answer is: {meaning}")

# Program starts here
while True:
    print("\nSelect a mode:")
    print("1. Test")
    print("2. Practice")
    print("Type 'exit' to quit.")

    mode = input("Enter your choice (1/2): ").strip()
    if mode.lower() == 'exit':
        print("Exiting the program...")
        break
    elif mode not in ['1', '2']:
        print("Invalid choice. Please choose 1 for Test or 2 for Practice.")
        continue

    print("\nAvailable stacks:")
    for stack in flashcard_stacks.keys():
        print(f"- {stack}")
    print("- Random (select random stacks)")

    stack_selection = input("\nEnter the stack name(s) separated by commas, or type 'random': ").strip()
    if stack_selection.lower() == 'exit':
        print("Exiting the program...")
        break
    elif stack_selection.lower() == 'random':
        stack_name = random.choice(list(flashcard_stacks.keys()))
        print(f"Randomly selected stack: {stack_name}")
        selected_stack = flashcard_stacks[stack_name]
    else:
        stack_names = [name.strip() for name in stack_selection.split(',')]
        selected_stack = combine_stacks(stack_names)
        if not selected_stack:
            print("Invalid stack selection. Please try again.")
            continue
        print(f"Selected stacks: {', '.join(stack_names)}")

    if mode == '1':
        test(selected_stack)
    elif mode == '2':
        practice(selected_stack)