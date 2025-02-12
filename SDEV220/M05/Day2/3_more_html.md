# More Advanced HTML

So, we really only showed a LITTLE TINY BIT of HTML,
let's get into more HTML infoL

# Head V Body

So we have seen the HTML body, the thing actually containing the 
THINGS WE WANT TO DISPLAY.

Now, there is a lot more information that goes into a webpage other than what we see,
and we need a place for a lot of that.

This is where the HEAD comes in. We can a lot of things here, one such thing is the TITLE of the
page. This will populate the things like the name displayed on your tab.

Here is a small example:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>I'm in the tab AHHH</title>
    </head>
    <body>
        <p>Words and what not</p>
    </body>
</html>
```

A few things to note here:
- the head and body tags are both contained within the greater html tag, but not within each other.
- We need to make sure all the inner tags of another tag needs to be closed and done before we can close the current tag; otherwise we would experience some sort of syntax error
- I can add all of this as an additional page to my RUNNING service and still access it without re-running the entire service. This is due to django's dynamic nature
- The head comes before the body in this example, but this is merely typical of a html document, and not NECESSARY (it can come after it, for instance)

# Many, Many Other Tags

In html, there are many, many other tags to describe different things.

-----------------

# Fonts and Things

## Headers (h1, h2, h3 ...)

Making a header in html is very easy, just use the header tag, h1
Then there's h2 and h3... The only different between these tags is the size of the 
header. As the number gets bigger, the smaller the header gets.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Example</title>
</head>
    <body>
        <h1>BIG</h1>
        <h2>BIG</h2>
        <h3>BIG</h3>
        <h4>BIG</h4>
        <p>Small, normal text</p>
    </body>
</html>
```


## em and strong

These both format the text within it differently. The `em` tag will _italicize_ the text by default, and
the `strong` tag will **bold** it. They are both used to emphasize the text.

```html
    <em>Whoa</em>
    <strong>Whoa</strong>
    <p>Whoa</p>
```


--------------------

# Functional Tags

## a (LINKS)

The `a` tag is used to designate links.
This is used just like the other tags, BUT, for the link to work properly, we need
to actually give it some sort of link to go to. This is where we get to use another **attribute**

<h4>The attribute we want to use here is <em>href</em></h4>. NOTE, we want to put the link within double quotes like a string

```html
        <a href="https://www.bing.com">I am a link to the best search engine!</a>
        <p>I am not a link, but a mere piece of text :(</p>
```

To link to a page within our own website, we just need to provide it with
the url extended from the root page.

For example, we need DON'T need to put localhost:8000/simple to get
to the previously made simple page, just `/simple`

```html
        <a href="/simple">To the SIMPLE PAGE</a>
```

------------

# Structures

## br

To add a line break on your page, use br.

This essentially acts as a \n or newline character in other languages

```html
        <p>Here is some <br>text interrupted by a line break</p>
        <p>Here is some text otherwise</p>
```

## hr

Adds a HORIZONTAL line to break up your page:

```html
        <p>Top Text</p>
        <hr/>
        <p>Bottom Text</p>
```

## lists (ul and li)

To automatically render your text into a list of some sort, you can use ul + li to do so.

Use UL to distinguish the beginning and end of your list, and LI to distinguish the beginning and end of each list item
Here is an example:
```html
        <p>Here are my favorite foods:</p>
        <ul>
            <li>Apple</li>
            <li>Spinach</li>
            <li>Strawberries</li>
            <li>Carrot</li>
            <li>Lettuce</li>
            <li>Asparagus</li>
        </ul>
```

------

# Organization

These upcoming tags are good to know, BUT, without properly adding
formatting to you page, these may appear unchanged compared to just using no
tag at all!

These more help in designing our page!!!

Also, there are many, MANY programs which rely on your html page to be
using these different organizational tags to find specific information.

For instance, we will see the NAV tag, and it is used by some programs
to get rid of that section as to only view the text on the screen (since the nav
wouldn't be essential)

## nav

NAV is used to list out NAVIGATIONAL links.
You could use it, for instance, to list out all the different MAIN links on your website.

Nav will by default list its content in a header type structure (on the same line)

Here is an example:

```html
        <nav>
            <a href="/simple">Simple</a> |
            <a href="/test">Test</a> |
            <a href="/">Home</a> |
        </nav>
```

## div

div stands for division

div is used to distinguish a particular section of your page.
Again, it bears to change on the text simple by itself.

This is more for the custom division that will need to be done

```html
        <p>Bingo</p>
        <div>
            <p>Bingo</p>
        </div>
        <div>
            <div>
                <div>
                    <div>
                        <div>
                            <p>Bingo</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
```

## article

This is used, typically, to hold an article

```html
        <article>
            Here is an article
        </article>
```


## section

This is used, typically, to hold an article

```html
        <section>
            Here is a section 
        </section>
```

## header

This is used, typically, to hold a header

There are some rules with the header, for instance, it
can't be the descendent of a footer tag.

```html
        <header>
            Here is a header, and it is typically found at the top of your page
        </header>
```

## main

This is used, typically, to bear the main content of your page.

Just like the header tag, the main tag has some rules as well, for instance, it cannot the descendent of these
tags:

- article
- aside
- footer
- header
- nav

Also, to note: it is not enforced by languages and renderers (like django) to follow these 'rules'

```html
        <main>
            THIS IS THE MAIN STUFF
        </main>
```



## footer

This is used, typically, to hold a footer

```html
        <footer>
            Here is a footer, and it is typically found at the bottom of your page
        </footer>
```

----

# Tooling

## time

As you might suspect, the time tag is used to hold information about time


## img

With img you can display images

If placed in a file in templates, under normal conditions, this would put the image on the file.
However, since we are within django, we are at its mercy and this does not work at the moment, but we shall fix this later.

```html
<p>Important Guy:</p>
<img src="important.jpg" alt="important guy"/>
<hr/>
<p>Bottom Text</p>
```

# We can make a 'better' looking page now though

See day_social/templates/main_page.html

Still looks pretty ugly! We will fix that soon!