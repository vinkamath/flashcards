# A Thousand Flashcards
Our toddler loves flashcards. Inhales them, infact. The enthusiastic parents that we are, we would like to have an endless supply of flashcards to keep up with our son's varcious apetite for flashcards. There are only so many you can buy. What then? How do you print a thousand flashcards?

Can we use generative AI to help us generate printable flashcard files? Ideally, we would like to be able to create a printable PDF based off a single prompt
## The Process
1. **List**: Create a list of categorized objects
1. **Generate**: Use a texttoimage model to generate images
1. **Caption**: Caption each image
1. **Combine**: Convert captioned images into a printable PDF

### List
We use a chat completion LLM to generate a human readable list of objects. Category names start with `#`. Here is an example:
```
# Animals
Alligator
Leopard
Bear

# Birds
Seagull
Puffin
Crane
```
### Generate

### Caption

### Combine

## Installation