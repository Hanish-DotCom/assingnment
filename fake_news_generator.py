import random

subjects = ["Narendra Modi", "Virat Kohli", "Priyanka Chopra", "Donald Trump", "Nirmala Sitharaman"]

actions = ["found eating gobar", "dancing on", "caught sleeping at", "launches new app for", "arguing with"]

objects = ["the moon", "the Parliament", "a rabbit", "students in Delhi", "a robot"]


def generate_headline():
    subject = random.choice(subjects)
    action = random.choice(actions)
    obj = random.choice(objects)
    headline = f"{subject} {action} {obj}!" 
    return headline

def main(): 
    print("=============================") 
    print(" FAKE NEWS HEADLINES ")
    print("=============================")

    while True:
      try:
          count = int(input("How many headlines do you want to generate?: "))
          print("\nGenerating Headlines...\n")
          print()
          
          for i in range(count):
              print(f"{i+1}. {generate_headline()}")
          
          again = input("\nDo you want to generate more? (yes/no): ").strip().lower()
          if again != "yes":
              print("\nThanks for using Fake News Headline Generator!")
              break

      except ValueError:
          print("Please enter a valid number.")

if __name__ == "__main__":
    main()

