# Flashcards
We want to print 1500 flashcards. For a smaller number, we would manually download and caption images and combine them into a single PDF that can be sent over for printing. However, at this scale, we need to automate the entire proess.

## The Process
1. Create a list of categories and objects
1. Download or generate an image for each subject
1. Caption the images
1. Combine the images into a single PDF

## List
Use a GPT to generate a list. Start category names with `#`. For example:
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

## Image
Use a text to image model like Kankinsky3 or SDXL.

## Caption
Use PIL to add the `object` name at bottom of each image.

## Combine
Combine all images into a single PDF.
