# A Thousand Flashcards
Our toddler loves flashcards. Inhales them, infact. The enthusiastic parents that we are, we would like to have an endless supply of flashcards to keep up with our son's voracious appetite for flashcards. There are only so many you can buy. What then? How do you print a thousand flashcards?

Can we use generative AI to generate printable flashcard files? Can we go from a single prompt to a file you can just print at home?
## The Process
1. **List**: Create a list of categorized objects
1. **Generate**: Use a texttoimage model to generate images
1. **Caption**: Caption each image
1. **Combine**: Convert captioned images into a printable PDF

## Installation
Setup up a virutal environment and install packages
```
python -v venv env
source env/bin/activate
pip install -r requirements.txt
```
