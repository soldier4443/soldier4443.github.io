---
title: "유니티 NetworkManager"
layout: post
tags:
  - unity
excerpt: 이번 포스트에서는 유니티에서 네트워크 작업을 쉽게 해주는 NetworkManager에 대해서 알아봅니다.
---

<img src="/images/2017/network_manager_thumbnail.png" width="200" class="center"/>

### NetworkManager / NetworkManagerHUD

유니티에서 네트워크 관리를 편리하게 할 수 있도록 개발자들에게 제공하는 기능이 있습니다.
이름만 들어도 관리를 잘할 것 같은 `NetworkManager`는 High-Level API로 작성되어 손쉽게 커스터마이징할 수 있다고 합니다.
유니티 레퍼런스에서 언급하는 `NetworkManager`의 대표적인 기능은 아래와 같습니다.

 - 게임 상태 관리 (Client, Server, Host 손쉽게 사용 가능)
 - 리스폰 관리
 - Scene 관리 (Online, Offline Scene 등 상태에 따른 Scene Transition)
 - 디버깅 정보 제공
 - 매치메이킹 서비스
 - 손쉬운 커스터마이징!

`NetworkManager` 컴포넌트는 다른 컴포넌트들과 마찬가지로, Inspector를 통해서 추가할 수 있습니다.

<img src="/images/2017/unity-network-components-2/network-manager.PNG" width="280" />

`NetworkManagerHUD` 컴포넌트는 프로젝트를 처음 진행할 때 유용한 컴포넌트입니다.
실행했을 때 GUI 창을 하나 띄워서 네트워크 상태를 조절할 수 있도록 해줍니다.

<img src="/images/2017/unity-network-components-2/network-manager-hud.PNG" width="280" />

이제 NetworkManager의 기능을 하나씩 알아볼까요?

<br/>

### 게임 상태 관리

멀티플레이어 게임에는 세 가지 유형의 접속 방식이 있습니다.

- Server : 연결할 수 있는 서버입니다.
- Client : 접속할 서버가 필요한 클라이언트입니다.
- Host : 서버이면서 동시에 클라이언트인 호스트입니다.

각 유형별로 시작할 수 있는 `NetworkManager`의 메서드는 다음과 같습니다.

- Server : StartServer()
- Client : StartClient()
- Host : StartHost()

이 세 가지 메서드는 `NetworkManagerHUD` 컴포넌트에서도 실행할 수 있습니다.

<img src="/images/2017/unity-network-components-2/network-manager-hud-gui.PNG" width="280" />

어떤 방식으로 시작하든, `NetworkManager`의 `networkAddress`와 `networkPort`가 설정됩니다.

서버나 호스트의 경우 `networkPort`는 열린 포트가 되고, 클라이언트의 경우
`networkAddress`는 연결되는 주소, `networkPort`는 연결되는 포트를 나타냅니다.

<br/>

### 스폰 제어

`NetworkManager`는 게임을 시작하면 플레이어가 리스폰되는 기능을 제공합니다.
`Player Prefab` 항목에 원하는 플레이어 프리팹을 가져다 놓으면 이 기능을 사용할 수 있습니다.

<img src="/images/2017/unity-network-components-2/network-manager-spawn-info.PNG" width="280" />

기본적으로는 클라이언트로 접속하면 캐릭터가 스폰되고, 접속을 끊으면 캐릭터가 사라지게 됩니다.
만약 이 동작을 바꾸고싶다면 `NetworkManager.OnServerAddPlayer()` 메소드를 오버라이딩해서
직접 동작을 작성하면 됩니다. 레퍼런스를 참고해서 말이지요...

플레이어가 아닌 다른 `GameObject`를 네트워크 상에 생성하고 싶다면 먼저 `NetworkManager`에게 등록해야합니다.

`NetworkManager` 컴포넌트의 `Spawn Info`에서 `Registered Spawnable Prefabs` 목록에 프리팹을 추가하거나,
`ClientScene.RegisterPrefab()` 메소드를 호출해 스크립트 상에서 추가할 수도 있습니다.

```
ClientScene.RegisterPrefab (playerObject);
```

#### 시작 위치

시작 위치를 명시하는 것도 가능합니다. 아래의 스크린샷을 보세요.

<img src="/images/2017/unity-network-components-2/network-manager-starting-point.PNG" width="480" />

`NetworkManager`는 연결이 되면 `NetworkStartPosition`을 가진 GameObject를 찾아서 스폰할 때 사용합니다.

<br/>

#### 참고 자료
 - [유니티 레퍼런스](https://docs.unity3d.com/Manual/UNetManager.html)
