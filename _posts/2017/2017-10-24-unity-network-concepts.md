---
title: "유니티 Network 개념 정리"
layout: post
tags: 
  - unity
excerpt: 유니티 네트워크에서 중요한 세 가지 클래스를 알아봅니다.
---

### NetworkBehaviour 클래스

`NetworkBehavior` 클래스는 `MonoBehaviour`를 상속받은 클래스로써,
네트워크에 관련된 기능을 사용하려는 스크립트에서 `MonoBehaviour` 대신 상속받습니다.

```
public class BallOnNetwork : NetworkBehavior {
    ...
```

`NetworkBehaviour`를 사용하면 좋은 점을 정리 해보았습니다.

 - 네트워크 관련 여러 액션 수행
 - 네트워크 관련 콜백 호출 가능
 - 자동으로 서버와 클라이언트 간 동기화

이 `NetworkBehaviour`를 사용하기 위해서는 `NetworkIdentity`라는 컴포넌트가 필요하다고 합니다.

<br/>

### NetworkIdentity 컴포넌트

`NetworkIdentity`는 지극히 단순한 컴포넌트입니다. 네트워크 내에서 특정 GameObject를 구분하기 위해서 필요하죠.
서버는 `NetworkIdentity`를 가지고 있는 GameObject를 생성할 때, `NetworkIdentity.NetworkInstanceId`를 새로 할당하고
이를 클라이언트에서 설정하게 됩니다. 일종의 주민등록번호라고 생각하면 좋을 것 같네요.

기본적으로 네트워크가 들어가는 게임에서, 네트워크 액션(서버 생성, 클라이언트 접속 등)에 따라
GameObject를 제어하기 위해서는 이 `NetworkIdentity` 컴포넌트가 꼭 필요합니다.
조금 전에 언급한 `NetworkBehaviour`를 사용하기 위해서도 필요하다는 걸 확인했습니다.

<br/>

### NetworkTransform 컴포넌트

`NetworkTransform`은 네트워크 상에서 오브젝트의 움직임을 동기화하기 위해서 필요한 컴포넌트입니다.
이 컴포넌트가 없으면 로컬에서 내가 플레이어를 움직여도 상대방의 화면에서는 가만히 있는 것처럼 보이게 되죠.

누가 권한을 가지느냐에 따라서 두 가지 방식으로 동작합니다.

- Authority on Client

  클라이언트가 제어를 하고, 변경 사항이 서버로 전송되어 반영된 후 다시 다른 클라이언트로 뿌려집니다.
  일반적인 플레이어 오브젝트가 이에 해당하죠. (각 클라이언트 별로 고유)

- Authority on Server

  서버가 제어를 하고, 변경 사항이 연결된 클라이언트들에게 뿌려집니다.
  중립 몬스터와 같이 공통적으로 적용되는 것들에게 적합할 것 같네요.

<br/>

#### 참고 자료
 - [유니티 레퍼런스](https://docs.unity3d.com/ScriptReference/Networking.NetworkBehaviour.html)
