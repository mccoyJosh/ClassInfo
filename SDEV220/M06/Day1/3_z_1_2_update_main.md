# UPDATING MAIN

With all of this CSS, we can now update our main page to not make it look horrible:

All we need to do is

- create css file
- direct html to css file
- use some tags probably within our html

Let's see how that looks!

# CSS

```css
body {
    background-color: rgb(255, 221, 146);
    font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif
}

header {
    border-radius: 50px;
    font-size:large;
    text-align: center;
    color: white;
    background-color: #da9351;
}

header a {
    color: white;
}

#epic {
    font-size: 25px;
    font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
}

#outer_post {
    padding: 20px;
}

#post {
    border-radius: 15px 50px;
    background: #fff5ce;
    padding: 1px;
    padding-left: 40px;
}

#post p {
    font-family: cursive;
    font-size: 30px;
    font-weight: 900;
}

#post_header {
    font-size:large
}

#button {
    border-radius: 15px;
    background: #f06630;
    border-color: rgb(230, 111, 14);
    border-style: solid;
    border-width: 5px;
    width: 50px;
    text-align: center;
    color: white;
    text-decoration: none;
}
```

# HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Home</title>
    <link rel="stylesheet" href="static/css/main.css">
</head>
<body>
    <header>
        <h1>Epic App</h1>
        <nav>
            |
            <a href="/trending">
                Trending
            </a> |
            <a href="/search">
                Search
            </a> |
            <a href="/login">
                Login
            </a> |
        </nav>
    </header>

    <main>
        <em>Welcome to the super awesome social media here!</em>
        <em>I am glad social media is always so wholesome and epic and awesome and good for society</em>
        <br>
        <em>Here are our top posts from today:</em>
        <div>
            {% for post in posts %}
                <div id="outer_post">
                    <div id="post">
                        <div id="post_header">
                            <a id="epic">{{ post.epic_value }} </a>
                            <a href="" id="button" >EPIC</a>
                            <a href="topics/{{post.topic}}"> {{ post.topic }} </a> / <a> {{ post.author }}  </a>
                        </div>
                        <p> {{ post.text }} </p>
                   </div>
                </div>
            {% endfor %}
        </div> 
    </main>

    <footer>
        <hr/>
        FOOTER FOOTER FOOTER FOOTER FOOTER FOOTER FOOTER FOOTER FOOTER FOOTER FOOTER FOOTER
    </footer>
</body>
</html>
```

Now our website is looking a little bit better!