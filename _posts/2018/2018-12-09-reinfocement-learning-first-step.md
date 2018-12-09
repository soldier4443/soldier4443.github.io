---
title: "강화학습 발 담그기"
layout: post
tags: [ai, reinforcement-learning, ml]
---

이번에 강화학습을 주제로 한 스터디에 참여하게 되었습니다. 기본적인 내용으로 강화학습이 무엇인지 훑고 넘어가는 시간을 가지려고 해요.

<br>

## Prerequisites

- Python

  이야기를 들어가기에 앞서서, 파이썬을 써보지 않으셨다면 한 번쯤 써보는 것을 추천드립니다. 이번 기회에 써보셔도 좋습니다 :)

<br>

## Reinforcement Learning

강화 학습은 사실 우리에게 정말 친숙한 개념입니다. 삶을 살아가면서 우리는 여러 가지 환경을 접하고, 그 환경과 다양한 상호작용을 하면서 새로운 것들을 배우고 성장합니다.

이런 개념을 컴퓨터 상에서 구현해볼 수 있을까요? 우선은 이 추상적인 개념을 조금 더 정형화된 형태로 표현해봐야겠죠. 다음은 위키피디아에서 가져온 이미지입니다.

<img src="/images/2018/reinforcement-learning/reinforcement-learning-diagram.png" class="image fit" style="width: 480px" alt="강화학습 다이어그램">

가장 먼저 눈에 들어오는 Agent는 **환경으로부터 정보를 받고 스스로 학습**하는, 시스템의 주인공입니다. 에이전트가 어떠한 액션을 취하면 먼저 Environment의 상태가 바뀌게 되고, 에이전트에게는 행동에 대한 **보상**이 주어집니다. 기본적으로는 이 **보상을 극대화하는 것**이 바로 에이전트의 목표가 되는 것이에요.

강화 학습이 흔히 기계학습라고 부르는 범주에 속하는 것이긴 하지만, 행동을 하는 주체와 그 주체가 상호작용하는 환경이 있다는 점에서 데이터를 기반으로 특정 도메인에 특화된 모델과 인프라를 만드는 분야와는 조금 다르다는 생각이 드는데요.

이 시스템을 어떻게 구축할 수 있을까요? 다행히 아주 쉽게 이것을 구축할 수 있는 방법이 있답니다.

<br>

## [OpenAI Gym](https://gym.openai.com/)

> We provide the environment; you provide the algorithm.

<img src="/images/2018/reinforcement-learning/openai-gym-environments.gif" class="image fit" style="width: 480px" alt="OpenAI Gym environments">

OpenAI는 AI를 연구/개발하고 공개하는 비영리 연구 기업입니다. 이 곳에서 강화학습을 연구하고 개발하는 사람들을 위해서 Environment를 제공하는 **OpenAI Gym**이라는 것을 만들었답니다.

[이곳](https://gym.openai.com/envs)에서 다양한 환경을 확인해보실 수 있습니다. 간단한 텍스트 기반 환경부터 로보틱스, Atari 게임 등 다양하죠! 물론 필요한 환경이 없다면 형식에 맞게 직접 환경을 만들 수도 있습니다.

<br>

### Setup

일반적인 파이썬 패키지처럼 pip를 통해서 gym을 설치할 수 있습니다.

프로젝트 간 환경 설정 편의를 위해서 [virtualenv](https://virtualenv.pypa.io/en/latest/)를 사용하도록 할게요. `virtualenv`는 파이썬을 가지고 다양한 프로젝트를 구성할 때 독립적인 실행 환경을 만들어주는 도구입니다. 자세한 건 구글링해보세요!

##### Windows

```bash
$ virtualenv venv
$ venv/bin/activate
```

##### Mac/Linux

```bash
$ virtualenv venv
$ source venv/bin/activate
```

가상 환경을 잡은 뒤에는 pip를 이용해서 gym을 설치합니다. 이외에 연산 작업을 하기 위해서 필요한 패키지들도 미리 설치해둘게요.

```bash
(venv) $ pip install gym numpy matplotlib
```

<br>

### Use

Gym의 구성은 매우 간단합니다. 아래는 전체적인 사용 흐름을 보이는 코드입니다.

```python
# 환경 생성
env = gym.make('SpaceInvaders-v0')

for i in range(100):
  state = env.reset() # (1)

  # 끝날 때 까지 반복.
  while True:
    # 다음 액션을 구합니다.
    action = next_action(state, i) # (2)

    # 새로운 상태와 보상을 가져옵니다.
    # 종료됬을 경우 done이 True가 됩니다.
    new_state, reward, done, info = env.step(action) # (3)
    print("Perform {}, State change {} -> {}".format(
      action, state, new_state))

    if done:
      break

    state = new_state
```

1. `env.reset()` - 환경을 초기화합니다.
2. `next_action(state, i)` - 우리가 정의한 사용자 함수입니다. 현재 상태와 step 정보를 가지고 다음에 취할 action을 결정합니다.
   위의 다이어그램에서 agent가 하는 역할이라고 볼 수도 있겠네요.
3. `env.step(action)` - action을 수행합니다. 그 결과로 새로운 상태와 보상, 종료 여부를 얻습니다.

이제 이 Gym API를 이용해서 강화학습 알고리즘을 검증해볼 수 있습니다.

<br>

## Q-learning with tables

먼저 강화학습의 중요한 아이디어 중 하나인 **Q**에 대해서 이야기해볼게요. **Q**는 다음과 같이 정의됩니다.

<img src="/images/2018/reinforcement-learning/q-equation.gif" class="center-image" alt="Q equation">

여기서 S는 state, A는 action, R은 reward를 의미합니다. 즉 **Q**는 **상태와 행동을 입력으로 받아서 예상되는 보상을 반환**하는 함수입니다.

한 가지 상태에서 취할 수 있는 행동의 개수는 물론 여러 가지일 수 있으니, **가능한 모든 행동에 대해서 예상되는 보상을 확인**해보고 그 중 **보상이 가장 최대가 되는 행동**을 취하면 되겠죠?

수학적으로는 다음과 같이 나타낼 수 있습니다.

<img src="/images/2018/reinforcement-learning/next-action-argmax.gif" class="center-image" alt="Q equation">

이제 이 알고리즘은 아주 잘 작동할겁니다. Q가 존재하기만 한다면 말이죠..

### Learning Q

문제는 우리가 처음부터 Q를 알 수 없기 때문에 처음에는 무작위로 이곳 저곳 돌아다니면서 여러 가지 행동을 해보는 수 밖에 없다는 것이에요.

<img src="/images/2018/reinforcement-learning/blind-at-first.png" class="center-image" width="480px" alt="Blind at first">

일단 몇 번 탐색을 하다보면 성공하는 경우와 실패하는 경우(즉 보상을 받은 경우와 그렇지 못한 경우)가 나올 것이고, 이 값을 가지고 **Q**를 학습시키면 우리가 원하는 결과를 얻을 수 있을 것입니다.

전체적인 알고리즘을 표현하면 다음과 같습니다.

1. Q를 초기화합니다.
2. action을 선택합니다.

   이 때 다음과 같은 수식을 사용합니다. 여기서 `s`는 현재 상태, `a`는 취할 행동을 의미합니다.

   <img src="/images/2018/reinforcement-learning/next-action-argmax-small.gif">

3. action을 실행하고 새로운 상태 `s'`과 보상 `r`을 확인합니다.
4. Q를 업데이트합니다. 이 때 다음과 같은 수식을 사용합니다.

   <img src="/images/2018/reinforcement-learning/update-q-initial-small.gif">

   - 첫 번째 항 `r`은 액션을 취했을 때의 보상이므로 당연히 들어가야 합니다.
   - 두 번째 항은 조금 복잡한데요, **미래의 보상의 최대값**을 가지고 현재 보상을 업데이트하게 되므로 단순히 `s`라는 액션을 취했을 때의 보상 뿐만 아니라 그 **이후에 얻을 수 있는 보상까지 고려해서 액션을 선택할 수 있도록** 합니다.

### In Code

이를 코드로 구현하면 다음과 같습니다.

```python
import numpy as np
import random as pr

def rargmax(vector):
  m = np.amax(vector)
  indices = np.nonzero(vector == m)[0]
  return pr.choice(indices)

# 1. Q를 초기화합니다.
state_size = 16
action_size = 4
Q = np.zeros([state_size, action_size])
for i in range(num_episodes):
  state = env.reset()
  done = False

  while not done:
    # 2. state의 모든 action에 대해서 argmax 계산
    action = rargmax(Q[state, :])

    # 3. action을 실행하고 새로운 상태와 보상을 얻습니다.
    new_state, reward, done, info = env.step(action)

    # 4. Q를 업데이트합니다.
    Q[state, action] = reward + np.max(Q[new_state, :])

    state = new_state
```

<br>

## Improvement

지금까지 살펴본 알고리즘은 잘 작동하지만, 몇 가지 문제점이 있습니다.

1. **항상 최적의 경로를 찾지는 못합니다.**

   매 번 Q에게 답을 물어보기 때문에 한 번 Reward를 얻을 수 있는 경로가 마련되면 그 경로가 최적인지(가장 빠른 길인지)는 상관 없이 그 경로로만 움직입니다.

2. **같은 행동을 했을 때 매 번 같은 결과가 나와야만 합니다.**

   가령 "오른쪽으로 움직이기"라는 행동을 취했을 때 항상 오른쪽으로 움직이지 않는다면(아래로 가거나 위로 가기도 한다면), 보상을 찾더라도 그 과정 자체가 매 번 달라질 수 있기 때문에 우리의 알고리즘은 유효하지 않습니다.

이 두 가지 문제에 대한 해결책을 하나씩 알아보겠습니다.

<br>

### Problem 1 - Not optimal path

첫 번째 문제 - 최적의 경로를 찾지 못하는 문제는 `Exploration & Exploit`과 `Sum of discounted rewards`라는 방법을 통해서 해결할 수 있습니다.

<br>

##### Exploration & Exploit

간단한 비유를 통해서 이 개념을 설명해볼 수 있습니다.

```
새로운 곳으로 이사를 왔습니다. A라는 카페를 가봤는데 아주 괜찮습니다.

이후에 카페를 갈 때,
Exploit     - 기존에 알고 있던 것처럼 A를 갈 수도 있고,
Exploration - 좀 더 좋은 카페는 없을지 알아보기 위해서 A가 아니라
              다른 곳을 가보는 새로운 시도를 해볼 수도 있습니다.
```

즉, 다시 이야기하면 **매 번 Q의 말을 듣는 것이 아니라 가끔씩 새로운 시도를 해보는 것**입니다.

```python
# E-greedy method
e = 0.1

if random.random() < e:
  action = randrange(action_size)
else:
  action = rargmax(Q[state, :])
```

다른 방법으로는 기존의 Q 값에 랜덤한 값을 더한 다음 argmax를 구하는 방법이 있습니다.
이 방법의 장점은 기존의 Q 값을 기반으로 random noise를 더하기 때문에 어느 정도의 신뢰성이 보장된다는 것입니다.

```python
# Random noise
random_noise = np.random.random(action_size)
altered_Q = Q[state, :] + random_noise
action = rargmax(altered_Q)
```

<br>

##### Decaying

다음과 같은 상황을 생각해봅시다.

```
새로운 곳으로 이사를 오고 6개월 정도가 지났습니다.
이제 근처의 괜찮은 카페는 모두 알고 있습니다.
더 이상 새로운 시도를 해볼 필요는 없을 것 같습니다.
```

이 말은 즉 **어느 정도 환경에 익숙해지면, 새로운 시도를 할 필요성이 줄어든다**는 것입니다. 이 개념을 `Decaying`이라고 하고, 아주 간단하게 매 번 학습을 할 때마다 `exploration factor`의 값을 줄임으로써 적용해볼 수 있습니다.

```python
decay = 1 / (step + 1)

# E-greedy
e = 0.1 * decay

# Random noise
randon_noise = np.random.random(action_size) * decay
```

<br>

##### Sum of discounted rewards

위의 두 방법을 통해서 새로운 경로를 발견해내긴 했지만, 지금까지는 어느 곳이 최적인지는 알 수 없는 상황이 발생합니다.

가령 아래와 같이 기대 보상이 동일한 경우는 어디로 가야할지 알 수가 없기 때문에 왼쪽과 아래쪽, 둘 중 하나를 랜덤하게 선택하게 됩니다.

<img src="/images/2018/reinforcement-learning/with-no-discounted-rewards.png" class="center-image" alt="Wito no discounted rewards">

`Sum of discounted rewards`를 구해서 이런 상황을 해결할 수 있습니다. 이 역시 비유를 통해서 설명해볼 수 있는데요.

```
(1) 오늘 당장 100만원 받기
(2) 10일 후에 100만원 받기

위 둘 중 하나를 선택하라고 한다면 대부분의 사람이 (1)을 고를 것입니다.
```

핵심 아이디어는 **나중에 받을 보상보다 지금 받을 보상이 더 좋다**는 것입니다. 알고리즘의 (4)번 수식에 `𝛾`라는 상수를 도입해서 이를 표현합니다.

<img src="/images/2018/reinforcement-learning/update-q-discounted-rewards.gif">

`𝛾`의 값을 0~1 사이의 값으로 두면, 미래의 보상을 의미하는 두 번째 항의 값 매 번 업데이트될 때마다 `𝛾`배로 줄어들겠죠. 그래서 이것을 `discounted rewards`라고 부릅니다.

코드로는 다음과 같이 아주 간단하게 구현할 수 있습니다.

```python
# With no discounted rewards
Q[state, action] = reward + np.max(Q[new_state, :])

# With discounted rewards
gamma = 0.9
Q[state, action] = reward + gamma * np.max(Q[new_state, :])
```

`𝛾`를 도입함으로써 아래와 같이 경로의 거리가 Q 값에 반영이 됩니다. 이제 언제나 최적의 해를 찾아갈 수 있겠네요!

<img src="/images/2018/reinforcement-learning/with-discounted-rewards.png" class="center-image" alt="Wito discounted rewards">

<br>

### Problem 2 - Non-deterministic environment

두 번째 문제 - 같은 행동을 해도 다른 결과가 나올 수 있는 환경에서는 `Incremental Learning`이라는 개념을 사용할 수 있습니다.

> 이러한 환경을 Non-deterministic, 혹은 Stochastic environment라고 이야기합니다.

컨셉은 **Q**를 전적으로 신뢰하는 것이 아니라 **일부분만 신뢰하는 것**입니다. Q 값을 모두 그대로 채택하기보다, 기존의 있던 값에 점진적으로 더해가는 방식을 취합니다.

다음과 같이 `α`라는 상수를 추가해서 이 개념을 표현했습니다.

<img src="/images/2018/reinforcement-learning/update-q-with-learning-rate.gif">

- 첫 번쨰 항은 Q를 업데이트하기 이전의 Q 값입니다. 즉 기존의 값을 그대로 이용하는 것이죠.

  이 때 `Q(s, a) != r` 임을 주의하세요. `Q(s, a)`는 예상 값이고, `r`은 실제 보상 값입니다. (환경 자체가 비결정적이므로 `s`와 `a`가 같더라도 `r`은 매 번 달라질 수 있습니다.)

- 두 번째 항은 기존의 Q를 업데이트하던 수식과 동일합니다.
- learning rate를 두 번째 항에 곱해서 새로운 Q 값의 일부분만 받아들입니다. 전체적으로 값의 크기를 유지하기 위해서 (1-α)를 첫 번째 항에 곱해줍니다.

코드로 표현하면 다음과 같습니다. (수식과 거의 유사합니다.)

```python
alpha = 0.1
new_q_values = reward + gamma * np.max(Q[new_state, :])
Q[state, action] = (1 - alpha) * Q[state, action] + alpha * new_q_values
```

<br>

## Summary

이렇게 해서 완성된 최종 코드는 다음과 같습니다.

```python
import numpy as np
import random as pr

env = gym.make('FrozenLake-v3')

# Initialize Q
state_size = env.observation_space.n
action_size = env.action_space.n
Q = np.zeros([state_size, action_size])

# Random argmax
def rargmax(vector):
  m = np.amax(vector)
  indices = np.nonzero(vector == m)[0]
  return pr.choice(indices)

learning_rate = 0.85
gamma = 0.99

for i in range(num_episodes):
  state = env.reset()
  done = False

  while not done:
    action = rargmax(Q[state, :] + np.random.random(env.action_space.n) / (i + 1))

    new_state, reward, done, info = env.step(action)

    Q[state, action] = (1 - learning_rate) * Q[state, action] \
      + learning_rate * (reward + gamma * np.max(Q[new_state, :]))

    state = new_state
```

실행할 수 있는 예제를 찾으시는 분은 제 [Github](https://github.com/soldier4443/rl-playground)를 참고해주세요. 몇 가지 세부 디테일(키 매핑, 로깅 등)과 함께 계속 업데이트가 되고 있답니다.

위 코드에서 reward를 누적해서 평균을 구하면 성공 확률을 대략적으로 구할 수 있습니다.

제가 여러 번 돌려보았을 때는 `0.5 ~ 0.6` 정도의 성공률을 보였는데,
비록 굉장히 낮은 수이기는 하지만 Non-deterministic한 환경임을 감안했을 때는 상당히 잘 나온 것 같습니다.
무작위로 움직였을 때보다는 확실히 좋게 나왔죠.

<br>

이렇게 강화학습이란 무엇이고, Q-learning이라는 것은 무엇인지, 그리고 몇 가지 문제를 해결하기 위한 여러 방법론까지 강화학습의 기본적인 내용에 대해서 알아보았습니다.

지금까지 살펴본 이 알고리즘에는 한 가지 큰 문제가 있는데요, 상태와 액션의 경우의 수를 가지고 Table을 만들었기 때문에 가능한 상태와 액션의 조합이 많아지면 적용이 불가능합니다.

다음에는 이 문제를 해결하기 위해서 Q-learning에 DNN의 개념을 접목한 Q-network, 그리고 DQN에 대해서 알아보겠습니다. 그럼 아듀!

<br>

### References

[Sung Kim 교수님의 RL 강좌](https://www.youtube.com/playlist?list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG)

[Wikipedia, Q 러닝](https://ko.wikipedia.org/wiki/Q_%EB%9F%AC%EB%8B%9D)