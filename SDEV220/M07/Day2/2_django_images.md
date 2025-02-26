# How to add images to your django website!

Just like css, we ar going to need to store our images in the static folder.
This is because it shouldn't change once the website is up and running!

Inside my static folder, I now have an `images` directory. In there, I have one example image (epic.png)
which is going to be used as the example image today!

So, with our image in place, we can simply direct a html element to it!

(My image is going to go on the header of our page)

All we need to do is address it from the root of our project, just like what we did for the
css:
```html
<img src="/static/images/epic.png" alt="Epic">
```

With this in place, we now have an image on our page!