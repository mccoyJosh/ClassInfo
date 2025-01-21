# Django Introduction

Django is simply a web framework and it is what you are going to use for this class!

## Networks Intro

[See this](https://tutorial.djangogirls.org/en/how_the_internet_works/)

Networks are like mail!

You want to talk to someone, so you send them mail.
Post office uses the address to determine where to send it. 
The other people has a return address so they can return the favor and send you the message.

In the computer world, instead of addresses, your computer and the place you want to connect to
have IP addresses. When you want to connect to a website, you are essentially sending a require ASKING
that server for the website (the HTML for it), and them taking the request and responding
to your IP address with said HTML. Now, typically an IP address is a string of numbers like
123.456.790.111... which normally, you don't need to type in.

What typically happens is you connect to a website URL, like https://github.com, and a DNS (Domain Name System)
converts the website to an IP address. At that point, its simply your two IP addresses asking for files (HTML, JSON, ~other~ info) and the other one responding.

In this class, we are going to be using a framework which sets up one of these servers for us. We
are simply going to be responsible for creating the pages and backend for said server.

## Show off Django Example

Start server (inside of S_DJANGO_EXAMPLE directory)

```
python manage.py runserver
```

