---
title: About internals of Git
layout: post
tags: [git]
---

갑자기 Git의 내부가 궁금해졌습니다.

## Why?

Git은 개발하는 사람이라면 거의 대부분 사용하고 있을, 잘 알려진 버전 관리 툴이죠.

그간 잘 사용하고 있었는데, 어느 순간 제 자신이 Git에 대해서 하나도 아는게 없다는 걸 깨달았습니다.
아마 David Wickes의 [Why you shouldn't use a web framework](https://dev.to/gypsydave5/why-you-shouldnt-use-a-web-framework-3g24)라는 글을 본 후였을거에요.

제목과는 조금 다른 내용이긴 하지만, 한 번 읽어보면 초심자의 입장에서 꽤나 도움이 됩니다. 물론 조금은 주의해야할 것이 있겠지만요.
(개인 프로젝트의 프론트 프레임워크를 써야할지 말아야할지 고민하고 있을 때 답을 얻었습니다..)

어쨌든 Git이 어떻게 동작하는지, 그 동작 원리가 궁금해져서 Git 홈페이지에 있는 [Pro Git](https://git-scm.com/book/en/v2)이라는 책의 마지막 챕터,
[Git Internals](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain)를 살펴보기 시작했습니다.

이 글은 Git Internals의 간략한 요약이자 정리로 이해하시면 좋을 것 같습니다.

## Plubming and Porcelain
