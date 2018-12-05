---
title: "Gradle, 제대로 알고 쓰자"
layout: post
tags: [android, gradle, build-automation]
---

안드로이드 개발자로써 1년 절반이 넘도록 개발을 하면서 항상 접해왔던 build.gradle이라는 파일.
개발하면서 별 의식하지 않고 사용하고 있던 Gradle을 다시 재조명하는 시간을 가져보려고 합니다.

<br>

## Prerequisites

- JVM based language
- Gradle

  적어도 한 개 이상의 JVM 기반 언어(Java, Scala 등)를 다루어보셔야 이해가 수월하고, Gradle을 한 번이라도 사용해보셨다면 더 좋을거에요.

  이 글에서는 여러분이 Gradle 빌드 시스템 기반의 안드로이드 개발자라고 가정하고 있습니다. 때문에 안드로이드 개발자라면 조금 더 이해가 빠를 수도 있지만, 꼭 안드로이드 개발을 하지 않더라도 이해하는데 무리가 없도록 작성하였습니다.

<br>

## Introduction

Gradle은 많은 분들이 아시다시피 빌드 과정을 자동화해주는 도구인데요,
사실 근본적으로 Gradle은 일련의 Task를 수행하는 Task Runner에 지나지 않습니다.

우리가 원하는 작업과 그 순서를 명시하면, Gradle은 그 관계를 파악하고 필요한 작업만을 수행해주는 것이지요.

<br>

## Setup

Gradle을 사용하려면 먼저 설치를 해야겠죠?

Gradle에서는 CLI 환경에서 사용할 수 있도록 명령줄 도구를 제공하고 있습니다. 설치 방법은 정말 간단하답니다. 물론 Package Manager를 이용했을 경우에 말이죠.

##### Mac

    > brew install gradle

##### Windows

    > choco install gradle

추가로 JDK가 설치되어 있어야 하는데요, JDK는 다들 설치하셨을 거라고 생각하고 따로 설명하지 않겠습니다.

자세한 설치 방법은 [Gradle 문서](https://docs.gradle.org/current/userguide/installation.html)를 참고해주세요.

<br>

## 인사부터 해봅시다

간단하게 Task를 하나 생성해볼까요?

```groovy
// build.gradle
task echoTask {
  doLast {
    println "Hello World"
  }
}
```

위 Task를 실행하면 어떻게 될까요? 아래 명령어를 통해서 결과를 확인해볼 수 있습니다.

    > gradle echoTask
    
    Hello World

제가 명시한 대로 `Hello World` 라는 문장이 출력되었습니다.

<br>

## Plugins

Gradle이 정말로 그저 작업을 수행하는 역할만 한다면
어떻게 자바 코드를 빌드하고, 유닛 테스트를 수행하고, apk 파일을 만들어낼 수 있는 걸까요?

안드로이드에서 개발을 하면 이런 식으로 `build.gradle` 파일 상단에 `apply plugin: [플러그인 이름]` 과 같은 형식으로 플러그인 사용을 명시하는 부분이 있습니다.

```groovy
apply plugin: 'com.android.application'
```

이 플러그인은 `android { }`, `buildTypes { }` 같은 Configuration Block을 가지고 있어서 우리가 사용할 수 있도록 해줍니다. 물론 `assemble`과 같이 소스 코드를 빌드하고 apk를 생성하는 Task도 들어있을거에요.

<br>

프로젝트에서 사용할 수 있는 Task의 목록을 확인하려면 아래 명령어를 사용하세요.

    > gradle tasks

결과는 다음과 같습니다. (안드로이드 예시입니다.)

<img src="/images/2018/gradle/gradle-tasks.png" />

Android-Gradle 플러그인의 세부 내용은 [레퍼런스 문서](http://google.github.io/android-gradle-dsl/current/)에 상세하게 정의되어 있습니다. 플러그인으로 무엇을 할 수 있는지 궁금하신 분들은 참고하시면 좋을 것 같아요.

<br>

## Structure

Gradle은 크게 **Project**와 **Task**라는 개념으로 설명할 수 있습니다.

 - **Project**는 라이브러리나 어플리케이션 등, 무엇을 만들 것인지를 나타냅니다.

 - **Task**는 실제로 빌드를 하면서 수행하는 작업들입니다. 콘솔에 메시지를 출력하는 것이나 소스 파일을 엮어서 JAR 파일로 압축하는 등의 작업도 일종의 Task라고 볼 수 있죠.

 - **Build Configuration Script**라고 부르는 `build.gradle` 파일을 통해서 Project와 Task를 정의할 수 있습니다.

간단하게 구조에 대해서 살펴봤으니 Gradle에서 사용하는 DSL에 대해서 자세히 알아보겠습니다.

<br>


## Gradle DSL (with Groovy)

저는 처음 접한 빌드 도구가 Gradle이었는데요, 이후에 Maven을 접하고 나서 빌드 스크립트를 프로그래밍 언어로 작성하는 것이 얼마나 편한 것인지 느끼게 됬습니다.

> Maven은 XML을 가지고 스크립트를 작성하죠. 이름에서 알 수 있듯이 XML은 프로그래밍 언어가 아니라 Markup 언어입니다.

Gradle의 스크립트는 `Groovy`라는 언어를 통해서 정의할 수 있습니다. Groovy는 JVM 위에서 동작하는 **동적 프로그래밍 언어**입니다. Kotlin이나 Scala와 비슷하지만, 동적 프로그래밍 언어라는 점이 독특하죠.

그루비가 JVM 기반이라는 것은 자바의 모든 기능을 적극적으로 활용할 수 있음을 의미합니다. 여기에 더해서 동적 프로그래밍 언어가 가지는 유연함과 편리성, 그리고 Closure, Optionality 등의 Feature를 통해서 Script 작성이 더 편해진답니다.

<br>

## Task 작성해보기

이번에는 apk 파일을 읽어서 버전 정보를 출력하는 Task를 직접 정의해볼게요.

Android build tools 중 [aapt](https://developer.android.com/studio/command-line/aapt2)를 이용하면 apk manifest 정보를 읽어올 수 있습니다. (물론 직접 압축 해제해서 가져올 수도 있습니다.)

```bash
# extractApk.sh
AAPT=/Users/tura/Library/Android/sdk/build-tools/28.0.3/aapt
$AAPT dump badging $1 | head -n 1 > tmp
```

작성한 스크립트를 실행하려면 [Exec Task](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.Exec.html#org.gradle.api.tasks.Exec)를 확장하고, 필요한 작업을 명시하면 됩니다.

앞서 말한 것처럼, 그레이들의 스크립트는 Groovy로 쓰여져 있고, 따라서 자바의 모든 기능을 이용할 수 있습니다. 뿐만 아니라 meta programming을 통해서 다양한 확장 메서드도 쓸 수 있답니다.

```groovy
task extractApk(type: Exec) {
  def apkPath = new File(".").listFiles().toList().stream()
    .filter { it.name.endsWith(".apk") }
    .findFirst()
    .orElseThrow { new IllegalStateException("apk does not exist.") }

  executable "./extractApk.sh"
  args "$apkPath"
}
```

결과는 다음과 같습니다.

    > gradle extractApk
    > cat tmp

    package: name='com.turastory.sampleapp' versionCode='1' versionName='1.0.0'

이제 여기서 versionCode와 versionName에 해당하는 부분을 추출해내면 되겠네요!

<br>

##### 의존성 정의

apk에서 버전 정보에 해당하는 라인을 추출해내는 작업은 버전 정보를 출력하는 작업보다 반드시 먼저 수행되어야 하기 때문에, `dependsOn` 키워드를 사용해서 Task 간의 의존성을 정의해줍니다.

```groovy
// build.gradle
// Groovy의 ExpandoMetaClass를 이용, String 객체에 extractValue라는 메서드를 추가합니다.
String.metaClass.extractValue {
  def startIndex = delegate.indexOf("'", delegate.indexOf(it)) + 1
  def endIndex = delegate.indexOf("'", startIndex)
  return delegate.substring(startIndex, endIndex)
}

task printVersionInfo(dependsOn: 'extractApk') {
  doLast {
    def file = new File("tmp")
    def line = file.readLines().get(0)

    def versionCode = line.extractValue("versionCode")
    def versionName = line.extractValue("versionName")

    println "VersionCode: $versionCode"
    println "VersionName: $versionName"

    file.delete()
  }
}
```

결과를 확인해보면 의도했던 대로 버전 정보를 출력하는 것을 볼 수 있습니다. 이 때 `-i` 옵션을 사용하면 Task가 실행되는 순서를 볼 수 있습니다.

    > gradle printVersionInfo

    Tasks to be executed: [task ':extractApk', task 'printVersionInfo']
    ...
    VersionCode: 1
    VersionName: 1.0.0

<br>

## Kotlin DSL

안드로이드를 개발하고 있다면 Kotlin을 사용할 수도 있을텐데요,
Gradle에서는 2016년부터 스크립트를 Kotlin으로 작성할 수 있도록 지원하고 있습니다.

Intellij, Android Studio 등의 Jetbrains 계열 IDE와의 연계도 뛰어나고, 소스와 빌드 스크립트를 같은 언어로 작성할 수 있다는 것은 굉장히 매력적입니다.

Kotlin을 사용해서 빌드 스크립트를 작성하려면 `.gradle` 확장자를 `.gradle.kts`와 같은 형식으로 변경하기만 하면 됩니다. 물론 Kotlin에 맞도록 코드를 수정해야겠지만요.

##### Task 작성해보기

앞서서 작성한 Task들을 코틀린으로 작성해볼게요.

```kotlin
tasks {
  task<Exec>("extractApk") {
    val apkPath = File(".").listFiles()
      .firstOrNull { it.name.endsWith(".apk") }

    apkPath?.let {
      executable = "./extractApk.sh"
      args("$it")
    } ?: run {
      throw IllegalStateException("apk does not exist.")
    }
  }

  // Kotlind의 Extension Function을 이용, String 객체에 extractValue라는 메서드를 추가합니다.
  fun String.extractValue(str: String): String {
    val startIndex = indexOf("'", indexOf(str)) + 1
    val endIndex = indexOf("'", startIndex)
    return substring(startIndex, endIndex)
  }

  task("printVersionInfo") {
    dependsOn("extractApk")
    doLast {
      val file = File("tmp")
      val line = file.readLines()[0]

      val versionCode = line.extractValue("versionCode")
      val versionName = line.extractValue("versionName")

      println("VersionCode: $versionCode")
      println("VersionName: $versionName")

      file.delete()
    }
  }
}
```

Kotlin DSL에 좀 더 관심이 있으신 분들은 Gradle 문서의 [Kotlin DSL Primer](https://docs.gradle.org/current/userguide/kotlin_dsl.html) 페이지를 살펴보시기 바랍니다.

<br>

## Summary

이렇게 Gradle이라는 빌드 자동화 도구에 대해서 살펴보았습니다.

조금 더 자세한 설명이 필요하신 분들은 [Gradle 레퍼런스](https://docs.gradle.org/current/userguide/userguide.html)를 보시면 좋을 것 같아요. 굉장히 정리가 잘 되어 있습니다.

더불어 Packt 출판사의 [Gradle Essentials](https://www.packtpub.com/web-development/gradle-essentials)라는 책을 참고했답니다.