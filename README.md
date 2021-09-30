![workflow](https://github.com/ptswarm/reFlutter/actions/workflows/main.yml/badge.svg)

![stars](https://img.shields.io/github/stars/ptswarm/reFlutter)
[![github_downloads](https://img.shields.io/github/downloads/ptswarm/reFlutter/total?label=downloads)](https://github.com/ptswarm/reFlutter/tags)
<h2 align="center">reFlutter</h1>
<p align="center"><img src="https://user-images.githubusercontent.com/87244850/135372439-822467e7-03db-4593-9063-09a2cec460c2.jpg" width="100%"/></p>


A framework to help reverse engineer Flutter with the correct version of the engine, which is pre-compiled and modified to read and deserialize the snapshot. Added a patch for intercepting traffic in ```socket.cc```, modified ```dart.cc``` to display classes, functions and some fields, as well as several changes for successful compilation. Manual modification of the Flutter source code is supported using a custom Dockerfile.
## Supported engines
- Android: arm64, arm32;
- IOS: arm64 (Unstable);
- Release: Stable, Beta
## Install
```
pip install reflutter

pip3 install reflutter
```
## Usage
```console
impact@f:~$ reflutter main.apk

Please enter your Burp IP: <input_ip>

SnapshotHash: 8ee4ef7a67df9845fba331734198a953
The resulting apk file: ./release.RE.apk
Please sign the apk file

Configure Proxy in Burp -> *:8083
Request Handling -> Support Invisible Proxying -> true

impact@f:~$ reflutter main.ipa
```
## Output Example
```console
impact@f:~$ adb logcat -e reflutter | sed 's/.*DartVM//' >> reflutter.txt
```
```
Library:'package:anyapp/navigation/DeepLinkImpl.dart' Class: Navigation extends Object {  

String DeepUrl = anyapp://evil.com/;

 Function 'Navigation.': constructor. (dynamic, dynamic, dynamic, dynamic) => NavigationInteractor { 
  
                   }
    
 Function 'initDeepLinkHandle':. (dynamic) => Future<void>* { 
  
                   }
    
 Function '_navigateDeepLink@547106886':. (dynamic, dynamic, {dynamic navigator}) => void { 

                   }
 
       }
 
 Library:'package:anyapp/auth/navigation/AuthAccount.dart' Class: AuthAccount extends Account {
 
 PlainNotificationToken* _instance = sentinel;
 
 Function 'getAuthToken':. (dynamic, dynamic, dynamic, dynamic) => Future<AccessToken*>* { 

                  }
  
 Function 'checkEmail':. (dynamic, dynamic) => Future<bool*>* { 
 
                 }

 Function 'validateRestoreCode':. (dynamic, dynamic, dynamic) => Future<bool*>* { 
 
                 }

 Function 'sendSmsRestorePassword':. (dynamic, dynamic) => Future<bool*>* { 

                 }
          }
```
## Flutter version table
Based on ```https://storage.googleapis.com/flutter_infra_release/flutter/<version_hash>/android-arm64-release/linux-x64.zip```
| version           | Engine_commit                            | Snapshot_Hash                     |
| ----------------- | ---------------------------------------- | --------------------------------- |
| 2.6.0-5.2.pre     | 1d521d89d8d98f27be4e0ff84d5c6b72dbdc91ca | f10776149bf76be288def3c2ca73bdc1  |
| 2.5.0             | f0826da7ef2d301eb8f4ead91aaf026aa2b52881 | 9cf77f4405212c45daf608e1cd646852  |
| 2.4.0             | 844c29f42a614420b2205c178f22d30b43a8b0bb | 659a72e41e3276e882709901c27de33d  |
| 2.3.0             | 9d517f475ba1282b619477bde8e708d6a34287cf | 7a5b240780941844bae88eca5dbaa7b8  |
| 2.2.0             | a9d88a4d182bdae23e3a4989abfb7ea25954aad1 | e4a09dbf2bb120fe4674e0576617a0dc  |
| 2.2.0-10.1.pre    | d2a2e93510ad6cfc3d62a90d903b7056e4da8264 | 34f6eec64e9371856eaaa278ccf56538  |
| 2.1.0-12.2.pre    | 711ab3fda05004ee5f6035f2a0bf099fca39a129 | 39a9141bbcc3cae43e6f9f6b7fbaafe3  |
| 2.0.6             | 05e680e202af9a92461070cb2d9982acad46c83c | 5b97292b25f0a715613b7a28e0734f77  |
| 1.25.0-8.3.pre    | 7a8f8ca02c276dce02f8dd42a44e776ac03fa9bc | 9e2165577cef0f0f70f9ff072107920c  |
| 1.24.0-10.2.pre   | 07c1eed46b9d9b58df78566e9b8b2e42e80d3380 | a2bdb58c7edf9471da9180bf8185e7f7  |
| 1.23.0-18.1.pre   | 1d12d82d9cb54876f58044aa52198d53ec841c3d | 953aa80d78c4d8886e3e4d784fd9d95f  |
| 1.22.6            | 2f0af3715217a0c2ada72c717d4ed9178d68f6ed | 8ee4ef7a67df9845fba331734198a953  |
| 1.21.0-9.2.pre    | 20a953183580250aac2e15d36007664118bda5ab | 5f40b0a9f04b5018fa08a9b67fd316cd  |
| 1.20.4            | d1bc06f032f9d6c148ea6b96b48261d6f545004f | 04645b6182fad3d68350d84669869ce5  |
| 1.20.0-7.2.pre    | 60b269d898cbe0be27e9b9ba9d21eae97b887ab6 | 8b2ca977d1d2920b9839d1b60eade6a7  |
| 1.19.0-4.3.pre    | 9a28c3bcf40ce64fee61e807ee3e1395fd6bd954 | 59da07d9da5a83be4ce75b7913b63dbd  |
| 1.18.0-11.1.pre   | ef9215ceb2884ddf520d321bcd822d1461330876 | b58ead73b2c5dfec69565df469bba387  |
| 1.17.5            | ee76268252c22f5c11e82a7b87423ca3982e51a7 | be7d304ff826e2dfac63538e227c3cc5  |
| 1.17.1            | 6bc433c6b6b5b98dcf4cc11aff31cdee90849f32 | 74edb834fac3fcea79d7ac2d1d6f1fb2  |
| 1.17.0-dev.3.1    | c9506cb8e93e5e8879152ff5c948b175abb5b997 | 9e7cb7c9394c24c2398410b902673e13  |
| v1.15.17          | 5aff3119480996ca014ec0f8d26d74db617b5852 | ee91a9191a5286c31d91a89754ba36af  |
| v1.14.6           | c4229bfbbae455ad69c967be19aee3fadd6486e1 | e739779cc1d28f0f697a92f2daf5f10f  |
| v1.13.6           | bdc9708d235e582483d299642ad8682826ebb90d | 81662522448cdd4d02eb060669e5d48b  |
| v1.12.13+hotfix.9 | af51afceb8886cc11e25047523c4e0c7e1f5d408 | 20e5c4f7dc44368ac5a17643b93665f6  |
| v1.11.0           | af04338413c3ed73316350f64248a152433073b6 | 2fb364d659ea53f7892be9ba5e036047  |
| v1.10.7           | 9e6314d348f9b5521e3c66856324d7a9c4a928c9 | c3bbfe8f226120ad0569d7b78ed2d9ef  |
| v1.9.1+hotfix.6   | b863200c37df4ed378042de11c4e9ff34e4e58c9 | c8562f0ee0ebc38ba217c7955956d1cb  |
| v1.8.3            | 38ac5f30a7026e870619c2e8e8c99c070d74036f | 34948253b59d5a56b2ec161e17975a4e  |
| v1.7.8+hotfix.4   | fee001c93f25a1e7258e762781a7361f122d29f5 | 1d7acad1540192ac459cf60344efb7c1  |

......stub...
