from django.contrib.auth.models import User
from .models import Post
from .models import Topic
from random import randrange
from django.http import HttpResponse

topic_list = ['Food', 'Gaming', 'Politics', 'History', 'Aliens', 'Computers', 'I_Hate_Computers', 'Sports',
              'Technology', 'News', 'Straight_Up_Being_Evil', 'Epic_Moments', 'Nice People :)', 'Music']


def insert_everything(request):
    insert_some_topics(False)
    insert_some_posts()
    return HttpResponse('Hopefully no errors!')


def insert_everything_ignore(request):
    insert_some_topics(True)
    insert_some_posts()
    return HttpResponse('REALLY hopefully no errors!')


def insert_some_topics(ignore):
    if not ignore:
        all_topics = Topic.objects.all()
        if len(all_topics) > 0:
            return
    admin_user = User.objects.get(username='admin')
    for topic in topic_list:
        Topic.objects.create(author=admin_user, name=topic)


def insert_some_posts():
    all_posts = Post.objects.all()
    if len(all_posts) > 0:
        return
    admin_user = User.objects.get(username='admin')
    last_topic = topic_list[len(topic_list) - 1]
    for topic in topic_list:
        this_topic_obj = Topic.objects.get(name=topic)
        texts = []
        texts.append(f'I love the topic of {topic}')
        texts.append(f'People in the topic of {topic} have become too means >:(')
        texts.append(f'I think aliens have somehow affected {topic}')
        texts.append(f'Big famous guy stinks right now!')
        texts.append(f'Small guy is epic!!!')
        texts.append(
            f'The {topic} community is dying! Please repost and like and subscribe to make sure {topic} doesn\'t die out')
        texts.append(f'Money influencing {topic} is probably not good')
        texts.append(f'EPIC MOMENT TODAY FOR ALL FANS OF {topic}')
        texts.append(f'Dating Advice?')
        texts.append(f'Why is everyone in {topic} always talking about {topic}!!! IMO, this is silly')
        texts.append(f'New to {topic}; where to start?')
        texts.append(f'Not sure how to feel about recent thing in {topic}')
        texts.append(f'I\'m scared')
        texts.append(f'I think pizza is pretty good, but you can argue with me if you want')
        texts.append(f'Which one is better: {topic} or {last_topic}?? >>> DEBATE')
        last_topic = topic

        for text_text in texts:
            random_epic_number = randrange(4000)

            Post.objects.create(
                author=admin_user,
                topic=this_topic_obj,
                text=text_text,
                epic_value=random_epic_number,
                visible=True
            )
