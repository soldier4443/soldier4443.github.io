---
title: Liquid 템플릿 언어로 TIL 관리하기
layout: post
tags: [liquid, blog]
excerpt: 늘어나는 TIL를 관리할 방법이 필요합니다.
---

TIL 포스트가 늘어남에 따라서 기존 포스트가 가려서 보이지 않는 지경에 다다랐는데요. TIL 포스트는 매일매일 기록하는 일기와도 같은 것이라, 굳이 페이지 상단에 노출시켜야할 필요는 없습니다.

조금 시간을 내서 이 TIL 포스트를 정리할 수 있는 방법을 찾아봤습니다.

<br>

## Approach

##### Github pages, Jekyll, Liquid

우선 이 블로그는 [Github pages](https://pages.github.com/)를 통해서 만들어졌는데,
자세한 내용은 잘 모르지만 **Jekyll**이라는 정적 사이트 생성기를 사용하고 있다는 점은 알고 있었습니다.

Jekyll은 몇 가지 작업을 통해서 쉽고 빠르게 정적인 사이트를 만들 수 있게 도와줍니다. 여기서는 **Liquid**라는 [템플릿 언어](https://stackoverflow.com/questions/4026597/what-is-a-templating-language)를 사용합니다. 관련 문서는 [여기](https://shopify.github.io/liquid/) 있습니다.

<br>

##### Configuration

먼저 `_config.yml` 파일을 보니 `navigation` 부분에 페이지 상단 헤더부분에 있는 "About", "Archive" 등의 탭이 있는 걸 확인할 수 있었습니다.

이곳에 TIL를 보관할 탭 하나를 더 추가했습니다.

```
  navigation:
    - name: About
      url: /about
    - name: Archive
      url: /archive
+   - name: TIL
+     url: /til
    - name: Tags
      url: /tags
```

<br>

파일들을 조금 살펴보니 `about.md`, `archive/index.html`과 같이 `_config.yml`에서 정의한 탭에 해당하는 문서가 하나씩 있었습니다.

우선은 `archive/index.html`을 복사해서 `til/index.html`을 만들었습니다. 이 문서 상단에는 다음과 같은 헤더가 있는데, 이 부분을 `_config.yml`에 정의한 대로 수정해줘야 합니다.

```
  layout: page
- title: Archive
- permalink: /archive/
+ title: TIL
+ permalink: /til/
```

<br>

##### Edit layouts

이제 메인 페이지, 아카이브에서 기존에 보여주던 TIL를 모두 가려야합니다.

<br>

1. TIL 구분하기

   첫 번째 단계는 포스트가 TIL인지 아닌지 구분하는 작업입니다.

   그 동안 이럴 때를 염두해서 사이트 상단에 작성하는 `tags`에 `til`를 포함해서 작성했기 때문에, 생각보다 어렵지 않았습니다.

   ```
   ---
   ...
   tags: [til]
   ...
   ---
   ```

   Jekyll에서는 `site.posts`를 통해서 사이트의 모든 포스트에 접근할 수 있고, `post.tags`를 통해서 해당 포스트가 가지고 있는 태그 목록을 알 수 있습니다.

   ```
   {% raw %}{% for post in site.posts %}
     {{post.tags}}
   {% endfor %}{% endraw %}
   ```

   <br>

2. TIL일 경우 숨기기 (main, archive)

   다음 단계는 TIL일 경우 포스트를 보여주지 않는 작업입니다.

   `post.tags`로 태그 목록을 확인할 수 있으니, 이 중 `til`가 포함되어 있지 않은 경우에만 보여주도록 하면 되겠죠.

   기존에 포스트를 보여주는 부분을 다음과 같이 unless 문 내에 포함시켰습니다.

   ```
   {% raw %}{% for post in site.posts %}
     {% unless post.tags contains 'til' %}
       Rest of contents..
     {% endunless %}
   {% endfor %}{% endraw %}
   ```

   <br>

3. TIL일 경우 숨기기 (til)

   이와 정 반대의 경우인데, 정말 간단하죠. `til`가 태그에 포함되어 있는 경우에만 보여주도록 하면 됩니다.

   ```
   {% raw %}{% for post in site.posts %}
     {% if post.tags contains 'til' %}
       Rest of contents..
     {% endif %}
   {% endfor %}{% endraw %}
   ```

<br>

##### Pagination?

작업을 하다보니 문제가 하나 있었습니다.

기존에 메인 페이지에서는 Pagination(한 번에 전체 포스트를 보여주지 않고 5개, 10개 등으로 묶어서 페이지마다 한 묶음씩 보여주는 것)을 하고 있었는데,

이미 Pagination이 적용된 포스트 묶음 내에서 필터링을 하니 한 번에 5개를 보여줘야하는데 3개를 보여주는 등의 문제가 생겼습니다.

즉 필터링을 거친 후 페이지네이션을 적용해야 하는데, 페이지네이션을 적용한 후 필터링을 해서 생기는 문제입니다.

<br>

조사를 조금 해봤는데, [jekyll-paginator-v2](https://github.com/sverrirs/jekyll-paginate-v2)에서 tag를 필터링할 수 있는 기능이 있는 것 같습니다.

문제는 github-pages에서 이 플러그인을 지원하지 않는다는 것이라.. 어떻게 할 수 있는 방법이 없는 것 같습니다. 그래서 부득이하게 Pagination을 삭제했습니다 ㅠ

<br>

뭐, 또 방법을 찾을 수 있겠죠.