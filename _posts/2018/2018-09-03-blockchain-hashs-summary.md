---
title: "블록 체인의 Building Block: Hash"
layout: post
tags:
  - blockchain
  - cryptography
excerpt: 블록 체인에서 다른 모든 것들의 기초가 되는 Hash를 알아볼까요?
---

블록 체인의 근간을 이루는 Hash에 대한 개념을 정리해보았습니다.

## Hash Function

블록 체인에서 빼놓고 이야기할 수 없는 것 중 하나가 바로 [Hash Function][hash-wikipedia]입니다.

Hash Function은 **어떤 입력을 고정된 입력으로 매핑**하는 함수인데요. 암호학에서는 **어떤 값을 해시 값으로 바꾸는 건 쉽지만 다시 돌리는 건 어렵다**는 점을 이용해 여러 분야의 보안에 활용하고 있습니다.

Hash Tree를 이야기할 때 아래 그림과 같이 `x`의 해시 값을 `h(x)`으로 정의해서 사용하겠습니다.

<img src="/images/2018/hash/hash-function.PNG" class="image fit" style="width: 480px" alt="해시 함수">

## Hash Chain

Hash Chain은 해시 함수의 개념을 확장한 것으로,
해시 함수의 결과에 **다시 해시 함수를 적용**하는 개념이라고 볼 수 있습니다.

<img src="/images/2018/hash/hash-chain.PNG" class="image fit" style="width: 480px" alt="해시 체인">

위의 해시 체인은 초기의 하나에 값에 대한 해시 체인인데요, 여러 값에 대한 해시 체인을 만들 때는
다음과 같이 **각 단계에서 이전 해시값과 새로운 값을 묶어** 새로운 해시를 만드는 방법을 사용해볼 수 있습니다.

<img src="/images/2018/hash/hash-chain-extended.PNG" class="image fit" style="width: 480px" alt="해시 체인 확장">

## Hash Tree

해시 트리는 [이진 트리][binary-tree-wikipedia] 형태로 이루어진 구조입니다. *머클 트리*라고도 합니다.
핵심은 **자식 노드의 해시 값을 가지고 부모 노드의 값을 만든다**는 것이에요.

<img src="/images/2018/hash/hash-tree.PNG" class="image fit" style="width: 480px" alt="해시 트리">

해시 트리를 사용하면 데이터가 무결한지 쉽게 찾아낼 수 있습니다.

먼저 하나의 데이터를 여러 조각으로 쪼개서 해시 트리를 만든 다음 원본 데이터를 전송합니다.

<img src="/images/2018/hash/sender-sends.PNG" class="image fit" style="width: 480px">

받는 쪽에서 이 데이터를 받고 해시 트리를 계산해 보내는 쪽의 해시 트리와 비교합니다.
이 떄 특정 데이터에 문제가 있으면 관련된 트리 계층이 전부 문제가 있을거에요.

<img src="/images/2018/hash/receiver-failed.PNG" class="image fit" style="width: 480px">

어떤 데이터가 문제인지 확인했다면 문제가 있는 데이터만 다시 전송해달라고 부탁할 수 있겠죠?

<img src="/images/2018/hash/sender-resends.PNG" class="image fit" style="width: 480px">

<!-- TODO: 머클 트리 -->


[hash-wikipedia]: https://ko.wikipedia.org/wiki/%ED%95%B4%EC%8B%9C_%ED%95%A8%EC%88%98
[binary-tree-wikipedia]: https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%A7%84_%ED%8A%B8%EB%A6%AC