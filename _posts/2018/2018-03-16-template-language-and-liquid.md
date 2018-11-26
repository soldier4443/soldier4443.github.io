---
title: "Template language and Liquid"
layout: post
tags:
  - jekyll
  - liquid
excerpt: 템플릿 언어가 무엇인지 알아보고, Liquid를 사용해봅니다.
---

## 시작은..

Github blog를 열고 나서, 테마가 어떻게 구현되있는지 구경도 하고 제 필요에 따라서 커스텀도 할 목적으로
`index.html`, `blog.html` 등의 파일을 열어 보았습니다. 그 중에 다음과 같은 문장이 있더군요.

{% raw %}
  `{% include nav.html %}`
{% endraw %}

`nav.html`가 이 자리에 포함된다는 것은 이해했지만, 어떤 구문인지, 어떻게 활용할 수 있는지 궁금증이 생겼습니다.

Jekyll을 제대로 활용하고 자기 입맛대로 커스터마이징하기 위해서는 Liquid가 무엇이고 어떻게 활용할 수 있는지 알면 좋습니다. 이제 막 Github 블로그를 시작한 분들이 이 글을 읽고 조금이나마 팁을 얻어가면 좋겠네요.

<br/>



## Template Language

어떤 문장 안에 코드가 포함되는 식으로, 즉 **문장이 코드를 감싸는 식으로** 동작할 때 그 언어를 템플릿 언어라고 부릅니다.

예를 한 번 들어볼까요. 아래 문장은 템플릿 언어가 아닙니다. 코드가 우리가 표현하고자 하는 문장을 감싸고 있기 때문이죠.

`println("My name is " + author)`

그와는 달리 아래의 문장은 템플릿 언어라고 할 수 있을 것 같습니다. 코드는 거의 등장하지 않고, 문장 속에 포함되어 있습니다.

{% raw %}
  `My name is {{ page.author }}`
{% endraw %}

<br/>



## Web Template System

우리가 탐험하는 이 웹이라는 세상에는 수 많은 웹 사이트가 있고, 각각의 웹 사이트들은 정보를 제공하거나, 사용자와 상호작용을 하는 등의 다양한 기능을 수행합니다.

웹이 등장한 초기에는 정적인 컨텐츠를 표현하는 Html밖에 없었기 때문에 사용자에 따라 필요한 정보를 제공하거나, 시간에 따라서 사이트의 디자인을 바꾸는 등의 작업이 가능하지 않았습니다.

[Web Template System](https://en.wikipedia.org/wiki/Web_template_system)은 **동일한 하나의 템플릿을 가지고, 다양한 웹 사이트를 만들어내는 기술**입니다. 일종의 중복 제거인 셈이죠. 방금 전에 이야기한 Template Language는 바로 여기에서 사용됩니다.

사이트를 작성하는 사람들은 달라질 가능성이 있는, 혹은 달라지게 하고 싶은 정보를 템플릿 언어로 명시한 다음, 필요한 시점에 원하는 정보로 대체하는 방법을 사용합니다. 이로서 동적인 사이트의 구현이 가능합니다.

Web Template System의 종류에는 크게 세 가지가 있는데, 간단하게 정리를 한다면 다음과 같습니다:

- ##### Server-side systems
  대부분의 시스템들이 여기에 해당합니다. 서버에서 디비 등에서 가져온 데이터를 바인딩하고
  브라우저는 그것을 사용자에게 보여주는 방식으로, PHP가 대표적입니다.

- ##### Client-side systems
  사용자의 액션에 의해서 생기는 여러 정보들을 가지고 웹브라우저가 서버에서 받아온
  기존의 웹 페이지를 수정한 후 보여주는 방식. 대표적으로 JavaScript같은 것들이 있습니다.

- ##### Static site generators
  대표적으로 지금 제가 사용하고 있는 **Jekyll**이 있습니다. 여기서 사용하는 템플릿 언어가 바로 Ruby 기반의 **Liquid**입니다.

이 중에서 마지막, 정적 페이지 생성에 사용되는 Liquid에 대해서 알아볼게요.

<br/>



## Liquid

정적 페이지를 생성하는 플랫폼인 Jekyll은 템플릿 언어(혹은, 템플릿 엔진)으로 Liquid를 사용합니다.

Liquid에는 **Object**, **Tag**, **Filter** 라는 세 가지의 핵심 개념이 존재합니다.

{% raw %}
- Object는 **컨텐츠를 보여줄 때** 사용합니다.
  
  `{{ site.posts.size }}`

- Tag는 **제어의 흐름을** 결정합니다.
  
  `{% if site.posts.size >= 10 %}`

- Filter는 Liquid Object의 **결과에 변형을 가할 때** 사용합니다.
  
  `{{ "/blog/" | absolute_url }}`

  위 문장은 사이트의 절대 경로를 Liquid Object 앞에 붙이는 기능을 합니다. `http://blog.turastory.com/blog/`처럼 말이죠.
{% endraw %}

아래의 예시는 몇 가지 Liquid 구문을 보여줍니다.

##### Input - Author of the page
{% raw %}
```
{{ page.title }}
```
{% endraw %}

##### Output
```
{{ page.title }}
```

##### Input - Number of posts
{% raw %}
```
{% if site.posts.size >= 10 %}
  This site has at least 10 posts.
{% else %}
  This site has less than 10 posts, which is {{ site.posts.size }}
{% endif %}
```
{% endraw %}

##### Output
```
{% if site.posts.size >= 10 %} This site has at least 10 posts.
{% else %} This site has less than 10 posts, which is {{ site.posts.size }} {% endif %}```

Liquid 구문에 대한 자세한 내용이 궁금하신 분들은 [Liquid 공식 레퍼런스](https://shopify.github.io/liquid/)에서 확인하세요.
저는 Liquid 자체에 대한 내용보다, Liquid가 어떻게 Jekyll과 함께 어우러지는지 살펴보겠습니다.

<br/>


## Liquid with Jekyll

Jekyll은 상당히 많은 부분을 Liquid 확장으로 지원하고 있습니다. [사이트의 메타 정보, 페이지의 정보](http://jekyllrb-ko.github.io/docs/variables/) 등이죠.
그리고 몇 가지 [추가적인 태그와 필터](http://jekyllrb-ko.github.io/docs/templates/)도 지원하고 있습니다.

아래는 해당하는 몇 가지 예시입니다.

##### Input - Display created date
{% raw %}
```
{{page.date | date_to_string}}
```
{% endraw %}
##### Output
```
{{page.date | date_to_string}}
```

##### Input - Include another file
{% raw %}
```
{% include head.html %}
```
{% endraw %}

<br/>


## Summary

Liquid는 보다 쉽고 간결한 페이지 생성을 위한 템플릿 언어 - 혹은 템플릿 엔진입니다.
헥심은 바로 Object와 Tag, Filter가 무엇인지, 그리고 어떻게 활용할 수 있는지 아는 것 같습니다.

기본적인 건 모두 다 배운 것 같으니.. 이제 실제로 써먹는 일만 남았네요.
조금 경험이 쌓이면 Cheetsheet를 만들어볼게요.
