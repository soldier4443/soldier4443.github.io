---
title: "Cloud IDE - Cloud9"
layout: post
tags:
  - aws
  - cloud
  - cloud9
excerpt: 클라우드 상에서 동작하는 IDE인 Cloud9을 소개합니다.
---

AWS(아마존 웹 서비스)는 클라우드에서 동작하는 IDE인 Cloud9을 제공하고 있습니다.

설정도 매우 간단하고, 로컬에서 만들기 귀찮은 환경 설정들을 어느 정도 자동으로 해주고 있어
간단하게 무언가를 배우고싶을 때 사용하기 좋습니다. 원격에서 여러 사용자가 수정해야 하는 경우에도 유용하다고 합니다.

기본적으로 Cloud9은 EC2 Instance 위에서 동작합니다. 해당하는 설정을 담은 파일은
HOME 디렉토리의 .c9 폴더인 것으로 보입니다. Git처럼 이 파일 하나만 관리하면 되서 간단하고 좋은 것 같네요.

<br>

## Usage

AWS 콘솔에서 [Cloud9](https://ap-southeast-1.console.aws.amazon.com/cloud9/home?region=ap-southeast-1)으로 들어간 다음,
**[Create Environment]**를 누르고 몇 가지 설정을 입력하기만 하면 됩니다.

### Hosted by EC2

Cloud9 환경은 기본적으로 EC2의 Amazon Linux 위에서 동작합니다.
아마 아마존 EC2를 사용해보신 분들이라면 아주 쉽게 이해하고 사용하실 수 있을거에요.
30분 동안 아무런 동작이 없으면 자동으로 휴면 상태에 들어가서 비용이 갑자기 마구마구 늘어나는 걱정도 안 해도 될 것 같구요.

### Share with others

클라우드 환경의 장점은 뭐니뭐니해도 여럿이 함께 작업할 수 있다는 것이겠죠!
cloud9 IDE를 다른사람에게 공유하려면 오른쪽 상단의 **[Share]** 버튼을 클릭하고 **"Environment"**란에 있는 주소를 다른 사람에게 공유하면 됩니다.

<img src="/images/2018/using-cloud9-sharing-with-others.PNG" width="100%">

<br>

## 사용 후기

먼저 조금 아쉬운 점은 Cloud9이 서울 리전에서 지원하지 않아서 옆 동네 싱가포르 리전을 이용해야 한다는게 있구요.

단점으로는, 일단 웹브라우저 상에서 동작하는 IDE이다 보니 일반적으로 창을 닫는 __[Ctrl-W]__ 같은 단축키를 브라우저에서 받아서
창 자체를 꺼버리는(...) 상황이 발생합니다. 그래서 __[Alt-W]__와 같이 별도의 단축키를 제공하고 있지만
익숙하지 못한 새로운 명령어를 익혀야 한다는 점이 가장 아쉽습니다. 비슷한 맥락으로 Visual Studio Code나,
Sublime Text같이 좋은 텍스트 에디터를 사용하지 못한다는 것도 있겠네요.

그리고 클라우드 환경에다가 Amazon Linux를 사용하기 때문에 일반적인 실행 환경과는 다르게 동작할 가능성이 있습니다.
저는 MongoDB를 사용할 때 기존에 리눅스에서 하던 방식으로 했다가 안되서 조금 헤메인 기억이 있습니다..

그래도 웹 기반의 IDE이 치고는 상당히 깔끔하게 동작하고,
디자인도 수려한 편이어서 나름 적응하면 쓰기 괜찮을 것 같습니다.
