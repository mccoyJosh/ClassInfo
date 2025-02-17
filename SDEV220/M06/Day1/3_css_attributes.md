# CSS Attributes

Again, there are A LOT of different css elements.
But, we can begin looking at the most common items to start understanding it:

## color

This changes the color of text on a page.

The value it takes can be a pre-defined color word, like
'blue', but can also be a hexadecimal, rgb, or hsl value for said color

```css
p {
 color:blue;
}
```

HEXADECIMAL:
```css
p {
    color: #FF5733;
}
```

RGB:
```css
p {
    color: rgb(231, 124, 62);
}
```

For anything that is a color, this will be the case (being able to
use a single word describing or a input value to determine it).


## font-family

This changes the font of the text inside of it.

```css
p {
    font-family: 'Courier New', Courier, monospace;
}
```


## text-align

This changes the alignment of elements within your html document.
This takes a few keywords like right, left, center!

```css
h1 {
    text-align: right;
}

p {
    text-align: center;
}
```


## text-indent

This changes the first line of a section
to be indented by an overall percentage.

```css
p {
    text-indent: 10%;
}
```


## text-transform

This TRANSFORMS text to become either
capitalized, uppercase, or lowercase (or none of the above).

```css
h1 {
    text-transform: uppercase;
}

p {
    text-transform: capitalize;
}
```


## text-decoration

This adds some decorations line
underlines and line through to text

```css
h1 {
    text-decoration: underline;
}

p {
    text-decoration:line-through;
}
```


## background-color

This changes the background color for a element in 
html.

```css
h1 {
    background-color: springgreen;
}

p {
    background-color: blanchedalmond;
}

body {
    background-color: black;
}
```


## font-size

This changes the size of the font.
There are a few built in key words
like "small" and "large", or
you can specifically use the number 
of pixels you want with a number + px.

This is going to be the case for most
things which describe the size and/or thickness of
something.

```css
h1 {
    font-size: 100px;
}

p {
    font-size:small;
}

```


## font-weight

This changes the thickness of your text.

This essentially makes it really bold.

```css
p {
    font-weight:900;
}

```


## border

There are many, many things we can do with borders.

Really, borders are going to be what sets different assets
apart, as they provide the mechanism to round out your edges,
bring emphasis to certain items, and separate things.

There are many parts of a border, but to even see it,
you are going to need to use the `border-style` property
to have something instead of nothing (it is none by default)

```css
p {
    border-style: solid;
}
```

Past that, we can change it's color and width with 
their corresponding attributes.

Also, to get the nice, rounded edges, we can use
'border-radius' along with a size to
give some radius to our corners.

```css
h1 {
    border-color: rgb(72, 72, 77);
    border-width: 50px;
    border-style: solid;

    border-radius: 25px;
}

p {
    border-color: black;
    border-width: 5px;
    border-style: dotted;
}
```

Also, there are specific tags about describing the top, bottom, left, right (and more) borders. This is so that you can use
more advanced borders if need be (maybe you just need a top border
and nothing else, in which case you can do that).


## padding

This changes the padding around an object.
This can give you some nice formatting to your page!

```css
p {
    padding:100px;
}
```


## width & height

This changes the width and height of an element.
In the provided example, we are also
using background color so you can even see the difference.

Note that if you don't provide enough room for your element for
the content inside of it, it will bleed out of it into other elements!

```css
h1 {
    width: 200px;
    height: 300px; 
    background-color: aquamarine;
}
```
