---
title: "build variants, product flavors와 Android Studio 3에서 달라진 점"
layout: post
tags:
  - android
  - android-studio
---

build variants와 product flavors는 기능에 따라서 다양한 버전의 앱을 구성하거나, 개발 및 출시 버전을 관리할 때 유용합니다.
이 기능들은 module 레벨의 build.gradle에서 설정할 수 있습니다.

<br/>

## Build Variants

한국어로 빌드 변형이라고 하는 이 녀석은 **어떠한 형태의 빌드**인지를 나타냅니다.
기본적으로 안드로이드 스튜디오에는 debug와 release라는 변형이 있습니다.

아래 코드를 보세요. release 버전에서는 proguard를 활성화해서 불필요한 코드를 최적화시키고,
변수의 이름을 난독화시켜 디컴파일로 인한 보안 문제를 방지합니다. debug 버전에서는 기존의 applicationId에 ".debug" 라는 이름을 추가해서
디버그 빌드라는 것을 나타내고 있습니다. (Gradle plugin 레퍼런스는 [여기로](http://google.github.io/android-gradle-dsl/current/index.html))

```
android {
    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }

        debug {
            applicationIdSuffix ".debug"
        }
    }
}
```

<br/>

## Product Flavors

제품 버전은 build variants와 비슷하게 동작합니다. 말 그대로 **어플리케이션의 제품 구성**을 의미하죠.
예를 들어, 데모 버전의 앱과 유료 버전의 앱을 만들고 싶을 때, 아래와 같이 설정할 수 있습니다.

```
android {
    productFlavors {
        demo {
            applicationIdSuffix ".demo"
            versionNameSuffix "-demo"
        }
        full {
            applicationIdSuffix ".full"
            versionNameSuffix "-full"
        }
    }
}
```

이렇게 정의된 build variants와 proudct flavors는 다음과 같은 4개의 변형을 만들어 냅니다.

`demoDebug, fullDebug, demoRelease, fullRelease`

생성되는 apk의 이름은 다음과 같습니다.

`app-demo-debug.apk, app-full-debug.apk, app-demo-release.apk, app-full-release.apk`

<br/>

### Android Studio 3에서는..

Android Studio 3.0 이상 버전에서는 product flavors를 설정할 때 `dimension`을 반드시 설정하도록 바뀌었습니다.
제품을 구성할 때, 유/무료 여부에 따라서도 구성할 수 있지만, api에 따라서 지원하는 기능이 다르므로 기기의 API 레벨에 따라서 제품을 구성하고 싶을 수도 있습니다.
dimension을 사용하면 여러 제품 구성을 조합할 수 있습니다.

아래와 같이 `api` dimension과 `mode` dimension을 정의하면 먼저 쓰인 dimension, 즉 api을 우선으로 제품 구성이 조합됩니다.
이렇게 말이죠: `api26DemoDebug`

```
flavorDimensions "api", "mode"

productFlavors {
    demo {
        dimension "mode"
    }

    full {
        dimension "mode"
    }

    api26 {
        dimension "api"
        minSdkVersion '26'
    }

    ..
}
```



<br/>

## 그래서 이걸 어디에 써먹지...?

버전에 따라서 설정을 다르게 할 수 있는 건 좋은데, 어디에 활용해야 할지 의문이 생깁니다.
이렇게 빌드 구성을 하면, 구성에 따라서 서로 다른 소스 세트를 만들 수 있습니다. 기본적인 기능은 main/ 소스 세트에 두고,
각 빌드 별로 필요하거나 불필요한 기능을 추가/제거할 수 있지요. 예를 들어 유료 버전에서는 광고를 제거하고, 무료 버전에서는 광고를 포함시키는 식입니다.

main: app/src/main/java

debug: app/src/debug/java

<br/>

### build variants를 이용한 테스팅 방법

이러한 소스 세트를 이용하면 테스팅을 아주 간단하게 할 수 있습니다. Android testing codelab에서도 소개하는 방법입니다.

먼저 product flavors를 `mock`와 `prod` 두 개 만듭니다.

```
// module level build.gradle

android {
    productFlavors {
        mock
        prod
    }
}
```

좌측 하단 Build Variants 탭에서 빌드 변형이 제대로 생성되었는지 확인하세요.

<img src="/images/2017/android-build-variants-product-flavors/build-variants.png" width="400" />


다음은 소스 셋을 생성할 차례입니다.

Project 뷰에서, app/src/ 폴더 밑에 debug/java/와 prod/java/를 추가합니다.

 * `Gradle task 중 sourceSets을 실행하면, Gradle console에서 예상되는 소스셋 경로를 확인할 수 있습니다.`

debug/java/ 와 prod/java/ 안에 각각 아무런 파일이나 하나 추가하고, Android 뷰를 열어보면 아래와 같이 소스 셋이 추가되어 있는 것을 확인할 수 있습니다.

<img src="/images/2017/android-build-variants-product-flavors/mock-debug.png" width="280" />
<img src="/images/2017/android-build-variants-product-flavors/prod-debug.png" width="280" />

이제 모든 준비가 되었습니다.

하나의 상황을 예로 들어 보겠습니다. 어플리케이션을 테스트해야하는데, 아직 데이터베이스를 구현하지 않은 상태입니다.
데이터베이스를 모두 구현하려면 시간이 꽤 걸릴테니, 데이터베이스 역할을 하는 모의 객체를 만드는 것이 현명하겠죠.

이런 경우, prod 소스 세트와 mock 소스 세트에 같은 이름으로 두 개의 클래스를 생성합니다.
그리고 mock 소스 세트에는 실제 DB를 완성할 떼 까지 DB의 역할을 해줄 모의 객체를,
나중에 prod 소스 세트에는 실제 DB Helper 소스를 작성하면 되겠죠? 물론 메소드 이름 역시 같아야하니..
main 소스 세트에서 interface 하나를 정의하고, 그 인터페이스를 구현하게 하면 이 역시 어렵지 않게 일치시킬 수 있습니다.

자바 클래스 파일 뿐만 아니라 리소스 역시 정의할 수 있으니 여러 곳에 유용하게 사용할 수 있을겁니다.

<br/>

#### 참고 자료
 - [안드로이드 공식 페이지](https://developer.android.com/studio/build/build-variants.html)
 - [안드로이드 Testing codelab](https://codelabs.developers.google.com/codelabs/android-testing/index.html?index=..%2F..%2Findex#0)
